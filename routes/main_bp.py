from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required

from extensions import db
from models.claim import Claim
from models.owner import Owner
from models.pet import Pet
from models.quotes import InsurancePlan, PetInsurance

# 1. Organize
# 2. app needs to be in main.py
main_bp = Blueprint("main_bp", __name__)


@main_bp.get("/home")
def homepage():
    return render_template("home-page.html")


@main_bp.get("/owner-form")
def add_owner():
    return render_template("owner-form.html")


@main_bp.post("/owner-form")
def create_owner():
    try:
        data = {
            "name": request.form.get("owner_name").title(),  # type: ignore
            "surname": request.form.get("owner_surname").title(),
            "date_of_birth": request.form.get("owner_date_of_birth"),
            "contact_number": request.form.get("owner_contact_number"),
            "physical_address": request.form.get("owner_physical_address").title(),
            "email_address": request.form.get("owner_email_address"),
            "password": request.form.get("owner_password"),
        }

        # Hashing password before sent to DB
        if data["password"]:
            from werkzeug.security import generate_password_hash

            data["password"] = generate_password_hash(data["password"])

        # Create new owner
        new_owner = Owner(**data)
        db.session.add(new_owner)
        db.session.commit()

        # ✅ Clear previous session data to prevent old pet carryover
        session["added_pet_ids"] = []
        session["insured_pet_ids"] = []

        # Optionally store owner ID if needed
        session["current_owner_id"] = new_owner.owner_id

        # Redirect to pet form, passing owner_id
        return redirect(url_for("pet_input_bp.add_pet", owner_id=new_owner.owner_id))

    except Exception as e:
        db.session.rollback()
        return {"message": str(e)}, 500


@main_bp.get("/dashboard")
@login_required
def dashboard():
    pets = Pet.query.filter_by(owner_id=current_user.get_id()).all()

    # Join Pet and PetInsurance, and get the related insurance information
    pets_with_insurance = []
    for pet in pets:
        pet_data = pet.to_dict()
        pet_insurance = PetInsurance.query.filter_by(pet_id=pet.pet_id).first()
        if pet_insurance:
            pet_data["insurance_name"] = pet_insurance.insurance_plan.insurance_name
            pet_data["insurance_logo"] = pet_insurance.insurance_plan.insurance_logo
        else:
            pet_data["insurance_name"] = None
        pets_with_insurance.append(pet_data)

    return render_template("dashboard.html", pets=pets_with_insurance)


@main_bp.get("/claim-form")
@login_required
def show_claim_form():
    # owner_id = session.get("current_owner_id")
    pets = Pet.query.filter_by(owner_id=current_user.owner_id).all()
    return render_template("claim-form.html", pets=pets)


@main_bp.post("/claim-form")
@login_required
def submit_claim():
    try:
        pet_id = request.form.get("pet_id")
        reason = request.form.get("reason")
        amount = request.form.get("amount")
        claim_date = request.form.get("claim_date")

        if not all([pet_id, reason, amount, claim_date]):
            return {"message": "All fields are required."}, 400

        # Convert to proper types
        new_claim = Claim(
            pet_id=int(pet_id),
            reason=reason,
            amount=float(amount),
            claim_date=datetime.strptime(claim_date, "%Y-%m-%d").date(),
        )

        db.session.add(new_claim)
        db.session.commit()

        return redirect(url_for("main_bp.claim_tracker"))

    except Exception as e:
        db.session.rollback()
        return {"message": f"Error submitting claim: {str(e)}"}, 500


