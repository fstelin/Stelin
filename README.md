# Blood Bank Management System
Stelin Francis
Student id : 10608737
We have done the assignment is a Life saver-an online blood bank and my contribution is that create and successfully compiled python Django frame work portion in our project.

2.  Django framework:
The following folders that, I have successfully created in our assignment.
	bbApp(app folder)
	Django_bbms(project folder)

2.1 BbApp(app folder) : In this folder, there are many files like

	_init.py_
	Admin.py
	Apps.py
	Forms.py
	Models.py
	Tests.py
	Urls.py
	Views.py

	_init.py
As you can see in the image below, this file is empty. This file's purpose is to inform the Python interpreter that the directory in question is a package and that the presence of the __init.py_ file therein qualifies it as a Python project. 
	Admin.py
The Django models are added to the Django administration using the Admin.py file.
In the Django admin panel, it is used to display the Django model. It accomplishes three key tasks:
signing up models
Establishing a Superuser
utilizing the web application after logging in
	apps.py

A file called Apps.py is utilized to assist users in including the application setup for their app.

Using the apps.py file, users can set the properties of their application.

The default setup is usually adequate for working with, thus customizing the attributes is a job a user rarely undertakes.
Models
	The models of web applications are represented as classes in Models.py. It is regarded as the component of the App file structure that is most crucial. The database's structure is specified by models. It describes the actual design, connections between the data sources, and restrictions on their attribute values.
Tests.py
Users can create test code for their web apps using Tests.py. It is used to evaluate how well the program functions.
Its operation is rather complicated. In the future pieces, we'll go into greater information about it
Urls.py
The functionality of Urls.py is identical to that of Urls.py in the project file structure. Linking the user's URL request to the matching pages it is pointing to is the main goal.
Views.py
When discussing the Django app structure, views play a significant role as well. An interface for interacting with a Django web application is provided via views. It includes every view as a set of classes.

Django Rest Framework's idea of serializers is used to create a variety of views. CustomFilter Views, Class-Based List Views, and Detail Views are a few of these.
Project folder

	Our project folder name is Django_bbms. This folder contains 5 python files.
They are,

Init.py

Asgi.py

Settings.py

Urls.py

Wsgi.py

	Asgi.py
         Along with wsgi.py, the most recent versions of Django contain a file called asgi.py. An alternative interface to the WSGI is the ASGI.
Asynchronous Server Gateway Interface, or ASGI, does work that is comparable to WSGI, although it is superior to the former since it allows for more flexibility in Django development. Because of this, ASGI is currently displacing WSGI more and more.


Settings.py
This file is available for adding all of the programs and middleware that are already installed. Additionally, it has details on databases and templates. The main file of our Django web application may be found here.




## Deployed to
https://github.com/fstelin/Stelin.git

## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```
For Linux
```
$  virtualenv .
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

For Linux
```
$  source bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/fstelin/Stelin.git
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip3 install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Use **[]** as your host. 
```python
ALLOWED_HOSTS = []
```
*Do not use the fault allowed settings in this repo. It has security risk!*


**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

Command for Linux:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User (HOD)
Command for PC:
```
$  python manage.py createsuperuser
```

Command for Mac:
```
$  python3 manage.py createsuperuser
```

Command for Linux:
```
$  python3 manage.py createsuperuser
```



Then Add Email and Password
