import os
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
import sqlalchemy
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import renewable_scrape
import json

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

    return render_template("index.html")

@app.route("/scrape")
def scrape():

    # Run the scrape function
    renewable_scrape.renewable_scrape()


    # Update the Mongo database using update and upsert=True
    # mongo.db.renewables.replace_one({}, renewable_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

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
    return render_template("templates/location.html")

@app.route("/sunburst")
def sunburst():
    data = json.load("my_renewables.json")
    print("Read Json")
    print(data)
    # data = mongo.db.renewables.find_one()
    return render_template("webscrape_sunburst.html")
    #,r_last_refresh=data["renewable_refresh"],renewable_title_0=data["renewable_titles"][0],renewable_link_0=data["renewable_links"][0],renewable_title_1=data["renewable_titles"][1],renewable_link_1=data["renewable_links"][1], renewable_title_2 = data["renewable_titles"][2],renewable_link_2=data["renewable_links"][2],renewable_title_3=data["renewable_titles"][3],renewable_link_3=data["renewable_links"][3])
    # return render_template("templates/sunburst.html")


if __name__ == '__main__':
    app.run(debug=True)
