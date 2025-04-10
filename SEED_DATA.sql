CREATE TABLE owner (
    owner_id INT PRIMARY KEY IDENTITY(1,1),  -- Auto-incremented primary key
    name VARCHAR(255) NOT NULL,               -- Owner's first name
    surname VARCHAR(255) NOT NULL,            -- Owner's surname
    date_of_birth DATE NOT NULL,              -- Owner's date of birth
    contact_number VARCHAR(15) NOT NULL,      -- Owner's contact number
    physical_address VARCHAR(255) NOT NULL,   -- Owner's physical address
    email_address VARCHAR(255) NOT NULL UNIQUE,  -- Owner's email address, must be unique
    password VARCHAR(255) NOT NULL            -- Owner's password (hashed ideally)
);

INSERT INTO owner (name, surname, date_of_birth, contact_number, physical_address, email_address, password)
VALUES
('Emma', 'Johnson', '1990-03-12', '0834567890', '123 Rose Street, Cape Town', 'emma.johnson@email.com', 'hashed_pw1'),
('Liam', 'Smith', '1985-07-22', '0741234567', '45 Daisy Ave, Johannesburg', 'liam.smith@email.com', 'hashed_pw2'),
('Olivia', 'Brown', '1992-11-03', '0822345678', '78 Sunset Blvd, Durban', 'olivia.brown@email.com', 'hashed_pw3'),
('Noah', 'Williams', '1988-01-18', '0769876543', '10 Ocean View Rd, Port Elizabeth', 'noah.williams@email.com', 'hashed_pw4'),
('Ava', 'Jones', '1995-09-30', '0731230987', '15 Sandton Drive, Johannesburg', 'ava.jones@email.com', 'hashed_pw5'),
('Lucas', 'Miller', '1991-05-11', '0847654321', '33 Flamingo Way, Pretoria', 'lucas.miller@email.com', 'hashed_pw6'),
('Sophia', 'Davis', '1987-02-27', '0719876543', '89 Main Rd, Stellenbosch', 'sophia.davis@email.com', 'hashed_pw7'),
('Mason', 'Garcia', '1993-10-05', '0828765432', '22 Pine Street, Bloemfontein', 'mason.garcia@email.com', 'hashed_pw8'),
('Isabella', 'Martinez', '1996-12-21', '0832345678', '99 Tulip Lane, East London', 'isabella.martinez@email.com', 'hashed_pw9'),
('Ethan', 'Rodriguez', '1989-06-14', '0723456789', '67 Cedar Crescent, George', 'ethan.rodriguez@email.com', 'hashed_pw10');

CREATE TABLE pet (
    pet_id INT PRIMARY KEY IDENTITY(1,1),
    owner_id INT,
    pet_type VARCHAR(10) NOT NULL,
    pet_name VARCHAR(255) NOT NULL,
    pet_age INT NOT NULL,
    pet_gender VARCHAR(6) NOT NULL,
    breed_type VARCHAR(10) NOT NULL,
    breed VARCHAR(255),
    medical_conditions TEXT,
	vacc_date DATE,
    FOREIGN KEY (owner_id) REFERENCES owner(owner_id)
);


INSERT INTO pet (owner_id, pet_type, pet_name, pet_age, pet_gender, breed_type, breed, medical_conditions, vacc_date)
VALUES
(1, 'Dog', 'Bella', 3, 'Female', 'Purebred', 'Labrador', 'None', '2025-04-20'),
(1, 'Cat', 'Rocky', 3, 'Male', 'Purebred', 'Siamese', 'Diabetes', '2025-04-21'),
(2, 'Dog', 'Charlie', 5, 'Male', 'Purebred', 'Boston Terrier', 'None', '2025-05-06'),
(3, 'Dog', 'Milo', 2, 'Male', 'Mixed', 'Jack Russell Terrier', 'Epilepsy', '2025-08-09'),
(3, 'Dog', 'Lucy', 1, 'Female', 'Mixed', 'Pitbull Terrier', 'None', '2025-08-09'),
(4, 'Dog', 'Max', 4, 'Male', 'Purebred', 'Staffordshire Terrier', 'Leukemia', '2025-06-07'),
(5, 'Cat', 'Daisy', 6, 'Female', 'Purebred', 'Persian', 'None', '2025-11-25'),
(6, 'Cat', 'Luna', 2, 'Female', 'Mixed', 'Siberian', 'None', '2025-09-27'),
(7, 'Cat', 'Chester', 1, 'Male', 'Purebred', 'Sphynx', 'Diabetes', '2026-01-01'),
(8, 'Cat', 'Bella', 7, 'Female', 'Mixed', 'Russian Blue', 'Hypertension', '2025-12-30');


CREATE TABLE insurance_plans (
    insurance_id INT PRIMARY KEY IDENTITY(1,1),  -- Auto-increment for insurance_id
    insurance_name VARCHAR(50) NOT NULL,
    price_per_month DECIMAL(10, 2) NOT NULL,
    features TEXT NOT NULL,
	insurance_logo TEXT NOT NULL
);

