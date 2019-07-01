import paths
import sys

sys.path.append(paths.utils)
sys.path.append(paths.models)

from database import Database
from bicycle_trips import BicycleTrip
from station import Station
from validator import Validator

bicycle_controller = BicycleTrip()
station_controller = Station()

# print(bicycle_controller.get_by_primary_key(3))

trip_dic = {
  'Fecha_Retiro': '2015-05-24',
  'Edad_Usuario': 15,
  'Bici': 1656,
  'Genero_Usuario': 'F',
  'Ciclo_Estacion_Retiro': 66,
  'Fecha_Arribo': '2015-05-24',
  'Ciclo_Estacion_Arribo': 22,
  'Hora_Retiro': '08:10:06',
  'Hora_Arribo': '08:50:04'
}

trip_tuple = (
  'F',
  15,
  1656,
  66,
  '2015-05-24',
  '08:10:06',
  22,
  '2015-05-24',
  '08:50:04'
)

props = (
      'Fecha_Retiro',
      'Edad_Usuario',
      'Bici',
      'Ciclo_Estacion_Retiro',
      'Hora_Retiro',
      'Ciclo_Estacion_Arribo',
      'Fecha_Arribo',
      'Hora_Arribo',
      'Genero_Usuario'
    )

rules = {
  'Fecha_Retiro': 'is_date_in_mysql_format',  
  'Bici': 'is_required|max_length,5'  
}

data = {
  'Fecha_Retiro': 30,
  'Bici': 'hola mund'
}

val = Validator(rules)

# try:
#   val.validate(data)
#   print("No hay errores :D")
# except Exception as error:
#   print(error)
#   print(val.result)
hola = [2]

print(len(hola))