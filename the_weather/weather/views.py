import requests
from django.shortcuts import render 

# Create your views here.
def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=d416fabbdafa48e73001e8402addc5ab'
    city = 'Chisinau'
    r = requests.get(url.format(city))
    print(r.text)
    return render(request, 'weather/weather.html')
