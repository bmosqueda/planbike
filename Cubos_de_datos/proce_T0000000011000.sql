create  procedure SP_T0000000011000()
BEGIN  
    
  DROP TABLE IF EXISTS T0000000011000;
  
  CREATE TABLE T0000000011000
    (`Ciclo_Estacion_Retiro` INT(11) NULL DEFAULT NULL,
    `year(Fecha_Retiro)` INT(4) NULL DEFAULT NULL,
    `todos` BIGINT(21) NOT NULL DEFAULT '0')
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;
    
  INSERT INTO T0000000011000
    SELECT
      Ciclo_Estacion_Retiro,
      YEAR(Fecha_Retiro),
      COUNT(Ciclo_Estacion_Retiro) todos
    FROM
      RegistroBicis
    GROUP BY 
      Ciclo_Estacion_Retiro,
      YEAR(Fecha_Retiro)
    ORDER BY
      Ciclo_Estacion_Retiro,
      YEAR(Fecha_Retiro);   
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('T000000001100','Recalculo', NOW());
    
END;