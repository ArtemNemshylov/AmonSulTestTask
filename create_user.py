from app import app
from models import db, User, Group

# Ensure app context is pushed for database operations
with app.app_context():
    # Create groups
    group1 = Group(name='Customer 1')
    group2 = Group(name='Customer 2')
    group3 = Group(name='Customer 3')

    # Create users with plaintext passwords
    admin = User(username='admin', password='adminpass', role='Admin')
    manager1 = User(username='manager1', password='managerpass1', role='Manager', group=group1)
    manager2 = User(username='manager2', password='managerpass2', role='Manager', group=group2)
    analyst1 = User(username='analyst1', password='analystpass1', role='Analyst', group=group1)
    analyst2 = User(username='analyst2', password='analystpass2', role='Analyst', group=group2)

    # Add groups and users to the session and commit to the database
    db.session.add_all([group1, group2, group3, admin, manager1, manager2, analyst1, analyst2])
    db.session.commit()

    print("Users and groups created successfully.")
