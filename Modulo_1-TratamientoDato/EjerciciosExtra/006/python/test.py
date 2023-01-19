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
        host='localhost',
        user="root",
        password="my_secret_password",
        database="app_db",
        port=3308
        )

        break

    except Exception as err:
        print('Waiting for database to intialize: {}'.format(err))
        time.sleep(1)

print("DB connected")

mycursor = mydb.cursor()


# while True:
#     try:
#         # engine = create_engine('mysql+pymysql://username:password@host/database')
#         # or in your case-
#         engine = create_engine('mysql+pymysql://root:my_secret_password@localhost:3308/app_db')

#         # db_connection = sql.connect(host='localhost', 
#         #         database="app_db", user='root', password='my_secret_password',port=3308)

#     except Exception as err:
#         print('Waiting for database to intialize: {}'.format(err))
#         time.sleep(1)

# print("DB connected")

#Including names of files generated in mockaroo


list_files = ["product"]

id_dict = dict()

for i in list_files:

    file_name = "./db/" + i + ".csv"

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

        # df.to_sql(con=engine, name=i, if_exists='replace')

        # mydb.commit()


        placeholders = ', '.join(['%s'] * len(df.columns))
        columns = ', '.join(df.columns)

        sql_sale = "INSERT INTO %s ( %s ) VALUES ( %s );\n" % (i, columns, placeholders)

        for row in df.values.tolist():

            # print(sql_sale, row)
            mycursor.execute(sql_sale, row)

            mydb.commit()
        print(len(df), "record in table {} inserted.".format(i))



        



    # else:
        
        # Extracting countries from cities.csv original file
        # df_countries = df[[list(df)[-2]]].copy()
        # df_countries.drop_duplicates(inplace=True)
        # df_countries = df_countries.reset_index(drop=True)
        # df_countries["country_id"] = df_countries.index + 1 # Creating country_id column
        # df_countries = df_countries[list(df_countries)[::-1]]

        # id_dict["country_id"] = df_countries["country_id"].values.tolist()

        # df_countries.to_csv(file_name[:-4] + '_countries.csv',index = False)

        # sql_csv = """LOAD DATA  INFILE '/var/lib/mysql-files/%s.csv'
        # INTO TABLE %s 
        # FIELDS TERMINATED BY ',' 
        # ENCLOSED BY '"'
        # LINES TERMINATED BY '\n'
        # IGNORE 1 ROWS;""" % (i+'_countries','country')

        # mycursor.execute(sql_csv)

        # mydb.commit()

        # print(mycursor.rowcount, "record order_status inserted.")

        # # Extracting store names from cities.csv original file
        # df_store = df[[list(df)[3], list(df)[0]]].copy()
        # df_store = df_store.reset_index(drop=True)
        # df_store["store_id"] = df_store.index + 1
        # df_store = df_store[[list(df_store)[-1]]+list(df_store)[:-1]]
        # id_dict["store_id"] = df_store["store_id"].values.tolist()
 
        # # Merging Countries and Cities to obtain country_id in cities df
        # df = pd.merge(df, df_countries, on='country_name', how='inner').sort_values(by=[list(df)[0]]).reset_index(drop=True)

        # # Saving new cities file with the columns that we need for the DB 
        # df[[list(df)[0],list(df)[1],list(df)[4]]].to_csv(file_name[:-4] + '_modified.csv',index = False)
        
        # sql_csv = """LOAD DATA  INFILE '/var/lib/mysql-files/%s.csv'
        # INTO TABLE %s 
        # FIELDS TERMINATED BY ',' 
        # ENCLOSED BY '"'
        # LINES TERMINATED BY '\n'
        # IGNORE 1 ROWS;""" % (i+'_modified',i)

        # mycursor.execute(sql_csv)

        # mydb.commit()

        # print(mycursor.rowcount, "record order_status inserted.")


        # df_store.to_csv(file_name[:-4] + '_stores.csv',index = False)
        
        # sql_csv = """LOAD DATA  INFILE '/var/lib/mysql-files/%s.csv'
        # INTO TABLE %s 
        # FIELDS TERMINATED BY ',' 
        # ENCLOSED BY '"'
        # LINES TERMINATED BY '\n'
        # IGNORE 1 ROWS;""" % (i+'_stores','store')

        # mycursor.execute(sql_csv)

        # mydb.commit()

        # print(mycursor.rowcount, "record order_status inserted.")