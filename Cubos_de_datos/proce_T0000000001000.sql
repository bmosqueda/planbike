create  procedure SP_T0000000001000()
BEGIN  
    
  DROP TABLE IF EXISTS T0000000001000;
  
  CREATE TABLE T0000000001000
    (`Ciclo_Estacion_Retiro` INT(11) NULL DEFAULT NULL,
    `todos` BIGINT(21) NOT NULL DEFAULT '0')
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;
    
  INSERT INTO T0000000001000
    SELECT 
      Ciclo_Estacion_Retiro ciclo,
      COUNT(Ciclo_Estacion_Retiro) todos
    FROM 
      RegistroBicis rb
    GROUP BY
      Ciclo_Estacion_Retiro
    ORDER BY
      Ciclo_Estacion_Retiro;  
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('T0000000001000','Recalculo', NOW());
    
END;