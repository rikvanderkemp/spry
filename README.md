# Spry #

This came about since I needed a quick way to prototype projects. Using static HTML files can be tiresome and it misses a nice way of reusing elements as I am used to in template engines such as Twig or Jinja2. 

Now my main web language is PHP. But setting up a Twig enabled project and using slow systems like composer to bootstrap these prototype apps didn't help me personally. So I chose to create a Python alternative stand-alone Jinja2 server which gives me the power to quickly prototype projects using a powerful templating engine.

# Setup #

## Python 3 & Virtualenv ##

Make sure you have Python 3.x and Virtualenv installed. Take a look [here](https://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation) for an installation guide of Virtualenv and come back when finished.

## Initialising ##

Create a virtualenv for your new project:

	 virtualenv -p python3 example_env
	 
(where example is your newly create project folder)

Activate your environment using:
	
	source bin/activate

Within your environment or where ever you want to create your prototype create a folder and checkout all files within this repository. Or just run:

	git clone https://github.com/rikvanderkemp/spry
	
Navigate into this folder and run:
	
	pip install -r requirements.txt
	
This will install all requirements needed to run Spry.

## Starting / Stopping ##

Still in your app folder run
	
	./spry.sh start
	
If the file is not executable run
	
	chmod +x spry.sh
	
Point your browser to:

	http://localhost:8000/
	
You will see a __hello.html__ link. This is just an example to get you started. All files from /web/templates/ are listed here.

To stop the server simply run

	./spry.sh stop
	
## What is next? ##

Go and prototype, learn Jinja2 to make it easier for yourself.