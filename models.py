# Import SQLAlchemy module
from flask_sqlalchemy import SQLAlchemy

# Define generic image URL for pets without a specific photo
GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

# Initialize SQLAlchemy object
db = SQLAlchemy()

# Model class for adoptable pets
class Pet(db.Model):
    """Adoptable pet."""

    # Table name in the database
    __tablename__ = "pets"

    # Columns definition
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each pet
    name = db.Column(db.Text, nullable=False)  # Name of the pet (cannot be empty)
    species = db.Column(db.Text, nullable=False)  # Species of the pet (cannot be empty)
    photo_url = db.Column(db.Text)  # URL of the pet's photo (optional)
    age = db.Column(db.Integer)  # Age of the pet (optional)
    notes = db.Column(db.Text)  # Additional notes about the pet (optional)
    available = db.Column(db.Boolean, nullable=False, default=True)  # Availability status of the pet (defaults to true)

    # Method to get the image URL of the pet
    def image_url(self):
        """Return image for pet -- bespoke or generic."""
        return self.photo_url or GENERIC_IMAGE

# Function to connect database to Flask app
def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """
    db.app = app
    db.init_app(app)
