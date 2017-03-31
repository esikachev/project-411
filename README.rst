Project 411 group
===========

.. image:: https://travis-ci.org/esikachev/project-411.svg?branch=master
    :target: https://travis-ci.org/esikachev/project-411

This repo contains a simple chat bot with the ability to learn during the session with the user.

Requirements
---------------
* eventlet==0.17.4
* Flask==0.11.1
* Flask-SocketIO==2.8.2

How to run application with docker
---------------

.. code-block:: sh

    $ docker build -t project-411 . && docker run -p 80:5000 project-41

..

How to run tox tests
--------

.. code-block:: sh

    $ tox -e api

..
