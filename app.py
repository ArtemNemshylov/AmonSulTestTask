from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash

from models import db, User, Ticket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():
    if current_user.role == 'Admin':
        tickets = Ticket.query.all()
    else:
        tickets = Ticket.query.filter_by(group_id=current_user.group_id).all()
    return render_template('index.html', tickets=tickets)


@app.route('/ticket/<int:ticket_id>', methods=['GET', 'POST'])
@login_required
def ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    if request.method == 'POST':
        ticket.status = request.form['status']
        ticket.note = request.form['note']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('ticket.html', ticket=ticket)
