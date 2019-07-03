from database import Database
import sql_query_formatter as formatter

class BicycleTrip(Database):
  def __init__(self):
    props = (
      'Genero_Usuario',
      'Edad_Usuario',
      'Bici',
      'Ciclo_Estacion_Retiro',
      'Fecha_Retiro',
      'Hora_Retiro',
      'Ciclo_Estacion_Arribo',
      'Fecha_Arribo',
      'Hora_Arribo'
    )

    Database.__init__(self, 'registrobicis', props, 'idRegistroBicis')

  def insert_many_from_csv(self, data):
    sql = '''INSERT INTO {} (
               Genero_Usuario,
               Edad_Usuario,
               Bici,
               Ciclo_Estacion_Retiro,
               Fecha_Retiro,
               Hora_Retiro,
               Ciclo_Estacion_Arribo,
               Fecha_Arribo,
               Hora_Arribo
             ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''.format(self.table)

    cursor = self.connector.cursor(dictionary = True)

    cursor.executemany(sql, data)

    self.connector.commit()

    return cursor