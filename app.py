# Import necessary modules and packages
from flask import Flask, url_for, render_template, redirect, flash, jsonify

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

# Create Flask app instance
app = Flask(__name__)

# Set secret key for session management
app.config['SECRET_KEY'] = "abcdef"

# Configure database URI and disable track modifications
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect the database and create tables
connect_db(app)

def create_app():
    """Create the Flask app and initialize database."""
    with app.app_context():
        # Create all database tables
        db.create_all()

# Call the function to create app and initialize database
create_app()

##############################################################################

# Route to list all pets
@app.route("/")
def list_pets():
    """List all pets."""
    # Query all pets from the database
    pets = Pet.query.all()
    # Render the pet list template with pets data
    return render_template("pet_list.html", pets=pets)

# Route to add a pet
@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""
    # Instantiate the AddPetForm
    form = AddPetForm()

    # Check if form is submitted and valid
    if form.validate_on_submit():
        # Extract data from form excluding CSRF token
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        # Create a new pet object using form data
        new_pet = Pet(**data)
        # Add new pet to the database session
        db.session.add(new_pet)
        # Commit changes to the database
        db.session.commit()
        # Flash success message
        flash(f"{new_pet.name} added.")
        # Redirect to the pet list route
        return redirect(url_for('list_pets'))
    else:
        # Re-render the form for editing if validation fails
        return render_template("pet_add_form.html", form=form)

# Route to edit a pet
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""
    # Query the pet by ID or return 404 if not found
    pet = Pet.query.get_or_404(pet_id)
    # Instantiate the EditPetForm with pet data
    form = EditPetForm(obj=pet)

    # Check if form is submitted and valid
    if form.validate_on_submit():
        # Update pet attributes with form data
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        # Commit changes to the database
        db.session.commit()
        # Flash success message
        flash(f"{pet.name} updated.")
        # Redirect to the pet list route
        return redirect(url_for('list_pets'))
    else:
        # Re-render the form for editing if validation fails
        return render_template("pet_edit_form.html", form=form, pet=pet)

# Route to get pet info in JSON format
@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""
    # Query the pet by ID or return 404 if not found
    pet = Pet.query.get_or_404(pet_id)
    # Construct JSON response with pet information
    info = {"name": pet.name, "age": pet.age}
    # Return JSON response
    return jsonify(info)
