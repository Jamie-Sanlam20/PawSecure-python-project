from flask import Blueprint, redirect, render_template, request, url_for

from extensions import db

# from constants import STATUS_CODE
from models.pet import Pet

# 1. Organize
# 2. app needs to be in main.py
pet_input_bp = Blueprint("pet_input_bp", __name__)


@pet_input_bp.get("/new")
def add_pet():
    return render_template("pet-form-incomplete.html")


@pet_input_bp.post("/pet-form")  # HOF
def create_pet():
    try:
        owner_id = request.form.get("owner_id")
        if not owner_id:
            return {
                "message": "Owner ID missing. Please start with the owner form."
            }, 400

        data = {
            "owner_id": owner_id,
            "pet_name": request.form.get("pet-name"),
            "pet_age": request.form.get("pet-age"),
            "pet_type": request.form.get("pet-type"),
            "pet_gender": request.form.get("pet-gender"),
            "breed_type": request.form.get("breed-type"),
            "breed": request.form.get("breed"),
            "medical_conditions": request.form.get("medical-condition"),
        }

        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()

        # Redirect to pet form again to add more pets
        return redirect(url_for("pet_input_bp.add_pet", owner_id=owner_id))

    except Exception as e:
        db.session.rollback()
        return {"message": str(e)}, 500
