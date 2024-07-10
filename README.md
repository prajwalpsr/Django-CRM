# Django Customer Records Management System

This is a simple Django-based web application for managing customer records. It allows users to register, log in, view, add, update, and delete customer records. The project includes authentication features to ensure that only authenticated users can access certain functionalities.

## Features

- User registration and login
- Add, update, and delete customer records
- View customer records
- Authentication to restrict access to certain features
- User-friendly forms with Django's built-in form handling and validation

## Installation

To get a local copy up and running, follow these steps:
- activate the Virtual env located in venv
- install the django module (pip install django)
- Update settings.py to include your MySQL database configuration
- Make the migrations on MySQL:
- - python manage.py makemigrations
- - python manage.py migrate
- Create a superuser (python manage.py createsuperuser)
- Run the development server (python manage.py runserver)

### Prerequisites

- Python 3.x
- Mysql
- pip
- virtualenv (optional but recommended)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/django-customer-records.git
   cd django-customer-records
