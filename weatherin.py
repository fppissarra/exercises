# Weather in...
print("Weather in... \n")

# Welcome a user then ask her/him to tell you a place on Earth. 
# When the user gives you the answer, you check the weather exactly on that time and then print a message letting her/him know.

# To make a request to a web page you must import some things.
import requests
# From package bs4 (managed by the developer of Beautiful Soup to prevent name squatting) use the Beautiful Soup (a Python library) to extract information from websites.
# In this case, Google.com.
from bs4 import BeautifulSoup
# The datetime module supplies classes for manipulating dates and times.
from datetime import datetime

# Get the timestamp when you start the programme.
agora = datetime.now()

# Formatting data. Value comes from query.
def Change(f):
  # Remove the "º F" from the string.
  f = f.strip("°F")
  # Return the value without the "º F" formatting - and transformed into an integer.
  return int(f)

# Transform Fahrenheit into Celsius. Value comes from query.
def toC(fah):
  # Fahrenheit to Celsius formula: 0 ºC = (32 ºF − 32) × 5/9
  c = (fah-32)*5/9
  # Return value in Celsius.
  return c

# Ask user for a location.
city = str(input("Enter a city: "))
# Assign the search to the location provided by the user.
search = "Weather in %s" %city
# Specify the URL' search.
url = f"https://www.google.com/search?&q={search}"

# Request to access page via URL.
r = requests.get(url)

# Use BeautifulSoup to extract data from HTML.
s = BeautifulSoup(r.text,"html.parser")

# The temperature is stored inside the class "BNeawe" as a string.
f = s.find("div",class_="BNeawe").text

# To transform the Fahrenheit-temperature-string into Fahrenheit-temperature-integer, it sends the value to function Change() to format data.
fah = Change(f)
# Now with the number (integer), it sends the value to the toC function to transform the temperature from Fahrenheit to Celsius.
c = toC(fah)

# It assigns a timestamp formatted.
horario = agora.strftime("%m-%d-%Y %H:%M")

# Show the user what (s)he asked for.
print("\n The weather in %s on %s (UTC) was %2.f°C." %(city,horario,c))
