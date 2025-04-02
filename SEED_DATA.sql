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
    FOREIGN KEY (owner_id) REFERENCES owner(owner_id)
);

-- Insert sample owner
INSERT INTO owner (name, surname, date_of_birth, contact_number, physical_address, email_address, password)
VALUES ('John', 'Doe', '1990-01-01', '1234567890', '123 Elm Street', 'john@example.com', 'password123');

-- Insert sample pet for the owner
INSERT INTO pet (owner_id, pet_type, pet_name, pet_age, pet_gender, breed_type, breed, medical_conditions)
VALUES (1, 'Dog', 'Rex', 5, 'Male', 'Pure Breed', 'Labrador', 'None');
