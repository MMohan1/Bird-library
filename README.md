# Bird-library
==============

Overview
========
This is a python flask base mini we application that has functionality of

- `GET /api/v1.0/birds` - List all birds
- `POST /api/v1.0/birds` - Add a new bird
- `GET /api/v1.0/birds/{id}` - Get details on a specific bird
- `DELETE /api/v1.0/birds/{id}` - Delete a bird by id

Requirements
===========
MongoDb should be setup on the machine.


How To run
===========
steps
1) Clone the repo-

       git clone https://github.com/MMohan1/Bird-library.git

2) create a virtual env and activate it

       virtualenv birds_venv
       
       . birds/bin/activate


3) install the require python packages - got to clone repo and inside Bird-library run
    
       pip install -r requirements.txt

4) change the app confuguration if require - go to open /Bird-library/birds/config.ini and make change for mongo and app port
5) run the app

       python run.py

Please view #birds.json from flow and how to test.
