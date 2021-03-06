from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'users'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydb'
#app.config['MONGO_URI'] = 'mongodb+srv://<user>:<pass>@cluster0-lvn1g.mongodb.net/test'

mongo = PyMongo(app)


@app.route('/framework', methods=['GET'])
def get_all_frameworks():
    framework = mongo.db.framework

    output = []

    for q in framework.find():
        output.append({'name': q['name'], 'language': q['language']})

    return jsonify({'result': output})


@app.route('/framework/<name>', methods=['GET'])
def get_one_framework(name):
    framework = mongo.db.framework

    one = framework.find_one({'name': name})
    if one:
        output = {'name': one['name'], 'language': one['language']}
    else:
        output = "No results found"
    return jsonify({'result': output})


@app.route('/framework', methods=['POST'])
def add_framework():
    framework = mongo.db.framework

    name = request.json['name']
    language = request.json['language']

    print(name)
    print(language)

    framework_id = framework.insert({'name': name, "language": language})
    new_framework = framework.find_one({'_id': framework_id})

    output = {'name': new_framework['name'], 'language': new_framework['language']}
    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug=True)
