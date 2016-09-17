.. image:: jobautomate/images/title.png


|travis| |coverage| |dependencies| |quality| |pyversions| |pypi| |status| |wheel| |license|

Job Automate is a command line application written in Python using the Selenium and Click libraries.
The application uses the Indeed Job Search API to find and automatically apply to 'easily apply' jobs scraped by
Indeed's job crawler. Job Automate requires access to Indeed's API with an Indeed Publisher Key. To obtain a key, please visit: http://www.indeed.com/publisher.

Disclaimer: This project was created as a proof of concept.

*************
Installation
*************

To install the script merely run the following command in a command line prompt::

    $  pip install jobautomate

If you would rather install from source, run the following commands::

    $  git clone https://github.com/mandeep/Job-Automate.git
    $  cd Job-Automate
    $  python install setup.py

************
Usage
************

Job Automate accepts the Indeed Publisher ID as an environment variable or as a command line flag. In order
to be used as an environment variable, one must export API_KEY=ID. The command line application may be invoked with the following command, flags, and arguments::

    $  jobautomate --key INDEED_PUBLISHER_ID FIRST_NAME LAST_NAME EMAIL_ADDRESS JOB_DESCRIPTION
            RESUME_PATH [JOB_LOCATION]

    Optional arguments:
        --verbose         Print to stdout the jobs that are not easily apply applications
        --vxfb            Run the application in a virtual display (Linux only)

    Example:

    $  jobautomate --key 12345 "Bender" "Rodriguez" "bender@ilovebender.com" "Metalworking" "girder.doc"

Once entered the script will open a Firefox webdriver instance and search for 'easily apply' jobs in the URLs given by the Indeed API. Due to the API only allowing 25 urls at a given time, the application will prompt for continuation after 25 urls have been traversed. The output will look similar to the image below:

.. image:: jobautomate/images/cli.png

.. |travis| image:: https://travis-ci.org/mandeep/Job-Automate.svg?branch=master
    :target: https://travis-ci.org/mandeep/Job-Automate
.. |coverage| image:: https://coveralls.io/repos/github/mandeep/Job-Automate/badge.svg?branch=master 
    :target: https://coveralls.io/github/mandeep/Job-Automate?branch=master
.. |dependencies| image:: https://img.shields.io/librariesio/github/mandeepbhutani/Job-Automate.svg
    :target: https://dependencyci.com/github/mandeep/Job-Automate
.. |quality| image:: https://img.shields.io/codacy/grade/3f52ff806b7747e7a15a60ef8242c574.svg
    :target: https://www.codacy.com/app/bhutanimandeep/Job-Automate/dashboard
.. |pypi| image:: https://img.shields.io/pypi/v/jobautomate.svg
    :target: https://pypi.python.org/pypi/jobautomate
.. |status| image:: https://img.shields.io/pypi/status/jobautomate.svg
    :target: https://pypi.python.org/pypi/jobautomate
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/jobautomate.svg
    :target: https://pypi.python.org/pypi/jobautomate 
.. |wheel| image:: https://img.shields.io/pypi/format/jobautomate.svg
    :target: https://pypi.python.org/pypi/jobautomate
.. |license| image:: https://img.shields.io/pypi/l/jobautomate.svg
    :target: https://pypi.python.org/pypi/jobautomate