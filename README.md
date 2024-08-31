# Pet Adoption Management Application

## Overview

This project is a Flask-based web application that allows users to manage a list of adoptable pets. The application provides features to list all pets, add new pets, and edit existing pet information.

## Project Structure

- **`app.py`**: The core application file, setting up the Flask app, defining routes, and integrating with the database.
- **`forms.py`**: Defines form classes (`AddPetForm`, `EditPetForm`) for handling user input when adding or editing pet information.
- **`models.py`**: Contains the `Pet` model using SQLAlchemy, representing pets in the database.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLAlchemy
- PostgreSQL (or another supported database)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   python -c "from app import db, create_app; create_app()"
   ```

4. Set the environment variable for the database URI (optional, defaults to local PostgreSQL):
   ```bash
   export DATABASE_URL=postgresql:///adopt
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Access the application in your web browser at `http://127.0.0.1:5000`.

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.
