from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://hello_flask:hello_flask@localhost/contact_book"
app.config["SECRET_KEY"] = "random string"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
app.app_context().push()
migrate = Migrate(app, db)


class Contact(db.Model):
    __tablename__ = "contact"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    number = db.Column(db.Text)
    color = db.Column(db.Text)

    def __init__(self, name, number, color):
        self.name = name
        self.number = number
        self.color = color


db.create_all()


@app.route("/", methods=['POST'])
def add():
    name = request.json.get("name")
    number = request.json.get("number")
    color = request.json.get("color")
    contact = Contact(name,number,color)
    db.session.add(contact)
    db.session.commit()
    return{
        "succes":True,
        "message":"Contact Added"
    }

if __name__ == "__main__":
    app.run(debug=True)