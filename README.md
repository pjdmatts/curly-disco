# curly-disco

### An Application for Creating an online Item Catalog

Curly-Disco is an application that provides a list of items within a variety of
categories as well as providing a user registration and authentication system.

Registered users have the ability to post, edit and delete their own items.

### Application Features

Curly-Disco is a [RESTful](http://flask.pocoo.org/docs/0.12/quickstart/#routing) web application using the Python framework [Flask](http://flask.pocoo.org/) along with implementing third-party OAuth authentication.

Third-part OAuth authentication is through [Google Accounts](https://developers.google.com/identity/protocols/OAuth2).


## API Features

The application provides a JSON endpoint that serves the same information as displayed in the HTML endpoints for items in the catalog.

### Installation

Download the necessary files from [this Github repository](https://github.com/pjdmatts/curly-disco)

### Requirements

In addition to the files in the repository above you will need to install Vagrant and VirtualBox

### Usage

The application runs from within a Vagrant VM:

- Clone the vm
- Launch the Vagrant VM.
- ssh into the Vagrant machine
- navigate to /vagrant/catalog folder in the vm
- initialize the database with the `database_setup.py` script
- run the app with the following command: `python/project.py`
- Access and test the application by visiting http://localhost:5000 locally

The application will allow you to build a catalog of items. However if you require a set of seed data run `lotsOfitems.py` after the `database_setup.py` and before running the app

### To-Do

Notes to self on further enhancements to the application.
