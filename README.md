# 📝 Technical Report: PawSecure – Pet Insurance Marketplace & Tracker

## 📋 Overview

This technical report outlines the key features implemented in the PawSecure web application and identifies the respective developer responsible for each feature. The application streamlines the process of managing pet profiles, selecting insurance plans, submitting claims, and tracking claim status.

---

## 🐾 Introduction

Our Pet Insurance Web Application is a user-friendly platform designed to simplify the process of managing pet insurance. It allows pet owners to:

- Create and manage profiles for their pets
- Select and compare insurance plans
- Submit claims
- Track claim status

—all from one centralised dashboard. The goal of the application is to make pet healthcare more accessible and organised through digital convenience and clear user flows.

---

## 🔧 Feature Breakdown

- **User Authentication System (Sign Up, Login, Logout)**
  Developed by **Jamie** using Flask-Login for secure owner session management.

- **Dashboard Display with Navigation Sidebar**
  Built by **Jamie** to provide responsive access to all major functionalities.

- **Single Pet Insurance Selection with Quote Management**
  Handled by **Jamie** (functionality) and **Jevan** (styling). Allows owners to get quotes and store selected plans in the database.

- **Multi-Pet Insurance Selection Page (`multi_select_insurance`)**
  Implemented by **Jamie**, enabling users to select insurance plans for multiple pets at once.

- **Pet Profile Management (Add, View, Update Pet Info)**
  Created by **Jamie**. Supports CRUD operations on pet data, including vaccination and medical condition tracking.

- **Insurance Quote Status Pages (`quotes-single`, `quotes-multi`)**
  Built by **Jamie** to notify users of incomplete selections or display available multi-pet quotes.

- **Claim Submission Form**
  Developed by **Jamie**. Users can submit insurance claims through a guided interface.

- **Claim Tracker with Real-Time Status Updates**
  Implemented by **Jamie** to display claim progress and current status.

- **Profile Page with Owner Information**
  Designed and styled by **Jamie**, with editable personal details.

- **Responsive Layout and Styling with Sidebar Integration**
  Led by **Jamie**, ensuring consistent UI across devices.

- **Homepage**
  Built by **Jevan**, introducing the app and listing the insurance partners used when quoting.

- **Contact Us Page**
  Designed and styled by **Jevan**. Allows the user to send a message to through the site on any queries they may have. Flash message popping up upon submission was implemented by **Jamie**.

- **Partners Page**
  Designed and styled by **Jevan**. 'Learn more' button links to individual insurance provider's websites.

- **Owner Form**
  Designed and styled by **Jevan**, with backend/database integration by **Jamie**.

---

## 📦 Technologies Used

- **Flask** – Backend Framework
- **Jinja2** – Templating
- **Flask-Login** – User Authentication
- **SQLAlchemy** – ORM for Database Management
- **HTML/CSS** – Frontend Structure & Styling
- **FontAwesome** – Icons
