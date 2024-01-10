from flask import Flask, render_template, request, redirect

from models import db, Nachweis_model


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bn-tracker.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


with app.app_context():
    db.create_all()


# route() decorator to tells Flask what URL should trigger our function
@app.route("/")
def index():
    return "Index Page"


@app.route("/new")
def hello():
    return "Here you will be able to add a new BN!"


# Create view.
@app.route("/data/create", methods=["GET", "POST"])
def create():  # new BN
    if request.method == "GET":
        return render_template("createpage.html")

    if request.method == "POST":
        from_class == request.form["from_class"]
        type_of == request.form["type_of"]
        hislsf_nr == request.form["hislsf_nr"]
        nachweis = Nachweis_model(
            from_class=from_class,
            type_of=type_of,
            hislsf_nr=hislsf_nr,
        )
        db.session.add(nachweis)
        db.session.commit()
        return redirect("/data")
