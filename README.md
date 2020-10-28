# Cyber Security Base 2020 - Project 1

Project for [Cyber Security Base 2020](https://cybersecuritybase.mooc.fi/) course at the University of Helsinki.

Project consists of a simple django-based web application for money transfers purposely built with different security flaws from the [OWASP top ten list](https://owasp.org/www-project-top-ten/).

## Instructions

1. Create database structure on command prompt (pyhton3 manage.py migrate)
1. Create admin user on command prompt (python3 manage.py createsuperuser)
2. Start the server on command prompt (python3 manage.py runserver)
3. Create additional users through the admin interface (https://localhost:8000/admin/)
4. When a new user is created, they must first login and open fiat account by clicking “Open account and claim free deposit” to have balance on their account. Two or more users must first open their accounts this way before real transactions can be made.
