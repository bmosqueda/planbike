CREATE PROCEDURE SP_P0000001110000(NombreTablaTemporal TEXT)
BEGIN      
  INSERT INTO P0000001110000
  SELECT
    -- Sugerir usar alias aquí
    YEAR(bicis.Fecha_Retiro) AS anio,
    MONTH(bicis.Fecha_Retiro) AS mes,
    DAY(bicis.Fecha_Retiro) AS dia,
    -- No es el promedio, es el número de registros
    COUNT(bicis.idRegistroBicis) AS num_registros
  FROM (
    SELECT * FROM NombreTablaTemporal
    WHERE esta_dentro_horario_valido(
            Hora_Retiro, 
            Hora_Arribo, 
            Fecha_Retiro, 
            Fecha_Arribo
          )
  ) AS bicis
  GROUP BY anio, mes, dia;
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
  VALUES('P0000001110000', 'Actualizado', NOW());    
END;