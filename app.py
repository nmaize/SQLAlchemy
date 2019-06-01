import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

#First Route - Homepage
#Need - List all routes available:
    # `/api/v1.0/precipitation`
    # `/api/v1.0/stations`
    # `/api/v1.0/tobs`

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
    )

   
#Second Route - `/api/v1.0/precipitation`
    # From "prec_data", return date as key and prcp asvalue
    # Return the JSON representation of your dictionary (jsonify)
    # Queries have  been defined in jupyter notebook/Copy and Paste here
    #Use as a reference to create the dictionary of date as key and prcp as value
    # Create a dictionary from the row data and append to a list of all_passengers
    # all_passengers = []
    # for passenger in results:
    #     passenger_dict = {}
    #     passenger_dict["name"] = passenger.name
    #     passenger_dict["age"] = passenger.age
    #     passenger_dict["sex"] = passenger.sex
    #     all_passengers.append(passenger_dict)


#Third Route - `/api/v1.0/stations`
    # Return "station_list" and return (jsonify)

#Fourth Route - `/api/v1.0/tobs`
    # Use station_TOBS from jupyter notebook and return results using (jsonify)

if __name__ == '__main__':
    app.run(debug=True)
