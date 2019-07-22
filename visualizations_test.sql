SELECT DISTINCT MONTH(Fecha_Retiro)
FROM registrobicis
WHERE YEAR(Fecha_Retiro) = 2019;

SELECT COUNT(*) FROM registrobicis
WHERE MONTH(Fecha_Retiro) > 6;

SELECT COUNT(*) FROM viajes_2019
WHERE MONTH(Fecha_Retiro) > 6;

-- 8,539,906
SELECT COUNT(*) FROM registrobicis2018;

-- 4,270,031
SELECT COUNT(*) FROM viajes_2019;

-- Enero: 697,161
SELECT COUNT(*) FROM viajes_2019 WHERE MONTH(Fecha_Retiro) = 1;

-- Mayo: 750,906
SELECT COUNT(*) FROM viajes_2019 WHERE MONTH(Fecha_Retiro) = 5;

-- Junio: 695,639
SELECT COUNT(*) FROM viajes_2019 WHERE MONTH(Fecha_Retiro) = 6;

-- 8,540,062
SELECT COUNT(*) FROM rutas_ene_jun_2019;

-- 0
SELECT COUNT(*) FROM rutas_jul_dic_2019;

-- Visualizaciones como origen de viaje
  -- 1) CICLOESTACIONES MÁS UTILIZADAS COMO ORIGEN EN VIAJES A PARTIR DE UNA ALCALDÍA O COLONIA
  -- Viajes de la alcaldía cuauhtémoc los lunes de febrero de 2019
  SELECT MONTH(Fecha_Arribo) AS mes,
         Ciclo_Estacion_Arribo,
         DAYOFWEEK(Fecha_Arribo) AS dia_semana,
         DAYOFMONTH(Fecha_Arribo) AS dia_mes,
         COUNT(*) AS total
  FROM viajes_2019 AS viajes
  INNER JOIN estacion ON viajes.Ciclo_Estacion_Arribo = estacion.idEstacion
  WHERE DAYOFWEEK(Fecha_Arribo) = 2 
        AND MONTH(Fecha_Arribo) = 2
        AND codAlcadia = 'CHT'
  GROUP BY mes, Ciclo_Estacion_Arribo
  ORDER BY total DESC;

  -- 2) GRÁFICA CON LA FRECUENCIA REGULAR DE VIAJES EN UNA CICLOESTACIÓN COMO ORIGEN
  -- No implementado aún

  -- 3) PATRONES DE USO POR HORA POR DÍAS DE SEMANA O DÍAS ENTRE-SEMANA O DÍAS DE FIN DE SEMANA POR ORIGEN
  -- Viajes por cada hora del día todos los lunes de febrero en la alcadía de cuauhtémoc
  SELECT MONTH(Fecha_Arribo) AS mes,
         DAYOFMONTH(Fecha_Arribo) AS dia_mes,
         HOUR(Hora_Arribo) AS hora,
         Ciclo_Estacion_Arribo,
         COUNT(*) AS total
  FROM viajes_2019 AS viajes
  INNER JOIN estacion ON viajes.Ciclo_Estacion_Arribo = estacion.idEstacion
  WHERE DAYOFWEEK(Fecha_Arribo) = 2 
        AND MONTH(Fecha_Arribo) = 2 
        AND codAlcadia = 'CHT'
  GROUP BY mes, dia_mes, hora;

  -- 4) PATRONES EN CICLOESTACIONES COMO ORIGEN DE VIAJES, POR HORAS, EN DIAS DE SEMANA Y POR COLONIAS
  -- Viajes por cada hora del día todos los lunes de febrero en la colonia Buenavista
  SELECT MONTH(Fecha_Arribo) AS mes,
         DAYOFMONTH(Fecha_Arribo) AS dia_mes,
         HOUR(Hora_Arribo) AS hora,
         Ciclo_Estacion_Arribo,
         COUNT(*) AS total
  FROM viajes_2019 AS viajes
  INNER JOIN estacion ON viajes.Ciclo_Estacion_Arribo = estacion.idEstacion
  WHERE DAYOFWEEK(Fecha_Arribo) = 2 
        AND MONTH(Fecha_Arribo) = 2 
        AND districtName = 'Buenavista'
  GROUP BY mes, dia_mes, hora;

  -- 5) PATRONES EN UNA CICLOESTACIÓN COMO ORIGEN DE VIAJES, POR HORAS Y EN DIAS DE SEMANA
  -- Viajes por cada hora del día todos los lunes de febrero en la estación 271 Av. Central J. Meneses
  SELECT MONTH(Fecha_Arribo) AS mes,
         DAYOFMONTH(Fecha_Arribo) AS dia_mes,
         HOUR(Hora_Arribo) AS hora,
         Ciclo_Estacion_Arribo,
         COUNT(*) AS total
  FROM viajes_2019 AS viajes
  WHERE DAYOFWEEK(Fecha_Arribo) = 2 
        AND MONTH(Fecha_Arribo) = 2 
        AND Ciclo_Estacion_Arribo = 271
  GROUP BY mes, dia_mes, hora;

