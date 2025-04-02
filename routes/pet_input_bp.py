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
            "breed": request.form.get("pet-breed"),
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


# @pet_input_bp.post("/quotes")  # HOF
# def create_pet():
#     try:
#         owner_id = request.form.get("owner_id")
#         if not owner_id:
#             return {
#                 "message": "Owner ID missing. Please start with the owner form."
#             }, 400

#         data = {
#             "owner_id": owner_id,
#             "pet_name": request.form.get("pet-name"),
#             "pet_age": request.form.get("pet-age"),
#             "pet_type": request.form.get("pet-type"),
#             "pet_gender": request.form.get("pet-gender"),
#             "breed_type": request.form.get("breed-type"),
#             "breed": request.form.get("pet-breed"),
#             "medical_conditions": request.form.get("medical-condition"),
#         }

#         new_pet = Pet(**data)
#         db.session.add(new_pet)
#         db.session.commit()

#         # Redirect to the insurance plan selection page after pet is created
#         return redirect(url_for("pet_input_bp.select_insurance", pet_id=new_pet.pet_id))

#     except Exception as e:
#         db.session.rollback()
#         return {"message": str(e)}, 500


# @pet_input_bp.get("/select_insurance/<int:pet_id>")  # HOF
# def select_insurance(pet_id):
#     # Fetch the pet by ID
#     pet = Pet.query.get(pet_id)
#     if not pet:
#         return {"message": "Pet not found."}, 404

#     # Fetch all available insurance plans
#     insurance_plans = InsurancePlan.query.all()

#     return render_template(
#         "select_insurance.html", pet=pet, insurance_plans=insurance_plans
#     )


# @pet_input_bp.post("/select_insurance/<int:pet_id>")  # HOF
# def link_insurance_plan(pet_id):
#     try:
#         # Fetch the selected insurance plan
#         insurance_plan_id = request.form.get("insurance_plan_id")
#         if not insurance_plan_id:
#             return {"message": "Insurance plan is required."}, 400

#         # Create the DogInsurance entry linking the pet to the insurance plan
#         new_dog_insurance = PetInsurance(
#             pet_id=pet_id, insurance_plan_id=insurance_plan_id
#         )
#         db.session.add(new_dog_insurance)
#         db.session.commit()

#         # Redirect back to the pet creation page so the user can add more pets
#         return redirect(url_for("main_bp.create_pet", owner_id=pet.owner_id))

#     except Exception as e:
#         db.session.rollback()
#         return {"message": str(e)}, 500
