from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId

from flask import jsonify, request

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "secretkey"

app.config["MONGO_URI"] = app.config['MONGO_URI'] = 'mongodb://localhost:27017/new_db'

mongo = PyMongo(app)


@app.route("/add", methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']

    if _name and _email and _password and request.method == 'POST':

        _hashed_password = generate_password_hash(_password)

        id = mongo.db.Users.insert({'name': _name, 'email': _email, 'pwd': _hashed_password})
        resp = jsonify("User added successfully. Id: {}".format(id))
        resp.status_code = 200

        return resp
    else:
        return not_found()


@app.route("/users")
def get_users():
    users = mongo.db.Users

    output = []

    for q in users.find():
        print(q)
        output.append({'id': (str(q['_id'])), 'name': q['name'], 'email': q['email'], 'pwd': q['pwd']})

    return jsonify({"result": output})


@app.route("/users/<id>")
def get_some_user(id):
    user = mongo.db.Users.find_one({"_id": ObjectId(id)})

    if user:
        output = {'id': (str(user['_id'])), 'name': user['name'], 'email': user['email'], "pwd": user['pwd']}
    else:
        output = "No results found"

    return jsonify({'result': output})


@app.route("/delete/<id>", methods=["DELETE"])
def delete_user(id):

    mongo.db.Users.delete_one({'_id': ObjectId(id)})
    resp =jsonify("User with id {} deleted successfully".format(id))

    resp.status_code = 200

    return resp


@app.route("/update/<id>", methods=["PUT"])
def update_user(id):
    _json = request.json
    _id = id
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']

    if _name and _email and _password and _id and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)

        mongo.db.Users.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(id)}, {'$set': {'name': _name, 'email': _email, 'pwd': _hashed_password}})
        resp = jsonify("User updated successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not found ' + request.url
    }

    resp = jsonify(message)

    resp.status_code = 404
    return resp



if __name__ == "__main__":
    app.run(debug=True)
