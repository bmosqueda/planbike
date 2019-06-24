create  procedure SP_P1000001110000()
BEGIN  
             
  DROP TABLE IF EXISTS P1000001110000;
    
    CREATE TABLE P1000001110000 (
    `year(Fecha_Retiro)` INT(4) NULL,
    `month(Fecha_Retiro)` INT(2) NULL,
    `day(Fecha_Retiro)` INT(2) NULL,
    `promedio` DOUBLE NOT NULL)
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;
    
  INSERT INTO P1000001110000
  SELECT
    cajones.anio,
    cajones.mes,
    cajones.dia,
    cajones.slots / bicicletas.bicis promedio
  FROM
    (SELECT
      tbl.anio,
      tbl.mes,
      tbl.dia,
      SUM(slots) slots
    FROM
      (SELECT
        YEAR(rb.Fecha_Retiro) anio,
        MONTH(rb.Fecha_Retiro) mes,
        DAY(rb.Fecha_Retiro) dia,
        rb.Ciclo_Estacion_Retiro estacion,
        es.slots
      FROM
        RegistroBicis rb
        INNER JOIN
          Estacion es
          ON
            rb.Ciclo_Estacion_Retiro = es.idEstacion
      GROUP BY
        YEAR(Fecha_Retiro),
        MONTH(Fecha_Retiro),
        DAY(Fecha_Retiro),
        Ciclo_Estacion_Retiro) tbl
    GROUP BY
      tbl.anio,
      tbl.mes,
      tbl.dia) cajones
    INNER JOIN
      (SELECT
        YEAR(re.Fecha_Retiro) anio,
        MONTH(re.Fecha_Retiro) mes,
        DAY(re.Fecha_Retiro) dia,
        COUNT(DISTINCT(Bici)) bicis
      FROM
        RegistroBicis re
      GROUP BY
        YEAR(re.Fecha_Retiro),
        MONTH(re.Fecha_Retiro),
        DAY(re.Fecha_Retiro)) bicicletas
    ON
      cajones.anio = bicicletas.anio
      AND
        cajones.mes = bicicletas.mes
      AND
        cajones.dia = cajones.dia;
      
  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('P1000001110000','Recalculo', NOW());
        
END;