============
Jobautomate
============

Overview
============

Jobautomate uses the Indeed Job Search API to apply to 'easily apply' jobs posted to Indeed's website.
Jobautomate comes in two forms. A command line interface (working) and a web application (in development).
Both require user input for first name, last name, and email
address for the user's details. The résumé is uploaded on the web interface
and read from file when using the command line interface. 

Disclaimer: This project was created as a  proof of concept.

Command Line Interface
======================

To install the script use the following commands in a command line prompt::

    git clone https://github.com/mandeepbhutani/Job-Automate.git
    cd Job-Automate
    python setup.py install


Place a résumé file in your current working directory and then run the script
in a command line prompt using the following command::

    jobautomate

The script will ask for first name, last name, email address, job description,
and job location. Once entered the script will open a Firefox webdriver instance
and search for 'easily apply' jobs in the URLs given by the Indeed API. The output
will look similar to the image below:

.. image:: jobautomate/images/cli.png
