# encoding=UTF-8
#!flask/bin/python

from flask import Flask
app = Flask(__name__)

import requests
import logging
from flask import Flask, request
app = Flask(__name__)

app.debug = True
fh = logging.FileHandler('/tmp/appd/logs/flask.log')
app.logger.addHandler(fh)

# url = 'http://localhost:5000/'
# url = 'http://localhost/test/'
# url = 'http://google.com'
# url = google_url
ec2_t2_server = 'ec2-18-218-79-162.us-east-2.compute.amazonaws.com'
ec2_t2 = 'http://{}/t2/test2/tier2/'.format(ec2_t2_server)
url = ec2_t2

@app.route('/', methods=['GET'])
def index2():
        app.logger.info('Calling test2/.')
        return "Hello, this is test 2 ~"
      
@app.route('/tier2/', methods=['GET'])
def call_tier2():
        app.logger.info('Calling call_tier2.')
        app.logger.info('Calling call_tier2 with {}.'.format(url))
        response = requests.get(url)
        app.logger.info('Response from {}: {}'.format(url, response))
        ret_string = '{}   {}  {}'.format(response.status_code, response.content[0:200], len(response.content))
        app.logger.info('Response content: {}'.format(ret_string))
        return ret_string


if __name__ ==  '__main__':
	app.run()
        # debug=True)      
        
