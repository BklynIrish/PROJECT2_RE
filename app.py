import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///project.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Dataset = Base.classes.dataset


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/")
def welcome():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/hydro")
def hydro():
    """Return dashboard.html."""
    return render_template("hydro.html")

@app.route("/wind")
def wind():
    """Return dashboard.html."""
    return render_template("wind.html")


@app.route("/heatmap")
def heatmap():
    """Return dashboard.html."""
    return render_template("heatmap.html")

@app.route("/solar")
def solar():
    """Return dashboard.html."""
    return render_template("solar.html")

@app.route("/location")
def location():
    """Return dashboard.html."""
    return render_template("location.html")

@app.route("/sunburst")
def sunburst():
    """Return dashboard.html."""
    return render_template("sunburst.html")


# @app.route("/")
# def welcome():
#     """List all available api routes."""
#     return (
#         f"Available Routes:<br/>"
#         f"/api/v1.0/name<br/>"
#         f"/api/v1.0/primary_fuel"
#     )

# @app.route("/api/v1.0/name")
# def names():

#     session = Session(engine)
#     results = session.query(Dataset.name).all()
#     session.close()
#     all_names = list(np.ravel(results))
#     return jsonify(all_names)



if __name__ == '__main__':
    app.run(debug=True)
