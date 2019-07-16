from enum import IntEnum
from validator import is_int

class SemesterEnum(IntEnum):
  FIRST = 1
  SECOND = 2
  BOTH = 3

class InvalidSemesterException(Exception):
  pass

class Semester:
  def __init__(self, semester):
    if(not self.is_valid(semester)):
      raise InvalidSemesterException(f'{semester} no es un semestre válido')

    self.num = int(semester)

  def is_first(self):
    return self.num == SemesterEnum.FIRST

  def is_second(self):
    return self.num == SemesterEnum.SECOND

  def are_both(self):
    return self.num == SemesterEnum.BOTH

  def is_valid(self, semester):
    return (
      is_int(semester) and (
        int(semester) == SemesterEnum.FIRST or
        int(semester) == SemesterEnum.SECOND or
        int(semester) == SemesterEnum.BOTH
      )
    )

  def get_name(self):
    names = [ 'Primero', 'Segundo', 'Ambos' ]
    return names[ self.num - 1 ]