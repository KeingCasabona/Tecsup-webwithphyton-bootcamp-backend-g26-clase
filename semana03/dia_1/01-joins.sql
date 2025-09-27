SELECT * 
FROM profesores LEFT JOIN direcciones  -- LEFT JOIN devolverá todo lo de la izq y si tiene algua relación con la derecha
ON profesores.id=direcciones.profesor_id;

-- Sirve para cambiar la visualización en formato de tabla a un formato de tarjetas
\x

SELECT *
FROM profesores AS prof LEFT JOIN direcciones AS dir
ON prof.id = dir.profesor_id
ORDER BY prof.id ASC;

INSERT INTO direcciones (id, calle, numero, referencia, distrito, provincia, profesor_id) VALUES 
                        (DEFAULT, 'Los tulipanes', '120A', 'A dos cuadras de la cancha sintetica', 'Jesus Maria', 'Lima', null),
                        (DEFAULT, 'Los Jazmines', '1040A', null, 'Manuel Pastor', 'Moquegua', null),
                        (DEFAULT, 'Los Rosales', '2050A', 'Al frente del tambo', 'Cayma', 'Arequipa', null);


SELECT *
FROM profesores AS prof RIGHT JOIN direcciones AS dir
ON prof.id = dir.profesor_id
ORDER BY dir.profesor_id DESC;

-- 
SELECT *
FROM profesores AS prof FULL OUTER JOIN direcciones AS dir;
ON prof.id = dir.profesor_id;


-- 1. Mostrar los nombres de los profesores que vivan en Jesus Maria o Lima
SELECT prof.nombre FROM profesores AS prof INNER JOIN direcciones AS dir ON prof.id=dir.profesor_id
WHERE dir.distrito IN ('Jesus Maria', 'Lima');

-- 2. Mostrar los correos de los profesores que vivan en el distrito de Trujillo y la provincia de  Cajabamba
SELECT prof.correo FROM profesores AS prof INNER JOIN direcciones AS dir ON prof.id=dir.profesor_id
WHERE dir.distrito='Trujillo' AND dir.provincia='Cajabamba';

-- 3. Contar todos los profesores que tengan direcciones
SELECT count(DISTINCT prof.id) FROM profesores AS prof INNER JOIN direcciones AS dir ON prof.id=dir.profesor_id;

SELECT count(DISTINCT profesor_id) FROM direcciones;

-- 4. Contar todos los profesores que tengan 2 o mas direcciones
SELECT count(*) 
FROM (
SELECT prof.id FROM profesores AS prof INNER JOIN direcciones AS dir ON prof.id=dir.profesor_id
GROUP BY prof.id
-- En la clausula WHERE no se pueden utilizar funciones de agregación, cuando queremos usar condicionales con funciones
-- de agregación tenemos que usar la clausula HAVING
-- EL HAVING va después del GROUP BY y si se puede utilizar el having y el where en la misma consulta
HAVING count(dir.id)>=2);

-- 5. Contar todos los profesores que no tengan direcciones asociadas
SELECT count(*) FROM profesores AS prof LEFT JOIN direcciones AS dir ON prof.id=dir.profesor_id
WHERE dir.id IS NULL;