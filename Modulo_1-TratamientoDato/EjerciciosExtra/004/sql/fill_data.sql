-- RANDOM DATA GENERATED PARTIALY USING https://www.mockaroo.com



-- import the file product

LOAD DATA  INFILE '/var/lib/mysql-files/product.csv' 
INTO TABLE product 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- import the file country

LOAD DATA  INFILE '/var/lib/mysql-files/cities_countries.csv' 
INTO TABLE country
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


-- import the file cities

LOAD DATA  INFILE '/var/lib/mysql-files/cities_modified.csv' 
INTO TABLE city
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;



-- import the file stores

LOAD DATA  INFILE '/var/lib/mysql-files/cities_stores.csv' 
INTO TABLE store
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


-- import the file users

LOAD DATA  INFILE '/var/lib/mysql-files/names.csv' 
INTO TABLE users
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


-- import the file status_name

LOAD DATA  INFILE '/var/lib/mysql-files/status.csv' 
INTO TABLE status_name
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


