from app import app
from db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    """Create the tables in the database before the first request occurs."""
    db.create_all()
