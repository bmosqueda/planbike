create  procedure SP_P0000001110001()
BEGIN  
             
  DROP TABLE IF EXISTS P0000001110001;
    
    CREATE TABLE P0000001110001 (
    `year(Fecha_Retiro)` INT(4) NULL,
    `month(Fecha_Retiro)` INT(2) NULL,
    `day(Fecha_Retiro)` INT(2) NULL,
    `Genero_Usuario` VARCHAR(45) NULL,
    `promedio` DOUBLE NOT NULL)
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;
    
  INSERT INTO P0000001110001
    SELECT
      YEAR(rb.Fecha_Retiro),
      MONTH(rb.Fecha_Retiro),
      DAY(rb.Fecha_Retiro),
      rb.Genero_Usuario,
      COUNT(rb.idRegistroBicis) promedio
    FROM
      (SELECT 
        *
      FROM
        RegistroBicis
      WHERE
        Hora_Retiro >= '05:00:00'
        OR
          Hora_Retiro <= '00:30:00'
        AND
          TIMESTAMP(Fecha_Arribo, Hora_Arribo) > 
            DATE_ADD(TIMESTAMP(Fecha_Retiro, Hora_Retiro), 
            INTERVAL 2 MINUTE)) rb
    GROUP BY
      YEAR(rb.Fecha_Retiro),
      MONTH(rb.Fecha_Retiro),
      DAY(rb.Fecha_Retiro),
      rb.Genero_Usuario;   
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('P0000001110001','Recalculo', NOW());
        
END;