INSERT INTO insurance_plans (insurance_name, features, price_per_month, insurance_logo)
VALUES
('Essential Care', 'Essential Cover, Accidents, Annual Wellness Exams, Core Vaccines', 180.00, 'https://www.oneplan.co.za/assets/images/Logos/New%20logos/OnePlan%20Logo%20Health%20Insurance-01.png'),
('Everyday Cover', 'Accident Coverage, Routine Checkups, Vaccinations, Dental Care', 200.00, 'https://medshield.co.za/wp-content/uploads/2023/03/blue-logo.png'),
('Comprehensive Care', 'Accident Coverage, Vaccinations, Dental Care, Surgery, Specialist Visits', 300.00, 'https://wereallaboutpets.com/wp-content/uploads/2020/11/agria-pet-insurance.jpg'),
('Essential Plan', 'Accident Coverage, Routine Checkups, Vaccinations, Dental Care, Surgery', 250.00, 'https://medshield.co.za/wp-content/uploads/2023/03/blue-logo.png'),
('ProCare', 'Accident & Illness Coverage, Vaccinations, Surgery, Emergency Care', 180.00, 'https://www.lifetimepetcover.co.uk/src/images/logos/Sml_Blue_Logo.png'),
('Total Wellness', 'Full Medical Cover, Preventative Care, Hospitalization, Chronic Condition Support', 380.00, 'https://wereallaboutpets.com/wp-content/uploads/2020/11/agria-pet-insurance.jpg'),
('Vital Plan', 'Full Medical Cover, Dental Treatment, Hospitalization, Chronic Condition Support', 350.60, 'https://medipet.co.za/wp-content/uploads/2021/05/medipet-pet-insurance-south-africa-logo-tm-white.png'),
('Prime Cover', 'Preventative Care, Annual Exams, Vaccinations, Basic Dental Care, Minor Surgery', 230.50, 'https://www.oneplan.co.za/assets/images/Logos/New%20logos/OnePlan%20Logo%20Health%20Insurance-01.png'),
('Optimum Plan', 'Accident Coverage, Routine Checkups', 120.00, 'https://imageserver.petsbest.com/website/PetsBestLogoshort.png');



CREATE TABLE pet_insurance (
    id INT PRIMARY KEY IDENTITY(1,1),
    pet_id INT,
    insurance_plan_id INT,
    FOREIGN KEY (pet_id) REFERENCES pet(pet_id),
    FOREIGN KEY (insurance_plan_id) REFERENCES insurance_plans(insurance_id)
);

INSERT INTO pet_insurance (pet_id, insurance_plan_id) VALUES (1, 1);
INSERT INTO pet_insurance (pet_id, insurance_plan_id) VALUES (2, 2);
INSERT INTO pet_insurance (pet_id, insurance_plan_id) VALUES (3, 1);
INSERT INTO pet_insurance (pet_id, insurance_plan_id) VALUES (4, 3);
INSERT INTO pet_insurance (pet_id, insurance_plan_id) VALUES (5, 2);
INSERT INTO pet_insurance (pet_id, insurance_plan_id) VALUES (6, 1);
INSERT INTO pet_insurance (pet_id, insurance_plan_id) VALUES (7, 3);
INSERT INTO pet_insurance (pet_id, insurance_plan_id) VALUES (8, 2);
INSERT INTO pet_insurance (pet_id, insurance_plan_id) VALUES (9, 1);
INSERT INTO pet_insurance (pet_id, insurance_plan_id) VALUES (10, 2);


CREATE TABLE claim (
    claim_id INTEGER PRIMARY KEY IDENTITY(1,1),
    pet_id INTEGER NOT NULL,
    reason TEXT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    claim_date DATE NOT NULL,
    claim_status VARCHAR(20) NOT NULL DEFAULT 'Pending',
    FOREIGN KEY (pet_id) REFERENCES pet(pet_id)
);

INSERT INTO claim (pet_id, reason, amount, claim_date, claim_status) VALUES (1, 'Vaccination', 450.00, '2025-03-15', 'Approved');
INSERT INTO claim (pet_id, reason, amount, claim_date, claim_status) VALUES (2, 'Grooming', 3200.00, '2025-03-20', 'Pending');
INSERT INTO claim (pet_id, reason, amount, claim_date, claim_status) VALUES (3, 'Nail Clipping', 780.50, '2025-02-28', 'Rejected');
INSERT INTO claim (pet_id, reason, amount, claim_date, claim_status) VALUES (4, 'Other', 1200.00, '2025-03-05', 'Approved');
INSERT INTO claim (pet_id, reason, amount, claim_date, claim_status) VALUES (5, 'Grooming', 650.00, '2025-03-18', 'Approved');
INSERT INTO claim (pet_id, reason, amount, claim_date, claim_status) VALUES (6, 'Emergency', 4100.75, '2025-03-22', 'Pending');
INSERT INTO claim (pet_id, reason, amount, claim_date, claim_status) VALUES (7, 'Vaccination', 500.00, '2025-03-10', 'Approved');
INSERT INTO claim (pet_id, reason, amount, claim_date, claim_status) VALUES (8, 'Vaccination', 300.00, '2025-03-08', 'Approved');
INSERT INTO claim (pet_id, reason, amount, claim_date, claim_status) VALUES (9, 'Grooming', 960.00, '2025-02-25', 'Rejected');
INSERT INTO claim (pet_id, reason, amount, claim_date, claim_status) VALUES (10, 'Emergency', 2800.00, '2025-03-30', 'Pending');
