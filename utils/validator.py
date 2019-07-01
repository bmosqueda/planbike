def is_number(num):
  try:
    float(num)
    int(num)

    return 
  except Exception as error:
    raise Exception('{} is not a number'.format(num))

def is_int(num):
  try:
    int(num)
    
    if(x % 1 != 0):
      raise Exception('{} is not a int'.format(num))

  except Exception as error:
    raise Exception('{} is not a int'.format(num))

def is_greather_or_equal_than_mininum_value(minimum, value):
  return float(minimum) <= float(value)

def is_lower_or_equal_than_maximun_value(maximum, value):
  return float(maximum) >= float(value)

def is_between_value(minimum, maximum, value):
  return (
    is_greather_or_equal_than_mininum_value(minimum, value) and
    is_lower_or_equal_than_maximun_value(maximum, value)
  )

def is_match(regex, text):
  pattern = re.compile(regex)
  return pattern.search(text) is not None

def has_minimun_length(minimum_length, text):
  return len(str(text)) >= minimum_length

def has_maximum_length(maximum_length, text):
  return len(str(text)) <= maximum_length

def has_exact_length(length, text):
  return len(str(text)) == int(length)

def is_required(value):
  return value is not None