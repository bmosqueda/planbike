import re

def is_number(num):
  if(num is None):
    return True
  elif(type(num) is bool):
    return False

  try:
    float(num)

    return True
  except Exception as error:
    return False

def is_int(num):
  if(num is None):
    return True
  elif(type(num) is bool):
    return False

  try:
    int(num)
    
    if(float(num) % 1 != 0):
      return False

    return True
  except Exception as error:
    return False

def is_required(value):
  return value is not None

def is_date_in_mysql_format(date):
  if(date is None):
    return True

  date = str(date)
  # yyyy-mm-dd
  valid_format_regex = '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
  return is_match(valid_format_regex, date)

def is_hour_in_mysql_format(hour):
  if(hour is None):
    return True

  hour = str(hour)
  valid_format_regex = '^[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}(\.[0-9]{2,6})?$'

  return is_match(valid_format_regex, hour)

def is_valid_hour(hour_string):
  if(hour_string is None):
    return True

  hour_string = str(hour_string)
  hour_list = hour_string.split(':')

  hours = float(hour_list[0])
  minutes = float(hour_list[1])
  seconds = float(hour_list[2])

  return (
        hours >= 0 and hours <= 23 and
        minutes >= 0 and minutes < 60 and
        seconds >= 0 and seconds < 60
      )

def min_value(minimum, value):
  if(not is_number(minimum) or not is_number(value)):
    return False

  return float(minimum) <= float(value)

def max_value(maximum, value):
  if(not is_number(maximum) or not is_number(value)):
    return False

  return float(maximum) >= float(value)

def is_between_value(minimum, maximum, value):
  if(value is None):
    return True

  return (
    min_value(minimum, value) and
    max_value(maximum, value)
  )

def is_match(regex, text):
  if(text is None):
    return True

  pattern = re.compile(regex)

  return pattern.search(str(text)) is not None

def min_length(length, text):
  if(text is None):
    return True
  elif(type(text) is bool):
    return False

  return len(str(text)) >= int(length)

def max_length(length, text):
  if(text is None):
    return True
  elif(type(text) is bool):
    return False

  return len(str(text)) <= int(length)

def has_exact_length(length, text):
  if(text is None):
    return True
  elif(type(text) is bool):
    return False

  return len(str(text)) == int(length)

class ValidationException(Exception):
  pass

class Validator:
  def __init__(self, rules):
    self.rules = rules
    self.result = []

    self.errors = {
      'is_number': '{} debe ser un número: {}',
      'is_int': '{} debe de ser un valor entero: {}',
      'min_value': '{} debe ser mayor o igual a {} : {}',
      'max_value': '{} debe ser menor o igual a {} : {}',
      'is_between_value': '{} debe estar entre {} y {} : {}',
      'is_date_in_mysql_format': '{} debe tener el formato de fecha yyyy-mm-dd : {}',
      'is_hour_in_mysql_format': '{} debe tener el formato de hora hh:mm:ss[.ss[ssss]] : {}',
      'is_valid_hour': '{} no es una hora válida : {}',
      'is_match': '{} no cumple {} : {}',
      'min_length': '{} debe de tener por lo menos {} caracteres : {}',
      'max_length': '{} debe de tener máximo {} caracteres : {}',
      'has_exact_length': '{} debe tener exactamente {} caracteres : {}',
      'is_required ': '{} es requerido: {}'
    }

    self.validators = {
      'is_number': is_number,
      'is_int': is_int,
      'min_value': min_value,
      'max_value': max_value,
      'is_between_value': is_between_value,
      'is_date_in_mysql_format': is_date_in_mysql_format,
      'is_hour_in_mysql_format': is_hour_in_mysql_format,
      'is_valid_hour': is_valid_hour,
      'is_match': is_match,
      'min_length': min_length,
      'max_length': max_length,
      'has_exact_length': has_exact_length,
      'is_required': is_required
    }

  def get_field_rules(self, field):
    return self.rules[ field ].split('|')

  def is_rule_whit_paramether(self, rule):
    try:
      rule.index(',')
      return True
    except Exception as error:
      return False

  def validate(self, data, fields = None):
    self.result = []

    if(fields is None):
      fields = list(self.rules)

    for field in fields:
      field_rules = self.get_field_rules(field)

      for rule in field_rules:
        if(self.is_rule_whit_paramether(rule)):
          rule = rule.split(',')
          param = rule[ 1 ]
          rule = rule[ 0 ]

          if(not self.validators[ rule ](param, data[ field ])):
            self.result.append(self.errors[ rule ].format(field, param, data[ field ]))
        else:
          if(not self.validators[ rule ](data[ field ])):
            self.result.append(self.errors[ rule ].format(field, data[ field ]))

    if(len(self.result) > 0):
      raise ValidationException('There are some errors, look at result property to see them')