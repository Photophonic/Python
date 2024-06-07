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

def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    # get a city value
    city = input('\nPlease enter a city name:\n')

    # create a variable for url from https://openweathermap.org/current#data
    # use an f string, set the appid to get the .env value from the file
    # pass in the city from input prompt as the search location 
    request_url = (f"https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=imperial")

    # print(request_url)

    # create var to hold the retrieved json data
    weather_data  = requests.get(request_url).json()

    # pprint(weather_data)

    # to access the levels in json, {variable_name}[item] 
    # or {variable}[level][item]
    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nTemp is {weather_data["main"]["temp"]}')
    # weather is an array and we want the first item [0]
    print(f'\n{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°\n')


# add this to make this a module
# if this file is the calling program then run
if __name__ == "__main__":  
    get_current_weather()


