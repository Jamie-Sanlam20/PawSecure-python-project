from flask import Blueprint, flash, redirect, render_template, request, url_for

from extensions import db
from models.pet import Pet
from models.quotes import InsurancePlan, PetInsurance  # Your renamed model

quotes_bp = Blueprint("quotes_bp", __name__)


@quotes_bp.get("/select_insurance/<int:pet_id>")
def select_insurance(pet_id):
    pet = Pet.query.get(pet_id)
    if not pet:
        return {"message": "Pet not found."}, 404

    insurance_plans = InsurancePlan.query.all()
    return render_template(
        "quotes-incomplete.html",
        pet=pet,
        insurance_plans=insurance_plans,
        pet_id=pet_id,
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
            pet_id=pet_id,
            insurance_plan_id=insurance_plan_id,  # type: ignore
        )
        db.session.add(new_pet_insurance)
        db.session.commit()

        # Redirect to next step (dashboard or summary)
        flash("Purchase Successful", "success")
        return redirect(url_for("auth_bp.login_page"))  # Update this as needed

    except Exception as e:
        db.session.rollback()
        return {"message": str(e)}, 500
