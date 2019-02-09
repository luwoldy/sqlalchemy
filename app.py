from flask import Flask, jsonify
import pandas as pd

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
file = 'Data/rainfall.csv'
rainfall_data = pd.read_csv(file).drop(['Unnamed: 0'], axis=1).to_dict(orient='index')


@app.route("/v1.0/precipitation")
def precipitation():

    return jsonify(rainfall_data)


@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate Data API!<br/>"
        f"Available Routes:<br/>"
        f"/v1.0/precipitation"
    )


if __name__ == "__main__":
    app.run(debug=True)
