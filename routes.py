from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user

from models import db, User, Ticket, Group

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    if current_user.role == 'Admin':
        tickets = Ticket.query.all()
    else:
        tickets = Ticket.query.filter_by(group_id=current_user.group_id).all()
    return render_template('index.html', tickets=tickets)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('login.html')


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@main.route('/ticket/<int:ticket_id>', methods=['GET', 'POST'])
@login_required
def ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    if request.method == 'POST':
        ticket.status = request.form['status']
        ticket.note = request.form['note']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('ticket.html', ticket=ticket)


@main.route('/create_ticket', methods=['GET', 'POST'])
@login_required
def create_ticket():
    if request.method == 'POST':
        status = request.form['status']
        note = request.form['note']
        group_id = current_user.group_id
        user_id = current_user.id
        new_ticket = Ticket(status=status, note=note, user_id=user_id, group_id=group_id)
        db.session.add(new_ticket)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create_ticket.html')


@main.route('/manage_groups', methods=['GET', 'POST'])
@login_required
def manage_groups():
    if current_user.role != 'Admin':
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        group_name = request.form['group_name']
        if group_name:
            new_group = Group(name=group_name)
            db.session.add(new_group)
            db.session.commit()
            return redirect(url_for('main.manage_groups'))


