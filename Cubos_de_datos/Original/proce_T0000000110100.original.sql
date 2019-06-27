create procedure SP_T0000000110100()
BEGIN  

  DROP TABLE IF EXISTS T0000000110100;
  
  CREATE TABLE T0000000110100
    (`Bici` INT(11) NULL DEFAULT NULL,
    `year(Fecha_Retiro)` INT(4) NULL DEFAULT NULL,
    `month(Fecha_Retiro)` INT(2) NULL DEFAULT NULL,
    `todos` BIGINT(21) NOT NULL DEFAULT '0')
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;
    
  INSERT INTO T0000000110100
    SELECT
      Bici,
      YEAR(Fecha_Retiro),
      MONTH(Fecha_Retiro),
      COUNT(idRegistroBicis) todos
    FROM
      RegistroBicis
    GROUP BY
      Bici,
      YEAR(Fecha_Retiro),
      MONTH(Fecha_Retiro)
    ORDER BY
      Bici,
      YEAR(Fecha_Retiro),
      MONTH(Fecha_Retiro);   
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('T0000000110100','Recalculo', NOW());
    
END;