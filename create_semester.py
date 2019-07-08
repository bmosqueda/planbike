import sys
import config

sys.path.append(config.UTILS_PATH)
sys.path.append(config.MODELS_PATH)

from validator import is_int
from os import system
import os

semesters_options = {
  'first': 1,
  'second': 2,
  'both': 3
}

semesters_names = [ 'Primero', 'Segundo', 'Ambos' ]

def clear_screen(): 
  if(os.name == 'posix'):
    _ = system('clear') 
  else:
    _ = system('cls')

def ask_for_confirmation(confirmation):
  confirmation = confirmation.lower()

  if(confirmation != 's' and confirmation != 'n'):
    print(f'{confirmation} no es una opción válida')
    raise Exception('Not valid confirmation option')
  else:
    return confirmation == 's'

def call_month_data_loader(base_path, files_to_load):
  command = 'python3 month_data_loader.py '
  
  for file_name in files_to_load:
    command = command + ' ' + os.path.join(base_path, file_name)

  system(command)

def get_yes_no_by_boolean(value):
  return 'Sí' if value else 'No'

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

  # clear_screen()

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

  print("Todo correcto")
  
  if(len(files_names) > 0):
    print('Include files_names')
    # call_month_data_loader(base_path, files_names)

is_correct_info()