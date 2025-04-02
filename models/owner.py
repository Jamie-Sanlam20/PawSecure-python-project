from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db


class Owner(UserMixin, db.Model):
    __tablename__ = "owner"

    owner_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    physical_address = db.Column(db.String(255), nullable=False)
    email_address = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(
        db.String(255), nullable=False
    )  # ✅ Use 'password' to match DB schema

    # Relationship with pet table (one-to-many)
    pets_list = db.relationship("Pet", backref="owner", lazy=True)

    def __repr__(self):
        return f"<Owner {self.name} {self.surname}>"

    def get_id(self):
        """Returns the unique ID for Flask-Login."""
        return str(self.owner_id)

    def set_password(self, password):
        """Hashes and sets the password."""
        self.password = generate_password_hash(password)  # ✅ Correct field name

    def check_password(self, password):
        """Checks a hashed password."""
        return check_password_hash(self.password, password)  # ✅ Correct field name

    def to_dict(self):
        """Returns a dictionary representation of the Owner object (excluding sensitive info)."""
        return {
            "owner_id": self.owner_id,
            "name": self.name,
            "surname": self.surname,
            "date_of_birth": str(self.date_of_birth),  # Convert to string for JSON
            "contact_number": self.contact_number,
            "physical_address": self.physical_address,
            "email_address": self.email_address,
        }
