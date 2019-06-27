CREATE PROCEDURE SP_P0000001110000()
BEGIN

  DROP TABLE IF EXISTS P0000001110000;

    CREATE TABLE P0000001110000 (
    `year(Fecha_Retiro)` INT(4) NULL,
    `month(Fecha_Retiro)` INT(2) NULL,
    `day(Fecha_Retiro)` INT(2) NULL,
    `promedio` DOUBLE NOT NULL)
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = latin1;

  INSERT INTO P0000001110000
    SELECT
      YEAR(rb.Fecha_Retiro),
      MONTH(rb.Fecha_Retiro),
      DAY(rb.Fecha_Retiro),
      COUNT(rb.idRegistroBicis) promedio
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
      YEAR(rb.Fecha_Retiro),
      MONTH(rb.Fecha_Retiro),
      DAY(rb.Fecha_Retiro);

  INSERT INTO Bitacora_Cubos(Tabla, Accion, Fecha_Hora)
    VALUES('P0000001110000','Recalculo', NOW());

END;