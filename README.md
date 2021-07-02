Homework 11
Annotate, aggregate, select_related and prefetch_related demonstration

Overview

This web application creates an online catalog of books, authors, publishers and stores.

The main features that have currently been implemented are:

    There are models for books, authors, publishers and stores.
    Users can view list and detail information for all models.
    Admin users can manage models. 

Quick Start

To get this project up and running locally on your computer:

    Set up the Python development environment. We recommend using a Python virtual environment.
    Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python to start Python):

    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver

    To generate new data from the file "Title_List.xlsx" run the management command:
    python3 manage.py make_data

    There is a dump of some data in the file ann_agg/fixtures/db.json
    Available users: 
    "test" with password "tst123456"
    "admin" with password "adm123456" - superuser

    Open a browser to http://127.0.0.1:8000/admin/ to open the admin site.

    Open tab to http://127.0.0.1:8000/ann_agg/author/ to see all authors information.
    Open tab to http://127.0.0.1:8000/ann_agg/book/ to see all books information.
    Open tab to http://127.0.0.1:8000/ann_agg/pub/ to see all publishers information.
    Open tab to http://127.0.0.1:8000/ann_agg/store/ to see all stores information.
