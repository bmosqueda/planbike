import json
import mysql.connector
import sql_query_formatter as formatter

credentials = None

with open('credentials.json') as json_file:  
  credentials = json.load(json_file)

credentials = credentials["development"]

class Database:
  def __init__(self, table, props, primary_key):
    self.props = props
    self.table = table
    self.primary_key = primary_key

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

  def get_all(self):    
    return self.get_by_sql('SELECT * FROM {}'.format(self.table))

  def get_by_primary_key(self, primary_key):    
    return self.get_by_sql(
             'SELECT * FROM {} WHERE {} = %s'
                .format(self.table, self.primary_key),
              (primary_key,)
           )

  def insert(self, data):
    sql = ('INSERT INTO {} ({}) VALUES({})'
          .format(
            self.table, 
            formatter.get_params_string_separated_by_commas(self.props),
            formatter.get_percentage_s_separated_by_commas(len(self.props))
          ))

    if(type(data) == dict):
      data = formatter.dictionary_to_tuple(data, self.props)
    
    if(type(data) == list):
      data = tuple(data)

    cursor = self.query(sql, data)
    return cursor