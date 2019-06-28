from database import Database

class Station(Database):
  def __init__(self):
    Database.__init__(self, 'estacion')