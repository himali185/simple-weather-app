import requests
import json

#api key from OpenWeatherMap
API_KEY = '138e1c5d420361efd0af4a9790351ee5'

#fetch_data() will take a city name as input and make an API call 
#to OpenWeatherMap to fetch the weather data for that city. The function should return the JSON response.
def fetch_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}appid={API_KEY}&q={city}"
    response = requests.get(complete_url)
    return response.json()

#The following function will take the JSON response from fetch_data() as input, 
#extract the relevant information, and display it in a user-friendly format.

def display_data(weather_data):
    if weather_data['cod'] != '404':
        main_data = weather_data['main']
        # Convert from Kelvin to Celsius
        temperature = main_data['temp'] - 273.15
        humidity = main_data['humidity']
        weather_description = weather_data['weather'][0]['description']
 
        print(f"Temperature: {temperature:.2f}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_description.capitalize()}")
 
    else:
        print("City not found. Please try again.")

#main function is to handle user input and call our previously defined functions.
def main():
    city = input("Enter the name of the city: ")
    weather_data = fetch_data(city)
    display_data(weather_data)
 
if __name__ == "__main__":
    main()