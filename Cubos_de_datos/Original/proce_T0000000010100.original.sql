create  procedure SP_T0000000010100()
BEGIN  
    
  DROP TABLE IF EXISTS T0000000010100;
  
  CREATE TABLE T0000000010100
    (`Bici` INT(11) NULL DEFAULT NULL,
    `year(Fecha_Retiro)` INT(4) NULL DEFAULT NULL,
    `todos` BIGINT(21) NOT NULL DEFAULT '0')
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;
    
  INSERT INTO T0000000010100
    SELECT
      Bici,
      YEAR(Fecha_Retiro),
      COUNT(Bici) todos
    FROM
      RegistroBicis
    GROUP BY
      Bici,
      YEAR(Fecha_Retiro)
    ORDER BY
      Bici,
      YEAR(Fecha_Retiro);   
    
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('T0000000010100','Recalculo', NOW());
        
END;