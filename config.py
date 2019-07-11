import json

config = None
stage = 'development'
# stage = 'production'

with open('config.json') as json_file:  
  config = json.load(json_file)
  config = config[ stage ]

BASE_PATH = config[ "basePath" ]
UTILS_PATH = BASE_PATH + 'utils'
MODELS_PATH = BASE_PATH + 'models'
ERRORS_PATH = BASE_PATH + 'errors'

database = {
  'host': config[ 'host' ],
  'database': config[ 'database' ],
  'user': config[ 'user' ],
  'password': config[ 'password' ]
}