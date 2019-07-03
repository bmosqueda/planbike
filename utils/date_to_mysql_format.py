from validator import is_date_in_mysql_format
from validator import is_int
from validator import is_hour_in_mysql_format
import re

class DateFormatException(Exception):
  pass

# date  ->  yyyy-mm-dd
def date_to_mysql_format(date):
  if(len(date) != 10):
    raise DateFormatException('Not valid date, it does not have 10 length')

  if(is_date_in_mysql_format(date)):
    if(is_valid_date(date)):
      return date
    else:
      raise DateFormatException('{} is not a valid date'.format(date))
  
  date_list = split_date(date)

  corrected_date = (
    date_list[ 0 ] + '-' +
    date_list[ 1 ] + '-' +
    date_list[ 2 ]
  )

  if(not is_date_in_mysql_format(corrected_date)):
    raise DateFormatException(
            'It was not possible format date: {} to correct format. Result: {} '
            .format(date, corrected_date)
          )

  if(is_valid_date(corrected_date)):
    return corrected_date
  else:
    raise DateFormatException('{} is not a valid date'.format(corrected_date))

def is_valid_date(date):
  date = str(date)
  date_list = date.split('-')

  year = date_list[0]
  month = date_list[1]
  day = date_list[2]
  
  return is_valid_year(year) and is_valid_month(month) and is_valid_day(year, month, day)

def is_valid_year(year):
  year = int(year)

  return year >= 2010 and year <= 2050

def is_valid_month(month):
  month = int(month)

  return month >= 1 and month <= 12

def is_valid_day(year, month, day):
  days_months = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

  month = int(month)
  day = int(day)

  try:
    days_month = days_months[ month - 1 ]

    if(month == 2 and is_leap_year(year)):
      days_months = 29

    return day >= 1 and day <= days_month

  except Exception as error:
    return False

def is_leap_year(year):
  year = int(year)

  if (year % 4) == 0:  
    if (year % 100) == 0:  
      if (year % 400) == 0:  
        return True
      else:  
        return False
    else:  
      return True
  else:  
    return False
    
def split_date(date):
  list_date = []

  try:
    list_date = date.index('-')
    
  except Exception as error:
    list_date = date.index('/')

  # El año siempre va al principio
  if(len(list_date[ 2 ]) == 4)
    temp = list_date[ 0 ]
    list_date[ 0 ] = list_date[ 2 ]
    list_date[ 2 ] = temp

  return list_date