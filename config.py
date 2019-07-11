import json
from os import path 

config = None
stage = 'development'

with open('config.json') as json_file:  
  config = json.load(json_file)
  config = config [ stage ]

BASE_PATH = config[ "basePath" ]
UTILS_PATH = path.join(BASE_PATH, 'utils')
MODELS_PATH = path.join(BASE_PATH, 'models')
ERRORS_PATH = path.join(BASE_PATH, 'erros')

database = {
  'host': config[ 'host' ],
  'database': config[ 'database' ],
  'user': config[ 'user' ],
  'password': config[ 'password' ]
}