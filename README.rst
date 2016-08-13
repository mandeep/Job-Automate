.. image:: jobautomate/images/title.png


|travis| |coverage|

Job Automate is a command line application written in Python using the Selenium and Click libraries.
The application uses the Indeed Job Search API to find and apply to 'easily apply' jobs scraped by
Indeed's job crawler. 

Disclaimer: This project was created as a proof of concept.

*************
Installation
*************

To install the script use the following commands in a command line prompt::

    git clone https://github.com/mandeepbhutani/Job-Automate.git
    cd Job-Automate
    pip install .

************
Usage
************

Once Job Automate is installed, the command line application can be
invoked with the following command and mandatory arguments::

    jobautomate FIRST_NAME LAST_NAME EMAIL_ADDRESS JOB_DESCRIPTION RESUME_PATH

    Example:

    jobautomate "Bender" "Rodriguez" "bender@ilovebender.com" "Metalworking" "girder.doc"

Once entered the script will open a Firefox webdriver instance
and search for 'easily apply' jobs in the URLs given by the Indeed API. The output
will look similar to the image below:

.. image:: jobautomate/images/cli.png

.. |travis| image:: https://travis-ci.org/mandeepbhutani/Job-Automate.svg?branch=master
    :target: https://travis-ci.org/mandeepbhutani/Job-Automate
.. |coverage| image:: https://coveralls.io/repos/github/mandeepbhutani/Job-Automate/badge.svg?branch=master
    :target: https://coveralls.io/github/mandeepbhutani/Job-Automate?branch=master