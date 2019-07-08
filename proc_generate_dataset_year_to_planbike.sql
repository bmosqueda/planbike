-- completed in 10 m 2 s 590 ms
DROP PROCEDURE IF EXISTS generate_dataset_year_to_planbike;

CREATE PROCEDURE generate_dataset_year_to_planbike(new_year INT, semester_to_generate INT)
BEGIN
  SET @only_first_semester = 1;
  SET @only_second_semester = 2;
  SET @both_semesters = 3;

  -- Base table
  SET @table_name = CONCAT('viajes_', new_year);

  SET @delete_base_table_query = CONCAT(
    'DROP TABLE IF EXISTS ', @table_name
  );

  CALL execute_drop_table_query(@delete_base_table_query);

  SET @create_base_table_query = CONCAT(
    'CREATE TABLE ', @table_name, ' AS 
      SELECT * FROM registrobicis 
      WHERE YEAR(Fecha_Retiro) = ', new_year
  );

  CALL execute_create_table_query(@create_base_table_query);

  SET @table_origin = CONCAT('
    SELECT idRegistroBicis AS IDRegistro,
           Genero_Usuario AS `Género`,
           Edad_Usuario AS `Edad`,
           Bici AS `Bici`,
           Ciclo_Estacion_Retiro AS `Estación`,
           Fecha_Retiro AS `Fecha`,
           Hora_Retiro AS `Hora`,

           \'Origen\' AS TipoRuta,
           
           CONCAT(Ciclo_Estacion_Retiro, \'_\', Ciclo_Estacion_Arribo) AS Ruta,

           (CASE 
             WHEN are_valid_dates_diff(
                    Fecha_Retiro,
                    Hora_Retiro,
                    Fecha_Arribo,
                    Hora_Arribo
                  ) THEN
                     TIMEDIFF(
                       CONCAT(Fecha_Arribo, \' \', Hora_Arribo),
                       CONCAT(Fecha_Retiro, \' \', Hora_Retiro)
                     ) 
             ELSE \'00:00:00\'
           END) AS Tiempo
    FROM ', @table_name
  );

  SET @table_destiny = CONCAT('
    SELECT idRegistroBicis AS IDRegistro,
           Genero_Usuario AS `Género`,
           Edad_Usuario AS `Edad`,
           Bici AS `Bici`,
           Ciclo_Estacion_Arribo AS `Estación`,
           Fecha_Arribo AS `Fecha`,
           Hora_Arribo AS `Hora`,

           \'Destino\' AS TipoRuta,
           
           CONCAT(Ciclo_Estacion_Retiro, \'_\', Ciclo_Estacion_Arribo) AS Ruta,

           (CASE 
             WHEN are_valid_dates_diff(
                    Fecha_Retiro,
                    Hora_Retiro,
                    Fecha_Arribo,
                    Hora_Arribo
                  ) THEN
                     TIMEDIFF(
                       CONCAT(Fecha_Arribo, \' \', Hora_Arribo),
                       CONCAT(Fecha_Retiro, \' \', Hora_Retiro)
                     ) 
             ELSE \'00:00:00\'
           END) AS Tiempo
    FROM ', @table_name
  );

  -- First semester table
  IF semester_to_generate = @only_first_semester OR
     semester_to_generate = @both_semesters 
  THEN  
    SET @delete_first_semester_table_query = CONCAT(
      'DROP TABLE IF EXISTS rutas_ene_jun_', new_year
    );

    CALL execute_drop_table_query(@delete_first_semester_table_query);

    SET @create_first_semester_table_query = CONCAT(
      'CREATE TABLE rutas_ene_jun_', new_year ,' AS ',
      @table_origin, ' 
        WHERE MONTH(Fecha_Retiro) <= 6
      UNION ALL ',
      @table_destiny, ' 
        WHERE MONTH(Fecha_Retiro) <= 6'
    );

    CALL execute_create_table_query(@create_first_semester_table_query);
  END IF;

  -- Second semester table
  IF semester_to_generate = @only_second_semester OR
     semester_to_generate = @both_semesters 
  THEN 
    SET @delete_second_semester_table_query = CONCAT(
      'DROP TABLE IF EXISTS rutas_jul_dic_', new_year
    );

    CALL execute_drop_table_query(@delete_second_semester_table_query);

    SET @create_second_semester_table_query = CONCAT(
      'CREATE TABLE rutas_jul_dic_', new_year ,' AS ',
      @table_origin, ' 
        WHERE MONTH(Fecha_Retiro) > 6
      UNION ALL ',
      @table_destiny, ' 
        WHERE MONTH(Fecha_Retiro) > 6'
    );

    CALL execute_create_table_query(@create_second_semester_table_query);
  END IF;
END;

CALL generate_dataset_year_to_planbike(2019, 3);

-- 3574317 registros hasta mayo
CREATE TABLE viajes_2019
SELECT * FROM registrobicis
WHERE YEAR(Fecha_Retiro) = 2019;

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

       TIME(
         TIMEDIFF(
           CONCAT(Fecha_Arribo, ' ', Hora_Arribo),
           CONCAT(Fecha_Retiro, ' ', Hora_Retiro)
         )
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

       TIME(
         TIMEDIFF(
           CONCAT(Fecha_Arribo, ' ', Hora_Arribo),
           CONCAT(Fecha_Retiro, ' ', Hora_Retiro)
         )
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

-- Esta vista no se utiliza, los joins se hacen directamente en Tableau
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