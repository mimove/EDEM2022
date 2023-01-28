""" Serverless Data Processing with Dataflow
    Master Data Analytics EDEM
    Academic Year 2022-2023"""

""" Import libraries """

#Import beam libraries
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.combiners import MeanCombineFn
from apache_beam.transforms.combiners import CountCombineFn
from apache_beam.transforms.core import CombineGlobally
import apache_beam.transforms.window as window

from apache_beam.io.gcp.bigquery import parse_table_schema_from_json
from apache_beam.io.gcp import bigquery_tools

#Import Common Libraries
from datetime import datetime
import argparse
import json
import logging
import requests

""" Helpful functions """
def ParsePubSubMessage(message):
    #Decode PubSub message in order to deal with
    pubsubmessage = message.data.decode('utf-8')
    #Convert string decoded in json format(element by element)
    row = json.loads(pubsubmessage)
    #Logging
    logging.info("Receiving message from PubSub:%s", pubsubmessage)
    #Return function
    return row

#PTransform Classes
class getBestProduct(beam.PTransform):
    def expand(self, pcoll):
        best_product = (pcoll
            | "Pair keys" >> beam.Map(lambda x: (x,1))
            # CombinePerKey
            | "CombinePerKey" >> beam.CombinePerKey(sum)
            # Swap the key,value to make the process easier
            | "Swap k,v" >> beam.KvSwap()
            # Get the Max Value
            | "Get max value" >> beam.CombineGlobally(max).without_defaults())
        return best_product

# DoFn Classes

# DoFn 01 : Add Processing Timestamp
class AddTimestampDoFn(beam.DoFn):
    """ Add the Data Processing Timestamp."""
    #Add process function to deal with the data
    def process(self, element):
        #Add ProcessingTime field
        element['Processing_Time'] = str(datetime.now())
        #return function
        yield element

# DoFn 02 : Call GCP Data Loss Prevention
class DLPMaskingDataDoFn(beam.DoFn):
    """ Call API to simulate Data Loss Prevention Service."""
    #Initialize the class by setting the host and endpoint to call
    def __init__(self, hostname):
        self.hostname = hostname
        self.dlp_endpoint = '/dlp_masking'
    #Add process function
    def process(self, element):
        #Dealing with sensitive fields
        if element['Email'] != None:
            logging.info("Masking an Email field...")
            #Make API Request
            try:
                api_request = requests.get(self.hostname + self.dlp_endpoint, params={"item": element['Email']})
                #Show the status response in the logs
                logging.info("Request was finished with the following status: %s", api_request.status_code)
                #Dealing with API Response
                element['Email'] = api_request.content.decode('utf-8')
                logging.info(element)
                yield element
            #Error handle
            except Exception as err:
                logging.error("Error while trying to call to the API: %s", err)
        if element['Credit_Card_Number'] != None:
            logging.info("Masking a Credit_Card_Number field...")
            #Make API Request
            try:
                api_request = requests.get(self.hostname + self.dlp_endpoint, params={"item": element['Credit_Card_Number']})
                #Show the status response in the logs
                logging.info("Request was finished with the following status: %s", api_request.status_code)
                #Dealing with API Response
                element['Credit_Card_Number'] = api_request.content.decode('utf-8')
                yield element
            #Error handle
            except Exception as err:
                logging.error("Error while trying to call to the API: %s", err)

# DoFn 03 : Call Machine Learning Model
class CallMLModelDoFn(beam.DoFn):
    """ Call API to simulate Machine Learning Model."""
    #Initialize the class by setting the host and endpoint to call
    def __init__(self, hostname):
        self.hostname = hostname
        self.ml_endpoint = '/ml_model'
    #Add process function
    def process(self, element):
        #Make API Request
        try:
            api_request = requests.get(self.hostname + self.ml_endpoint, json=element)
            #Show the status response in the logs
            logging.info("Request was finished with the following status: %s", api_request.status_code)
            #Dealing with API Response
            element['Transaction_Status'] = api_request.content.decode('utf-8')
            yield element
        #Error handle
        except Exception as err:
            logging.error("Error while trying to call to the API: %s", err)

