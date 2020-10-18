#import dependencies for SQL
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


import renewable_scrape

app = Flask(__name__)

#Need to fix
app.config["MONGO_URI"] = "mongodb://localhost:27017/renewables"
mongo = PyMongo(app)

@app.route("/")
def home():


    data = mongo.db.renewables.find_one()

    return render_template("index.html",r_last_refresh=data["renewable_refresh"],renewable_title_0=data["renewable_titles"][0],renewable_link_0=data["renewable_links"][0],renewable_title_1=data["renewable_titles"][1],renewable_link_1=data["renewable_links"][1], renewable_title_2 = data["renewable_titles"][2],renewable_link_2=data["renewable_links"][2],renewable_title_3=data["renewable_titles"][3],renewable_link_3=data["renewable_links"][3])


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    renewable_data = renewable_scrape.renewable_scrape()


    # Update the Mongo database using update and upsert=True
    mongo.db.renewables.replace_one({}, renewable_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

@app.route("/maps")
def maps():
    #put html for maps


    return



if __name__ == "__main__":
    app.run(debug=True)

