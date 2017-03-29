# -*- coding: utf-8 -*-
from birds import config_dict
from mongoengine import DynamicDocument,connect,StringField,ListField,BooleanField,DateTimeField
connect(db=config_dict["mongo"]["db_name"],host=config_dict["mongo"]["host"])

class Birds(DynamicDocument):
    id = StringField(required=True, primary_key=True,min_length=1) #Object id from the database
    name = StringField(required=True,min_length=1)  #English bird name
    family = StringField(required=True,min_length=1) #Latin bird family name
    continents = ListField(StringField(),required=True,null=False) #Continents the bird exist on
    added = DateTimeField(required=True) #Date the bird was added to the registry. Format YYYY-MM-DD
    visible = BooleanField(default=False) #Determines if the bird should be visible in lists
    

    # meta = {
    #     'indexes':['id']
    # }
