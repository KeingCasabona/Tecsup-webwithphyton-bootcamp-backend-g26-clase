-- Los select es la forma en la cual podemos obtener la información

-- LIKE: Se usa para tener similitudes por una parte del texto
SELECT * FROM personas WHERE nombre LIKE 'in';--nombre exacto
SELECT * FROM personas WHERE nombre LIKE '%in%'; --tiene que estar estas silabas en cuarquier parte de la palabra

INSERT INTO personas (nombre, apellido, correo, fecha_nacimiento) VALUES
                    ('Keing', null, 'keing1408@gmail.com', '1992-09-01');

SELECT * FROM personas WHERE nombre LIKE '%ke%';

-- ILIKE: Sera como un like pero insensible a mayus y minus en el texto a buscar
SELECT * FROM personas WHERE nombre ILIKE '%ke%';

-- Mostrar todas las personas que tengan correos gmail o outlook
SELECT * FROM personas WHERE correo LIKE '%gmail%' OR correo LIKE '%outlook%';

-- Si queremos hacer la busqueda de varios elementos de una misma columna pero por una busqueda exacta
SELECT * FROM personas WHERE nombre IN ('Luis', 'Sebastian');
SELECT * FROM personas WHERE id IN (2,4,5);

-- Si al usar el like o ilike se desea ver en que posicion exacta esta el valor a buscar se usa:
SELECT * FROM personas WHERE apellido ILIKE '__m%';