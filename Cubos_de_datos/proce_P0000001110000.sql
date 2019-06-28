CREATE PROCEDURE SP_P0000001110000(NombreTablaTemporal TEXT)
BEGIN      
  INSERT INTO P0000001110000
  SELECT
    YEAR(viajes.Fecha_Retiro),
    MONTH(viajes.Fecha_Retiro),
    DAY(viajes.Fecha_Retiro),
    COUNT(viajes.idRegistroBicis) AS promedio
  FROM (
    SELECT * FROM NombreTablaTemporal
    WHERE esta_dentro_horario_valido(
            Hora_Retiro, 
            Hora_Arribo, 
            Fecha_Retiro, 
            Fecha_Arribo
          )
  ) AS viajes
  GROUP BY anio, mes, dia;
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
  VALUES('P0000001110000', 'Actualizado', NOW());    
END;