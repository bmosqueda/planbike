from validator import is_date_in_mysql_format
import re

class DateFormatException(Exception):
  pass

# dd/mm/yyyy  ->  yyyy-mm-dd
def date_to_mysql_format(date):
  if(len(date) != 10):
    raise DateFormatException('Not valid date, it does not have 10 length')

  if(is_date_in_mysql_format(date)):
    return date

  corrected_date = (
    date[6] + date[7] + date[8] + date[9] + '-' +
    date[3] + date[4] + '-' +
    date[1] + date[0]
  )

  if(not is_date_in_mysql_format(corrected_date)):
    raise DateFormatException(
            'It was not possible format date: {} to correct format. Result: {} '
            .format(date, corrected_date)
          )

  return corrected_date