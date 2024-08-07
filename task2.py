import requests

def get_weather(api_key, city):
    api_key = "181172c3788d0836a07e448325f84838"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data['cod'] == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return {'error': data.get('message', 'City not found')}

def print_weather(weather):
    if 'error' in weather:
        print(f"Error: {weather['error']}")
    else:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")

if __name__ == "__main__":
    API_KEY = 'your_openweathermap_api_key_here'
    city = input("Enter city name: ")
    weather = get_weather(API_KEY, city)
    print_weather(weather)


