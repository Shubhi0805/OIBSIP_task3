# OPENWEATHERMAP API

The code provided is a Python script that uses the Requests library to make a request to the OpenWeatherMap API to retrieve weather information for a given city. The script takes two arguments: an API key and a city name. If the API key is not provided, the script raises a ValueError. If the city name is not provided, the script raises a ValueError.

The script makes a GET request to the OpenWeatherMap API with the provided parameters, and then extracts relevant information from the response. If the response status code is 200, the script prints the weather information to the console. If the response status code is not 200, the script prints an error message.

The script also handles exceptions that may occur during the request process.
