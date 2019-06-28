import json
import mysql

with open('credentials.json') as json_file:  
class Database(mysql):
  def __init__(self):
    credentials = json.load(json_file)