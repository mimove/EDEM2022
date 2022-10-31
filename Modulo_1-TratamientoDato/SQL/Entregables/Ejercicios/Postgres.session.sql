/* -- Proporciona una SQL que muestre los siguientes datos:
-- Nombre Actor
-- Apellido Actor


select a.first_name, a.last_name from actor a;

select count(*) from (select a.first_name, a.last_name from actor) as a; 


-- Proporciona una SQL que muestre los siguientes datos:
-- Nombre y apellido Actor,
-- Titulo de la Película

select a.first_name,  a.last_name, f.title from actor a
join film_actor fa
on a.actor_id = fa.actor_id
join film f
on fa.film_id = f.film_id;

/*
select count(*) from (
select a.first_name,  a.last_name, f.title from actor a
join film_actor fa
on a.actor_id = fa.actor_id
join film f
on fa.film_id = f.film_id ) as count2;
*/


-- Proporciona una SQL que muestre los siguientes datos:
-- Nombre y apellido Actor
-- Número de películas 
-- Ordenar de mayor a menor


select a.first_name,  a.last_name, count(*) from actor a
join film_actor fa
on a.actor_id = fa.actor_id
join film f
on fa.film_id = f.film_id
group by a.first_name, a.last_name
order by 3 desc;



/* select count(*) from (
select a.first_name,  a.last_name, count(*) from actor a
join film_actor fa
on a.actor_id = fa.actor_id
join film f
on fa.film_id = f.film_id
group by a.first_name, a.last_name
order by 3 desc) as count3; 
 */

-- Proporciona una SQL que muestre los siguientes datos:
-- Película
-- Dinero recaudado por película(ordenado)
/* 
select f.title, sum(p.amount) from film f
join inventory i
on f.film_id = i.film_id
join rental r
on i.inventory_id = r.inventory_id
join payment p
on r.rental_id = p.rental_id
group by f.title
order by 2 desc */


