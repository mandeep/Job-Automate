# Job Automate

## Overview

jobautomate.py takes user input for a job description and a location then searches for jobs
using the Indeed API. The script will only apply to jobs that use the 'Easily Apply' application.
This allows the script to read from file just the name, email address, and resume of the job
applicant in order to apply to the job. The PhantomJS WebDriver is used to load the job
application links in its headless browser and to apply to each job individually.