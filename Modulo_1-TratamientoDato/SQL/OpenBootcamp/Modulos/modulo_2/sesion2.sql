-- Sentencias DML: Data Manipulation Language 

-- 1. Consultas o recuperación de datos

select * from employees;

select id, name from employees;

-- Filtrar filas

select * from employees where name = 'Pepe';

select * from employees where married = false;

select * from employees where married = false and name = 'Pepe';

-- 2. Inserción de datos

insert into employees(name,email) values ('Juan','juan@gmail.com');

insert into employees(name, email, married, genre, salary) 
values('antonio', 'antonio3@gmail.com', true, 'M', 12121.25);

-- 3. Actualizar o editar

update employees set birth_date = '1979-3-2'  where id = 2 returning *;

update employees set married = true, start_at = '10:30:00'  where email = 'juan@gmail.com';


-- 4. Borrar 

delete from employees where id = 1;

delete from employees where salary is null;




