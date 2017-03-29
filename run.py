# -*- coding: utf-8 -*-
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer
import sys
from birds import birds_app,config_dict
port_number = config_dict["birds_conf"]["port"]
sys.dont_write_bytecode = True
http_server = HTTPServer(WSGIContainer(birds_app))
http_server.listen(port_number, '0.0.0.0')
print "started service",port_number
IOLoop.instance().start()