# GRanDpa-Family-Tree
####A Family Tree utilizing GraphQL, React and Django

## Description
This is a web app to be installed on any server with python3 and reactjs.
It can be used by multiple users and family tree can be crowdsourced by enabling
users to update their information as well as their immediate family.

Currently the app uses sqlite but for more heavy duty application, it can be replaced with
a more robust db solution.

GraphQL is a scalable API framework that should make getting relationship and family information faster.

TODO: Enable Web ID authentication so any user can login using Google/FB or amazon login.

## Getting Started with Django
You need python3 for this project.

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

This shoulkd ensure that all the required packages are installed. 

    cd django_graphql_react
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser
    > enter name, email, password
    python3 manage.py runserver
    
This should start the django server at port 8000. You can browse the app at

    http://localhost:8000/admin

Here enter your superuser name and password and you will be able to see the admin screen.    
## Getting Javascript running
    
    cd react-app
    npm install
    npm start
    
Javascript should start at 
    
    http://localhost:3000
    
  
    
