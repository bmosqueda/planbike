create table bitacora_cubos
(
  ID int auto_increment
    primary key,
  Tabla varchar(45) not null,
  Accion varchar(45) not null,
  Fecha_Hora datetime not null
)
comment 'Bitacora de los cambios en la tabla Banderolas_Cubos';