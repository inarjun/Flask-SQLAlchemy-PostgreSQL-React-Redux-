# Flask-SQLAlchemy-PostgreSQL-React-Redux-

#login Page########################################################################################################################################################################
Python Flask postgreSQL Login Register Sytem with password hash

install psycopg2 https://pypi.org/project/psycopg2/
Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
(venv) PS C:\flaskmyproject> pip install psycopg2

Create TABLE
CREATE TABLE users (
	id serial PRIMARY KEY,
	fullname VARCHAR ( 100 ) NOT NULL,
	username VARCHAR ( 50 ) NOT NULL,
	password VARCHAR ( 255 ) NOT NULL,
	email VARCHAR ( 50 ) NOT NULL
);

PostgreSQL SERIAL To Create Auto-increment Column
CREATE TABLE users (
	id serial PRIMARY KEY
);
SMALLSERIAL	= 2 bytes	= 1 to 32,767
SERIAL	= 4 bytes	= 1 to 2,147,483,647
BIGSERIAL	= 8 bytes	= 1 to 9,223,372,036,854,775,807

###################################################################################################################################################################################
