-- Explorar tablas

select * from actor;

select * from actor where last_name = 'WAHLBERG';


select * from address where district = 'California' and postal_code = '17886' or postal_code = '2299';



select * from category where name = 'Action';


select * from city where country_id = 87;


select * from city where city like 'A%';


select * from customer;

select * from customer where activebool = false;

update customer set activebool = true where customer_id = 1;

select * from film;

select f.film_id, f.title, a.first_name from film as f 
join film_actor as fm 
on fm.film_id = f.film_id
join actor as a 
on a.actor_id = fm.actor_id
order by f.film_id ASC
;