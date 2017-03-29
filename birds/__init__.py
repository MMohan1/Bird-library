from flask import Flask
import os
from flask_restful import Api
import ConfigParser
birds_app = Flask(__name__)
birds_api= Api(birds_app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
ini_path = APP_ROOT + '/' + 'config.ini'
config = ConfigParser.ConfigParser()
config.read(ini_path)
config_dict = {s: dict(config.items(s)) for s in config.sections()}


from birds.router import routes

def run_server():
    birds_app.run('0.0.0.0', config["birds_conf"]["port"])



if __name__ == '__main__':
    run_server()