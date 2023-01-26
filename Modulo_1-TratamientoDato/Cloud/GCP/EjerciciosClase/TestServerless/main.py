
project_id = deft-epigram-375817
bucket-name = edem-serverless-bucket


gcloud builds submit --tag 'gcr.io/deft-epigram-375817/dataflow/edem:latest' .


gcloud dataflow flex-template build "gs://edem-serverless-bucket/dataflowtemplate.json" \
  --image 'gcr.io/deft-epigram-375817/dataflow/edem:latest' \
  --sdk-language "PYTHON" 



gcloud dataflow flex-template run "edem-dataflow-job" \
    --template-file-gcs-location "gs://edem-serverless-bucket/dataflowtemplate.json" \
    --region "europe-west4"


python edemDeviceData.py \
    --algorithm RS256 \
    --cloud_region europe-west4 \
    --device_id edemDevice \
    --private_key_file rsa_private.pem \
    --project_id deft-epigram-375817 \
    --registry_id edemRegistry