# Django Todo Application

## Overview
This project is a simple **To-Do app built with Django** that allows users to add, view, update, and delete tasks. It demonstrates core Django concepts including models, views, templates, forms, and URL routing to perform CRUD operations.

## Features
- Add new tasks
- View all tasks in a list
- Mark tasks as complete or incomplete
- Edit existing tasks
- Delete tasks
- Simple and user-friendly interface

## Tech Stack
- **Backend:** Python, Django
- **Database:** SQLite (default Django database)
- **Frontend:** HTML, CSS (optionally Bootstrap or similar)

## Installation and Setup

1. **Clone the repository:**

git clone <your-repo-url>
cd <your-repo-folder>

text

2. **Create and activate a virtual environment (optional but recommended):**

python -m venv venv

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate

text

3. **Install required packages:**

pip install -r requirements.txt

If requirements.txt is not available, install Django manually:
pip install django

text

4. **Apply migrations to set up the database:**

python manage.py makemigrations
python manage.py migrate

text

5. **Create a superuser (admin) to manage data:**

python manage.py createsuperuser

text

6. **Run the development server:**

python manage.py runserver

text

7. **Access the app:**

Open your web browser and go to [http://127.0.0.1:8000/todos](http://127.0.0.1:8000/todos) or the relevant URL configured.