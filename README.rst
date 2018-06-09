==============
Store REST API
==============

Description
-----------

A store REST API to be uploaded to Heroku and DigitalOcean.

Packages
--------

The backbone of this app is Flask, though Flask-RESTful and Flask-JWT are also important.

Heroku
------

This app was uploaded to Heroku, both manual and automatic deployment were used. The database was also switched to use PostgreSQL and the corresponding addon was used to keep the database persistent. Since using SQLite would not achieve this.

DigitalOcean
------------

The steps taken to set up the DigitalOcean server took roughly this form:

- A server running Ubuntu 18.04 was created, on this server postgresql and postgresql-contrib were installed.
- A new UNIX user was setup and given the power to enter password for root. SSH login via root was disabled and now will SSH via user and password.
- The UNIX user was given PostgreSQL permissions and had a db created for it.
- PostgreSQL was modified to require a password instead of accepting peer connections (required for SQLAlchemy and good practice).
- Nginx was installed, firewall was activated and rules added for nginx and ssh.
- Conf params were added to nginx, some files and folders were created to hold relevant files.
- Repository cloned to the server and a virtualenv setup with required packages installed.
- uWSGI setup, a service was created using systemctl and uwsgi.ini was adjusted.
