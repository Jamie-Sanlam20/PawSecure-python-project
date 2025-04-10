from flask import Blueprint, redirect, render_template, request, session, url_for
from flask_login import current_user

from extensions import db
from models.pet import Pet

pet_input_bp = Blueprint("pet_input_bp", __name__)


@pet_input_bp.get("/pet-form")
def add_pet():
    owner_id = request.args.get("owner_id")

    # Fallback to logged-in user if available
    if not owner_id and current_user.is_authenticated:
        owner_id = current_user.owner_id

    if not owner_id:
        return {
            "message": "Owner ID missing. Please log in or start from the sign-up form."
        }, 400

    return render_template("pet-form.html", owner_id=owner_id)


@pet_input_bp.post("/pet-form")  # type: ignore
def create_pet():
    try:
        # 1. Get owner_id from form
        owner_id = request.form.get("owner_id")

        # 2. Validate and convert owner_id
        if not owner_id or owner_id == "None" or not owner_id.isdigit():
            return {
                "message": "Invalid or missing owner ID. Please log in or start with the owner form."
            }, 400

        owner_id = int(owner_id)  # Now it's safe to use

        # 3. Prepare pet data
        data = {
            "owner_id": owner_id,
            "pet_name": request.form.get("pet-name").title(),  # type: ignore
            "pet_age": request.form.get("pet-age"),
            "pet_type": request.form.get("pet-type"),
            "pet_gender": request.form.get("pet-gender"),
            "breed_type": request.form.get("breed-type"),
            "breed": request.form.get("pet-breed"),
            "medical_conditions": request.form.get("medical-condition").capitalize(),  # type: ignore
            "vacc_date": request.form.get("vacc-date"),
        }

        # 4. Create and store pet
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()

        # 5. Session tracking for added pets
        if "added_pet_ids" not in session:
            session["added_pet_ids"] = []

        session["added_pet_ids"].append(new_pet.pet_id)
        session.modified = True

        # 6. Redirect logic
        if "add_more_pets" in request.form:
            return redirect(url_for("pet_input_bp.add_pet", owner_id=owner_id))
        elif "get_quote" in request.form:
            if len(session["added_pet_ids"]) == 1:
                return redirect(
                    url_for(
                        "quotes_bp.select_insurance", pet_id=session["added_pet_ids"][0]
                    )
                )
            else:
                return redirect(url_for("quotes_bp.multi_select_insurance"))

    except Exception as e:
        db.session.rollback()
        return {"message": str(e)}, 500
