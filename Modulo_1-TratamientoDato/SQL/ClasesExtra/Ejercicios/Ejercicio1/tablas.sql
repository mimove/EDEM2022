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


CREATE TABLE 

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





