DROP TABLE pet_insurance;
DROP TABLE insurance_plans;
DROP TABLE claim;
DROP TABLE pet;
DROP TABLE owner;

CREATE TABLE owner (
    owner_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    physical_address VARCHAR(255) NOT NULL,
    email_address VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO owner (name, surname, date_of_birth, contact_number, physical_address, email_address, password) VALUES
('Jamie', 'Isaacs', '1994-05-12', '0712345678', '12 Birchwood Avenue', 'jamie@gmail.com', 'scrypt:32768:8:1$Uh2PBBJr1lJ6a47U$2810ffd20965ab3ec44c38cc0760f6c45f8e1e8e933c6bf876b7012b7ddfd6a39361531f3dddcda86615ee8a9d54bf2f380b1e0f72a3a2c3139116d1bb23f267'),
('Taylor', 'Morgan', '1989-11-03', '0723456789', '24 Acorn Street', 'taylor@gmail.com', 'scrypt:32768:8:1$JdLkU2B9tGa92Z1Y$57009000c34d83a89d35a92bf8e1b833174edaf2389ef933336937ed567539ba887dade4db83d705312b9c03a0a0f15b85b032d088c6dd26aac1ddfd4d651a45'),
('Avery', 'Smith', '1992-08-21', '0734567890', '78 Oakridge Crescent', 'avery@gmail.com', 'scrypt:32768:8:1$JdLkU2B9tGa92Z1Y$57009000c34d83a89d35a92bf8e1b833174edaf2389ef933336937ed567539ba887dade4db83d705312b9c03a0a0f15b85b032d088c6dd26aac1ddfd4d651a45'),
('Jordan', 'Lee', '1987-01-15', '0745678901', '50 Meadow Lane', 'jordan@gmail.com', 'scrypt:32768:8:1$Uh2PBBJr1lJ6a47U$2810ffd20965ab3ec44c38cc0760f6c45f8e1e8e933c6bf876b7012b7ddfd6a39361531f3dddcda86615ee8a9d54bf2f380b1e0f72a3a2c3139116d1bb23f267'),
('Casey', 'Reed', '1995-12-05', '0756789012', '91 Sunset Boulevard', 'casey@yahoo.com', 'scrypt:32768:8:1$Uh2PBBJr1lJ6a47U$2810ffd20965ab3ec44c38cc0760f6c45f8e1e8e933c6bf876b7012b7ddfd6a39361531f3dddcda86615ee8a9d54bf2f380b1e0f72a3a2c3139116d1bb23f267'),
('Morgan', 'Parker', '1991-04-18', '0767890123', '66 Willow Way', 'morgan@mail.com', 'scrypt:32768:8:1$JdLkU2B9tGa92Z1Y$57009000c34d83a89d35a92bf8e1b833174edaf2389ef933336937ed567539ba887dade4db83d705312b9c03a0a0f15b85b032d088c6dd26aac1ddfd4d651a45'),
('Skylar', 'Bennett', '1990-09-29', '0778901234', '17 Elmwood Drive', 'skylar@gmail.com', 'scrypt:32768:8:1$JdLkU2B9tGa92Z1Y$57009000c34d83a89d35a92bf8e1b833174edaf2389ef933336937ed567539ba887dade4db83d705312b9c03a0a0f15b85b032d088c6dd26aac1ddfd4d651a45'),
('Alex', 'Hunter', '1988-06-14', '0789012345', '3 Riverbend Road', 'alex@mail.com', 'scrypt:32768:8:1$Uh2PBBJr1lJ6a47U$2810ffd20965ab3ec44c38cc0760f6c45f8e1e8e933c6bf876b7012b7ddfd6a39361531f3dddcda86615ee8a9d54bf2f380b1e0f72a3a2c3139116d1bb23f267'),
('Reese', 'Quinn', '1993-10-08', '0790123456', '88 Maple Grove', 'reese@yahoo.com', 'scrypt:32768:8:1$Uh2PBBJr1lJ6a47U$2810ffd20965ab3ec44c38cc0760f6c45f8e1e8e933c6bf876b7012b7ddfd6a39361531f3dddcda86615ee8a9d54bf2f380b1e0f72a3a2c3139116d1bb23f267'),
('Drew', 'Taylor', '1996-02-26', '0801234567', '29 Cedar Point', 'drew@mail.com', 'scrypt:32768:8:1$Uh2PBBJr1lJ6a47U$2810ffd20965ab3ec44c38cc0760f6c45f8e1e8e933c6bf876b7012b7ddfd6a39361531f3dddcda86615ee8a9d54bf2f380b1e0f72a3a2c3139116d1bb23f267');

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
    insurance_id INT PRIMARY KEY IDENTITY(1,1),
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