# DoFn 04: Dealing with frequent clients
class getProductsDoFn(beam.DoFn):
    def process(self, element):
        #Get Product_id field from the input element
        yield element['Product_Id']

# DoFn 05 : Output data formatting
class OutputFormatDoFn(beam.DoFn):
    """ Set a specific format for the output data."""
    #Add process function
    def process(self, element):
        count, product_id = element
        #Send a notification with the best-selling product_id in each window
        output_msg = {"ProcessingTime": str(datetime.now()), "message": f"{product_id} was the best-selling product."}
        #Convert the json to the proper pubsub format
        output_json = json.dumps(output_msg)
        yield output_json.encode('utf-8')

""" Dataflow Process """
def run():

    """ Input Arguments"""
    parser = argparse.ArgumentParser(description=('Arguments for the Dataflow Streaming Pipeline.'))

    parser.add_argument(
                    '--project_id',
                    required=True,
                    help='GCP cloud project name')
    parser.add_argument(
                    '--hostname',
                    required=True,
                    help='API Hostname provided during the session.')
    parser.add_argument(
                    '--input_subscription',
                    required=True,
                    help='PubSub Subscription which will be the source of data.')
    parser.add_argument(
                    '--output_topic',
                    required=True,
                    help='PubSub Topic which will be the sink for notification data.')
    parser.add_argument(
                    '--output_bigquery',
                    required=True,
                    help='Table where data will be stored in BigQuery. Format: <dataset>.<table>.')
    parser.add_argument(
                    '--bigquery_schema_path',
                    required=False,
                    default='./schema/bq_schema.json',
                    help='BigQuery Schema Path within the repository.')

                    
    args, pipeline_opts = parser.parse_known_args()

    """ BigQuery Table Schema """

    #Load schema from /schema folder
    with open(args.bigquery_schema_path) as file:
        input_schema = json.load(file)

    schema = bigquery_tools.parse_table_schema_from_json(json.dumps(input_schema))

    """ Apache Beam Pipeline """
    #Pipeline Options
    options = PipelineOptions(pipeline_opts, save_main_session=True, streaming=True, project=args.project_id)

    #Pipeline
    with beam.Pipeline(argv=pipeline_opts,options=options) as p:

        """ Part 01: Format data by masking the sensitive fields and checking if the transaction is fraudulent."""
        data = (
            p 
                | "Read From PubSub" >> beam.io.ReadFromPubSub(subscription=f"projects/{args.project_id}/subscriptions/{args.input_subscription}", with_attributes=True)
                # Parse JSON messages with Map Function
                | "Parse JSON messages" >> beam.Map(ParsePubSubMessage) 
                # Adding Processing timestamp
                | "Add Processing Time" >> beam.ParDo(AddTimestampDoFn())
                # Masking Sensitive Data
                | "Masking Sensitive Data" >> beam.ParDo(DLPMaskingDataDoFn(args.hostname))
                # Check if the transacion is fraudulent
                | "Call ML model" >> beam.ParDo(CallMLModelDoFn(args.hostname))
        )

        """ Part 02: Writing data to BigQuery"""
        (
            data | "Write to BigQuery" >> beam.io.WriteToBigQuery(
                table = f"{args.project_id}:{args.output_bigquery}",
                schema = schema,
                create_disposition = beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                write_disposition = beam.io.BigQueryDisposition.WRITE_APPEND
            )
        )

        """ Part 03: Get Best-Selling product per Window and write to PubSub """
        (
            data 
                # Dealing with fraudulent transactions
                | "Get Product Field" >> beam.ParDo(getProductsDoFn())
                # Add Windows
                | "Set fixed window" >> beam.WindowInto(window.FixedWindows(60))
                # Get Best-selling product
                | "Get best-selling prduct" >> getBestProduct()
                # Define output format
                | "OutputFormat" >> beam.ParDo(OutputFormatDoFn())
                # Write notification to PubSub Topic
                | "Send Push Notification" >> beam.io.WriteToPubSub(topic=f"projects/{args.project_id}/topics/{args.output_topic}", with_attributes=False)
        )

if __name__ == '__main__':
    #Add Logs
    logging.getLogger().setLevel(logging.INFO)
    #Run process
    run()
