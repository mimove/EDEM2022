import json
import requests
import random
import pandas as pd
import datetime
import time
from time import sleep
from json import dumps
from faker import Faker

from kafka import KafkaProducer


connecting=True
print("Start Process")
while connecting:
    try:
        print("Start producer Connection")
        producer = KafkaProducer(bootstrap_servers=['kafka:29092'],value_serializer=lambda x: dumps(x).encode('utf-8'))
        print("Connection realised")
        connecting=False
    except Exception as e: 
        print(e)
        print("Broker not connected: {}".format(e))
        connecting=True
        sleep(5)


#Including names of json generated in mockaroo
list_json = ["city", "product", "users","status_name"]

id_dict = dict()

while True:
    try:

        for i in list_json:



            # Construir el json
            # response = requests.get('https://my.api.mockaroo.com/'+i+'.json?key=3f509750')

            # ENVIAR DATOS AL TOPICO

            # Construir el json
            response = requests.get('https://my.api.mockaroo.com/'+i+'.json?key=3f509750').json()

            # response = json.load(open('./db_test/'+i+'.json'))

            df = pd.DataFrame.from_dict(response) 

            #Removing duplicates from Pandas df
            df.drop_duplicates(subset=list(df)[1], inplace=True)

            df = df.reset_index(drop=True)

            # Reseting id column value
            df[list(df)[0]] = df.index + 1

            id_dict[i+"_id"] = df[list(df)[0]].values.tolist()

            if i != 'city':

                ## PRODUCT, USERS, STATUS_NAME ##

                print("Start sending {} data".format(i))
                
                response = df.to_json(orient='records')

                producer.send(i, value=response)

                producer.flush()

                print("Message {} Sent".format(i))
            
            else:

                ## COUNTRY ##
                
                print("Start sending {} data".format('country'))

                # Extracting countries from cities.csv original file
                df_countries = df[[list(df)[-2]]].copy()
                df_countries.drop_duplicates(inplace=True)
                df_countries = df_countries.reset_index(drop=True)
                df_countries["country_id"] = df_countries.index + 1 # Creating country_id column
                df_countries = df_countries[list(df_countries)[::-1]]

                id_dict["country_id"] = df_countries["country_id"].values.tolist()

                response = df_countries.to_json(orient='records')

                producer.send('country', value=response)

                producer.flush()

                print("Message {} Sent".format('country'))


                ## CITY ##
                
                print("Start sending {} data".format(i))

                # Merging Countries and Cities to obtain country_id in cities df
                df = pd.merge(df, df_countries, on='country_name', how='inner').sort_values(by=[list(df)[0]]).reset_index(drop=True)

                df_city = df[[list(df)[0],list(df)[1],list(df)[4]]].copy()

                response = df_city.to_json(orient='records')

                producer.send(i, value=response)

                producer.flush()

                print("Message {} Sent".format(i))



                ## STORE ##
                
                print("Start sending {} data".format('store'))

                # Extracting store names from cities.csv original file
                df_store = df[[list(df)[3], list(df)[0]]].copy()
                df_store = df_store.reset_index(drop=True)
                df_store["store_id"] = df_store.index + 1
                df_store = df_store[[list(df_store)[-1]]+list(df_store)[:-1]]
                id_dict["store_id"] = df_store["store_id"].values.tolist()


                response = df_store.to_json(orient='records')

                producer.send('store', value=response)

                producer.flush()

                print("Message {} Sent".format('store'))


            # print(id_dict)
        
        ######
        break
        ######
        
        # sleep(5)
        
    except Exception as e: 
        print(e)
        print("Error in the topic")
        print("Waiting")
        sleep(5)


    
# Generating n random initial values for sales

n = 100

n_st = 100

# Creating list of sales_id to use in order_status
id_dict["sales_id"] = list(range(1,n+1))

sale_date = list() # list with all the dates of the sales

while True:
    try:
        for i in range(n):


            # Creating a dict with all the values required for the sale table

            dict_sale = {"sale_id" : str(i+1)}

            dict_sale["amount"] = str(round(random.uniform(0.4, 5.0),2)) # random value between 0.4€ and 5.0€

            start = datetime.date(year=2023, month=1, day=1)

            dict_sale["date_sale"] = Faker().date_time_between(start_date=start).strftime('%Y-%m-%d %H:%M:%S') # Creates a str of a random date

            sale_date.append(dict_sale["date_sale"]) # Appending date to the list of dates

            # Selecting random values of product, user and store ids

            dict_sale["product_id"] = str(random.choice(id_dict["product_id"]))

            dict_sale["user_id"] = str(random.choice(id_dict["users_id"]))

            dict_sale["store_id"] = str(random.choice(id_dict["store_id"]))


            producer.send('sale', value=dict_sale)

            producer.flush()

            print("Message {} to {} Sent".format(i, 'sale'))


        


        # Same procedure as for the sale table

        for i in range(n_st):
            
            dict_order_st = {"order_status_id" : str(i+1)}

            sale_id = random.choice(id_dict["sales_id"]) 

            start = datetime.datetime.strptime(sale_date[sale_id-1], '%Y-%m-%d %H:%M:%S')

            dict_order_st["update_at"] = Faker().date_time_between(start_date=start).strftime('%Y-%m-%d %H:%M:%S')

            dict_order_st["sale_id"] = str(sale_id)


            dict_order_st["status_name_id"] = str(random.choice(id_dict["status_name_id"]))


            producer.send('order_status', value=dict_order_st)

            producer.flush()

            print("Message {} to {} Sent".format(i, 'order_status')) 

        break

    except Exception as e: 
        print(e)
        print("Error in the topic")
        print("Waiting")
        sleep(5)




# Creating a new sale every t seconds

t = 1

new_sale_id = n

new_ord_st_id = n_st

while True:
    try:
        
        #### New Sale ####

        # Creating a dict with all the values required for the sale table

        new_sale_id += 1

        id_dict["sales_id"].append(new_sale_id)

        dict_sale = {"sale_id" : str(new_sale_id)}

        dict_sale["amount"] = str(round(random.uniform(0.4, 5.0),2)) # random value between 0.4€ and 5.0€


        dict_sale["date_sale"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Creates a str of a random date

        sale_date.append(dict_sale["date_sale"]) # Appending date to the list of dates

        # Selecting random values of product, user and store ids

        dict_sale["product_id"] = str(random.choice(id_dict["product_id"]))

        dict_sale["user_id"] = str(random.choice(id_dict["users_id"]))

        dict_sale["store_id"] = str(random.choice(id_dict["store_id"]))


        producer.send('sale', value=dict_sale)

        producer.flush()

        print("New Message {} to {} Sent".format(new_sale_id, 'sale'))



        new_ord_st_id += 1

        dict_order_st = {"order_status_id" : str(new_ord_st_id)}

        sale_id = random.choice(id_dict["sales_id"]) 


        dict_order_st["update_at"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        dict_order_st["sale_id"] = str(sale_id)


        dict_order_st["status_name_id"] = str(random.choice(id_dict["status_name_id"]))


        producer.send('order_status', value=dict_order_st)

        producer.flush()

        print("New Message {} to {} Sent".format(new_ord_st_id, 'order_status')) 

        sleep(t)

    except Exception as e: 
        print(e)
        print("Error in the topic")
        print("Waiting")
        sleep(5)