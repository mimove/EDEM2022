-- Create a new database called 'TutorialDB'
-- Connect to the 'master' database to run this snippet
USE master
GO
IF NOT EXISTS (
   SELECT name
   FROM sys.databases
   WHERE name = N'TutorialDB'
)
CREATE DATABASE [TutorialDB]
GO



--Proporciona una Select que de los Alumnos de Portugal 
/*
SELECT * FROM `sesion_sql.ALUMNOS` 
WHERE PAIS = 'Portugal';

*/

--Proporciona una Select de los Masters que contengan una D
/* 
SELECT * 
FROM `sesion_sql.MASTERS` 
WHERE NOM LIKE '%D%';

 */

--Proporciona una Select con los Nombre e email de los Alumnos cuyo ID esté entre 37 y 45

/*
SELECT NOM, EMAIL, ID
FROM `sesion_sql.ALUMNOS`
WHERE ID BETWEEN 37 AND 45
ORDER BY ID ASC;

*/


--Generar un insert en la tabla Alumnos

/*
INSERT INTO `sesion_sql.ALUMNOS`
VALUES(153,'David','Moreno','China','32 Sesamo Street', 'david.moreno@gmail.com');
*/


--Consultar que está el registro añadido
/*
SELECT *
FROM `sesion_sql.ALUMNOS`
WHERE ID = 153;

*/

--Actualiza país de origen del registro introducido a Mexico

/*
UPDATE `sesion_sql.ALUMNOS`
SET PAIS = 'Mexico'
WHERE ID = 153;

*/

--Consultar que está el registro añadido
/*
SELECT *
FROM `sesion_sql.ALUMNOS`
WHERE ID = 153;

*/

--Inserta una fila con tu asistencia al master de MDA

  -- Primero comprobamos si existe el nombre MDA en la tabla MASTERS

/*
SELECT NOM 
FROM `sesion_sql.MASTERS`
WHERE NOM = 'MDA';
*/
  -- Como no está, lo tenemos que añadir

/*
INSERT INTO `sesion_sql.MASTERS`
VALUES(77,'MDA');
*/

  -- Una vez que tengo añadido el nombre del máster puedo añadir el registro 153 con el registro 77 a la tabla ALU_MASTER

/*
INSERT INTO `sesion_sql.ALU_MASTER`
VALUES(20001, 153, 77);
*/

-- Comprobamos que está bien añadido
/*
SELECT *
FROM `sesion_sql.ALUMNOS` AL, `sesion_sql.ALU_MASTER` AM, `sesion_sql.MASTERS` M
WHERE AL.ID = 153
AND AL.ID = AM.ALU_ID
AND M.ID = AM.MAS_ID;
*/


--Borra los alumnos que no asistan a ningún master


/*
SELECT * FROM `sesion_sql.ALUMNOS`
WHERE ID NOT IN (SELECT ALU_ID FROM `sesion_sql.ALU_MASTER`);


DELETE FROM `sesion_sql.ALUMNOS`
WHERE ID NOT IN (SELECT ALU_ID FROM `sesion_sql.ALU_MASTER`);
*/


-- Borra los masters que no tengan alumnos

/*
SELECT * FROM `sesion_sql.MASTERS`
WHERE ID NOT IN (SELECT MAS_ID FROM `sesion_sql.ALU_MASTER`);

DELETE FROM `sesion_sql.MASTERS`
WHERE ID NOT IN (SELECT MAS_ID FROM `sesion_sql.ALU_MASTER`);
*/


-- Actualiza a Nulo los emails de los alumnos del master de MDA

/* SELECT * FROM `sesion_sql.ALUMNOS`
WHERE ID IN (
SELECT ALU_ID FROM `sesion_sql.ALU_MASTER` WHERE MAS_ID IN 
(SELECT ID FROM `sesion_sql.MASTERS` WHERE NOM = 'Skiba')
);


UPDATE `sesion_sql.ALUMNOS` 
SET EMAIL = 'null'
WHERE ID IN 
(SELECT ALU_ID FROM `sesion_sql.ALU_MASTER` WHERE MAS_ID IN 
(SELECT ID FROM `sesion_sql.MASTERS` WHERE NOM = 'Skiba')) */



-- Crea la siguiente tabla en tu schema:
-- ID: Clave primaria único
-- Mes: No nulo
-- Cantidad: No nulo
--Descripcion:  250 caracteres



/* CREATE TABLE `sesion_sql.GASTOS` (
  gastos_id int64,
  fecha STRING,
  cantidad float64,
  descripcion STRING
);
 */

/* INSERT INTO `sesion_sql.GASTOS`
VALUES(1, '2022/01/01', 100.4, 'Cuota Mensual'); */



-- Borrar Tabla

/* DROP TABLE `sesion_sql.GASTOS` */




-- Query que haga Join y muestre cada alumno el master que tiene asociado

/* SELECT A.Nom, M.Nom FROM `sesion_sql.ALUMNOS` A
LEFT JOIN `sesion_sql.ALU_MASTER` AL
ON A.ID = AL.ALU_ID
LEFT JOIN `sesion_sql.MASTERS` M
ON AL.MAS_ID = M.id; */



