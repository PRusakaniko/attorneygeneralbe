# Instructions
 - clone this repo
 - ``` git clone https://github.com/PRusakaniko/jsc_web.git ```
 - navigate into repo
 - ``` cd jsc_web ```
 - install pipenv configuration in repo
 - ``` pipenv install ```
 - start virtual environment/pipenv
 - ``` pipenv shell ```
 - install requirements
 - ``` pipenv install -r requirements.txt ```
 - start server and enjoy
 - ``` python manage.py runserver ```
 - if server fails to start, it can only mean migrations aren't being read
 - ``` python manage.py makemigrations ``` then ``` python manage.py migrate ```
 - run server again
 - ``` python manage.py runserver ```
