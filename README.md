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

# Blood Bank Management System
Nithin Joseph
Student id : 10606808
We have done the assignment is a Life saver-an online blood bank and my contribution is that create and successfully compiled python Django frame work portion in our project.

We have done the assignment is a Life saver-an online blood bank and my contribution is that create html pages in our project.

The following folders that, I have successfully created in our assignment.
	base-fullscreen.html
You can set up your stylesheets to automatically change the size, style, or layout of content as elements alternate between full screen and conventional presentations by using the:fullscreen pseudo-class.
base-rtl.html

The element's content's text direction is specified by the dir attribute.
<p dir="rtl"> Type this text from right to left. </p>
	base.html

The base URL and/or target for each relative URL in a document are   specified by the <base> tag. 
Either a target attribute or a href attribute, or both, must be included in the         <base> tag.
A document may have just one base element, and that element must be located inside the head element.
	blood_group_mgt.html

It is page named blood group list where the user can access the 
Date/Time: available days in which they can receive the blood
Name: type of blood available for the user
Available: It means the user can see how much volume of blood is available
Status: Shows the activity of particular blood groups(whether it is available or not)
Action: can modify the details according to the needs by clicking edit or delete sign.

	donation_mgt.html

This page indicates the list of whole donar donation list.By clicking this page it displays 
Transfusion date time of donar 
Name of the particular donar 
Contact details of each donar 
Moreover blood type and volume of blood they given also shows
Finally by clicking action drop down menu we can edit or remove details of each donar
The models of web applications are represented as classes in Models.py. It is regarded as the component of the App file structure that is most crucial. The database's structure is specified by models. It describes the actual design, connections between the data sources, and restrictions on their attribute values.

	home.html
      Header, main, and footer are the three components that make up the home page
   The navigation bar and the logo are located in the header section.
   The main area of the page includes the introduction, accomplishments,projects.
   The copyright, contact information, and social networking connections are all  located in the footer area.
	login.html

It implies that businesses are now developing their websites. They must sell their goods or services to individuals in order to do that. The next step is for them to gather user or client data. People must fill out a registration form in order to create an account on that website. They will be able to log in to their account the following time after making one. They must do that by entering their user name or email from the signup process. A user will not be able to log in if they have entered their information incorrectly. On the other side, if any field is left empty, you will not be able to log in. You can retrieve your username and password if you've lost them by following the instructions in the text below. It also features a login button, which is used to access an account after creating one and correctly completing out the required details.

	manage_blood_group.html
It comprises of a Home Page that describes Blood Groups and Their Types, a Signup Page that registers Blood Donor Details and their contact Information, and a Search Page that enables users to search and receive updates on Blood Groups and Donor Information that are Available.
	manage_donation.html
The goal of the online blood donation management system is to compile e-Information on the donor and the organisation involved in blood donation. Any individual who is interested in donating blood can register through this application, and any organisation that wishes to register on this website can also do so. Additionally, this website can be used by any common consumer who wishes to request blood online. The primary authority who can make additions, deletions, and modifications as needed is the administrator.
	manage_profile.html
This page helps the admin to manage the users profile by pressing the edit button in order to add any details about user or admin can delete the users profile if there is no need of it.
Admin can also update the  type, and the volume of blood according to the availability. 
	manage_request.html
admin can manage the request of the users
he can allot the slot for which the users requested 
admin will grant the request of  user for the particular blood 
	profile.html
This page is used to edit the user profile
User will see his/her full name as email, username etc
He/she can update password as well as they can update their profile If there is something required
	register.html
By clicking the register button the users can register to the website 
They have to provide 
First Name, Last Name, Email, username, password, confirm password 
After their successful registration they would get the access for entering in to the website 
Before login into the website users must register 
	request_mgt.html
This page mainly used by the users in order to request for the blood
For the request they have to enter the 
Patient Name, Gender, Blood Group, Volume of blood, physician name etc
By mentioning  these details the admin will allow/reject the users need.
	update_password.html
The input attribute's password value shows a field where a user can enter a password into a form. It's vital to note that the characters entered in this field are obscured, making it impossible for onlookers to read the text displayed on the screen. Don't rely on a password field to truly safeguard the data because this doesn't apply any encryption when the data is transferred. Different browsers show obfuscated characters in different ways. In most instances, asterisks or circular bullets will be used in their stead.
Users can update their password by clicking the update password button 
	view_donation.html
Admin can view the list of donations of blood 
By analysing the blood detail he/she can make use of the blood for the appropriate user.
	view_request.html
This page allows admin to view the requisition of blood by different customers.
Admin will allow/reject the blood request 
Admin can modify the details of customers after the allocation or rejection of blood for the customers.





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
