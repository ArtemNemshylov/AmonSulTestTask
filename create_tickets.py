from app import app
from models import db, Ticket, User, Group

# Ensure app context is pushed for database operations
with app.app_context():
    # Fetch users and groups
    admin = User.query.filter_by(username='admin').first()
    manager1 = User.query.filter_by(username='manager1').first()
    manager2 = User.query.filter_by(username='manager2').first()
    analyst1 = User.query.filter_by(username='analyst1').first()
    analyst2 = User.query.filter_by(username='analyst2').first()
    group1 = Group.query.filter_by(name='Customer 1').first()
    group2 = Group.query.filter_by(name='Customer 2').first()

    # Create tickets
    ticket1 = Ticket(status='Pending', note='Ticket 1 for group 1', user_id=admin.id, group_id=group1.id)
    ticket2 = Ticket(status='In review', note='Ticket 2 for group 1', user_id=manager1.id, group_id=group1.id)
    ticket3 = Ticket(status='Closed', note='Ticket 3 for group 2', user_id=manager2.id, group_id=group2.id)
    ticket4 = Ticket(status='Pending', note='Ticket 4 for group 2', user_id=analyst1.id, group_id=group1.id)
    ticket5 = Ticket(status='In review', note='Ticket 5 for group 1', user_id=analyst2.id, group_id=group2.id)

    # Add tickets to the session and commit to the database
    db.session.add_all([ticket1, ticket2, ticket3, ticket4, ticket5])
    db.session.commit()

    print("Tickets created successfully.")
