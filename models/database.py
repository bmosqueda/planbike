import json
import mysql.connector

credentials = None

with open('credentials.json') as json_file:  
  credentials = json.load(json_file)

credentials = credentials["development"]

class Database:
  def __init__(self, table):
    self.table = table

    self.connector = mysql.connector.connect(
      host = credentials["host"],
      database = credentials["database"],
      user = credentials["user"],
      passwd = credentials["password"]
    )

  def query(self, sql, params = tuple()):
    cursor = self.connector.cursor(dictionary = True)
    cursor.execute(sql, params)

    return cursor

  def get_by_sql(self, sql, params = tuple()):
    cursor = self.query(sql, params)
    
    return cursor.fetchall()

  def insert(self, sql, params = tuple()):
    cursor = query(sql, params)

    return cursor._last_insert_id

  def get_all(self):    
    return self.get_by_sql('SELECT * FROM {}'.format(self.table))