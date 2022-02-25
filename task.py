
import click
import pytz
import datetime as dt
import dateutil  
from dateutil.relativedelta import *
from jinja2 import Template
from cffi import FFI
import os
from pyrsistent import pvector
import json
import facebook
#flake8 is great library toolkit for checking your code base against coding style, programming errors(like library mported but unused and undefined name)
#run it use python3 -m flake8 feedBack.py
 #McCabe automatically detects over-complex code basing on cyclomatic complexity
 #run it use python3 -m mccabe feedBack.py
# pytz is a library for working with timezones in Python. code example
# Print all supported timezones
print('The timezones supported by pytz module:\n', pytz.all_timezones, '\n')
# Retrieve the current date
source_date = dt.datetime.now()
# Print the current data and time
print('The current date and time:\n', source_date)

# Set the timezone to poland
currentTimeZone = pytz.timezone('Africa/Kigali')
# Print the current time-zone Poland
print('\nThe time-zone is set to:\n', currentTimeZone)
# Read and print the current date and time of the time-zone
currentDateWithTimeZone = currentTimeZone.localize(source_date)
print('The date and time of this time-zone:\n', currentDateWithTimeZone)

# Set the target time-zone
newTimeZone = pytz.timezone('Portugal')
print('\nThe time-zone is set to:\n', newTimeZone)
# Read and print the current date and time of the newly defined time-zone
newDateWithTimezone = currentDateWithTimeZone.astimezone(newTimeZone)
print('The date and time of this time-zone:\n', newDateWithTimezone)

#python-dateutil is a library for manipulating dates in a variety of formats.
#code example
source_date = dt.datetime.now()
month_next = source_date+ relativedelta(months=+1)
print('Date of next month:')
print(month_next)

#ninja2 is a python template engine need to create html, xml or other markup format that are returtner to the user via an http response
#code example
name = input("Enter your name: ")

tm = Template("Hello {{ name }}")
msg = tm.render(name=name)

print(msg)
#cffi is an extennal package proving a C foreign function interface for python
ffibuilder = FFI()

ffibuilder.cdef("float pi_approx(int n);")

ffibuilder.set_source("_pi",  # name of the output C extension
"""
    #include "pi.h"
""",
    sources=['pi.c'],   # includes pi.c as additional sources
    libraries=['m'])    # on Unix, link with the math library

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
#pyrsistent is a Python library for immutable data structures.
def test_addition(pvector):
    v = pvector([1, 2]) + pvector([3, 4])

    assert list(v) == [1, 2, 3, 4]
    
# facebook-sdk is a python library for the Facebook Graph API.
# code example
def main():
    token = "EAAJZBmdYgSIQBAOHZCAhWeNgC61T28JXHqOcaz4S1QTEJq0TtQ58Nf2vbzJ6HnMnhG1y7faHIJZCXYKeKCeoovPvz62BMt7bkz4WfIHcuX1zZB2U1kqmsJOZBYptQ4x5Q2Mvn9LBTarYeDJV5v7qjHX3UwhCgD2Y7LFTo1ZBrZBM2YjdhxszxdVJJrDrKwXoNAB72676DZBE7ZBlF3RrZA09xOnIkPaNt4zsePDFrggyeWE6KREhUY2LFZA"
    graph = facebook.GraphAPI(token)
	    #fields = ['first_name', 'location{location}','email','link']
    profile = graph.get_object('me',fields='first_name,location,link,email')	
	    #return desired fields
    print(json.dumps(profile, indent=4))

if __name__ == '__main__':
	main()
 
 
# Click is library for creating beautiful command line interfaces in easy way.

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()
    