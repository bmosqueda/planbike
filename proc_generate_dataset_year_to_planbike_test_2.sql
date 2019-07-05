DROP TABLE IF EXISTS test_rutas_ene_jun_2019;

CREATE TABLE test_rutas_ene_jun_2019 AS 

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
WHERE MONTH(Fecha_Retiro) <= 6

UNION ALL

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