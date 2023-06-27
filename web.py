import flask
from flask import request, jsonify
import student_generator_v2 as sg
#create an app
app= flask.Flask(__name__)

#use student generator program as a base
#write4 a function to create and return a list of student dictionaries
#create 2 routes
# - return all students
# - returns students by id

#automatically reload server when changes made
app.config["DEBUG"] = True

#load student dictionaries
student_dictionaries = sg.get_student_dictionaries()
@app.route('/', methods=["GET"])
def index():
    return "<h1 style='color:blue; font-size: 500%;'> My name is Riah Wigfall</h1>"

#create route to return all student data
@app.route('/api/students/all', methods=['GET'])
def api_all():
    return jsonify(student_dictionaries)

app.run()
#to see on the web write-/api/students/all
#to download flask type-pip3 install flask
