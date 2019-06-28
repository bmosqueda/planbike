import paths
import sys
sys.path.append(paths.utils)
sys.path.append(paths.models)
from database import Database
from bicycle_trips import BicycleTrip
from station import Station

station_controller = Station()

_all = station_controller.get_all()

print(len(_all))

for row in _all:
  print(row)