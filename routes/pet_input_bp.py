from pprint import pprint

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
    data = {
        "pet_type": request.form.get("pet-type"),
        "pet_name": request.form.get("pet-name"),  # use `name` attribute to get data
        "pet_age": request.form.get("pet-age"),
        "pet_gender": request.form.get("pet-gender"),
        "breed_type": request.form.get("breed-type"),
        "breed": request.form.get("pet-breed"),
        "medical_conditions": request.form.get("medical_condition"),
    }
    # data = request.get_json()  # body
    new_pet = Pet(**data)

    try:
        # print(new_movie, new_movie.to_dict())
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for("pet_input_bp.add_pet"))
    except Exception as e:
        db.session.rollback()  # Undo: Restore the data | After commit cannot undo
        return {"message": str(e)}
