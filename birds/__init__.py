from flask import Flask
import os
from flask_restful import Api
birds_app = Flask(__name__)
#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)
birds_api= Api(birds_app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
ini_path = APP_ROOT + '/' + 'config.ini'
# cfgreader = ConfigReaderWrapper()
# config_dict = cfgreader.read_configurations_from_ini(ini_path)
# port = config_dict['parser_conf']['port']


from birds.router import routes

def run_server():
    birds_app.run('0.0.0.0', "5010")



if __name__ == '__main__':
    run_server()