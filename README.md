# Simple to do list with Django REST framework and Vue.js
Write the to-dos from the frontend, hit enter and save them on the database!
# How to set up the project to run on your local machine?
Download the code to your PC, unpack the zip and move inside the folder.
# Create a new Python Virtual Environment:
python -m venv venv (Windows)

python3 -m venv venv (Linux/Mac)
# Activate the environment:
(Windows) :

cd venv/Scripts

activate

(Linux/Mac) :

cd venv

. bin/activate
# Go to the project folder and install all Python/Django dependencies
pip install -r requirements.txt 

# Open new terminal and install the Vue JS dependencies. From project folder:
cd frontend

npm install
# Run Vue JS Development Server:
npm run serve
# Run Django's development server:
python manage.py runserver
# Open up Chrome and go to 127.0.0.1:8000 and the app is now running in development mode!
