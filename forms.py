# Import necessary modules and packages
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

# Form class for adding pets
class AddPetForm(FlaskForm):
    """Form for adding pets."""

    # Field for pet name
    name = StringField(
        "Pet Name",
        validators=[InputRequired()],  # Validator: Field must not be empty
    )

    # Field for pet species with dropdown choices
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],  # Species choices
    )

    # Field for pet photo URL (optional)
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],  # Validator: Optional field, if provided, must be a valid URL
    )

    # Field for pet age (optional)
    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)],  # Validator: Optional field, if provided, must be between 0 and 30
    )

    # Field for pet notes (optional)
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],  # Validator: Optional field, if provided, must have a minimum length of 10 characters
    )

# Form class for editing an existing pet
class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    # Field for pet photo URL (optional)
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],  # Validator: Optional field, if provided, must be a valid URL
    )

    # Field for pet notes (optional)
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],  # Validator: Optional field, if provided, must have a minimum length of 10 characters
    )

    # Field for pet availability
    available = BooleanField("Available?")  # Checkbox field for indicating pet availability
