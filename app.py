from flask import Flask, jsonify

from db import Db
from tables import Measurement

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Welcome to the SQL Alchemy API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    return("precipitation")

@app.route("/api/v1.0/stations")
def stations():
    return("stations")

@app.route("/api/v1.0/tobs")
def tobs():
    return("tobs")

@app.route("/api/v1.0/<start>")
def start():
    return("start")

@app.route("/api/v1.0/<end>")
def end():
    return("end")

if __name__ == "__main__":
    app.run(debug=True)