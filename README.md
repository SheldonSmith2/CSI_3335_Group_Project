Project by Sheldon Smith, Zachary Scherer, and Jason Wu

Imported Python Modules (pip install)
 - flask: the main structure for the project
 - flask-wtf: to manage the forms
 - flask-sqlalchemy: to manage the databases in the application
 - flask-bcrypt: to manage hashing the password for the accounts
 - flask-login: to manage the log in system of the application
 - flask-mail: to manage the forgot email functionality
 - email_validator
 - pymysql

Instructions to Run Application
 - need to include a csi3335fall2021.py file in baseballModels directory with valid (user and password)
 - You also need to have the database running
 - execute: python run.py

To run the createDatabase.sql, just do \. createDatabase.sql in mariadb

To run the loadDatabase.py, you need to have the csv files in the same directory as the file, a csi3335fall2021.py file
  that has a valid user and password for the database, and be in an environment that has pymysql