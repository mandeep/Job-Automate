.. image:: jobautomate/images/title.png


|travis| |coverage| |pypi| |pyversion|

Job Automate is a command line application written in Python using the Selenium and Click libraries.
The application uses the Indeed Job Search API to find and apply to 'easily apply' jobs scraped by
Indeed's job crawler. Job Automate requires access to Indeed's API with an Indeed Publisher Key. To obtain a key, please visit: http://www.indeed.com/publisher.

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

Job Automate accepts the Indeed Publisher ID as an environment variable or as a command line flag. In order
to be used as an environment variable, one must export API_KEY=ID. The command line application may be invoked with the following command, flags, and arguments::

    jobautomate --key INDEED_PUBLISHER_ID FIRST_NAME LAST_NAME EMAIL_ADDRESS JOB_DESCRIPTION RESUME_PATH

    Example:

    jobautomate --key 123456789 "Bender" "Rodriguez" "bender@ilovebender.com" "Metalworking" "girder.doc"

Once entered the script will open a Firefox webdriver instance and search for 'easily apply' jobs in the URLs given by the Indeed API. Due to the API only allowing 25 urls at a given time, the application will prompt for continuation after 25 urls have been traversed. The output will look similar to the image below:

.. image:: jobautomate/images/cli.png

.. |travis| image:: https://travis-ci.org/mandeepbhutani/Job-Automate.svg?branch=master
    :target: https://travis-ci.org/mandeepbhutani/Job-Automate
.. |coverage| image:: https://codecov.io/gh/mandeepbhutani/Job-Automate/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/mandeepbhutani/Job-Automate
.. |pypi| .. image:: https://img.shields.io/pypi/v/jobautomate.svg
    :target: https://pypi.python.org/pypi/jobautomate
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/jobautomate.svg
    :target: https://pypi.python.org/pypi/jobautomate 
.. |wheel| image:: https://img.shields.io/pypi/format/jobautomate.svg   :target: https://pypi.python.org/pypi/jobautomate