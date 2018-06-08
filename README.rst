==============
Store REST API
==============

Description
-----------

A store REST API to be uploaded to Heroku.

Packages
--------

The backbone of this app is Flask, though Flask-RESTful and Flask-JWT are also important.

Heroku
------

This app was uploaded to Heroku, both manual and automatic deployment were used. The database was also switched to use PostgreSQL and the corresponding addon was used to keep the database persistent. Since using SQLite would not achieve this.
