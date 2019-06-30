import paths
import sys

sys.path.append(paths.utils)
sys.path.append(paths.models)

from database import Database
from bicycle_trips import BicycleTrip
from station import Station

bicycle_controller = BicycleTrip()
station_controller = Station()

trip_dic = {
  'Genero_Usuario': 'F',
  'Edad_Usuario': 15,
  'Bici': 1656,
  'Ciclo_Estacion_Retiro': 66,
  'Fecha_Retiro': '2015-05-24',
  'Hora_Retiro': '08:10:06',
  'Ciclo_Estacion_Arribo': 22,
  'Fecha_Arribo': '2015-05-24',
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

try:
  result = bicycle_controller.insert(trip_tuple)
  # print(result.__dict__)
  print("All right")
  print(bicycle_controller.get_by_primary_key(result._insert_id))
except Exception as error:
  print(error)