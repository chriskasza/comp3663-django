[![Build Status](https://travis-ci.com/comp-3663-weather-visualization/comp3663-django.svg?branch=master)](https://travis-ci.com/comp-3663-weather-visualization/comp3663-django)

# comp3663-project
Backend code, written in Django, providing a REST API.

## Setting up a dev environment

Install docker and docker-compose

installation for [Mac](https://docs.docker.com/docker-for-mac/) <br>
https://docs.docker.com/docker-for-mac/

Install for [unbuntu](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04) <br>

https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04

### Running the project

* Run ``` docker-compose up``` in the directory

### Running Tests

Run  ```# docker-compose -f docker-compose-test.yml up``` in the directory

The tests are located in the /tests module the command above will automatically run them. 

