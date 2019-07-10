import sys
import csv
import time

from config import UTILS_PATH, MODELS_PATH, ERRORS_PATH

sys.path.append(UTILS_PATH)
sys.path.append(MODELS_PATH)

from csv_month_loader import CSVMonthLoader

data_loader = CSVMonthLoader()

if(len(sys.argv) == 1):
  print('Es necesario la ruta de por lo menos un archivo a cargar')
else:
  start = time.time()

  for file_name in sys.argv[1:]:
    data_loader.load(file_name)

  print(f'Tiempo total tomando en la carga de registros: {time.time() - start}')