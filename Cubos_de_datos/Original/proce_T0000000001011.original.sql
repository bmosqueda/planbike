create  procedure SP_T0000000001011()
BEGIN  
    
  DROP TABLE IF EXISTS T0000000001011;
  
  CREATE TABLE T0000000001011
    (`Genero_Usuario` VARCHAR(45) CHARACTER SET 'utf8' NULL DEFAULT NULL,
    `Edad_Usuario` INT(11) NULL DEFAULT NULL,
    `Ciclo_Estacion_Retiro` INT(11) NULL DEFAULT NULL,
    `todos` BIGINT(21) NOT NULL DEFAULT '0')
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;
    
  INSERT INTO T0000000001011
    SELECT
      Genero_Usuario,
      Edad_Usuario,
      Ciclo_Estacion_Retiro,
      COUNT(Edad_Usuario) todos
    FROM
      RegistroBicis
    GROUP BY
      Genero_Usuario,
      Edad_Usuario,
      Ciclo_Estacion_Retiro
    ORDER BY
      Genero_Usuario,
      Edad_Usuario,
      Ciclo_Estacion_Retiro;   
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('T0000000001011','Recalculo', NOW());
    
END;