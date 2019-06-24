CREATE PROCEDURE SP_P0000001110000(NombreTablaTemporal TEXT)
BEGIN      
  INSERT INTO P0000001110000
  SELECT
    -- Sugerir usar alias aquí
    YEAR(rb.Fecha_Retiro),
    MONTH(rb.Fecha_Retiro),
    DAY(rb.Fecha_Retiro),
    -- No es el promedio, es el número de registros
    COUNT(rb.idRegistroBicis) AS promedio
  FROM (
    SELECT * FROM NombreTablaTemporal
    WHERE esta_dentro_horario_valido(
            Hora_Retiro, 
            Hora_Arribo, 
            Fecha_Retiro, 
            Fecha_Arribo
          )
          -- Encapsulado en una función
          -- Hora_Retiro >= '05:00:00' OR 
          -- Hora_Retiro <= '00:30:00' AND
          -- TIMESTAMP(Fecha_Arribo, Hora_Arribo) > 
          -- DATE_ADD(
          --   TIMESTAMP(Fecha_Retiro, Hora_Retiro), 
          --   INTERVAL 2 MINUTE
          -- )
  ) AS rb
  GROUP BY anio, mes, dia;
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('P0000001110000', 'Actualizado', NOW());    
END;