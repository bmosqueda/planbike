from datetime import datetime
import re

class DateFormatException(Exception):
  pass

min_date = datetime(2010, 2, 2)
max_date = datetime(2099, 12, 12)

# date  ->  yyyy-mm-dd
def date_to_mysql_format(date):
  date = str(date)

  try:
    date_list = split_date(date)
    
    if(len(date_list) != 3):
      raise Exception('Not valid date')

    date_obj = datetime(int(date_list[ 0 ]), int(date_list[ 1 ]), int(date_list[ 2 ]))

    if(not min_date <= date_obj <= max_date):
      raise DateFormatException(f'Date out of valid dates: {format_date(min_date)} - {format_date(max_date)}')
    
    return format_date(date_obj)

  except ValueError as error:
    raise DateFormatException('Not valid values to that date')
  except Exception as error:
    raise DateFormatException(error)

def format_date(date):
  return date.strftime('%Y-%m-%d')

def split_date(date):
  list_date = []
  try:
    separator = get_separator(date)
    list_date = date.split(separator)

    if(len(list_date) != 3 ):
      raise Exception("Not valid separator")

  except Exception as error:
    raise error

  # El año siempre va al principio
  if(len(list_date[ 2 ]) == 4):
    temp = list_date[ 0 ]
    list_date[ 0 ] = list_date[ 2 ]
    list_date[ 2 ] = temp

  return list_date

def get_separator(date):
  separator = re.findall(
                r"^\d*(.)\d*\1\d*$", 
                date
              )

  if(len(separator) == 0):
    raise Exception(f'{date} has no separator')

  return separator[ 0 ]