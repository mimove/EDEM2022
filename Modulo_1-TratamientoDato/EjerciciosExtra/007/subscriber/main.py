import json
import requests
import os
import pandas as pd
import random
import datetime
import time
import mysql.connector
from time import sleep
from json import dumps
from faker import Faker
from kafka import KafkaConsumer


connecting=True
print("Start Process")
while connecting:
    try:
        print("Start consumer Connection")
        consumer = KafkaConsumer(bootstrap_servers=['kafka:29092'], group_id = 'group1', auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))
        print("Connection realised")
        connecting=False
    except Exception as e: 
        print(e)
        print("Broker not connected")
        connecting=True
        sleep(5)


while True:
    try:

        mydb = mysql.connector.connect(
        host=os.environ["MYSQL_HOST"],
        user="root",
        password="my_secret_password",
        database="app_db",
        port=3306
        )

        break

    except Exception as err:
        print('Waiting for database to intialize: {}'.format(err))
        time.sleep(1)

print("DB connected")



mycursor = mydb.cursor()


#Including names of json generated in mockaroo
list_json = ["product","users","status_name","country","city","store","sale","order_status"]

# list_json_sale = ["sale", "order_status"]


mycursor.execute("SET FOREIGN_KEY_CHECKS = 0;") # Not an acceptable solution, because table integrity has to be checked, but to learn it works. I need to ask about an alternative

while True:
    try:
        
        

        print("Start receiving data")


        # ENVIAR DATOS AL TOPICO

        consumer.subscribe(list_json)

        # df = pd.read_json(consumer.poll())

        # raw_messages = consumer.poll()
        
        id_dict = dict()

        for msg in consumer:

            print('###########\n')
            print('Topic, ', msg.topic)

            i = msg.topic

            ####### TABLES #########
            print('Filling table '+i+'...')

            if i != 'sale' and i != 'order_status':


                df = pd.DataFrame.from_dict(json.loads(msg.value))

                # print(df)
            
            else:

                df = pd.DataFrame.from_records(json.loads(json.dumps(msg.value)), index = [0])

            placeholders = ', '.join(['%s'] * len(df.columns))
            columns = ', '.join(df.columns)

            sql_sale = "INSERT INTO %s ( %s ) VALUES ( %s );\n" % (i, columns, placeholders)

            for row in df.values.tolist():

                # print(sql_sale, row)
                mycursor.execute(sql_sale, row)

                mydb.commit()
            print(len(df), "record in table {} inserted.".format(i))
            print('\n##########')
            

        # break

        # sleep(5)

    except Exception as e: 
        print(e)
        print("Error in the topic")
        print("Waiting")
        sleep(5)





