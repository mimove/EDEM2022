DROP TABLE IF EXISTS alumnos_master;
DROP TABLE IF EXISTS alumnos;
DROP TABLE IF EXISTS master;

CREATE TABLE IF NOT EXISTS alumnos (
    idAlumno INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(45) NOT NULL UNIQUE,
    apellidos VARCHAR(45) NOT NULL,
    edad INT NOT NULL,
    dni VARCHAR(9),
    fechaNacimiento DATE,
    PRIMARY KEY (idAlumno)
);

CREATE TABLE IF NOT EXISTS master (
    idMaster INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    precio NUMERIC(10,2) NOT NULL,
    year VARCHAR(4) NOT NULL,
    UNIQUE (nombre, year)
);

CREATE TABLE IF NOT EXISTS alumnos_master (
    idAlumnoAM INT NOT NULL,
    idMasterAM INT NOT NULL,
    PRIMARY KEY (idAlumnoAM, idMasterAM),
    CONSTRAINT fk_alumnos_master_alumnos
        FOREIGN KEY (idAlumnoAM)
        REFERENCES alumnos (idAlumno),
    CONSTRAINT fk_alumnos_master_master
        FOREIGN KEY (idMasterAM)
        REFERENCES master (idMaster)
);

-- Inserting mock data for alumnos
INSERT INTO alumnos (nombre, apellidos, edad, dni, fechaNacimiento) VALUES
('John', 'Doe', 20, 'DNI1', '2003-01-01'),
('Jane', 'Smith', 21, 'DNI2', '2002-02-02'),
('Alice', 'Johnson', 22, 'DNI3', '2001-03-03'),
('Bob', 'Brown', 23, 'DNI4', '2000-04-04'),
('Charlie', 'Williams', 24, 'DNI5', '1999-05-05'),
('Diana', 'Jones', 25, 'DNI6', '1998-06-06'),
('Ethan', 'Davis', 26, 'DNI7', '1997-07-07'),
('Fiona', 'Miller', 27, 'DNI8', '1996-08-08'),
('George', 'Wilson', 28, 'DNI9', '1995-09-09'),
('Hannah', 'Moore', 29, 'DNI10', '1994-10-10'),
('Ivan', 'Taylor', 30, 'DNI11', '1993-11-11'),
('Julia', 'Anderson', 31, 'DNI12', '1992-12-12'),
('Kevin', 'Thomas', 32, 'DNI13', '1991-01-13'),
('Laura', 'Jackson', 33, 'DNI14', '1990-02-14'),
('Mike', 'White', 34, 'DNI15', '1989-03-15'),
('Nancy', 'Harris', 35, 'DNI16', '1988-04-16'),
('Oscar', 'Martin', 36, 'DNI17', '1987-05-17'),
('Patricia', 'Thompson', 37, 'DNI18', '1986-06-18'),
('Quentin', 'Garcia', 38, 'DNI19', '1985-07-19'),
('Rita', 'Martinez', 39, 'DNI20', '1984-08-20');

-- Inserting mock data for masters
INSERT INTO master (nombre, precio, year) VALUES
('Master1', 1000.00, '2023'),
('Master2', 2000.00, '2023'),
('Master3', 3000.00, '2023'),
('Master4', 4000.00, '2023'),
('Master5', 5000.00, '2023');

-- Linking students to Masters ensuring that each master has at least one student
INSERT INTO alumnos_master (idAlumnoAM, idMasterAM) VALUES
((SELECT idAlumno FROM alumnos WHERE nombre = 'John'), 1),
((SELECT idAlumno FROM alumnos WHERE nombre = 'Jane'), 2),
((SELECT idAlumno FROM alumnos WHERE nombre = 'Alice'), 3),
((SELECT idAlumno FROM alumnos WHERE nombre = 'Bob'), 4),
((SELECT idAlumno FROM alumnos WHERE nombre = 'Charlie'), 5);


