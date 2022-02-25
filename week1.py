from __future__ import print_function
from babel import Locale
from cachetools import cached, LRUCache, TTLCache
from cffi import FFI
import click
import importlib_metadata 
from markupsafe import Markup, escape
from PIL import Image
from pyrsistent import pvector
from datetime import *
from pytz import timezone
import qrcode
from speaklater import make_lazy_string
#babel is used to translate the strings and assist with internationalization and localization python applications.
local=Locale('rw','RW')
print(local.territories['RW'])
print('#output of calendar days')
local=Locale('en')
month_names=local.months['format']['wide'].items()
print(list(month_names))
# cachetools is helps to store data so then in future request fot that particular data can be solved fast
@cached(cache={})
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(10))

#jinja2 is a python template engine need to create html, xml or other markup format that are returtner to the user via an http response
print('Welcome ', ' Leapture Rwanda', sep = ' To ')
#MarkupSafe implements a text object that escapes characters so it is safe to use in HTML and XML

# escape replaces special characters and wraps in Markup
result=escape("<script>alert(document.cookie);</script>")
print(result)
# wrap in Markup to mark text "safe" and prevent escaping

result= Markup("<strong>Hello</strong>")
print(result)
# Pillow is Python Imaging Library(PIL) which adds support for opening, manipulating and saving images.
#Open image using Image module
im = Image.open("./images/mussa.png")
#Show actual Image
im.show()
#Show rotated Image
im = im.rotate(45)
im.show()
#python-dateutil is a library for manipulating dates in a variety of formats.
# Creating a few datetime objects to work with
NOW = datetime.now()
print("The datetime right now : ", NOW)
TODAY = date.today()
print("The date today : ", TODAY)
#pytz is a library for working with timezones in Python.
format = "%Y-%m-%d %H:%M:%S %Z%z"
# Current time in UTC
now_utc = datetime.now(timezone('Africa/Kigali'))
print(now_utc.strftime(format))
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
print(now_asia.strftime(format))
#qrcode is a library for creating and rendering QR codes.
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("./images/logo.png")
print(img) 
#speaklater is a library for lazy string evaluation.
sval = u'Hello World'
string = make_lazy_string(lambda: sval)
print(string)
print(string.upper())
    