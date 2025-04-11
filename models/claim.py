from extensions import db


class Claim(db.Model):
    __tablename__ = "claim"

    claim_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_id = db.Column(
        db.Integer, db.ForeignKey("pet.pet_id", ondelete="CASCADE"), nullable=False
    )
    reason = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    claim_date = db.Column(db.Date, nullable=False)
    claim_status = db.Column(db.String(20), nullable=False, default="Pending")

    def __repr__(self):
        return f"<Claim {self.claim_id} for Pet {self.pet_id}>"
