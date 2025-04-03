from extensions import db
from models.pet import Pet


class InsurancePlan(db.Model):
    __tablename__ = "insurance_plans"

    insurance_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    insurance_name = db.Column(db.String(50), nullable=False)
    price_per_month = db.Column(db.Float, nullable=False)
    features = db.Column(db.String(500), nullable=False)
    insurance_logo = db.Column(db.String(255))

    # Relationship with PetInsurance
    pet_insurances = db.relationship(
        "PetInsurance",
        backref="insurance_plan_ref",
        lazy=True,  # Ensuring correct reference name
    )


class PetInsurance(db.Model):
    __tablename__ = "pet_insurance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_id = db.Column(
        db.Integer, db.ForeignKey("pet.pet_id"), nullable=False
    )  # FK to pet table
    insurance_plan_id = db.Column(
        db.Integer, db.ForeignKey("insurance_plans.insurance_id"), nullable=False
    )  # FK to insurance plans

    # Relationship with Pet and InsurancePlan
    pet = db.relationship("Pet", backref="pet_ref", lazy=True)
    insurance_plan = db.relationship(
        "InsurancePlan",
        backref="insurance_plan_ref",
        lazy=True,  # Changed backref name here
    )

    def __repr__(self):
        return f"<PetInsurance pet_id={self.pet_id}, plan_id={self.insurance_plan_id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "pet_id": self.pet_id,
            "insurance_plan_id": self.insurance_plan_id,
        }
