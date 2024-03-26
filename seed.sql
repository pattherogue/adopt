-- Drop the database if it exists
DROP DATABASE IF EXISTS adopt;

-- Create a new database named 'adopt'
CREATE DATABASE adopt;

-- Connect to the 'adopt' database
\c adopt

-- Create a table named 'pets' to store information about pets available for adoption
CREATE TABLE pets
(
  id SERIAL PRIMARY KEY,             -- Unique identifier for each pet (auto-incrementing integer)
  name TEXT NOT NULL,                -- Name of the pet (cannot be empty)
  species TEXT NOT NULL,             -- Species of the pet (cannot be empty)
  photo_url TEXT,                    -- URL of the pet's photo (optional)
  age INT,                           -- Age of the pet (optional)
  notes TEXT,                        -- Additional notes about the pet (optional)
  available BOOLEAN NOT NULL DEFAULT TRUE  -- Availability status of the pet (defaults to true)
);

-- Insert initial data into the 'pets' table
INSERT INTO pets
  (name, species, photo_url, age, notes, available)
VALUES
  ('Woofly', 'dog', 'https://www.what-dog.net/Images/faces2/scroll001.jpg', 3, 'Incredibly adorable.', TRUE),
  ('Porchetta', 'porcupine', 'http://kids.sandiegozoo.org/sites/default/files/2017-12/porcupine-incisors.jpg', 4, 'Somewhat spiky!', TRUE),
  ('Snargle', 'cat', 'https://www.catster.com/wp-content/uploads/2017/08/A-fluffy-cat-looking-funny-surprised-or-concerned.jpg', null, null, TRUE),
  ('Dr. Claw', 'cat', null, null, null, TRUE);
