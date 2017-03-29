# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import request
from birds.controller.birds_library import BirdsOpration

class Birds(Resource):
    """
    """
    def get(self,id=None):
        """
        """
        response = BirdsOpration().get_birds(id)
        return response[0],response[1]
        

        
    def post(self):
        """
        """
        json_data = request.get_json(force=True)
        response = BirdsOpration().insert_birds(json_data)
        return response[0],response[1]



    def delete(self, id=None):
        """
        """
        response = BirdsOpration().delete_bird(id)
        return response[0],response[1]
    