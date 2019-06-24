import sys
sys.path.append('/home/bmosqueda/Downloads/BIKE/Code/utils')
from date_to_mysql_format import date_to_mysql_format

import json
import mysql

with open('credentials.json') as json_file:  
  credentials = json.load(json_file)
  print(credentials)

help(mysql)