from database import Database
import sql_query_formatter as formatter

class TableauDatasetCreator(Database):
  def __init__(self, year):
    # No es una tabla como tal, sólo encapsula todas las 
    # consultas necesarias para crear el dataset que usa Tableau
    # por eso no se le pasa nombre de la tabla, propiedades ni
    # llave primaria
    self.year = year
    self.base_table = f'viajes_{year}'
    self.first_semester_table = f'rutas_ene_jun_{year}'
    self.second_semester_table = f'rutas_jul_dic_{year}'

    Database.__init__(self, '', (), '')

  def create_base_table(self):
    self.are_valid_dates_diff_function()

    self.drop_table_if_exists(self.base_table)

    self.query(
      f'''CREATE TABLE {self.base_table} AS 
        SELECT * FROM registrobicis 
        WHERE YEAR(Fecha_Retiro) = {self.year}'''
    )

  def create_first_semester_table(self):
    return self.create_semester_table(self.first_semester_table, True)

  def create_second_semester_table(self):
    return self.create_semester_table(self.second_semester_table, False)

  def create_semester_table(self, table_name, is_first_semester):
    table_origin = f'''SELECT idRegistroBicis AS IDRegistro,
                              Genero_Usuario AS `Género`,
                              Edad_Usuario AS `Edad`,
                              Bici AS `Bici`,
                              Ciclo_Estacion_Retiro AS `Estación`,
                              Fecha_Retiro AS `Fecha`,
                              Hora_Retiro AS `Hora`,

                              'Origen' AS TipoRuta,
                               
                              CONCAT(Ciclo_Estacion_Retiro, '_', Ciclo_Estacion_Arribo) AS Ruta,

                              (CASE 
                                WHEN are_valid_dates_diff(
                                       Fecha_Retiro,
                                       Hora_Retiro,
                                       Fecha_Arribo,
                                       Hora_Arribo
                                     ) THEN
                                        TIMEDIFF(
                                          CONCAT(Fecha_Arribo, ' ', Hora_Arribo),
                                          CONCAT(Fecha_Retiro, ' ', Hora_Retiro)
                                        ) 
                                ELSE '00:00:00'
                              END) AS Tiempo
                        FROM {self.base_table}'''

    table_destiny = f'''SELECT idRegistroBicis AS IDRegistro,
                               Genero_Usuario AS `Género`,
                               Edad_Usuario AS `Edad`,
                               Bici AS `Bici`,
                               Ciclo_Estacion_Arribo AS `Estación`,
                               Fecha_Arribo AS `Fecha`,
                               Hora_Arribo AS `Hora`,

                               'Destino' AS TipoRuta,
                               
                               CONCAT(Ciclo_Estacion_Retiro, '_', Ciclo_Estacion_Arribo) AS Ruta,

                               (CASE 
                                 WHEN are_valid_dates_diff(
                                        Fecha_Retiro,
                                        Hora_Retiro,
                                        Fecha_Arribo,
                                        Hora_Arribo
                                      ) THEN
                                         TIMEDIFF(
                                           CONCAT(Fecha_Arribo, ' ', Hora_Arribo),
                                           CONCAT(Fecha_Retiro, ' ', Hora_Retiro)
                                         ) 
                                 ELSE '00:00:00'
                               END) AS Tiempo
                        FROM {self.base_table}'''

    self.drop_table_if_exists(table_name)

    month_operator = '<=' if is_first_semester else '>'
    
    self.query(
      f'''CREATE TABLE {table_name} AS
            {table_origin}
            WHERE MONTH(Fecha_Retiro) {month_operator} 6
          UNION ALL
            {table_destiny}
            WHERE MONTH(Fecha_Retiro) {month_operator} 6'''
    )

  def are_valid_dates_diff_function(self):
    return self.query(
      '''
        CREATE FUNCTION IF NOT EXISTS are_valid_dates_diff(
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
      '''
    )