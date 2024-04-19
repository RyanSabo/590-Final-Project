from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/santa.html")
def santa():
    return render_template("santa.html")

@app.route('/sign_in', methods=['POST'])
def sign_in():
    group_name = request.form["groupName"]
    password = request.form["password"]

    # TODO: check if group exists in database

    return render_template("santa.html")


@app.route('/create_group', methods=['POST'])
def create_group():
    new_group_name = request.form["newGroupName"]
    new_password = request.form["newPassword"]

    #TODO: create new group in database

    return render_template("santa.html")

@app.route('/input_data', methods=['POST'])
def input_data():
    first_name = request.form["firstName"]
    last_name = request.form["lastName"]
    price_limit = request.form["priceLimit"]

    prefered_person_first_name = request.form["preferedPersonFirstName"]
    prefered_person_last_name = request.form["preferedPersonLastName"]

    least_prefered_person_first_name = request.form["leastPreferedPersonFirstName"]
    least_prefered_person_last_name = request.form["leastPreferedPersonLastName"]

    #TODO: crypto stuff

    return render_template("santa.html")



