-- 3574317 registros hasta mayo
CREATE TABLE viajes_2019
SELECT * FROM registrobicis
WHERE YEAR(Fecha_Retiro) = 2019;

-- Consulta necesario para las gráficas en Tableau
SELECT viajes_2019.idRegistroBicis,
       viajes_2019.Edad_usuario,
       viajes_2019.Bici, 
       viajes_2019.Ciclo_Estacion_Retiro, 

       CONCAT(viajes_2019.Fecha_Retiro, ' ', viajes_2019.Hora_Retiro) AS Horario_Origen,
       CONCAT(viajes_2019.Fecha_Arribo, ' ', viajes_2019.Hora_Arribo) AS Horario_Destino,

       est_origen.Ubicacion AS Ubicacion_origen,
       est_origen.Latitud AS latitud_origen,
       est_origen.Longitud AS longitud_origen,
       est_origen.districtName AS districtname_origen,
       est_origen.nearbyStations AS nearbystations_origen,
       est_origen.slots AS slots_origen,
       alc_origen.Alcaldia AS Alcaldia_origen,

       est_destino.Ubicacion AS Ubicacion_destino,
       est_destino.Latitud AS latitud_destino,
       est_destino.Longitud AS longitud_destino,
       est_destino.districtName AS districtname_destino,
       est_destino.nearbyStations AS nearbystations_destino,
       est_destino.slots AS slots_destino,
       alc_destino.Alcaldia AS Alcaldia_destino

FROM viajes_2019
INNER JOIN estacion AS est_origen
  ON viajes_2019.Ciclo_Estacion_Retiro = est_origen.idEstacion
INNER JOIN estacion AS est_destino
  ON viajes_2019.Ciclo_Estacion_Arribo = est_destino.idEstacion
INNER JOIN alcaldias AS alc_origen
  ON est_origen.codAlcaldia = alc_origen.codigoAlcaldia
INNER JOIN alcaldias AS alc_destino
  ON est_destino.codAlcaldia = alc_destino.codigoAlcaldia;

/**
 * Tableau sólo permite subir 15 millones de registros en cada dataset.
 * Para realizar los mapas es necesario tener dos registros por cada viaje;
 * uno en donde se guarde la información de la estaión origen y otro en 
 * donde se guarde la información de la estación destino, pero como hacerlo de
 * esta forma excedería los 15 millones permitidos, cada año se divide en dos
 * tablas las cuales representan uno de los semestres del año.
 */
-- Viajes de origen primer semestre
CREATE VIEW rutas_origen_ene_jun_2019 AS
SELECT idRegistroBicis AS IDRegistro,
       Genero_Usuario AS `Género`,
       Edad_Usuario AS `Edad`,
       Bici AS `Bici`,
       Ciclo_Estacion_Retiro AS `Estación`,
       Fecha_Retiro AS `Fecha`,
       Hora_Retiro AS `Hora`,

       'Origen' AS TipoRuta,
       
       CONCAT(Ciclo_Estacion_Retiro, '_', Ciclo_Estacion_Arribo) AS Ruta,

       TIMEDIFF(
         CONCAT(Fecha_Arribo, ' ', Hora_Arribo),
         CONCAT(Fecha_Retiro, ' ', Hora_Retiro)
       ) AS Tiempo
FROM viajes_2019
WHERE MONTH(Fecha_Retiro) <= 6;
-- Para generar el segundo semestre del año sólo hay que cambiar esta condición
-- WHERE MONTH(Fecha_Retiro) > 6;

-- Viajes de destino primer semestre
CREATE VIEW rutas_destino_ene_jun_2019 AS
SELECT idRegistroBicis AS IDRegistro,
       Genero_Usuario AS `Género`,
       Edad_Usuario AS `Edad`,
       Bici AS `Bici`,
       Ciclo_Estacion_Arribo AS `Estación`,
       Fecha_Arribo AS `Fecha`,
       Hora_Arribo AS `Hora`,

       'Destino' AS TipoRuta,
       
       CONCAT(Ciclo_Estacion_Retiro, '_', Ciclo_Estacion_Arribo) AS Ruta,

       TIMEDIFF(
         CONCAT(Fecha_Arribo, ' ', Hora_Arribo),
         CONCAT(Fecha_Retiro, ' ', Hora_Retiro)
       ) AS Tiempo
FROM viajes_2019
WHERE MONTH(Fecha_Retiro) <= 6;
-- Para generar el segundo semestre del año sólo hay que cambiar esta condición
-- WHERE MONTH(Fecha_Retiro) > 6;

-- Vistas para unir los datos de origen y destino de un semestre
CREATE VIEW rutas_ene_jun_2019 AS
SELECT * FROM rutas_origen_ene_jun_2019
UNION ALL
SELECT * FROM rutas_destino_ene_jun_2019;

-- Vista que muestra información más detallada de la vista final de rutas generada
CREATE TABLE rutas_ene_jun_2019_mapas
SELECT viajes.`Género`,
       viajes.`Estación`,
       viajes.Edad,
       viajes.Bici,
       viajes.Fecha,
       viajes.Hora,
       viajes.idRegistro,
       viajes.Ruta,
       viajes.TipoRuta,
       viajes.Tiempo,

       estacion.Ubicacion,
       estacion.latitud,
       estacion.longitud,
       estacion.districtName,
       estacion.altitude,
       estacion.nearbyStations,
       estacion.stationType,
       estacion.slots,

       alcadias.Alcadia,

       metrica_ruta.distancia

FROM rutas_ene_jun_2019 AS viajes
INNER JOIN estacion ON viajes.`Estación` = estacion.idEstacion
INNER JOIN alcadias ON estacion.codAlcadia = alcadias.codigoAlcadia
INNER JOIN metrica_ruta ON viajes.Ruta = metrica_ruta.Ruta
WHERE viajes.Tiempo <= '23:59:59';
/*
  Se le agrega el WHERE porque el campo Tiempo tiene datos inválidos, 
  tiene campos de Tiempo más grandes que lo permitido
  Por ejemplo el registro con idRegistroBicis = 60622902
  SELECT TIMEDIFF('2019-04-12 17:05:33', '2019-01-15 18:56:49');
  que muestra el error:
  Truncated incorrect time value: '2086:08:44' y le asigna la hora 22:59:59.
  Hay 3574317 registros de 2019, de los cuales 3573929 tienen tiempos válidos,
  es decir, hay 388 con tiempos superiores a las '23:59:59'
  SELECT COUNT(*) FROM rutas_destino_ene_jun_2019
  WHERE Tiempo > '23:59:59';
*/