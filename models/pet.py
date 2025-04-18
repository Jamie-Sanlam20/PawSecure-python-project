from extensions import db


class Pet(db.Model):
    __tablename__ = "pet"

    pet_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(
        db.Integer, db.ForeignKey("owner.owner_id"), nullable=False
    )  # FK to owner id
    owner = db.relationship("Owner", backref="pets", lazy=True)
    # Relationship to link pet with insurance via PetInsurance table
    pet_insurance = db.relationship("PetInsurance", backref="pet_ref", lazy=True)
    claims = db.relationship(
        "Claim", backref="pet", cascade="all, delete", passive_deletes=True
    )

    pet_type = db.Column(db.String(10), nullable=False)
    pet_name = db.Column(db.String(255), nullable=False)
    pet_age = db.Column(db.Integer, nullable=False)
    pet_gender = db.Column(db.String(6), nullable=False)
    breed_type = db.Column(db.String(10), nullable=False)
    breed = db.Column(db.String(255), nullable=True)
    medical_conditions = db.Column(db.Text, nullable=True)
    vacc_date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"<Pet {self.pet_name}>"

    def to_dict(self):
        return {
            "pet_id": self.pet_id,
            "owner_id": self.owner_id,
            "pet_type": self.pet_type,
            "pet_name": self.pet_name,
            "pet_age": self.pet_age,
            "pet_gender": self.pet_gender,
            "breed_type": self.breed_type,
            "breed": self.breed,
            "medical_conditions": self.medical_conditions,
            "vacc_date": str(self.vacc_date) if self.vacc_date else None,
        }
