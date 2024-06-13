# The requests module allows you to send HTTP requests using Python
import requests

# Python-dotenv reads key-value pairs from a .env file and can set them as environment variables.
from dotenv import load_dotenv

# Python has a built-in os module with methods for interacting with the operating system,
import os

# import pretty print to format the output from the json variable
from pprint import pprint

# call the function from the dotenv library
load_dotenv()

# define function and pass in a default value
def get_current_weather(city="Kanas City"):
    # pass in the city from input prompt as the search location 
    request_url = (f"https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=imperial")
    
    # create var to hold the retrieved json data
    weather_data  = requests.get(request_url).json()
    
    # this will get the data from the site using the API and pass it to the calling process.
    return weather_data


# add this to make this a module
# if this file is the calling program then run
if __name__ == "__main__":  
    print('\n*** Get Current Weather Conditions ***')
    
    city = input('\nPlease enter a city name:\n')

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
