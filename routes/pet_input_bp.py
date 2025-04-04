from flask import Blueprint, redirect, render_template, request, url_for

from extensions import db

# from constants import STATUS_CODE
from models.pet import Pet

# from models.quotes import InsurancePlan, PetInsurance

# 1. Organize
# 2. app needs to be in main.py
pet_input_bp = Blueprint("pet_input_bp", __name__)


@pet_input_bp.get("/new")
def add_pet():
    return render_template("pet-form.html")


@pet_input_bp.post("/pet-form")  # type: ignore # HOF
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
            "breed": request.form.get("pet-breed"),
            "medical_conditions": request.form.get("medical-condition"),
            "vacc_date": request.form.get("vacc-date"),
        }

        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()

        # Redirect to pet form again to add more pets
        if "add_more_pets" in request.form:
            return redirect(url_for("pet_input_bp.create_pet"))
        elif "get_quote" in request.form:
            return redirect(
                url_for("quotes_bp.select_insurance", pet_id=new_pet.pet_id)
            )

    except Exception as e:
        db.session.rollback()
        return {"message": str(e)}, 500
