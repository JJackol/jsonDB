from flask import Flask, render_template, request, redirect,  json
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_json import JsonError, json_response, FlaskJSON
from flask_cors import CORS

from count import count_values_in_multiple_str

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
db = SQLAlchemy(app)
FlaskJSON(app)
CORS(app)

api = Api(app) #rest api

class JsonFile(db.Model):
    """JSON file table"""
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<JsonFile - id: %s>' % self.id


@app.route('/home', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        data = request.form['content']
        return add_json(data)

    else:
        files = [ f.data for f in JsonFile.query.all() ]
        nrOfVal = count_values_in_multiple_str(files)
        return render_template('home.html',
                               files=files,
                               nr_val=nrOfVal,
                               nr_files=len(files)
                               )

@app.route('/raise_error')
def raise_error():
    return json_response(description='Example text.', code=123)


def add_json(data=None):
    try:
        obj = json.loads(data, app)
        json_file = JsonFile(data=json.dumps(obj, app))
        db.session.add(json_file)
        db.session.commit()
        return redirect('/home')
    except:
        return 'There was a problem adding your json'


class JSONList(Resource):
    def get(self):
        return [ {"id":f.id, "data":json.loads(f.data)} for f in JsonFile.query.all() ]


api.add_resource(JSONList, '/list')

if __name__ == '__main__':
    app.run(debug=True)
