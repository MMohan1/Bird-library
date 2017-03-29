from birds.models.birds_model import Birds
from datetime import datetime
from uuid import uuid4

class BirdsOpration(object):
    """
    this calss is used to to all the opration realted to birds library
    opration are --
    1.insert birds details
    2.delete a birds data
    3.get all birds details
    4.get a bird details

    """
    def __init__(self):
        
        pass


    def validate_input_data(self, data):
        """
        this method is used to validate insert data validation
        to insert the bird data reuire fileds are--
        name
        family
        continents
        
        """

        if "name" not in data or "family" not in data or "continents" not in data:
            return {"success":False, "message": "Please provide mendatory fields name, family and continents"}
        return {"success":True}
        
    def insert_birds(self,bird_data):
        """
        method is used to insert bird data

        --input
        @bird_data -- bird data that need to insert type(dict)

        --output
        response that conation data ingetsed or not
        """
        data_validation = self.validate_input_data(bird_data)  #request data validation

        if not data_validation["success"]:
            return data_validation,400
            
        br = Birds()
        br.id = str(uuid4())
        br.name = bird_data["name"]
        br.family = bird_data["family"]
        br.continents = bird_data["continents"]
        br.added = datetime.utcnow()
        br.visible = bird_data.get("visible",False)
        try:
            br.save()
            # data = br._data
            # data["added"] = datetime.strftime(data["added"],"%Y-%m-%d")
            return {"success":True, "message":"new bird added to the library"},201
        except Exception as e:
            if type(e).__name__ == "ValidationError":
                error_details = e.to_dict()
                return {"success":False, "message":"Please provide valid data","error_details":error_details},400
            return {"success":False, "message":"Something went wrong we will back soon"},400

    def delete_bird(self, bird_id):
        """
        method is used to delete bird data

        --input
        @bird_data -- br id type(str)

        --output
        response that conation data ingetsed or not
        """
        br = Birds.objects(id=bird_id).first()
        if br:
            br.delete()
            return {"success":True, "message":"brid removed"},200
        else:
            return {"success":False, "message":"Not Found"},404
        
    def get_birds(self, bird_id=None):
        """
        """
        if not bird_id:
            brds = Birds.objects(visible=True)
            out_put = [br.id for br in brds]
            return out_put,200
        else:
            br = Birds.objects(id=bird_id).first()
            if br:
                data = br.to_mongo().to_dict()
                data["added"] = datetime.strftime(data["added"],"%Y-%m-%d")
                return data,200
            else:
                return {"success":False, "message":"Not Found"},404