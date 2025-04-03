from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from extensions import db
from models.owner import Owner
from models.pet import Pet

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
            "name": request.form.get("owner_name"),
            "surname": request.form.get("owner_surname"),
            "date_of_birth": request.form.get("owner_date_of_birth"),
            "contact_number": request.form.get("owner_contact_number"),
            "physical_address": request.form.get("owner_physical_address"),
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

        # Redirect to pet form, passing owner_id
        return redirect(url_for("pet_input_bp.add_pet", owner_id=new_owner.owner_id))

    except Exception as e:
        db.session.rollback()
        return {"message": str(e)}, 500


@main_bp.get("/dashboard")
@login_required
def dashboard():
    pets = Pet.query.filter_by(owner_id=current_user.get_id()).all()

    return render_template("dashboard.html", pets=pets)


@main_bp.get("/claim-form")
def add_claim():
    return render_template("claim-form.html")


@main_bp.get("/claim-tracker")
def claim_tracker():
    return render_template("claim-tracker.html")
