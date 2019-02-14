from flask import Flask, jsonify
import pandas as pd

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
rainfall_file = 'Data/rainfall.csv'
stations_file = 'Data/stations.csv'
rainfall_data = pd.read_csv(rainfall_file).drop(['Unnamed: 0'], axis=1).to_dict(orient='index')
stations_data = pd.read_csv(stations_file).drop(['Unnamed: 0'], axis=1).to_dict(orient='index')
@app.route("/v1.0/precipitation")
def precipitation():

    return jsonify(rainfall_data)


@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate Data API!<br/>"
        f"Available Routes:<br/>"
        f"/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
    )

@app.route("/api/v1.0/stations")
def stations():
        return jsonify(stations_data)
if __name__ == "__main__":
    app.run(debug=True)