-- Visualizaciones como destino de viaje
  -- 1) CICLOESTACIONES MÁS UTILIZADAS COMO DESTINO EN VIAJES A PARTIR DE UNA ALCALDÍA O COLONIA
  -- Visualizaciones de la alcaldía cuauhtémoc los lunes de febrero
  SELECT MONTH(Fecha_Arribo) AS mes,
         Ciclo_Estacion_Arribo,
         DAYOFWEEK(Fecha_Arribo) AS dia_semana,
         DAYOFMONTH(Fecha_Arribo) AS dia_mes,
         COUNT(*) AS total
  FROM viajes_2019 AS viajes
  INNER JOIN estacion ON viajes.Ciclo_Estacion_Arribo = estacion.idEstacion
  WHERE DAYOFWEEK(Fecha_Arribo) = 2 
        AND MONTH(Fecha_Arribo) = 2
        AND codAlcadia = 'CHT'
  GROUP BY mes, Ciclo_Estacion_Arribo
  ORDER BY total DESC;

  -- 2) GRÁFICA CON LA FRECUENCIA REGULAR DE VIAJES EN UNA CICLOESTACIÓN COMO DESTINO
  -- No implementado aún

  -- 3) PATRONES DE USO POR HORA POR DÍAS DE SEMANA O DÍAS ENTRE-SEMANA O DÍAS DE FIN DE SEMANA POR DESTINO
  -- Viajes por cada hora del día todos los lunes de febrero en la alcadía de cuauhtémoc
  SELECT MONTH(Fecha_Arribo) AS mes,
         DAYOFMONTH(Fecha_Arribo) AS dia_mes,
         HOUR(Hora_Arribo) AS hora,
         Ciclo_Estacion_Arribo,
         COUNT(*) AS total
  FROM viajes_2019 AS viajes
  INNER JOIN estacion ON viajes.Ciclo_Estacion_Arribo = estacion.idEstacion
  WHERE DAYOFWEEK(Fecha_Arribo) = 2 
        AND MONTH(Fecha_Arribo) = 2 
        AND codAlcadia = 'CHT'
  GROUP BY mes, dia_mes, hora;

  -- 4) PATRONES EN CICLOESTACIONES COMO DESTINO DE VIAJES, POR HORAS, EN DIAS DE SEMANA Y POR COLONIAS
  -- Viajes por cada hora del día todos los lunes de febrero en la colonia Buenavista
  SELECT MONTH(Fecha_Arribo) AS mes,
         DAYOFMONTH(Fecha_Arribo) AS dia_mes,
         HOUR(Hora_Arribo) AS hora,
         Ciclo_Estacion_Arribo,
         COUNT(*) AS total
  FROM viajes_2019 AS viajes
  INNER JOIN estacion ON viajes.Ciclo_Estacion_Arribo = estacion.idEstacion
  WHERE DAYOFWEEK(Fecha_Arribo) = 2 
        AND MONTH(Fecha_Arribo) = 2 
        AND districtName = 'Buenavista'
  GROUP BY mes, dia_mes, hora;

  -- 5) PATRONES EN UNA CICLOESTACIÓN COMO DESTINO DE VIAJES, POR HORAS Y EN DIAS DE SEMANA
  -- Viajes por cada hora del día todos los lunes de febrero en la estación 271 Av. Central J. Meneses
  SELECT MONTH(Fecha_Arribo) AS mes,
         DAYOFMONTH(Fecha_Arribo) AS dia_mes,
         HOUR(Hora_Arribo) AS hora,
         Ciclo_Estacion_Arribo,
         COUNT(*) AS total
  FROM viajes_2019 AS viajes
  WHERE DAYOFWEEK(Fecha_Arribo) = 2 
        AND MONTH(Fecha_Arribo) = 2 
        AND Ciclo_Estacion_Arribo = 271
  GROUP BY mes, dia_mes, hora;