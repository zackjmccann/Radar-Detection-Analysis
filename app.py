from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return("Slash page")

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