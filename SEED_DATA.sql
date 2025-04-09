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

CREATE TABLE insurance_plans (
    insurance_id INT PRIMARY KEY IDENTITY(1,1),  -- Auto-increment for insurance_id
    insurance_name VARCHAR(50) NOT NULL,
    price_per_month DECIMAL(10, 2) NOT NULL,
    features TEXT NOT NULL,
	insurance_logo TEXT NOT NULL
);

INSERT INTO insurance_plans (insurance_name, features, price_per_month)
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

CREATE TABLE claim (
    claim_id INTEGER PRIMARY KEY IDENTITY(1,1),
    pet_id INTEGER NOT NULL,
    reason TEXT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    claim_date DATE NOT NULL,
    claim_status VARCHAR(20) NOT NULL DEFAULT 'Pending',
    FOREIGN KEY (pet_id) REFERENCES pet(pet_id)
);
