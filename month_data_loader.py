import csv
from config import UTILS_PATH
from config import MODELS_PATH
from config import ERRORS_PATH
import os.path
import time
import sys

sys.path.append(UTILS_PATH)
sys.path.append(MODELS_PATH)

from date_to_mysql_format import date_to_mysql_format
from date_to_mysql_format import DateFormatException
from validator import Validator
from validator import ValidationException
from bicycle_trips import BicycleTrip

trips_controller = BicycleTrip()

INSERTIONS_BY_CYCLE = 10000
step = 1

GENDER_INDEX = 0
AGE_INDEX = 1
BIKE_NUMBER_INDEX = 2
REMOVAL_STATION_INDEX = 3
REMOVAL_DATE_INDEX = 4
REMOVAL_HOUR_INDEX = 5
ARRIVAL_STATION_INDEX = 6
ARRIVAL_DATE_INDEX = 7
ARRIVAL_HOUR_INDEX = 8

validator = Validator({
  'Genero_Usuario': 'is_required|has_exact_length,1',
  'Edad_Usuario': 'is_required|is_int',
  'Bici': 'is_required|is_int',
  'Ciclo_Estacion_Retiro': 'is_required|is_int',
  'Fecha_Retiro': 'is_required|is_date_in_mysql_format',
  'Hora_Retiro': 'is_required|is_hour_in_mysql_format|is_valid_hour',
  'Ciclo_Estacion_Arribo': 'is_required|is_int',
  'Fecha_Arribo': 'is_required|is_date_in_mysql_format',
  'Hora_Arribo': 'is_required|is_hour_in_mysql_format|is_valid_hour'
})

def row_to_dictionary(row):
  return {
    'Genero_Usuario': row[ GENDER_INDEX ],
    'Edad_Usuario': row[ AGE_INDEX ],
    'Bici': row[ BIKE_NUMBER_INDEX ],
    'Ciclo_Estacion_Retiro': row[ REMOVAL_STATION_INDEX ],
    'Fecha_Retiro': row[ REMOVAL_DATE_INDEX ],
    'Hora_Retiro': row[ REMOVAL_HOUR_INDEX ],
    'Ciclo_Estacion_Arribo': row[ ARRIVAL_STATION_INDEX ],
    'Fecha_Arribo': row[ ARRIVAL_DATE_INDEX ],
    'Hora_Arribo': row[ ARRIVAL_HOUR_INDEX ]
  }

def load_month(month_file_name):
  global INSERTIONS_BY_CYCLE
  global step

  data = []
  bad_lines = []

  with open(month_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    files_to_insert = 0
    line_count = 0
    step = 0

    for row in csv_reader:
      line_count += 1
      files_to_insert += 1
      
      if(len(row) > 9):
        row = row[:9]
      # Metadata line
      if(line_count == 1):
        continue

      try: 
        row[ ARRIVAL_DATE_INDEX ] = date_to_mysql_format(row[ ARRIVAL_DATE_INDEX ])
        row[ REMOVAL_DATE_INDEX ] = date_to_mysql_format(row[ REMOVAL_DATE_INDEX ])

        validator.validate(row_to_dictionary(row))

        data.append(tuple(row))
        
        if(files_to_insert == INSERTIONS_BY_CYCLE):
          trips_controller.insert_many_from_csv(data)
          data = []
          files_to_insert = 0
          print(INSERTIONS_BY_CYCLE * step)
          step = step + 1

      except DateFormatException as error:
        row.append(error)
        row.append(line_count)
        bad_lines.append(row)
        # print(error)
      except ValidationException as error:
        row.append(validator.result)
        row.append(line_count)
        bad_lines.append(row)
        # print(validator.result)

    # Faltaron algunos por insertarse
    if(len(data) > 0):
      trips_controller.insert_many_from_csv(data)

  if(len(bad_lines) > 0):
    with open(os.path.join(ERRORS_PATH, 'errors-' + os.path.basename(month_file_name)), 'w') as writeFile:
      writer = csv.writer(writeFile)
      writer.writerows(bad_lines)

  print(f'Carga de {month_file_name} terminada')
  print(f'Processed lines: {line_count}')
  print(f'Bad lines: {len(bad_lines)}')
  print(f'Good lines: {line_count - len(bad_lines)}')

if(len(sys.argv) == 1):
  print('Es necesario la ruta del archivo a cargar')
else:
  start = time.time()

  for file_name in sys.argv[1:]:
    if(os.path.isfile(file_name)):
      load_month(file_name)
    else:
      print(f'{file_name} no es un archivo válido')

  print(f'Tiempo total tomando en la carga de registros: {time.time() - start}')