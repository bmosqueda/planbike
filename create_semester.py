from os.path import exists
from os.path import isfile
from os import system

need_to_load_month = False
base_path = ''
files_names = []

def clear_screen(): 
  _ = system('cls')
  _ = system('clear') 

while True:
  print("¿Necesitas cargar datasets de algunos meses? (s/n)")
  
  need_to_load_month = input()

  if(need_to_load_month.lower() != 's' and need_to_load_month.lower() != 'n'):
    print(f'{need_to_load_month} no es una opción válida')
  else:
    need_to_load_month = need_to_load_month.lower() == 's'
    break;

if(need_to_load_month):
  clear_screen()

  while True:
    print('Escribe la ruta absoluta a la carpeta en donde están guardados los datasets')
    
    base_path = input()

    if(exists(base_path)):
      break;
    else:
      print('La ruta proporcionada no es válida, intenta con otra')

  clear_screen()
  
  print('Escribe el nombre de los archivos que quieres cargar. Para terminar escribe x')
  
  while True:
    file_name = input()
    
    if(file_name.lower() == 'x'):
      break
    elif(isfile(base_path + str(file_name))):
      files_names.append(str(file_name))
    else:
      print("Por favor proporciona el nombre de un archivo correcto")

  print(files_names)