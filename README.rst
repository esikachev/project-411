Project 411 group
===========

.. image:: https://travis-ci.org/esikachev/project-411.svg?branch=master
    :target: https://travis-ci.org/esikachev/project-411

This repo contains a simple chat bot with the ability to learn during the session with the user.

How to run application with docker
---------------

.. code-block:: sh

    $ docker build -t project-411 . && docker run -p 80:5000 project-411

..

How to run tests via tox
--------

Before running tests, you need install python-tox, python-dev packages via apt-get with sudo.

Use one of the following commands:

.. code-block:: sh

    $ apt-get install python-tox python-dev

..

To run test follow: 

.. code-block:: sh

    $ tox -e api

..
