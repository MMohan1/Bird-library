from mongoengine import DynamicDocument,connect,StringField,ListField,BooleanField,DateTimeField
connect(db='birds_library',host="localhost")

class Birds(DynamicDocument):
    id = StringField(required=True, primary_key=True) #Object id from the database
    name = StringField(required=True)  #English bird name
    family = StringField(required=True) #Latin bird family name
    continents = ListField(StringField()) #Continents the bird exist on
    added = DateTimeField(required=True) #Date the bird was added to the registry. Format YYYY-MM-DD
    visible = BooleanField(default=False) #Determines if the bird should be visible in lists
    

    # meta = {
    #     'indexes':['id']
    # }
