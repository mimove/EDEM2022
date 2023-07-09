-- SELECT a.idAlumno, a.nombre, a.apellidos, a.edad, a.dni, a.fechaNacimiento
-- FROM alumnos a
-- LEFT JOIN alumnos_master am ON a.idAlumno = am.idAlumnoAM
-- LEFT JOIN master m ON am.idMasterAM = m.idMaster
-- WHERE m.nombre = 'Yakijo';


select * from alumnos where lower(apellidos) like "%n%" ;

-- Query all alumnos with nombre less than 5 characters
select * from alumnos where length(nombre) < 5;




-- alter table alumnos add column segundoNomber varchar(255);


-- update the segundoNomber with random names from other alumnos in the table using mysql for all alumnos
CREATE TEMPORARY TABLE tmp SELECT nombre FROM alumnos ORDER BY RAND() LIMIT 1;

UPDATE alumnos SET segundoNomber = (SELECT nombre FROM tmp);

DROP TEMPORARY TABLE tmp;




select "A" as Letra, count(nombre) as Total from alumnos where lower(apellidos) like "%a%" 
union select "B" as Letra, count(nombre) as Total from alumnos where lower(apellidos) like "%b%";




select "A+B" as Letra, sum(total) as Suma from (select "A" as Letra, count(nombre) as Total from alumnos where lower(apellidos) like "%a%" 
union select "B" as Letra, count(nombre) as Total from alumnos where lower(apellidos) like "%b%") as total;




select apellidos, count(*) as total from alumnos group by apellidos ORDER BY total DESC limit 1;


select * from (select apellidos, count(*) as total from alumnos group by apellidos) as table1 where table1.total > 1;

select apellidos, count(*) as total from alumnos group by apellidos having total > 1 ORDER BY total DESC limit 1;


select apellidos from alumnos as a1 WHERE EXISTS (select apellidos from alumnos as a2 where a1.apellidos = a2.apellidos);