need_to_load_month = False

while True:
  print("¿Necesitas cargar datasets de algunos meses? (s/n)")
  
  need_to_load_month = input()

  if(need_to_load_month.lower() != 's' and need_to_load_month.lower() != 'n'):
    print(f'{need_to_load_month} no es una opción válida')
  else:
    need_to_load_month = need_to_load_month.lower() == 's'
    break;

print(need_to_load_month)