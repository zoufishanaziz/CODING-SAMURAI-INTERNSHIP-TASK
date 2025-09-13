import requests

cityname='Lahore'
API_key='7e13ea222e53b60219a951a19272561b'
url=f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={API_key}&units=metric'

resp=requests.get(url)
if resp.status_code==200:
    data=resp.json()
    print('weather is',data['weather'][0]['description'])
    print('current temperature is',data['main']['temp'])
    print('current temperature feels like', data['main']['feels_like'])
    print('current humidity is',data['main']['humidity'])



