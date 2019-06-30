from database import Database

class Station(Database):
  def __init__(self):
    props = ()

    Database.__init__(self, 'estacion', props, 'idEstacion')