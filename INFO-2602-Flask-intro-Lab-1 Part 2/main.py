from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)

person = [{
    "firstName": "Billy",
    "lastName": "Mith",
    "id": "Per0001",
}, {
    "firstName": "Bob",
    "lastName": "Smith",
    "id": "Per0002",
}]


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response


'''
@app.route('/students')
def get_students():
    return jsonify(data)# return student data in response
'''


@app.route('/students')  #e.g /students?pref=Fish
def get_students():
    result = []
    pref = request.args.get('pref')  # get the parameter from url
    if pref:
        for student in data:  # iterate dataset
            if student[
                    'pref'] == pref:  # select only the students with a given meal preference
                result.append(student)  # add match student to the result
        return jsonify(result)  # return filtered set if parameter is supplied
    return jsonify(data)  # return entire dataset if no parameter supplied


@app.route('/students/<id>')
def get_student(id):
    for student in data:
        if student[
                'id'] == id:  # filter out the students without the specified id
            return jsonify(student)


#Class Exercise
@app.route('/hello/<firstName>/<lastName>')
def get_person(firstName, lastName):
    for p in person:
        if p['firstName'] == firstName and p['lastName'] == lastName:  # filter
            return jsonify({"message": f"Hi, {firstName} {lastName}"})


#Exercise 1
@app.route('/stats')
def calculate():

    Chicken = 0
    Computer_Science_Major = 0
    Computer_Science_Special = 0
    Fish = 0
    Information_Technology_Major = 0
    Information_Technology_Special = 0
    Vegetable = 0

    for student in data:
        if student['programme'] == "Computer Science (Major)":
            Computer_Science_Major += 1
        elif student['programme'] == "Computer Science (Special)":
            Computer_Science_Special += 1
        elif student['programme'] == "Information Technology (Major)":
            Information_Technology_Major += 1
        elif student['programme'] == "Information Technology (Special)":
            Information_Technology_Special += 1

        if student['pref'] == "Chicken":
            Chicken += 1
        elif student['pref'] == "Fish":
            Fish += 1
        elif student['pref'] == "Vegetable":
            Vegetable += 1

    return jsonify({
        "Chicken": Chicken,
        "Computer Science Major": Computer_Science_Major,
        "Computer Science Special": Computer_Science_Special,
        "Fish": Fish,
        "Information Technology Major": Information_Technology_Major,
        "Information Technology Special": Information_Technology_Special,
        "Vegetable": Vegetable
    })


#Exercise 2
@app.route('/add/<a>/<b>')
def add_values(a, b):
    sum = float(a) + float(b)
    return jsonify({"Sum: ": sum})


@app.route('/subtract/<a>/<b>')
def subtract_values(a, b):
    if float(a) > float(b):
        subtract = float(a) - float(b)
    elif float(b) > float(a):
        subtract = float(b) - float(a)
    elif float(a) == float(b):
        subtract = 0
    return jsonify({"Result: ": subtract})


@app.route('/multiply/<a>/<b>')
def multiply_values(a, b):
    multiply = float(a) * float(b)
    return jsonify({"Product: ": multiply})


@app.route('/divide/<a>/<b>')  #Format 21/7 = 3, 21 is the a and 7 is the b
def divide_values(a, b):
    divide = float(a) / float(b)
    return jsonify({"Result: ": divide})


app.run(host='0.0.0.0', port=8080, debug=True)
