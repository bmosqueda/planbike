from database import Database

class BicycleTrip(Database):
  def __init__(self):
    Database.__init__(self, 'registrobicis')