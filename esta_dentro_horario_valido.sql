CREATE FUNCTION esta_dentro_horario_valido(
  Hora_Retiro TIME,
  Hora_Arribo TIME,
  Fecha_Retiro DATE,
  Fecha_Arribo DATE
) RETURNS BOOLEAN
BEGIN
  RETURN Hora_Retiro >= '05:00:00' OR 
         Hora_Retiro <= '00:30:00' AND
         TIMESTAMP(Fecha_Arribo, Hora_Arribo) > 
         DATE_ADD(
           TIMESTAMP(Fecha_Retiro, Hora_Retiro), 
           INTERVAL 2 MINUTE
         );
END;