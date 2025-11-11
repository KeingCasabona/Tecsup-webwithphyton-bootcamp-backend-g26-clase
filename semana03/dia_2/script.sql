-- Crear una tabla llamada productos que tenga la siguiente info:
-- Id autoincrementable PK
-- Nombre text no puede ser nulo
-- Precio flotante no puede ser nulo
-- Observacion text
-- Fecha_caducidad timestamp
-- Fecha_creacion timestamp y cuyo valor por defecto sera now()

CREATE TABLE productos(
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio FLOAT NOT NULL,
    observacion TEXT,
    fecha_caducidad TIMESTAMP,
    fecha_creacion TIMESTAMP DEFAULT now()
)