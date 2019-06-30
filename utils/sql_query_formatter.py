def get_params_string_separated_by_commas(params):
  params_separated_by_commas = ''

  for param in params:
    params_separated_by_commas += param.strip() + ', '

  return params_separated_by_commas[:-2]

def get_params_string_for_update_format(params):
  string_for_update_format = ''

  for param in params:
    string_for_update_format += param.strip() + ' = ?, '

  return string_for_update_format[:-2]

def get_percentage_s_separated_by_commas(marks_number):
  string_question_marks = ''

  for i in range(marks_number):
    string_question_marks += '%s, ';

  return string_question_marks[:-2]

def dictionary_to_tuple(dictionary, tuple_ordered_keys = None):
  to_tuple = []

  if(tuple_ordered_keys != None):
    for key in tuple_ordered_keys:
      to_tuple.append(dictionary[ key ])
  else:
    for key in dictionary:
      to_tuple.append(dictionary[ key ])

  return tuple(to_tuple)