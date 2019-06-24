create procedure SP_T0000100001010()
BEGIN  

  DROP TABLE IF EXISTS T0000100001010;
  
  CREATE TABLE T0000100001010
    (`Edad_Usuario` INT(11) NULL DEFAULT NULL,
    `Ciclo_Estacion_Retiro` INT(11) NULL DEFAULT NULL,
    `Ciclo_Estacion_Arribo` INT(11) NULL DEFAULT NULL,
    `todos` BIGINT(21) NOT NULL DEFAULT '0')
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;
    
  INSERT INTO T0000100001010
    SELECT
      Edad_Usuario,
      Ciclo_Estacion_Retiro,
      Ciclo_Estacion_Arribo,
      COUNT(idRegistroBicis) todos
    FROM
      RegistroBicis
    GROUP BY
      Edad_Usuario,
      Ciclo_Estacion_Retiro,
      Ciclo_Estacion_Arribo
    ORDER BY
      Edad_Usuario,
      Ciclo_Estacion_Retiro,
      Ciclo_Estacion_Arribo;   
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('T0000100001010','Recalculo', NOW());
    
END;