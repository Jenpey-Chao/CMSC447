# CMSC447 CRUD
i used Flask, flask_sqlalchemy, html. css.

to make the db.sqlite file
* open cmd
* cd to the outside of where the project is
* then enter python in cmd; py
* type: from "folder name" import db, create_app
* type: db.create_all(app=create_app())
* then the file should appear in the folder where the project is 

TO RUN THE WEBSITE:
* 1)cd into the folder
* 2) venv\Scripts\activate
* 3) set FLASK_APP=newproj
* 4) set FLASK_ENV=1
* 5) flask run
* 6) then it should tell you where its running on