# 🍽️ Food App – Built with Django

This project is a beginner-friendly Django-based web application designed to help you learn and understand key concepts of Django development.

---

## 📚 Sections Overview

### 📌 Section 1: Introduction & Installing Required Software
Learn what Django is and why it is used. Install all the tools needed to begin building Django web applications.

### ⚙️ Section 2: Setting Up the Django Project
Create your first Django project and run the development server.

### 🧠 Section 3: Views & URL Patterns
Understand the MVT (Model-View-Template) architecture. Create Django views and configure URL patterns for routing.

### 🗃️ Section 4: Database & Models
Create models to interact with the database and auto-generate database tables.

### 🖼️ Section 5: Templates
Use Django templates to display data and pass backend data to the frontend.

### 🎨 Section 6: Static Files & Site Design
Use CSS, JavaScript, and images to enhance and style your web pages.

### ✍️ Section 7: Forms
Create and manage forms to handle user input and perform **CRUD** operations.

### 🔐 Section 8: Authentication
Implement user **registration**, **login**, and **access control** with protected views.

### 🛎️ Section 9: Django Signals & Class-Based Views
Use Django signals for event handling and implement CBVs as a clean alternative to function-based views.

---

## 🚀 Features

- Clean and modular Django structure
- User-friendly frontend using templates and static files
- Full authentication system (login/register/logout)
- Dynamic routing and data rendering
- Form handling with validation
- Signals and Class-Based Views support

---

## 🛠️ Installation & Setup

### Clone the repository
git clone https://github.com/AnjaliYadav-04/Food_App.git
cd Food_App

### Install dependencies
pip install -r requirements.txt

### Run migrations
python manage.py migrate

### Start the development server
python manage.py runserver

---

## 🚢 Deployment Guide
### You can deploy this Django app on platforms like Render, Heroku, or PythonAnywhere. Here’s a quick guide for Render:
-Push code to GitHub.
-Sign in to Render and create a new Web Service.
-Connect your GitHub repository

### Set build command:
-pip install -r requirements.txt

### Set start command:
-gunicorn Food_App.wsgi:application

---

## 👤 Author
### Anjali Yadav

