from flask import Flask, request
from flask_cors import CORS
from pprint import pprint

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def root():
  pprint(request.__dict__)
  # log to server

  return 'Okay'
  # return 200

if __name__ == '__main__':
  app.run('0.0.0.0', port=7238)
