import unittest
import config
import sys

sys.path.append(config.UTILS_PATH)

from date_to_mysql_format import date_to_mysql_format, DateFormatException

class TestDates(unittest.TestCase):
  def test_to_mysql_format(self):
    date_to_mysql_format
    self.assertTrue(date_to_mysql_format('2019-03-05'))
    self.assertTrue(date_to_mysql_format('05-03-2019'))
    self.assertTrue(date_to_mysql_format('2019/03/05'))
    self.assertTrue(date_to_mysql_format('2019a03a05'))
    self.assertTrue(date_to_mysql_format('12/12/2019'))
    self.assertTrue(date_to_mysql_format('28*2*2019'))
    self.assertTrue(date_to_mysql_format('1*4*2018'))

    self.assertRaises(DateFormatException, date_to_mysql_format, '29-02-2010')
    self.assertRaises(DateFormatException, date_to_mysql_format, '12-04-2008')

    self.assertRaises(DateFormatException, date_to_mysql_format, '05-03-20159')
    self.assertRaises(DateFormatException, date_to_mysql_format, '29/02-2010')
    self.assertRaises(DateFormatException, date_to_mysql_format, '2902-2010')
    self.assertRaises(DateFormatException, date_to_mysql_format, '29/022010')
    self.assertRaises(DateFormatException, date_to_mysql_format, '1234567890')
    self.assertRaises(DateFormatException, date_to_mysql_format, '656564+54-5464')
    self.assertRaises(DateFormatException, date_to_mysql_format, '1*1*10')
    self.assertRaises(DateFormatException, date_to_mysql_format, 0)

if __name__ == '__main__':
    unittest.main()