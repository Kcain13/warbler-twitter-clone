# Warbler - Twitter Clone

## Overview

Warbler is a Twitter clone built using Flask, WTForms, SQLAlchemy, and Python. It allows users to sign up, log in, post messages, follow other users, and customize their profiles.

## Features

- User signup and login
- Posting and viewing messages
- Following and followers system
- Profile customization (image, bio, location)
- Like messages
- Privacy settings (public/private profile)

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- Other dependencies (install using `pip install -r requirements.txt`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/warbler.git
    cd warbler

2. Set up a virtual environment:
    ```bash

    python -m venv venv

3. Activate the virtual environment:
    On Windows:
    ```bash

    venv\Scripts\activate
    On macOS/Linux:
    ```bash

    source venv/bin/activate

4. Install dependencies:
    ```bash

    pip install -r requirements.txt

5. Set up the database:
    ```bash

    flask db init
    flask db migrate
    flask db upgrade

6. Usage
Run the application:
    ```bash

    flask run

7. Open your browser and go to http://localhost:5000 to access the application.

8. Project Structure
    app.py: Main application file.
    forms.py: Form classes using Flask-WTF for user input.
    models.py: SQLAlchemy models for database tables.
    templates/: HTML templates for rendering pages.
    static/: Static files (CSS, images, etc.).
    migrations/: Database migration files.

9. Contributing
    Feel free to contribute to the project by opening issues or submitting pull requests.

10. Make sure to replace placeholders like `yourusername` with your actual GitHub username, and adjust the content as needed for your specific project. Include any additional sections or information that you think would be useful for users and contributors.








