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