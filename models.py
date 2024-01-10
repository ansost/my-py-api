"""Create classes used in the app.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# class Module_model(db.Model):
#     __tablename__ = "table"

#     id = db.Column(db.Integer(), primary_key=True)

#     module_number = db.Column(db.Integer(), unique=True)
#     name = db.Column(db.String())
#     # description = ?

#     def __init__(self, module_number, name):
#         self.module_number = module_number
#         self.name = name

#     def __repr__(self):
#         return f"{self.name}:{self.employee_id}"


class Nachweis_model(db.Model):
    __tablename__ = "table_bn"

    id = db.Column(db.Integer(), primary_key=True)

    from_class = db.Column(db.String())
    type_of = db.Column(db.String(2))
    hislsf_nr = db.Column(db.Integer(), unique=True)

    def __init__(self, from_class, type_of, hislsf_nr=None):
        self.from_class = from_class
        self.type_of = type_of
        self.hislsf_nr = hislsf_nr

    def __repr__(self):
        return f"{self.from_class} from {self.typeof}, Pr.-Nr.:{self.pr_number}"
