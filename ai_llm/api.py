import requests
def call_weather(city):
    api_key = "0d314b8768233278d494a0e2313c3edf"
    url = f'''https://api.openweathermap.org/data/2.5/weather?q={city},uk&APPID={api_key}'''
    responce = requests.get(url)
    data = responce.json()
    return data

call_weather("London")
