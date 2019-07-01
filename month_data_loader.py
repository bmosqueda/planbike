import csv
import paths
import sys
sys.path.append(paths.utils)
from date_to_mysql_format import date_to_mysql_format
from date_to_mysql_format import DateFormatException
from validator import Validator
from validator import ValidationException

file_name = '2010-02-test.csv'
read_path = '/home/bmosqueda/Downloads/BIKE/Resources/Datasets/'
write_path = '/home/bmosqueda/Downloads/BIKE/Resources/Datasets/formated/'

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
  'Hora_Retiro': 'is_required|is_hour_in_mysql_format',
  'Ciclo_Estacion_Arribo': 'is_required|is_int',
  'Fecha_Arribo': 'is_required|is_date_in_mysql_format',
  'Hora_Arribo': 'is_required|is_hour_in_mysql_format'
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
  lines = []
  bad_lines = []

  with open(read_path + month_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0

    for row in csv_reader:
      line_count += 1
      # Metadata line
      if(line_count == 1):
        continue

      try: 
        row[ ARRIVAL_DATE_INDEX ] = date_to_mysql_format(row[ ARRIVAL_DATE_INDEX ])
        row[ REMOVAL_DATE_INDEX ] = date_to_mysql_format(row[ REMOVAL_DATE_INDEX ])

        validator.validate(row_to_dictionary(row))

        lines.append(row)

      except DateFormatException as error:
        print(line_count)
        row.append(error)
        row.append(line_count)
        bad_lines.append(row)
        print(error)
      except ValidationException as error:
        print(line_count)
        row.append(validator.result)
        row.append(line_count)
        bad_lines.append(row)
        print(validator.result)

  with open(write_path + month_file_name, 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

  if(len(bad_lines) > 0):
    with open(write_path + 'errors-' + month_file_name, 'w') as writeFile:
      writer = csv.writer(writeFile)
      writer.writerows(bad_lines)

  print(f'Processed {line_count} lines')

load_month(file_name)