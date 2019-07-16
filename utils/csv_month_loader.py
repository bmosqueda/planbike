import csv
import os.path
import json
import sys
from os.path import isfile

from config import UTILS_PATH, MODELS_PATH, ERRORS_PATH

sys.path.append(UTILS_PATH)
sys.path.append(MODELS_PATH)

from validator import Validator, ValidationException
from bicycle_trips import BicycleTrip
from date_to_mysql_format import date_to_mysql_format, DateFormatException

bicycle_controller = BicycleTrip()

options = None

with open(os.path.join(UTILS_PATH, 'csv_month_loader_config.json')) as json_file:  
  options = json.load(json_file)

class CSVMonthLoader:
  def __init__(self):
    self.INSERTIONS_BY_CYCLE = options[ 'insertions_by_cycle' ]
    self.validator = Validator(options[ 'fields_rules' ])
    self.result = []
    self.fields_num = options[ 'fields_num' ]

    self.indexes = type('', (), {})()

    self.indexes.AGE = options[ 'indexes' ][ 'age' ]
    self.indexes.GENDER = options[ 'indexes' ][ 'gender' ]
    self.indexes.BIKE_NUMBER = options[ 'indexes' ][ 'bike_number' ]
    self.indexes.REMOVAL_DATE = options[ 'indexes' ][ 'removal_date' ]
    self.indexes.ARRIVAL_DATE = options[ 'indexes' ][ 'arrival_date' ]
    self.indexes.REMOVAL_HOUR = options[ 'indexes' ][ 'removal_hour' ]
    self.indexes.ARRIVAL_HOUR = options[ 'indexes' ][ 'arrival_hour' ]
    self.indexes.REMOVAL_STATION = options[ 'indexes' ][ 'removal_station' ]
    self.indexes.ARRIVAL_STATION = options[ 'indexes' ][ 'arrival_station' ]

  def load(self, month_file_name):
    data = []
    bad_lines = []

    if(not isfile(month_file_name)):
      print(f'{month_file_name} no es un archivo válido, intenta con otro')
      return 0

    print(f'*** Cargando {os.path.basename(month_file_name)} ***')

    with open(month_file_name) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter = ',')
      files_to_insert = 0
      line_count = 0
      step = 1

      for row in csv_reader:
        line_count += 1
        
        # Metadata line
        if(line_count == 1):
          continue

        files_to_insert += 1
        
        if(self.has_excedent_fields(row)):
          row = row[ :self.fields_num ]
        elif(self.has_less_fields(row)):
          row.append('Número de campos menor que el establecido')
          row.append(line_count)
          bad_lines.append(row)
          continue

        try: 
          self.format_fields(row)

          self.validator.validate(self.row_to_dictionary(row))

          data.append(tuple(row))
          
          if(files_to_insert == self.INSERTIONS_BY_CYCLE):
            print(f'{self.INSERTIONS_BY_CYCLE * step} registros procesados  \r', end = "", flush = True),

            bicycle_controller.insert_many_from_csv(data)
            
            data = []
            files_to_insert = 0
            step = step + 1

        except DateFormatException as error:
          row.append(error)
          row.append(line_count)
          bad_lines.append(row)
        except ValidationException as error:
          row.append(self.validator.errors)
          row.append(line_count)
          bad_lines.append(row)

      # Faltaron algunos por insertarse
      if(len(data) > 0):
        bicycle_controller.insert_many_from_csv(data)

    print(f'Registros cargados correctamente: {line_count - len(bad_lines)}')

    if(len(bad_lines) > 0):
      incorrect_records_file = os.path.join(ERRORS_PATH, 'errors-' + os.path.basename(month_file_name))

      print(f'Registros con errores: {len(bad_lines)}')
      print(f'Puedes ver los errores en el archivo {incorrect_records_file}')

      self.write_file_of_errors(incorrect_records_file, bad_lines)

  def has_excedent_fields(self, row):
    return len(row) > self.fields_num

  def has_less_fields(self, row):
    return len(row) < self.fields_num

  def row_to_dictionary(self, row):
    return {
      'Genero_Usuario': row[ self.indexes.GENDER ],
      'Edad_Usuario': row[ self.indexes.AGE ],
      'Bici': row[ self.indexes.BIKE_NUMBER ],
      'Ciclo_Estacion_Retiro': row[ self.indexes.REMOVAL_STATION ],
      'Fecha_Retiro': row[ self.indexes.REMOVAL_DATE ],
      'Hora_Retiro': row[ self.indexes.REMOVAL_HOUR ],
      'Ciclo_Estacion_Arribo': row[ self.indexes.ARRIVAL_STATION ],
      'Fecha_Arribo': row[ self.indexes.ARRIVAL_DATE ],
      'Hora_Arribo': row[ self.indexes.ARRIVAL_HOUR ]
    }

  def dictionary_to_list(self, dictionary):
    return list(
      dictionary[ 'Bici' ],
      dictionary[ 'Edad_Usuario' ],
      dictionary[ 'Genero_Usuario' ],
      dictionary[ 'Hora_Arribo' ]
    )

  def format_fields(self, row):
    row[ self.indexes.ARRIVAL_DATE ] = date_to_mysql_format(row[ self.indexes.ARRIVAL_DATE ])
    row[ self.indexes.REMOVAL_DATE ] = date_to_mysql_format(row[ self.indexes.REMOVAL_DATE ])

  def write_file_of_errors(self, file_path, errors):
    with open(file_path, 'w') as writeFile:
      writer = csv.writer(writeFile)
      writer.writerows(errors)