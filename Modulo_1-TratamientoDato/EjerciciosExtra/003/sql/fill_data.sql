-- RANDOM DATA GENERATED PARTIALY USING https://www.mockaroo.com


-- import the file product
COPY product 
FROM '/data/product.csv' 
WITH (
    FORMAT csv,
    HEADER true
    );

-- import the file country
COPY country 
FROM '/data/cities_countries.csv' 
WITH (
    FORMAT csv,
    HEADER true
    );

-- import the file cities
COPY city 
FROM '/data/cities_modified.csv' 
WITH (
    FORMAT csv,
    HEADER true
    );

-- import the file stores
COPY store 
FROM '/data/cities_stores.csv' 
WITH (
    FORMAT csv,
    HEADER true
    );

-- import the file users
COPY users 
FROM '/data/names.csv' 
WITH (
    FORMAT csv,
    HEADER true
    );


-- import the file status_names
COPY status_name
FROM '/data/status.csv' 
WITH (
    FORMAT csv,
    HEADER true
    );


