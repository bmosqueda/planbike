import paths
import sys

sys.path.append(paths.utils)
sys.path.append(paths.models)

from database import Database
from bicycle_trips import BicycleTrip
from station import Station
import validator

bicycle_controller = BicycleTrip()
station_controller = Station()

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

def func():
  print("Yo soy funct")

a = func

a()