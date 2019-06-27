create procedure SP_T0011100001011()
BEGIN  

  DROP TABLE IF EXISTS T0011100001011;
  
  CREATE TABLE T0011100001011
    (`Genero_Usuario` VARCHAR(45) CHARACTER SET 'utf8' NULL DEFAULT NULL,
    `Edad_Usuario` INT(11) NULL DEFAULT NULL,
    `Ciclo_Estacion_Retiro` INT(11) NULL DEFAULT NULL,
    `Ciclo_Estacion_Arribo` INT(11) NULL DEFAULT NULL,
    `year(Fecha_Arribo)` INT(4) NULL DEFAULT NULL,
    `month(Fecha_Arribo)` INT(2) NULL DEFAULT NULL,
    `todos` BIGINT(21) NOT NULL DEFAULT '0')
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;
    
  INSERT INTO T0011100001011
    SELECT
      Genero_Usuario,
      Edad_Usuario,
      Ciclo_Estacion_Retiro,
      Ciclo_Estacion_Arribo,
      YEAR(Fecha_Retiro),
      MONTH(Fecha_Retiro),
      COUNT(idRegistroBicis) todos
    FROM
      RegistroBicis
    GROUP BY
      Genero_Usuario,
      Edad_Usuario,
      Ciclo_Estacion_Retiro,
      Ciclo_Estacion_Arribo,
      YEAR(Fecha_Retiro),
      MONTH(Fecha_Retiro)
    ORDER BY
      Genero_Usuario,
      Edad_Usuario,
      Ciclo_Estacion_Retiro,
      Ciclo_Estacion_Arribo,
      YEAR(Fecha_Retiro),
      MONTH(Fecha_Retiro);
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('T0011100001011','Recalculo', NOW());
    
END;