# This is a simple script to remove duplicates from csv files and transform the data obtained from https://www.mockaroo.com/

import pandas as pd
import random
import datetime
from faker import Faker


#Including names of files generated in mockaroo
list_files = ["cities", "product", "names","status"]

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

    if i == "cities":
        # Extracting countries from cities.csv original file
        df_countries = df[[list(df)[-2]]].copy()
        df_countries.drop_duplicates(inplace=True)
        df_countries = df_countries.reset_index(drop=True)
        df_countries["country_id"] = df_countries.index + 1 # Creating country_id column
        df_countries = df_countries[list(df_countries)[::-1]]

        id_dict["country_id"] = df_countries["country_id"].values.tolist()

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

        df_countries.to_csv(file_name[:-4] + '_countries.csv',index = False)

        df_store.to_csv(file_name[:-4] + '_stores.csv',index = False)
        



# Generating n random values in .sql file for the sale table

n = 10

# open file to remove content and append new content
sql_file_sale = open('./sql/fill_sales.sql', 'w+')

# Creating list of sales_id to use in order_status
id_dict["sales_id"] = list(range(1,n+1))

sale_date = list() # list with all the dates of the sales

for i in range(n):

    print('Adding line sale {}'.format(i+1))

    # Creating a dict with all the values required for the sale table

    dict_sale = {"sale_id" : str(i+1)}

    dict_sale["amount"] = str(round(random.uniform(0.4, 5.0),2)) # random value between 0.4€ and 5.0€

    start = datetime.date(year=2018, month=1, day=1)

    dict_sale["date_sale"] = "'" + Faker().date_time_between(start_date=start).strftime('%Y/%m/%d %I:%M %p') + "'" # Creates a str of a random date

    sale_date.append(dict_sale["date_sale"]) # Appending date to the list of dates

    # Selecting random values of product, user and store ids

    dict_sale["product_id"] = str(random.choice(id_dict["product_id"]))

    dict_sale["user_id"] = str(random.choice(id_dict["names_id"]))

    dict_sale["store_id"] = str(random.choice(id_dict["store_id"]))


    # Converting values and keys into string separated by commas

    placeholders = ', '.join(dict_sale.values())
    columns = ', '.join(dict_sale.keys())
    sql_sale = "INSERT INTO %s ( %s ) VALUES ( %s );\n" % ('sale', columns, placeholders)

    sql_file_sale.write(sql_sale)

# Generating n random values in .sql file for the order_status table

n = 15


# Same procedure as for the sale table

for i in range(n):
    print('Adding line order_status {}'.format(i+1))
    
    dict_order_st = {"order_status_id" : str(i+1)}

    sale_id = random.choice(id_dict["sales_id"]) 

    start = datetime.datetime.strptime(sale_date[sale_id-1][1:-1], '%Y/%m/%d %I:%M %p')

    dict_order_st["update_at"] = "'" + Faker().date_time_between(start_date=start).strftime('%Y/%m/%d %I:%M %p') + "'"

    dict_order_st["sale_id"] = str(sale_id)


    dict_order_st["status_name_id"] = str(random.choice(id_dict["status_id"]))

    placeholders = ', '.join(dict_order_st.values())
    columns = ', '.join(dict_order_st.keys())
    sql_sale = "INSERT INTO %s ( %s ) VALUES ( %s );\n" % ('order_status', columns, placeholders)

    sql_file_sale.write(sql_sale) 