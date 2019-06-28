import csv
import sys
sys.path.append('/home/bmosqueda/Downloads/BIKE/Code/utils')
from date_to_mysql_format import date_to_mysql_format

file_name = '2019-05.csv'
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

def load_month(month_file_name):
  lines = []

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
        lines.append(row)

      except Exception as error:
        print(error)
        print(row)

  with open(write_path + month_file_name, 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

  print(f'Processed {line_count} lines')

load_month('2019-02.csv')