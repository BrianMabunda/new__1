# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template
import pickle
from keras.models import load_model
from flask_cors import CORS

models={"Appples":load_model("../project_models/apples_model1.h5"),"Orange":load_model("../project_models/orange_model1.h5")}

app = Flask(__name__)
CORS(app, resources={r"*": {"origin": "*"}})
# api_conf = {"origins": ["http://localhost:5000"], "method": ["GET"]}
# cors = CORS(app, resources={r"*": {"origin": "*"}})


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    summary=""
    
    return render_template("Home.html")


@app.route('/TestPrediction')
# ‘/’ URL is bound with hello_world() function.
def cancer():
    return render_template("index.html")



# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
