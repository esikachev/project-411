# Project 411 group [![Build Status](https://travis-ci.org/esikachev/project-411.svg?branch=master)](https://travis-ci.org/esikachev/project-411)

This repo contains a simple chat bot with the ability to learn during the session with the user.

### Requirements
* eventlet==0.17.4
* Flask==0.11.1
* Flask-SocketIO==2.8.2

### How to run application with docker
`docker build -t project-411 . && docker run -p 80:5000 project-411`

### How to run tox tests
`tox -e api`



