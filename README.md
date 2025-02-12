# django_tut
Just a normal django tutorial
# Creating a virtual environment
-- python -m venv nameOfVirtualEnvironment

# Activating The virtual environment
-- nameOfVirtualEnvironment/Scripts/activate

# Downloading django
-- python -m pip install django

# Check django version
-- python -m django --version

# Creating django project
-- django-admin startproject nameOfProject

# Runing project server
- Change directory to project
-- cd nameOfProject 
-- python manage.py runserver

# Creating an app
-- python manage.py startapp nameOfApp
-  Add nameOfApp to 'installed apps' in settings.py

