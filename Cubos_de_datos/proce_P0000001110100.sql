create  procedure SP_P0000001110100()
BEGIN  
             
  DROP TABLE IF EXISTS P0000001110100;
    
    CREATE TABLE P0000001110100 (
    `year(Fecha_Retiro)` INT(4) NULL,
    `month(Fecha_Retiro)` INT(2) NULL,
    `day(Fecha_Retiro)` INT(2) NULL,  
    `Bici` INT(11) NULL,
    `promedio` DOUBLE NOT NULL)
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;
    
  INSERT INTO P0000001110100
  SELECT  
    year(tbl.fecha),
    month(tbl.fecha),
    day(tbl.fecha),
    tbl.bici,
    avg(tbl.uso) promedio
  FROM
    (SELECT
      DISTINCT(rb.Fecha_Retiro) fecha,
      rb.Bici,
      COUNT(rb.Bici) uso    
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
      rb.Bici,
      rb.Fecha_Retiro
      ASC) tbl
  GROUP BY
    year(tbl.fecha),
    month(tbl.fecha),
    day(tbl.fecha),
    tbl.bici;
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('P0000001110100','Recalculo', NOW());
        
END;