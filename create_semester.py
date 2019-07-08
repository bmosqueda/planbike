import sys
import config
import os

sys.path.append(config.UTILS_PATH)
sys.path.append(config.MODELS_PATH)

from validator import is_int
from bicycle_trips import BicycleTrip

bicycle_controller = BicycleTrip()

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

def call_month_data_loader(base_path, files_to_load):
  command = 'python3 month_data_loader.py '
  
  for file_name in files_to_load:
    command = command + ' ' + os.path.join(base_path, file_name)

  os.system(command)

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
  
  if(len(files_names) > 0):
    print('Cargando archivos...')
    call_month_data_loader(base_path, files_names)

  # Create database needed tables
  print('Creando tablas...')
  base_table = f'viajes_{year}'

  try:
    bicycle_controller.drop_table_if_exists(base_table)

    bicycle_controller.query(
      f'''CREATE TABLE {base_table} AS 
        SELECT * FROM registrobicis 
        WHERE YEAR(Fecha_Retiro) = {year}'''
    )

    print(f'Tabla base "{base_table}" creada')

    table_origin = f'''SELECT idRegistroBicis AS IDRegistro,
                               Genero_Usuario AS `Género`,
                               Edad_Usuario AS `Edad`,
                               Bici AS `Bici`,
                               Ciclo_Estacion_Retiro AS `Estación`,
                               Fecha_Retiro AS `Fecha`,
                               Hora_Retiro AS `Hora`,

                               'Origen' AS TipoRuta,
                               
                               CONCAT(Ciclo_Estacion_Retiro, '_', Ciclo_Estacion_Arribo) AS Ruta,

                               (CASE 
                                 WHEN are_valid_dates_diff(
                                        Fecha_Retiro,
                                        Hora_Retiro,
                                        Fecha_Arribo,
                                        Hora_Arribo
                                      ) THEN
                                         TIMEDIFF(
                                           CONCAT(Fecha_Arribo, ' ', Hora_Arribo),
                                           CONCAT(Fecha_Retiro, ' ', Hora_Retiro)
                                         ) 
                                 ELSE '00:00:00'
                               END) AS Tiempo
                        FROM {base_table}'''

    table_destiny = f'''SELECT idRegistroBicis AS IDRegistro,
                               Genero_Usuario AS `Género`,
                               Edad_Usuario AS `Edad`,
                               Bici AS `Bici`,
                               Ciclo_Estacion_Arribo AS `Estación`,
                               Fecha_Arribo AS `Fecha`,
                               Hora_Arribo AS `Hora`,

                               'Destino' AS TipoRuta,
                               
                               CONCAT(Ciclo_Estacion_Retiro, '_', Ciclo_Estacion_Arribo) AS Ruta,

                               (CASE 
                                 WHEN are_valid_dates_diff(
                                        Fecha_Retiro,
                                        Hora_Retiro,
                                        Fecha_Arribo,
                                        Hora_Arribo
                                      ) THEN
                                         TIMEDIFF(
                                           CONCAT(Fecha_Arribo, ' ', Hora_Arribo),
                                           CONCAT(Fecha_Retiro, ' ', Hora_Retiro)
                                         ) 
                                 ELSE '00:00:00'
                               END) AS Tiempo
                        FROM {base_table}'''

    first_semester_table = f'rutas_ene_jun_{year}'
    second_semester_table = f'rutas_jul_dic_{year}'

    if(is_first_semester(semester) or are_both_semesters(semester)):
      bicycle_controller.drop_table_if_exists(first_semester_table)

      bicycle_controller.query(
        f'''CREATE TABLE {first_semester_table} AS
              {table_origin}
              WHERE MONTH(Fecha_Retiro) <= 6
            UNION ALL
              {table_destiny}
              WHERE MONTH(Fecha_Retiro) <= 6'''
      )

      print(f'Tabla del primer semestre "{base_table}" creada')
    
    if(is_second_semester(semester) or are_both_semesters(semester)):
      bicycle_controller.drop_table_if_exists(second_semester_table)

      bicycle_controller.query(
        f'''CREATE TABLE {second_semester_table} AS
              {table_origin}
              WHERE MONTH(Fecha_Retiro) > 6
            UNION ALL
              {table_destiny}
              WHERE MONTH(Fecha_Retiro) > 6'''
      )

      print(f'Tabla del segundo semestre "{base_table}" creada')
  except Exception as error:
    print('Error al crear las tablas')
    print(error)

is_correct_info()