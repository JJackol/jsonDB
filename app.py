from flask import Flask, render_template, request, redirect,  json

from flask_sqlalchemy import SQLAlchemy
from count import count_values_in_multiple_str

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
db = SQLAlchemy(app)


class JsonFile(db.Model):
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


def add_json(data=None):
    try:
        obj = json.loads(data, app)
        json_file = JsonFile(data=json.dumps(obj, app))
        db.session.add(json_file)
        db.session.commit()
        return redirect('/home')
    except:
        return 'There was a problem adding your json'

if __name__ == '__main__':
    app.run(debug=True)
