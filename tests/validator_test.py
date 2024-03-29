import unittest
import config
import sys

sys.path.append(config.UTILS_PATH)

import validator

class TestStringMethods(unittest.TestCase):
  def test_is_number(self):
    self.assertTrue(validator.is_number(1))
    self.assertTrue(validator.is_number("1"))
    self.assertTrue(validator.is_number("1"))
    self.assertTrue(validator.is_number("-15"))
    self.assertTrue(validator.is_number(None))

    self.assertFalse(validator.is_number("15.655f"))
    self.assertFalse(validator.is_number("hola"))
    self.assertFalse(validator.is_number(False))
    self.assertFalse(validator.is_number(''))

  def test_is_int(self):
    self.assertTrue(validator.is_int(16))
    self.assertTrue(validator.is_int(-18))
    self.assertTrue(validator.is_int("-18"))
    self.assertTrue(validator.is_number(None))

    self.assertFalse(validator.is_int("3.1416"))
    self.assertFalse(validator.is_number(False))
    self.assertFalse(validator.is_int(3.1416))
    self.assertFalse(validator.is_int(''))

  def test_is_required(self):
    self.assertFalse(validator.is_required(None))

    self.assertTrue(validator.is_required("None"))
    self.assertTrue(validator.is_required(True))
    self.assertTrue(validator.is_required(56))
    self.assertTrue(validator.is_required(598.4654))
    self.assertTrue(validator.is_required(''))

  def test_is_date_in_mysql_format(self):
    self.assertTrue(validator.is_date_in_mysql_format('2019-07-01'))
    self.assertTrue(validator.is_date_in_mysql_format('2005-09-01'))
    self.assertTrue(validator.is_date_in_mysql_format(None))

    self.assertFalse(validator.is_date_in_mysql_format('2019/07/01'))
    self.assertFalse(validator.is_date_in_mysql_format(6565))
    self.assertFalse(validator.is_date_in_mysql_format(False))
    self.assertFalse(validator.is_date_in_mysql_format('20159-07-01'))
    self.assertFalse(validator.is_date_in_mysql_format(''))

  def test_min_value(self):
    self.assertTrue(validator.min_value(20, 65))
    self.assertTrue(validator.min_value(20, 20))
    self.assertTrue(validator.min_value(13.26, 13.27))

    self.assertFalse(validator.min_value(20, 19))
    self.assertFalse(validator.min_value(14.98, 13.2))
    self.assertFalse(validator.min_value(14.98, "13.2a"))
    self.assertFalse(validator.min_value(14.98, ""))

  def test_max_value(self):
    self.assertTrue(validator.max_value(65, 65))
    self.assertTrue(validator.max_value(20, 20))
    self.assertTrue(validator.max_value(13.26, 13.25))

    self.assertFalse(validator.max_value(50, 51))
    self.assertFalse(validator.max_value(14.98, 14.99))
    self.assertFalse(validator.max_value(14.98, "13.2a"))
    self.assertFalse(validator.max_value(14.98, ""))

  def test_is_match(self):
    self.assertTrue(validator.is_match('[0-9]', 5))
    self.assertTrue(validator.is_match('[0-9]', 'hola5mundo'))
    self.assertTrue(validator.is_match('[0-9]', None))
    self.assertTrue(validator.is_match('^[a-z]$', 'h'))
    self.assertTrue(validator.is_match('[a-z]', 'hola'))

    self.assertFalse(validator.is_match('[0-9]', 'hola'))

  def test_min_length(self):
    self.assertTrue(validator.min_length(5, 'holamundo'))
    self.assertTrue(validator.min_length(4, 'hola'))
    self.assertTrue(validator.min_length(5, 56565))
    self.assertTrue(validator.min_length(5, None))

    self.assertFalse(validator.min_length(50, 'holamundo'))
    self.assertFalse(validator.min_length(50, ''))

  def test_max_length(self):
    self.assertTrue(validator.max_length(5, 'hola'))
    self.assertTrue(validator.max_length(4, 'hola'))
    self.assertTrue(validator.max_length(8, 56565))
    self.assertTrue(validator.max_length(5, None))
    self.assertTrue(validator.max_length(10, ''))

    self.assertFalse(validator.max_length(10, 'holamundo hola :v'))
    self.assertFalse(validator.max_length(10, 'nada de nada'))
    self.assertFalse(validator.max_length(10, False))

  def test_has_exact_length(self):
    self.assertTrue(validator.has_exact_length(5, 'haola'))
    self.assertTrue(validator.has_exact_length(4, 'hola'))
    self.assertTrue(validator.has_exact_length(8, 56565698))
    self.assertTrue(validator.has_exact_length(5, None))

    self.assertFalse(validator.has_exact_length(10, 'holamundo hola :v'))
    self.assertFalse(validator.has_exact_length(10, 'nada de nada'))
    self.assertFalse(validator.has_exact_length(10, False))
    self.assertFalse(validator.has_exact_length(1, ''))

  def test_is_hour_in_mysql_format(self):
    self.assertTrue(validator.is_hour_in_mysql_format('15:10:32'))
    self.assertTrue(validator.is_hour_in_mysql_format('15:10:32.23'))
    self.assertTrue(validator.is_hour_in_mysql_format('15:10:32.23004'))
    self.assertTrue(validator.is_hour_in_mysql_format('15:10:32.230046'))

    self.assertFalse(validator.is_hour_in_mysql_format('15:10:32.2'))
    self.assertFalse(validator.is_hour_in_mysql_format('15:10:32.20300454'))
    self.assertFalse(validator.is_hour_in_mysql_format('15:10:325'))
    self.assertFalse(validator.is_hour_in_mysql_format('15:105:325'))
    self.assertFalse(validator.is_hour_in_mysql_format(6565))
    self.assertFalse(validator.is_hour_in_mysql_format(''))

  def test_is_valid_hour(self):
    self.assertTrue(validator.is_valid_hour('15:10:32'))
    self.assertTrue(validator.is_valid_hour('23:59:59.99000'))
    self.assertTrue(validator.is_valid_hour('00:00:00'))
    self.assertTrue(validator.is_valid_hour('21:10:32.230046'))

    self.assertFalse(validator.is_valid_hour('15:60:32.2'))
    self.assertFalse(validator.is_valid_hour('20:10:60.59'))
    self.assertFalse(validator.is_valid_hour('24:10:325'))
    self.assertFalse(validator.is_valid_hour('15:105:325'))
    self.assertFalse(validator.is_valid_hour(''))

if __name__ == '__main__':
    unittest.main()