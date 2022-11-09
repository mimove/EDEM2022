select * from film;
select * from film where description like '%Drama%';


-- insertar datos 

select * from actor;

insert into actor (first_name, last_name) values ('ALAN', 'SASTRE');


select * from customer;


insert into address (address, district, city_id, postal_code, phone) values ('Calle false', 'Nueva América', 300, '28004', '123453252');

select * from address;

insert into customer (store_id, first_name, last_name, email, address_id, activebool)
values (1, 'CUSTOMER NEW', 'LASTNAME EXAMPLE', 'customer@gmail.com', 606, true);