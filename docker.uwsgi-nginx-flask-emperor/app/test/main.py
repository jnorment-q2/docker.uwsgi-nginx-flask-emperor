# encoding=UTF-8
#!flask/bin/python

import platform

from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return "Hello, this is test 1 running in {}~".format(platform.python_version())
      
if __name__ ==  '__main__':
	app.run(debug=True)      
        
