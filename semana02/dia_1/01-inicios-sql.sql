-- Script: Archivo que se usa para ser ejecutado en la base de datos
-- SQL: Structured Query Language

-- DDL: Data Definition Language
-- CREATE: Crear entidades(BASE DE DATOS, TABLAS, USUARIOS, TRIGGER)
-- ALTER: Alterar (modificar) tablas, base de datos, usuarios, etc
-- DROP: Eliminar entidades (tablas, base de datos, usuarios)
-- TRUNCATE: Eliminar la data dentro de la tabla pero sin eliminar la tabla
-- RENAME: Cambiar el nombre de una entidad (BASE DE DATOS, TABLA, USUARIOS, ETC)

CREATE DATABASE pruebas;


-- NOTA: Cuando usemos alguno de los comandos de PSQL no es necesario colocar  ";" al final
-- Lista las bases de datos que tenemos en el servidor
\l

-- Cambiamos a la base de datos que vamos a utilizar
\c pruebas

-- \! Sirve para poder ejecutar cualquier comando del sistema operativo dentro del psql
-- cls en windows
-- clear en mac es para limpiar la terminal
\! clear

CREATE TABLE personas(
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT,
    correo TEXT UNIQUE, -- El correo jamas se va a repetir
    fecha_nacimiento TIMESTAMP -- Sirve para guardar el tiempo, adicional a ello se le puede indicar si queremos usar la zona horaria o no
);

-- DML: Data Manipulation Language
-- INSERT: Ingresar nuevos datos de las tablas
-- SELECT: Obtener la información de las tablas
-- UPDATE: Actualizar la información de las tablas
-- DELETE: Eliminar la información de las tablas
INSERT INTO personas (nombre, apellido, correo, fecha_nacimiento) VALUES
                    ('Keing', null, 'ederiveroman@gmail.com', '1992-08-01');

INSERT INTO personas VALUES(DEFAULT, 'Sebastian', null, 'keing@gmail.com','2003-1-07');

INSERT INTO personas VALUES(DEFAULT, 'Keing', 'Limache', 'Keing@gmail.com','2000-1-04'),
                            (DEFAULT, 'Luis', 'Salas','Lsalas@gmail.com','2003-09-1');

SELECT id, nombre FROM personas;            

SELECT * FROM personas;

SELECT * FROM personas WHERE id=3;

SELECT * FROM personas WHERE id>3 AND apellido='Salas';

SELECT * FROM personas WHERE id>2 AND id<=4;
