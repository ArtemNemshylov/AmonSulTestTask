# Flask Ticket System

## Overview

This is a simple ticket system web application built with Flask. It includes user authentication, role-based access control, and group management. Users can create and manage tickets, and admins can manage user groups.

## Features

- User authentication (login and logout)
- Role-based access control (Admin, Manager, Analyst)
- Group management
- Ticket creation, viewing, and status updates

## Roles

- **Admin**: Can manage all groups and view all tickets.
- **Manager**: Can manage tickets for their assigned group.
- **Analyst**: Can work with tickets from their assigned group.

## Setup

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/flask-ticket-system.git
    cd flask-ticket-system
    ```

2. **Create a virtual environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up the database**

    ```bash
    python
    ```

    In the Python shell, run the following commands:

    ```python
    from app import app
    from models import db

    app.app_context().push()
    db.create_all()
    exit()
    ```

6. **Create users and groups**
    Run the script:

    ```bash
    python create_users.py
    ```

7. **Create initial tickets**
    Run the script:

    ```bash
    python create_tickets.py
    ```

### Running the Application

1. **Run the Flask application**

    ```bash
    python app.py
    ```

2. **Open the application in your web browser**

    Visit `http://127.0.0.1:5000/` in your web browser.

### Usage

- **Login**

    - Admin: `username: admin`, `password: adminpass`
    - Manager: `username: manager1`, `password: managerpass1`
    - Analyst: `username: analyst1`, `password: analystpass1`

- **Create Tickets**

    Navigate to the "Create New Ticket" button to create a new ticket.

- **Manage Groups**

    Admins can navigate to the "Manage Groups" section to create and manage user groups.


