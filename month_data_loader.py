import csv
import utils/month_data_loader.py

data_path = '/home/bmosqueda/Downloads/BIKE/Resources/dataset_movimientos_2019-05.csv'

with open(data_path) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter = ',')
  line_count = 0
  for row in csv_reader:
    line_count += 1
    print(row)

print(f'Processed {line_count} lines')

