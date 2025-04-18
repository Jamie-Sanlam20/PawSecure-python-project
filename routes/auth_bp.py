from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from models.owner import Owner

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.get("/login")
def login_page():
    return render_template("login.html")


@auth_bp.post("/login")
def submit_login_page():
    email_address = request.form.get("email_address")
    password = request.form.get("password")

    try:
        # 🛡️ Validations
        if not email_address:
            flash("Email must be filled", "danger")
            return redirect(url_for("auth_bp.login_page"))

        if not password:
            flash("Password must be filled", "danger")
            return redirect(url_for("auth_bp.login_page"))

        # Fetch user from DB
        owner_from_db = Owner.query.filter_by(email_address=email_address).first()

        if not owner_from_db or not check_password_hash(
            owner_from_db.password, password
        ):
            flash("Invalid email or password", "danger")
            return redirect(url_for("auth_bp.login_page"))

        # Log in the user
        login_user(owner_from_db)
        return redirect(url_for("main_bp.dashboard"))

    except Exception as e:
        print(e)
        flash("An error occurred. Please try again.", "danger")
        return redirect(url_for("auth_bp.login_page"))


@auth_bp.get("/logout")
def logout_page():
    logout_user()
    return redirect(url_for("auth_bp.login_page"))
