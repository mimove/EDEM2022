## ENUNCIADOS Y SOLUCIONES DE LAS QUERIES A OBTENER

*Database dvdrental en [este enlace](<https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/>)


## Enunciado query 1

Proporciona una SQL que muestre los siguientes datos:
   
- Nombre Actor
  
- Apellido Actor
  

```sql
select a.first_name, a.last_name from actor a;
```

## Resultado

|first_name |last_name   |
|-----------|------------|
|Penelope   |Guiness     |
|Nick       |Wahlberg    |
|Ed         |Chase       |
|Jennifer   |Davis       |
|Johnny     |Lollobrigida|
|Bette      |Nicholson   |
|Grace      |Mostel      |
|Matthew    |Johansson   |
|Joe        |Swank       |
|Christian  |Gable       |
|Zero       |Cage        |
|Karl       |Berry       |
|Uma        |Wood        |


**Número de registros: 200**









<br>

## Enunciado query 2

Proporciona una SQL que muestre los siguientes datos:

- Nombre y apellido Actor,

- Titulo de la Película


```sql
select a.first_name,  a.last_name, f.title from film f
join film_actor fa
on f.film_id = fa.film_id
join actor a
on fa.actor_id = a.actor_id;
```


## Resultado 

|first_name|last_name|title                |
|----------|---------|---------------------|
|Penelope  |Guiness  |Academy Dinosaur     |
|Penelope  |Guiness  |Anaconda Confessions |
|Penelope  |Guiness  |Angels Life          |
|Penelope  |Guiness  |Bulworth Commandments|
|Penelope  |Guiness  |Cheaper Clyde        |
|Penelope  |Guiness  |Color Philadelphia   |
|Penelope  |Guiness  |Elephant Trojan      |
|Penelope  |Guiness  |Gleaming Jawbreaker  |
|Penelope  |Guiness  |Human Graffiti       |
|Penelope  |Guiness  |King Evolution       |
|Penelope  |Guiness  |Lady Stage           |
|Penelope  |Guiness  |Language Cowboy      |
|Penelope  |Guiness  |Mulholland Beast     |



**Número de registros: 5462**




<br>

## Enunciado query 3

Proporciona una SQL que muestre los siguientes datos:

- Nombre y apellido Actor

- Número de películas 

- Ordenar de mayor a menor

```sql
select a.first_name,  a.last_name, count(*) from film f
join film_actor fa
on f.film_id = fa.film_id
join actor a
on fa.actor_id = a.actor_id
group by a.first_name, a.last_name
order by 3 desc; 
```

## Resultado

|first_name|last_name  |count|
|----------|-----------|-----|
|Susan     |Davis      |54   |
|Gina      |Degeneres  |42   |
|Walter    |Torn       |41   |
|Mary      |Keitel     |40   |
|Matthew   |Carrey     |39   |
|Sandra    |Kilmer     |37   |
|Scarlett  |Damon      |36   |
|Vivien    |Basinger   |35   |
|Groucho   |Dunst      |35   |
|Val       |Bolger     |35   |
|Henry     |Berry      |35   |
|Angela    |Witherspoon|35   |
|Uma       |Wood       |35   |


**Número de registros: 199**


<br>








## Enunciado query 4


Proporciona una SQL que muestre los siguientes datos:

- Película

- Numero de veces alquilada(orden de mayor a menor)

```sql
select f.title, count(*) from rental r
join inventory i 
on r.inventory_id = i.inventory_id
join film f 
on i.film_id = f.film_id
group by f.title
order by 2 desc; 
```

## Resultado

|title              |count|
|-------------------|-----|
|Bucket Brotherhood |34   |
|Rocketeer Mother   |33   |
|Juggler Hardly     |32   |
|Ridgemont Submarine|32   |
|Scalawag Duck      |32   |
|Grit Clockwork     |32   |
|Forward Temple     |32   |
|Timberland Sky     |31   |
|Zorro Ark          |31   |
|Robbers Joon       |31   |
|Hobbit Alien       |31   |
|Network Peak       |31   |
|Apache Divine      |31   |

**Número de registros: 958**



<br>




## Enunciado query 5

Proporciona una SQL que muestre los siguientes datos:

- Película

- Dinero recaudado por película(ordenado)

```sql
select f.title, sum(p.amount) from payment p 
join rental r
on p.rental_id = r.rental_id
join inventory i
on r.inventory_id = i.inventory_id 
join film f 
on i.film_id = f.film_id
group by f.title
order by 2 desc;
```


## Resultado

|title            |sum   |
|-----------------|------|
|Telegraph Voyage |215.75|
|Zorro Ark        |199.72|
|Wife Turn        |198.73|
|Innocent Usual   |191.74|
|Hustler Party    |190.78|
|Saturday Lambs   |190.74|
|Titans Jerk      |186.73|
|Harry Idaho      |177.73|
|Torque Bound     |169.76|
|Dogma Family     |168.72|
|Pelican Comforts |165.77|
|Goodfellas Salute|164.75|
|Fool Mockingbird |162.79|

**Número de registros: 958**


<br>

## Enunciado query 6

Proporciona una SQL que muestre los siguientes datos:

- Nombre y apellido del mejor cliente (mayor gasto)


```sql
select c.first_name, c.last_name, sum(p.amount) from payment p
join customer c
on p.customer_id = c.customer_id
group by c.first_name, c.last_name
order by 3 desc
limit 1;
```



## Resultado

|first_name|last_name|sum   |
|----------|---------|------|
|Eleanor   |Hunt     |211.55|

**Número de registros: 1**


<br>

## Enunciado query 7

Proporciona una SQL que muestre los siguientes datos:

- Nombre y apellido del mejor cliente (mayor num alquileres)

```sql
select c.first_name, c.last_name, count(*) from rental r 
join customer c
on r.customer_id = c.customer_id
group by c.first_name, c.last_name
order by 3 desc
limit 1;
```


## Resultado

|first_name|last_name|count|
|----------|---------|-----|
|Eleanor   |Hunt     |46   |

**Número de registros: 1**