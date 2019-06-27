create  procedure SP_T0000000010000()
BEGIN  
    
  DROP TABLE IF EXISTS T0000000010000;
  
  CREATE TABLE T0000000010000 
    (`year(Fecha_Retiro)` INT(4) NULL DEFAULT NULL,
    `todos` BIGINT(21) NOT NULL DEFAULT '0')
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;
    
  INSERT INTO T0000000010000
    SELECT
      YEAR(Fecha_Retiro),
      COUNT(idRegistroBicis) todos
    FROM
      RegistroBicis
    GROUP BY
      YEAR(Fecha_Retiro)
    ORDER BY
      YEAR(Fecha_Retiro);    
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('T0000000010000','Recalculo', NOW());
    
END;