-- Consulta necesario para las gráficas en Tableau,
-- aquí se genera con consultas SQL pero a tableau se le pasa la tabla
-- base y se hace ahí mismo los JOINs necesarios
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