-- Retornará el número toral de registros
SELECT count(*) FROM profesores;

-- Si queremos agregar una columna  'normal' tenemos que obigatoriamente usar el GROUP BY para que realice
-- primero la agrupación de estos elementos y luego proceda con el conteo de los mismos:
SELECT count(*), activo FROM profesores GROUP BY activo;

SELECT * FROM profesores ORDER BY nombre ASC; -- ASC:A-Z | DESC:Z-A

-- Si tenemos dos ordenamientos el segundo entrará a funcionar si hay dos coincidencias con el primero:
SELECT * FROM profesores ORDER BY apellidos ASC, nombre ASC; 

-- PAGINACIÓN:
-- OFFSET: Indica cuantos registros me tengo que saltar
SELECT * FROM profesores OFFSET 5;

-- LIMIT: Indica cuantos registros quiero mostrar
SELECT * FROM profesores LIMIT 5;


SELECT * FROM profesores LIMIT 5 OFFSET 0; --Selecciono los 5 primeros registros

SELECT * FROM profesores LIMIT 5 OFFSET 5; --Selecciono los 5 segundos registros 

SELECT * FROM profesores LIMIT 5 OFFSET 10;


-- Orden para utilizar SELECT con todas sus opciones:
SELECT column1, column2, count(*)
FROM tabla
WHERE condicional1 AND condicional2 OR condicional3
GROUP BY columna1, columna2
ORDER BY columna1 ASC, columna2 DESC
LIMIT #
OFFSET #;

-- Mostrar todos los profesores que esten activos:

-- Mostrar todos los profesores que tengan una fecha de contratación del año pasado:

-- Mostrar todos los profesores que se llamen Susan o se apelliden King:

-- Mostrar todos los profesores cuyo correo sea hotmail.com o outlookl.com o example.com:

-- Mostrar el total de profesores

