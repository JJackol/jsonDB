# from urllib import request

from flask import Flask, render_template, request, redirect, json, sessions
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


class JsonFile(db.Model):
    """JSON file table"""
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<JsonFile - id: %s>' % self.id


class JSONList(Resource):
    """REST API - endpoint :/list"""

    def get(self):
        return [json.loads(f.data) for f in JsonFile.query.all()]


api.add_resource(JSONList, '/listsss')


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


@app.route('/list', methods=['POST', 'GET'])
@cross_origin(origins="*", methods=['POST', 'GET', 'PUT'])
def lista():
    print("lista wita")
    print(request.form)
    if request.method == 'POST':
        print(json.dumps(request.form, app))
        data = request.form['content']
        print(data)
        if add_json(data):
            return json_response(done=True)
        else:
            return JsonError()

    if request.method == 'GET':
        q = JsonFile.query.all()
        nrOfVal = count_values_in_multiple_str([record.data for record in q])
        stats = {"nr_of_files": len(q), "nr_values": nrOfVal}
        return json_response(stat=stats, jsons=[json.loads(f.data) for f in q])


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
