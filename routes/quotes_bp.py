from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from extensions import db
from models.pet import Pet
from models.quotes import InsurancePlan, PetInsurance  # Your renamed model

quotes_bp = Blueprint("quotes_bp", __name__)


# Single pet:
@quotes_bp.get("/select_insurance/<int:pet_id>")
def select_insurance(pet_id):
    pet = Pet.query.get(pet_id)
    if not pet:
        return {"message": "Pet not found."}, 404

    insurance_plans = InsurancePlan.query.all()
    return render_template(
        "quotes-single.html",
        pet=pet,
        insurance_plans=insurance_plans,
        pet_id=pet_id,
    )


@quotes_bp.get("/multi-select-insurance")
def multi_select_insurance():
    pet_ids = session.get("added_pet_ids", [])
    pets = Pet.query.filter(Pet.pet_id.in_(pet_ids)).all()

    total_pets = len(pets)
    insured_pet_ids = session.get("insured_pet_ids", [])
    if len(insured_pet_ids) == total_pets:
        return redirect(url_for("auth_bp.login_page"))

    insurance_plans = InsurancePlan.query.all()
    return render_template(
        "quotes-multi.html",
        pets=pets,
        insurance_plans=insurance_plans,
        total_pets=total_pets,
    )


@quotes_bp.post("/select_insurance/<int:pet_id>")
def link_insurance_plan(pet_id):
    try:
        pet = Pet.query.get(pet_id)  # Ensure pet exists
        if not pet:
            return {"message": "Pet not found."}, 404

        insurance_plan_id = request.form.get("insurance_plan_id")
        if not insurance_plan_id:
            return {"message": "Insurance plan is required."}, 400

        # Convert insurance_plan_id to integer
        try:
            insurance_plan_id = int(insurance_plan_id)
        except ValueError:
            return {"message": "Invalid insurance plan ID format."}, 400

        # Create a PetInsurance entry linking the pet to the selected plan
        new_pet_insurance = PetInsurance(
            pet_id=pet_id,  # type: ignore
            insurance_plan_id=insurance_plan_id,  # type: ignore
        )
        db.session.add(new_pet_insurance)
        db.session.commit()

        # Add the current pet to the insured pets list
        if "insured_pet_ids" not in session:
            session["insured_pet_ids"] = []

        session["insured_pet_ids"].append(pet_id)
        session.modified = True

        flash("Insurance plan selected successfully!", "success")
        # Redirect to insurance selection for the next pet or complete the process
        if len(session["added_pet_ids"]) == 1:
            return redirect(url_for("auth_bp.login_page"))  # After one pet, go to login
        else:
            # If multiple pets, return to the multi-select insurance page or dashboard
            return redirect(url_for("quotes_bp.multi_select_insurance"))

    except Exception as e:
        db.session.rollback()
        return {"message": str(e)}, 500
