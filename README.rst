.. image:: jobautomate/images/title.png


|travis| |coverage| |dependencies| |quality| |pyversions| |pypi| |status| |wheel| |license|

Job Automate is a command line application written in Python using the Selenium and Click libraries.
The application uses the Indeed Job Search API to find and automatically apply to 'easily apply' jobs 
published by employers on Indeed.com. Job Automate requires access to Indeed's API with an Indeed
Publisher Key. To obtain a key, please visit: http://www.indeed.com/publisher.

Due to Mozilla's move to the GeckoDriver for WebDriver instances, Job Automate does not currently
support Firefox versions above 47.0.

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
to be used as an environment variable, one must export API_KEY=ID to PATH. The command line application may be invoked with the following command, flags, and arguments::

    Usage: jobautomate [OPTIONS] FIRST_NAME LAST_NAME EMAIL JOB_DESCRIPTION RESUME_PATH [JOB_LOCATION]

    Optional arguments:
        --help            Show a help message and quit
        --key             Use the provided publisher key to access the Indeed API
        --verbose         Print to stdout the jobs that are not easily apply applications
        --vxfb            Run the application in a virtual display (Linux only)

    Example:
    $  jobautomate --key 12345 "Bender" "Rodriguez" "bender@ilovebender.com" "Metalworking" "girder.doc"

Once entered the script will open a Firefox WebDriver instance and search for 'easily apply' jobs in the URLs given by the Indeed API. Due to the API only allowing 25 urls at a given time, the application will prompt for continuation after 25 urls have been traversed. 

.. |travis| image:: https://travis-ci.org/mandeep/Job-Automate.svg?branch=master
    :target: https://travis-ci.org/mandeep/Job-Automate
.. |coverage| image:: https://coveralls.io/repos/github/mandeep/Job-Automate/badge.svg?branch=master 
    :target: https://coveralls.io/github/mandeep/Job-Automate?branch=master
.. |dependencies| image:: https://dependencyci.com/github/mandeep/Job-Automate/badge
    :target: https://dependencyci.com/github/mandeep/Job-Automate
.. |quality| image:: https://img.shields.io/scrutinizer/g/mandeep/Job-Automate.svg
    :target: https://scrutinizer-ci.com/g/mandeep/Job-Automate/
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