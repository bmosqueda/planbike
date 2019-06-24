create table registrobicis
(
  Genero_Usuario varchar(45) null,
  Edad_Usuario int null,
  Bici int null,
  Ciclo_Estacion_Retiro int null,
  Fecha_Retiro date null,
  Hora_Retiro time null,
  Ciclo_Estacion_Arribo int null,
  Fecha_Arribo date null,
  Hora_Arribo time null,
  idRegistroBicis int auto_increment
    primary key
)
charset=utf8;

create index IndexRetiro
  on registrobicis (Fecha_Retiro, Hora_Retiro);

create index indexArribo
  on registrobicis (Fecha_Arribo, Hora_Arribo);