import os
import time

def clear_screen(): 
  if(os.name == 'posix'):
    _ = os.system('clear') 
  else:
    _ = os.system('cls')

def ask_for_confirmation():
  confirmation = input()

  confirmation = confirmation.lower()

  if(confirmation != 's' and confirmation != 'n'):
    print(f'{confirmation} no es una opción válida')
    raise Exception('Not valid confirmation option')
  else:
    return confirmation == 's'

def get_elapsed_time(start_time):
  return round(time.time() - start_time, 2)