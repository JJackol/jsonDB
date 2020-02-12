# from urllib import request
import os
from flask import Flask, render_template, request, redirect, json, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_json import JsonError, json_response, FlaskJSON
from flask_cors import CORS, cross_origin

from src.count import count_values_in_multiple_str

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/local.db'

db = SQLAlchemy(app)
FlaskJSON(app)
cors = CORS(app, resources={r"/list": {"origins": "*"}}, origins="*")
api = Api(app)  # rest api

if not os.path.exists('db/local.db'):
    db.create_all()
    print("###info db created!")


class JsonFile(db.Model):
    """JSON file table"""
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<JsonFile - id: %s>' % self.id


class JSONList(Resource):
    """REST API - endpoint :/listsss"""
    def get(self):
        q = (JsonFile.query.all())
        nrOfVal = count_values_in_multiple_str([record.data for record in q])
        stats = {"nr_of_files": len(q), "nr_values": nrOfVal}
        return jsonify(stat=stats, jsons=reversed([json.loads(f.data) for f in q]))

    def post(self):
        data = request.form['content']
        if add_json(data):
            return jsonify(done=True)
        else:
            return jsonify(done=False)


api.add_resource(JSONList, '/list')


@app.route('/home', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
@cross_origin(origins="*", methods=['POST'])
def hello_world():
    print("hello")
    print(request)
    if request.method == 'POST':

        data = request.form['content']
        add_json(data)
        return redirect('/home')

    else:
        files = [f.data for f in JsonFile.query.all()]
        nrOfVal = count_values_in_multiple_str(files)
        return render_template('home.html',
                               files=files,
                               nr_val=nrOfVal,
                               nr_files=len(files)
                               )


@app.route('/lists', methods=['POST', 'GET'])
@cross_origin(origins="*", methods=['POST', 'GET', 'PUT'])
def lista():
    print("lista wita")
    print(request.form)
    if request.method == 'POST':
        print(json.dumps(request.form, app))
        data = request.form['content']
        print(data)
        if add_json(data):
            return jsonify(done=True)
        else:
            return JsonError()

    if request.method == 'GET':
        q = JsonFile.query.all()
        nrOfVal = count_values_in_multiple_str([record.data for record in q])
        stats = {"nr_of_files": len(q), "nr_values": nrOfVal}
        return jsonify(stat=stats, jsons=[json.loads(f.data) for f in q])


def add_json(data=None):
    try:
        obj = json.loads(data, app)
        json_file = JsonFile(data=json.dumps(obj, app))
        db.session.add(json_file)
        db.session.commit()
        return True
    except:
        return False


if __name__ == '__main__':
    app.run(debug=True)
