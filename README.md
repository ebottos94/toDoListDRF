# Simple to do list with Django REST framework and Vue.js
# How to set up the project to run on your local machine? (Windows version)
Download the code to your PC, unpack the zip and move inside the folder.
# Create a new Python Virtual Environment:
python -m venv venv
# Activate the environment:
cd venv\Script
activate
# Go back to the project folder and install all the Python/Django dependencies
pip install -r requirements.txt
# Time to install the Vue JS dependencies:
cd frontend
npm install
# Run Vue JS Development Server:
npm run serve
# Run Django's development server:
python manage.py runserver
# Open up Chrome and go to 127.0.0.1:8000 and the app is now running in development mode!
