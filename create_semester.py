import sys
import config
import os

sys.path.append(config.UTILS_PATH)
sys.path.append(config.MODELS_PATH)

from validator import is_int
from tableau_dataset_creator import TableauDatasetCreator
from csv_month_loader import CSVMonthLoader

data_loader = CSVMonthLoader()

semesters_options = {
  'first': 1,
  'second': 2,
  'both': 3
}

semesters_names = [ 'Primero', 'Segundo', 'Ambos' ]

def clear_screen(): 
  if(os.name == 'posix'):
    _ = os.system('clear') 
  else:
    _ = os.system('cls')

def ask_for_confirmation(confirmation):
  confirmation = confirmation.lower()

  if(confirmation != 's' and confirmation != 'n'):
    print(f'{confirmation} no es una opción válida')
    raise Exception('Not valid confirmation option')
  else:
    return confirmation == 's'

def is_valid_year(year):
  return is_int(year) and int(year) >= 2010 and int(year) < 2100

def is_first_semester(semester):
  global semesters_options

  return is_int(semester) and int(semester) == semesters_options[ 'first' ]

def is_second_semester(semester):
  global semesters_options

  return is_int(semester) and int(semester) == semesters_options[ 'second' ]

def are_both_semesters(semester):
  global semesters_options

  return is_int(semester) and int(semester) == semesters_options[ 'both' ]

def is_valid_semester(semester):
  return (
    is_first_semester(semester) or
    is_second_semester(semester) or
    are_both_semesters(semester)
  )

def is_correct_info():
  clear_screen()
  need_to_load_month = False
  base_path = ''
  files_names = []
  year = 0
  semester = 0

  print("¿Necesitas cargar datasets de algunos meses? (s/n)")

  # Ask if load datasets
  while True:
    need_to_load_month = input()

    try:
      need_to_load_month = ask_for_confirmation(need_to_load_month)
      break
    except Exception as error:
      error

  if(need_to_load_month):
    clear_screen()

    print('Escribe la ruta absoluta a la carpeta en donde están guardados los datasets')

    # Ask if base path
    while True:
      
      base_path = input()

      if(os.path.isdir(base_path)):
        break;
      else:
        print('La ruta proporcionada no es un directorio, intenta nuevamente')
    
    clear_screen()
    print('Escribe el nombre de los archivos que quieres cargar. Para terminar escribe X')
    
    # Ask files names
    while True:
      file_name = input()
      
      if(file_name.lower() == 'x'):
        break
      elif(os.path.isfile(os.path.join(base_path, file_name))):
        files_names.append(file_name)
        print(f'{file_name} agregado correctamente')
      else:
        print("Por favor proporciona el nombre de un archivo correcto")

    need_to_load_month = len(files_names) > 0

  clear_screen()
  print('Ingresa el año que quieres crear')

  # Ask year
  while True:
    year = input()

    if(not is_valid_year(year)):
      print(f'{year} no es un año válido, intenta con otro')
    else:
      break

  clear_screen()
  print('¿Qué semestre quieres crear?\n'
        '1) Primer semestre\n'
        '2) Segundo semestre\n'
        '3) Ambos semestres')

  # Ask semester
  while True:
    semester = input()

    if(not is_valid_semester(semester)):
      print(f'{semester} no es una opción válida, intenta con otra')
    else:
      break

  # Show resume
  clear_screen()
  print('¿Es correcta la información? (s/n)\n')

  if(need_to_load_month):
    files_to_load = '\n    - '.join(files_names)
    files_to_load = '\n    - ' + files_to_load

    print(f'Necesitas cargar datos: Sí\n'
          f'Directorio base de archivos: {base_path}\n'
          f'Archivos a cargar: {files_to_load}\n'
          f'Año a crear: {year}\n'
          f'Semestre(s) a crear: {semesters_names[ int(semester) - 1 ]}\n')
  else:
    print(f'Necesitas cargar datos: No\n'
          f'Año a crear: {year}\n'
          f'Semestre(s) a crear: {semesters_names[ int(semester) - 1 ]}\n')

  while True:
    try:
      confirmation = input()
      confirmation = ask_for_confirmation(confirmation)

      if(confirmation):
        break
      else:
        clear_screen()
        is_correct_info()

    except Exception as error:
      error
  
  if(need_to_load_month):
    clear_screen()
    print('Cargando registros...')
    for file_name in files_names:
      data_loader.load(os.path.join(base_path, file_name))

  # Create database needed tables
  print('\n\n*** Creando tablas ***')
  print('Esto puede tardar bastante tiempo, no apagues ni suspendas el equipo....')

  try:
    dataset_creator = TableauDatasetCreator(year)
    
    dataset_creator.create_base_table()

    print(f'Tabla base "{dataset_creator.base_table}" creada')

    if(is_first_semester(semester) or are_both_semesters(semester)):
      dataset_creator.create_first_semester_table()

      print(f'Tabla del primer semestre "{dataset_creator.first_semester_table}" creada')
    
    if(is_second_semester(semester) or are_both_semesters(semester)):
      dataset_creator.create_second_semester_table()

      print(f'Tabla del segundo semestre "{dataset_creator.second_semester_table}" creada')

    print('\n******* Se terminaron de crear correctamente las tablas *******')
  except Exception as error:
    print('Error al crear las tablas')
    print(error)

is_correct_info()