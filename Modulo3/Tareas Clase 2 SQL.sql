// Paso 1:

CREATE TABLE Lista_Alumnos (
    Lista INT PRIMARY KEY,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100),
    Edad INT,
    Celular INT
);


//Paso 2:

ALTER TABLE Lista_Alumnos
ADD COLUMN Email VARCHAR(120)

// Paso 3:

ALTER TABLE Lista_Alumnos
DROP COLUMN Edad;

// Pase 4:

INSERT INTO Lista_Alumnos (Lista, Nombre, Apellido, Celular, Email, Edad) VALUES
(1, 'Jose', 'Colina', 0412-9034040, 'josecolinadel7@gmail.com', 24),
(2, 'Sandy', 'Ordoñes', 0412-1234567, 'sandyordoñes@gmail.com', 30),
(3, 'Angel', 'Delmoral', 0416-1234567, 'angeldelmoral@gmail.com', 22),
(4, 'Javier', 'Mavarez', 0412-3216549, 'javiermavarez@gmail.com', 23),
(5, 'Maria', 'Paz', 0426-7894561, 'mariapaz@gmail.com', 21),
(6, 'Andres', 'Diaz', 0424-1234567, 'andresdiaz@gmail.com', 26);

// Paso 5:

UPDATE Lista_Alumnos
SET Edad = 24
WHERE Lista = 1;

// Paso 6:

DELETE FROM Lista_Alumnos
WHERE Lista = 2

// Paso 7:

SELECT Nombre, Apellido, Celular FROM Lista_Alumnos;

// Paso 8:

SELECT * FROM Lista_Alumnos ORDER BY Nombre ASC