@main_bp.get("/claim-tracker")
@login_required
def claim_tracker():
    owner_id = current_user.get_id()

    # Get all pets owned by this user
    pets = Pet.query.filter_by(owner_id=owner_id).all()
    pet_ids = [pet.pet_id for pet in pets]

    # Fetch all claims for these pets
    claims = (
        Claim.query.filter(Claim.pet_id.in_(pet_ids))
        .order_by(Claim.claim_date.desc())
        .all()
    )

    # Create a list of claim data with pet names
    claim_data = []
    for claim in claims:
        claim_data.append(
            {
                "claim_id": claim.claim_id,
                "pet_name": claim.pet.pet_name,
                "reason": claim.reason,
                "amount": claim.amount,
                "claim_date": claim.claim_date.strftime("%Y-%m-%d"),
                "claim_status": claim.claim_status,
            }
        )

    return render_template("claim-tracker.html", claims=claim_data)


@main_bp.get("/profile")
@login_required
def profile():
    return render_template("profile.html", owner=current_user)


@main_bp.get("/profile-update")
@login_required
def profile_update():
    return render_template("profile-update.html", owner=current_user)


@main_bp.post("/update-owner")
@login_required
def update_owner():
    # Fetch the current logged-in owner's record
    owner = Owner.query.get(current_user.owner_id)  # or use session["current_owner_id"]

    if not owner:
        flash("Owner not found.", "danger")
        return redirect(url_for("main_bp.profile"))

    # Update fields from the form
    owner.name = request.form.get("owner_name")
    owner.surname = request.form.get("owner_surname")
    owner.date_of_birth = request.form.get("owner_date_of_birth")
    owner.contact_number = request.form.get("owner_contact_number")
    owner.physical_address = request.form.get("owner_physical_address")
    owner.email_address = request.form.get("owner_email_address")

    # Commit changes
    try:
        db.session.commit()
        flash("Profile updated successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash("Failed to update profile. Please try again.", "danger")
        print("Update error:", e)

    return redirect(url_for("main_bp.profile"))


@main_bp.get("/partners-page")
def partners_page():
    return render_template("partners-page.html")


@main_bp.get("/contact")
def contact_page():
    return render_template("contact-us.html")


@main_bp.get("/pet-update/<int:pet_id>")
@login_required
def pet_update(pet_id):
    pet = Pet.query.get_or_404(pet_id)

    # Ensure the pet belongs to the logged-in owner
    if pet.owner_id != current_user.owner_id:
        flash("Unauthorized access to pet record.", "danger")
        return redirect(url_for("main_bp.profile"))

    return render_template("update-pet.html", pet=pet)


@main_bp.post("/update-pet/<int:pet_id>")
@login_required
def update_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)

    # Ensure the pet belongs to the logged-in owner
    if pet.owner_id != current_user.owner_id:
        flash("Unauthorized action.", "danger")
        return redirect(url_for("main_bp.profile"))

    # Update fields from form
    pet.pet_name = request.form.get("pet_name")
    pet.pet_age = request.form.get("pet_age")
    pet.breed = request.form.get("breed")
    pet.pet_gender = request.form.get("pet_gender")
    pet.vacc_date = request.form.get("vacc_date")
    pet.medical_conditions = request.form.get("medical_conditions")
    # pet.insurance_name = request.form.get("insurance_name")

    # Commit changes
    try:
        db.session.commit()
        flash("Pet info updated successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash("Failed to update pet info. Please try again.", "danger")
        print("Pet update error:", e)

    return redirect(url_for("main_bp.dashboard"))


@main_bp.post("/delete-pet/<int:pet_id>")
def delete_pet_by_id(pet_id):  # log
    # Auto converts data -> JSON (Flask)
    pet = Pet.query.get(pet_id)  # None if no movie

    if not pet:
        return {"message": "Pet not found"}, 404

    try:
        data = pet.to_dict()
        db.session.delete(pet)  # Error
        db.session.commit()  # Making the change (Update/Delete/Create) # Error
        return redirect(url_for("main_bp.dashboard"))
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return {"message": str(e)}, 404


@main_bp.get("/agria")
def agria_page():
    return render_template("agria.html")


@main_bp.get("/oneplan")
def oneplan_page():
    return render_template("oneplan.html")
