-- 11 ms
-- 252 ms
-- 3 m 11 s 563 ms
-- 2 m 58 s 794 ms

-- 6 minutos

DROP TABLE IF EXISTS viajes_2019;

CREATE TABLE viajes_2019
SELECT * FROM registrobicis
WHERE YEAR(Fecha_Retiro) = 2019;

DROP TABLE IF EXISTS test_rutas_ene_jun_2019;

CREATE TABLE test_rutas_ene_jun_2019(
  IDRegistro INT NOT NULL,
  `Género` VARCHAR(45),
  Edad INT,
  Bici INT,
  `Estación` INT,
  Fecha DATE,
  Hora TIME,
  TipoRuta VARCHAR(25),
  Ruta VARCHAR(45),
  Tiempo TIME
);

INSERT INTO 
  test_rutas_ene_jun_2019 (
    IDRegistro,
    `Género`,
    Edad,
    Bici,
    `Estación`,
    Fecha,
    Hora,
    TipoRuta,
    Ruta,
    Tiempo
  )
SELECT idRegistroBicis AS IDRegistro,
       Genero_Usuario AS `Género`,
       Edad_Usuario AS `Edad`,
       Bici AS `Bici`,
       Ciclo_Estacion_Retiro AS `Estación`,
       Fecha_Retiro AS `Fecha`,
       Hora_Retiro AS `Hora`,

       'Origen' AS TipoRuta,
       
       CONCAT(Ciclo_Estacion_Retiro, '_', Ciclo_Estacion_Arribo) AS Ruta,

       (CASE 
         WHEN are_valid_dates_diff(
                Fecha_Retiro,
                Hora_Retiro,
                Fecha_Arribo,
                Hora_Arribo
              ) THEN
                 TIMEDIFF(
                   CONCAT(Fecha_Arribo, ' ', Hora_Arribo),
                   CONCAT(Fecha_Retiro, ' ', Hora_Retiro)
                 ) 
         ELSE '00:00:00'
       END) AS Tiempo
FROM viajes_2019
WHERE MONTH(Fecha_Retiro) <= 6;


INSERT INTO 
  test_rutas_ene_jun_2019 (
    IDRegistro,
    `Género`,
    Edad,
    Bici,
    `Estación`,
    Fecha,
    Hora,
    TipoRuta,
    Ruta,
    Tiempo
  )
SELECT idRegistroBicis AS IDRegistro,
       Genero_Usuario AS `Género`,
       Edad_Usuario AS `Edad`,
       Bici AS `Bici`,
       Ciclo_Estacion_Arribo AS `Estación`,
       Fecha_Arribo AS `Fecha`,
       Hora_Arribo AS `Hora`,

       'Destino' AS TipoRuta,
       
       CONCAT(Ciclo_Estacion_Retiro, '_', Ciclo_Estacion_Arribo) AS Ruta,

       (CASE 
         WHEN are_valid_dates_diff(
                Fecha_Retiro,
                Hora_Retiro,
                Fecha_Arribo,
                Hora_Arribo
              ) THEN
                 TIMEDIFF(
                   CONCAT(Fecha_Arribo, ' ', Hora_Arribo),
                   CONCAT(Fecha_Retiro, ' ', Hora_Retiro)
                 ) 
         ELSE '00:00:00'
       END) AS Tiempo
FROM viajes_2019
WHERE MONTH(Fecha_Retiro) <= 6;