📌 Project Name: Expense Tracker Web Application
📌 Tech Stack: Python, Flask, SQLite, SQLAlchemy, HTML/CSS, Bootstrap
⭐ 1. Project Overview

This is a web-based Expense Tracker Application where a user can add, update, delete, and categorize their daily expenses.
The backend is built using Flask, data is stored in an SQLite database, and the UI is made using HTML, CSS, and Bootstrap.

⭐ 2. Languages & Frameworks Used
✅ 1. Python

All backend logic is written in Python.
Routes, functions, form handling, validations, and calculations are handled through Python.

Reason:
Python is simple, fast, and works perfectly with Flask for lightweight web applications.

✅ 2. Flask (Web Framework)

Flask is a micro web framework used to build APIs and web applications.

Flask handles:

Running the server

Handling routes ("/add-expense", "/delete", etc.)

Rendering frontend templates

Interacting with the database

Development Server Name:

👉 Werkzeug Development Server
Flask runs on this server during development.

⭐ 3. Database Related Technologies
✅ 1. SQLite (Database)

A lightweight, file-based database used to store expenses permanently.

Purpose:

Store expense records

Perform CRUD operations

Ideal for small/local applications

Database is stored in a file like:
database.sqlite3

✅ 2. SQLAlchemy (ORM – Object Relational Mapper)

ORM means:
👉 Converts Python code into SQL queries automatically.

Role of SQLAlchemy:

Manage database tables using Python classes

Insert/update/delete data without writing SQL manually

Makes database handling secure and fast

Example:
Python class Expense() = SQL table expense
expense.amount = table column

⭐ 4. Frontend Technologies
✅ 1. HTML Templates (Jinja2)

Flask uses the Jinja2 templating engine.

Used for:

Creating dynamic UI

Rendering expense data into HTML tables

Applying loops and conditions inside templates

✅ 2. CSS + Bootstrap

Bootstrap is used to create a clean and responsive user interface.

Used for:

Layout and design

Buttons, forms, tables, cards styling

Mobile responsive UI

⭐ 5. Tools Used

🛠 1. VS Code (Code Editor)
Used for writing and organizing code.

🛠 2. pip (Package Installer)
Used to install Flask, SQLAlchemy, etc.

🛠 3. Python Virtual Environment (optional but recommended)
Keeps project-specific packages isolated.

⭐ 6. How the App Works (Flow Explanation)

The user opens the web application in the browser.

Flask server receives and handles the request.

When a user adds an expense:

Form → Flask Route → SQLAlchemy Model → SQLite DB

The page updates and the new expense appears in the UI.

Users can also delete, update, or filter expenses.

Flow:
Frontend → Backend → Database → Backend → Frontend → User

⭐ 7. Why I Built This Project

To gain hands-on experience in Python + Flask

To understand CRUD operations and database management

To learn the basics of web development

To add a clean, practical project to my resume and portfolio