from validator import is_match
import re

def is_in_correct_format(date):
  # yyyy-mm-dd
  valid_format_regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

  return is_match(valid_format_regex, date)

# dd/mm/yyyy  ->  yyyy-mm-dd
def date_to_mysql_format(date):
  if(is_in_correct_format(date)):
    return date

  corrected_date = (
    date[6] + date[7] + date[8] + date[9] + '-' +
    date[3] + date[4] + '-' +
    date[1] + date[0]
  )

  if(not is_in_correct_format(corrected_date)):
    raise Exception(
            'It was not possible format date: {} to correct format. Result: {} '
            .format(date, corrected_date)
          )

  return corrected_date