# This is a simple script to remove duplicates from csv files and transform the data obtained from https://www.mockaroo.com/

import os
import pandas as pd
import random
import datetime
import time
import mysql.connector
from faker import Faker

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

    except:
        print('Waiting for database to intialize')
        time.sleep(1)

print("DB connected")



mycursor = mydb.cursor()


#Including names of files generated in mockaroo
list_files = ["city", "product", "users","status_name"]

id_dict = dict()

for i in list_files:

    file_name = "/datos/" + i + ".csv"

    df = pd.read_csv(file_name)

    
    # Notes:
    # - the `subset=list(df)[1]` means that only the second column is used 
    #    to determine if two rows are different; to change that specify
    #    the columns wantes as an array
    # - the `inplace=True` means that the data structure is changed and
    #   the duplicate rows are gone  

    #Removing duplicates from Pandas df
    df.drop_duplicates(subset=list(df)[1], inplace=True)

    df = df.reset_index(drop=True)

    # Reseting id column value
    df[list(df)[0]] = df.index + 1

    id_dict[i+"_id"] = df[list(df)[0]].values.tolist()

    # Writing back the df to the original csv file
    df.to_csv(file_name, index=False)

    if i != "city":
        # sql_csv = """LOAD DATA  INFILE '/var/lib/mysql-files/%s.csv'
        # INTO TABLE %s 
        # FIELDS TERMINATED BY ',' 
        # ENCLOSED BY '"'
        # LINES TERMINATED BY '\n'
        # IGNORE 1 ROWS;""" % (i,i)

        # mycursor.execute(sql_csv)

        df.to_sql(con=mydb, name=i, if_exists='replace')

        mydb.commit()

        print("record dataframe {} inserted.".format(i))

    else:
        # Extracting countries from cities.csv original file
        df_countries = df[[list(df)[-2]]].copy()
        df_countries.drop_duplicates(inplace=True)
        df_countries = df_countries.reset_index(drop=True)
        df_countries["country_id"] = df_countries.index + 1 # Creating country_id column
        df_countries = df_countries[list(df_countries)[::-1]]

        id_dict["country_id"] = df_countries["country_id"].values.tolist()

        df_countries.to_csv(file_name[:-4] + '_countries.csv',index = False)

        sql_csv = """LOAD DATA  INFILE '/var/lib/mysql-files/%s.csv'
        INTO TABLE %s 
        FIELDS TERMINATED BY ',' 
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;""" % (i+'_countries','country')

        mycursor.execute(sql_csv)

        mydb.commit()

        print(mycursor.rowcount, "record order_status inserted.")

        # Extracting store names from cities.csv original file
        df_store = df[[list(df)[3], list(df)[0]]].copy()
        df_store = df_store.reset_index(drop=True)
        df_store["store_id"] = df_store.index + 1
        df_store = df_store[[list(df_store)[-1]]+list(df_store)[:-1]]
        id_dict["store_id"] = df_store["store_id"].values.tolist()
 
        # Merging Countries and Cities to obtain country_id in cities df
        df = pd.merge(df, df_countries, on='country_name', how='inner').sort_values(by=[list(df)[0]]).reset_index(drop=True)

        # Saving new cities file with the columns that we need for the DB 
        df[[list(df)[0],list(df)[1],list(df)[4]]].to_csv(file_name[:-4] + '_modified.csv',index = False)
        
        sql_csv = """LOAD DATA  INFILE '/var/lib/mysql-files/%s.csv'
        INTO TABLE %s 
        FIELDS TERMINATED BY ',' 
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;""" % (i+'_modified',i)

        mycursor.execute(sql_csv)

        mydb.commit()

        print(mycursor.rowcount, "record order_status inserted.")


        df_store.to_csv(file_name[:-4] + '_stores.csv',index = False)
        
        sql_csv = """LOAD DATA  INFILE '/var/lib/mysql-files/%s.csv'
        INTO TABLE %s 
        FIELDS TERMINATED BY ',' 
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;""" % (i+'_stores','store')

        mycursor.execute(sql_csv)

        mydb.commit()

        print(mycursor.rowcount, "record order_status inserted.")


# Generating n random values in .sql file for the sale table

n = 1000

# Creating list of sales_id to use in order_status
id_dict["sales_id"] = list(range(1,n+1))

sale_date = list() # list with all the dates of the sales

for i in range(n):


    # Creating a dict with all the values required for the sale table

    dict_sale = {"sale_id" : str(i+1)}

    dict_sale["amount"] = str(round(random.uniform(0.4, 5.0),2)) # random value between 0.4€ and 5.0€

    start = datetime.date(year=2022, month=1, day=1)

    dict_sale["date_sale"] = Faker().date_time_between(start_date=start).strftime('%Y-%m-%d %H:%M:%S') # Creates a str of a random date

    sale_date.append(dict_sale["date_sale"]) # Appending date to the list of dates

    # Selecting random values of product, user and store ids

    dict_sale["product_id"] = str(random.choice(id_dict["product_id"]))

    dict_sale["user_id"] = str(random.choice(id_dict["users_id"]))

    dict_sale["store_id"] = str(random.choice(id_dict["store_id"]))


    # Converting values and keys into string separated by commas

    placeholders = ', '.join(['%s'] * len(dict_sale))
    columns = ', '.join(dict_sale.keys())
    sql_sale = "INSERT INTO %s ( %s ) VALUES ( %s );\n" % ('sale', columns, placeholders)

    mycursor.execute(sql_sale, list(dict_sale.values()))

    
    mydb.commit()

    print(mycursor.rowcount, "record sale inserted.")

# Generating n random values in .sql file for the order_status table

n = 2000


# Same procedure as for the sale table

for i in range(n):
    
    dict_order_st = {"order_status_id" : str(i+1)}

    sale_id = random.choice(id_dict["sales_id"]) 

    start = datetime.datetime.strptime(sale_date[sale_id-1], '%Y-%m-%d %H:%M:%S')

    dict_order_st["update_at"] = Faker().date_time_between(start_date=start).strftime('%Y-%m-%d %H:%M:%S')

    dict_order_st["sale_id"] = str(sale_id)


    dict_order_st["status_name_id"] = str(random.choice(id_dict["status_name_id"]))

    placeholders = ', '.join(['%s'] * len(dict_order_st))
    columns = ', '.join(dict_order_st.keys())
    sql_sale = "INSERT INTO %s ( %s ) VALUES ( %s );\n" % ('order_status', columns, placeholders)

    mycursor.execute(sql_sale, list(dict_order_st.values()))

    mydb.commit()

    print(mycursor.rowcount, "record order_status inserted.")