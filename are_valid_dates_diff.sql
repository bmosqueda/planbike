DROP FUNCTION IF EXISTS are_valid_dates_diff;

CREATE FUNCTION are_valid_dates_diff(
  Fecha_Retiro DATE,
  Hora_Retiro TIME,
  Fecha_Arribo DATE,
  Hora_Arribo TIME
) RETURNS BOOLEAN
BEGIN
  RETURN DATEDIFF(
           CONCAT(Fecha_Arribo, ' ', Hora_Arribo),
           CONCAT(Fecha_Retiro, ' ', Hora_Retiro)
         ) < 2;
END;