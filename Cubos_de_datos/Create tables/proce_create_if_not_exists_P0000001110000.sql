CREATE PROCEDURE create_if_not_exists_P0000001110000()
BEGIN
  CREATE TABLE IF NOT EXISTS P0000001110000 (
    `year(Fecha_Retiro)` INT(4) NULL,
    `month(Fecha_Retiro)` INT(2) NULL,
    `day(Fecha_Retiro)` INT(2) NULL,
    `promedio` DOUBLE NOT NULL)
  ENGINE = InnoDB
  DEFAULT CHARACTER SET = utf8;
END;
