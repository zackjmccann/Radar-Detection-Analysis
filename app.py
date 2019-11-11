from flask import Flask, jsonify
import datetime as dt
import pandas as pd
from db import Db
from tables import Measurement

app = Flask(__name__)

database = Db('hawaii')

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
    session = database.get_session()
    last_date = dt.datetime(2017, 8, 23)
    query_date = last_date - dt.timedelta(days=365)
    last_12_months = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date.between(query_date,last_date))
    dates = [x.date for x in last_12_months]
    prcp = [x.prcp for x in last_12_months]
    d = {key:value for key, value in zip(dates, prcp)}
    session.close()
    return jsonify(d)


@app.route("/api/v1.0/stations")
def stations():
    session = database.get_session()
    stations = session.query((Measurement.station).distinct())
    all_stations = []
    for x in stations:
        all_stations.append(x)
    session.close()
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = database.get_session()
    last_date = dt.datetime(2017, 8, 23)
    query_date = last_date - dt.timedelta(days=365)
    last_12_months_tobs = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date.between(query_date,last_date))
    tobs_dates = [x.date for x in last_12_months_tobs]
    tobs = [x.tobs for x in last_12_months_tobs]
    d = {key:value for key, value in zip(tobs_dates, tobs)}
    session.close()
    return jsonify(d)

@app.route("/api/v1.0/<start>")
def start():
    return("start")

@app.route("/api/v1.0/<end>")
def end():
    return("end")

if __name__ == "__main__":
    app.run(debug=True)