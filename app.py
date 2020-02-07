from flask import Flask, render_template, request, redirect, json
# from models import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
db = SQLAlchemy(app)


class JsonFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return '# JsonFile - id: %s' % self.id


@app.route('/home', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':

        json_file = None
        try:
            db.session.add(json_file)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        return render_template('home.html')
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
