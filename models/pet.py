import uuid

# Schema equivalent
from uuid import uuid4

from sqlalchemy import CheckConstraint

from extensions import db


class Pet(db.Model):
    __tablename__ = "Pets"  # Table name is 'Pets'

    pet_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True
    )  # Use Integer for auto-increment
    pet_type = db.Column(db.String(10), nullable=False)
    pet_name = db.Column(db.String(255), nullable=False)
    pet_age = db.Column(
        db.Integer, nullable=False
    )  # Use Integer for pet_age, as it's an INT in SQL
    pet_gender = db.Column(db.String(6), nullable=False)
    breed_type = db.Column(db.String(10), nullable=False)
    breed = db.Column(db.String(255), nullable=True)
    medical_conditions = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Pet {self.pet_name}>"

    # Object -> Dict to serialize Pet object
    def to_dict(self):
        return {
            "pet_id": self.pet_id,
            "pet_type": self.pet_type,
            "pet_name": self.pet_name,
            "pet_age": self.pet_age,
            "pet_gender": self.pet_gender,
            "breed_type": self.breed_type,
            "breed": self.breed,
            "medical_conditions": self.medical_conditions,
        }
