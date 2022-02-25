Step 1 : Clone the project

Step 2 : Creating the virtual environment

    virtualenv venv

Step 3 : Installing the packages in the virtual environment
       
   
    pip install -r requirements.txt

Step 4 : Running the project
       .\venv\Scripts\activate

    python3 manage.py runserver

Step 5 : Setting up the database / handling the database changes

    python manage.py makemigrations
    
    python manage.py migrate

Step 6 : Setting up the superuser [admin]

    python manage.py createsuperuser