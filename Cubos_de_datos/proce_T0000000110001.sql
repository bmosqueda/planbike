create  procedure SP_T0000000110001()
BEGIN  
    
  DROP TABLE IF EXISTS T0000000110001;
  
  CREATE TABLE T0000000110001
    (`Genero_Usuario` VARCHAR(45) CHARACTER SET 'utf8' NULL DEFAULT NULL,
    `year(Fecha_Retiro)` INT(4) NULL DEFAULT NULL,
    `month(Fecha_Retiro)` INT(2) NULL DEFAULT NULL,
    `todos` BIGINT(21) NOT NULL DEFAULT '0')
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;
    
  INSERT INTO T0000000110001
    SELECT
      Genero_Usuario,
      YEAR(Fecha_Retiro),
      MONTH(Fecha_Retiro),
      COUNT(idRegistroBicis) todos
    FROM
      RegistroBicis
    GROUP BY
      Genero_Usuario,
      YEAR(Fecha_Retiro),
      MONTH(Fecha_Retiro)
    ORDER BY
      Genero_Usuario,
      YEAR(Fecha_Retiro),
      MONTH(Fecha_Retiro);   
    
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('T0000000110001','Recalculo', NOW());
        
END;