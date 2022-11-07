-- 1. Proporciona una SQL que muestre los siguientes datos:
-- Nombre Actor
-- Apellido Actor


select a.first_name, a.last_name from actor a;

select count(*) from (select a.first_name, a.last_name from actor a) as a;  




-- 2. Proporciona una SQL que muestre los siguientes datos:
-- Nombre y apellido Actor,
-- Titulo de la Película

select a.first_name,  a.last_name, f.title from film f
join film_actor fa
on f.film_id = fa.film_id
join actor a
on fa.actor_id = a.actor_id;
 

select count(*) from (
select a.first_name,  a.last_name, f.title from film f
join film_actor fa
on f.film_id = fa.film_id
join actor a
on fa.actor_id = a.actor_id) as count2;



-- 3. Proporciona una SQL que muestre los siguientes datos:
-- Nombre y apellido Actor
-- Número de películas 
-- Ordenar de mayor a menor


select a.first_name,  a.last_name, count(*) from film f
join film_actor fa
on f.film_id = fa.film_id
join actor a
on fa.actor_id = a.actor_id
group by a.first_name, a.last_name
order by 3 desc; 



select count(*) from (
select a.first_name,  a.last_name, count(*) from film f
join film_actor fa
on f.film_id = fa.film_id
join actor a
on fa.actor_id = a.actor_id
group by a.first_name, a.last_name
order by 3 desc) as count3; 
 


-- 4. Proporciona una SQL que muestre los siguientes datos:
-- Película
-- Numero de veces alquilada(orden de mayor a menor)

select f.title, count(*) from rental r
join inventory i 
on r.inventory_id = i.inventory_id
join film f 
on i.film_id = f.film_id
group by f.title
order by 2 desc; 



select count(*) from(
select f.title, count(*) from rental r
join inventory i 
on r.inventory_id = i.inventory_id
join film f 
on i.film_id = f.film_id
group by f.title
order by 2 desc) as count4;



-- 5. Proporciona una SQL que muestre los siguientes datos:
-- Película
-- Dinero recaudado por película(ordenado)


select f.title, sum(p.amount) from payment p 
join rental r
on p.rental_id = r.rental_id
join inventory i
on r.inventory_id = i.inventory_id 
join film f 
on i.film_id = f.film_id
group by f.title
order by 2 desc;


select count(*) from (
select f.title, sum(p.amount) from payment p 
join rental r
on p.rental_id = r.rental_id
join inventory i
on r.inventory_id = i.inventory_id 
join film f 
on i.film_id = f.film_id
group by f.title
order by 2 desc) as count5;


-- 6. Proporciona una SQL que muestre los siguientes datos:
-- Nombre y apellido del mejor cliente (mayor gasto)


select c.first_name, c.last_name, sum(p.amount) from payment p
join customer c
on p.customer_id = c.customer_id
group by c.first_name, c.last_name
order by 3 desc
limit 1;



-- 7. Proporciona una SQL que muestre los siguientes datos:
-- Nombre y apellido del mejor cliente (mayor num alquileres)


select c.first_name, c.last_name, count(*) from rental r 
join customer c
on r.customer_id = c.customer_id
group by c.first_name, c.last_name
order by 3 desc
limit 1;