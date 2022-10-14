# Session ING-005 Get familiar with Notebooks: Zeppelin
# 3: Parameters

[![N|Apache](https://www.nobleprog.es/sites/hitrahr/files/category_images/height100_scale/apache_zeppelin_training.png?t=0b7d8a8e)](https://zeppelin.apache.org/)

#### Problem statement

During this part of the session we will learn how to make notebooks reusable using global variables, this will allow us to create a notebook that can be re-run based on input parameters.



0) You will need to copy the amazon.csv in the data folder into the data inside the container, place your console in the folder where the amazon.csv file is and execute the following:

Before running this ¡¡¡CAUTION!!! log into the image and create the folder data.

```bash
docker exec -it zeppelin_single /bin/bash
mkdir data
exit
docker cp amazon.csv zeppelin_single:/zeppelin/data
```



1) Create a new Notebook named "Parameters"

2) On first Cell paste the following code:

```bash
%spark 

spark
.read
.option("header", "true")
.option("delimiter", ",")
.option("inferSchema", "true")
.csv("data/amazon.csv")
.registerTempTable("amazon")
```

With this code we are loading our sample data.

3) In a cell perform a query to retrieve all the products containing the word "hobby"

4) Your code should be something like:

```bash
%spark.sql
select * from amazon where product_name like  '%hobby%'
```
5) In order to avoid repeating, Zeppelin provides **Dynamic Forms**

#### Creating Parameters

1) Let's create a cell to retrieve a parameter, use the following code

```bash
%spark
z.angularBind("numberReviews",z.input("Enter Number of Reviews"))
```
 2) Check that your code is correct with a new cell:
```bash
%spark
println(z.angular("numberReviews"))
```
3) Once you have checked this variable can be used in other cells:
```bash
%spark
z.show(sqlContext.sql("""
SELECT * FROM amazon WHERE number_of_reviews = """ + z.angular("numberReviews") + """
"""
))
```


```bash
%spark.sql
select * from amazon where number_of_reviews >= '${numberReviews}'
```
#### Creating Parameters

Different types of parameters:

##### Input Form
```bash
%spark
println("Hello "+z.textbox("name"))
```

![N|Apache](https://zeppelin.apache.org/docs/0.8.2/assets/themes/zeppelin/img/screenshots/form_input_prog.png)

##### Select Form
```bash
%spark
println("Hello "+z.select("day", Seq(("1","mon"),("2","tue"),("3","wed"),("4","thurs"),("5","fri"),("6","sat"),("7","sun"))))
```

![N|Apache](https://zeppelin.apache.org/docs/0.8.2/assets/themes/zeppelin/img/screenshots/form_select_prog.png)

##### CheckBox 
```bash
%spark
val options = Seq(("apple","Apple"), ("banana","Banana"), ("orange","Orange"))
println("Hello "+z.checkbox("fruit", options).mkString(" and "))`
```

![N|Apache](https://zeppelin.apache.org/docs/0.8.2/assets/themes/zeppelin/img/screenshots/form_checkbox_prog.png)
