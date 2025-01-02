# Flask Todo App

This is a simple Todo application built using Flask and SQLAlchemy. It allows users to create, edit, delete, and mark tasks as completed. The app also supports adding a due date to tasks.

## Features

- **Create**: Add new todo items with title, description, and due date.
- **Edit**: Edit existing todo items.
- **Delete**: Remove todo items.
- **Mark as Completed**: Mark todo items as completed or not.
- **Due Date**: Add a due date to each todo item.
- **Responsive UI**: A modern, responsive user interface.

## Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML, CSS (Bootstrap)
- **Database**: SQLite (for local development), PostgreSQL (for production)

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Jinja2

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/GauravKaklotar/Flask_TODO.git
    cd Flask_TODO
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
    
    ```bash
    venv\Scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Setup Database

1. Initialize the database:

    ```bash
    flask db init
    ```

2. Generate the migration scripts:

    ```bash
    flask db migrate -m "Initial migration"
    ```

3. Apply the migrations to create the database schema:

    ```bash
    flask db upgrade
    ```

## Running the Application

1. To run the Flask development server:

    ```bash
    flask run
    ```

2. The application will be available at `http://127.0.0.1:5000/`.

## Routes

- **Home Page**: `GET /` - Displays the list of all todos.
- **Add Todo**: `GET /add` - Form to add a new todo.
- **Edit Todo**: `GET /edit/<todo_id>` - Form to edit an existing todo.
- **Delete Todo**: `GET /delete/<todo_id>` - Deletes a todo item.
- **Mark Completed**: On the home page, you can mark todos as completed.

## Development

To contribute to the project, fork the repository, create a new branch, and submit a pull request. Ensure that you follow the code style and conventions used in the project.
