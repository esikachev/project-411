project-411
===========

.. image:: https://travis-ci.org/esikachev/project-411.svg?branch=master
    :target: https://travis-ci.org/esikachev/project-411

Chat bot

run with docker
---------------

.. code-block:: sh

    $ docker build -t project-411 . && docker run -p 80:5000 project-411

..

run test
--------

You can simply run api tests, using tox:

.. code-block:: sh

    $ tox -e api

..