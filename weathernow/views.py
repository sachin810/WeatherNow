from django.shortcuts import render
import requests
from urllib.request import urlparse
from urllib.parse import urlencode
import json
import urllib
from .forms import LocationForm

def weatherview(request):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        forminput = form.cleaned_data['location']
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql1 = 'select * from '
        yql2 = 'weather.forecast where woeid in '
        yql3 = '(select woeid from geo.places(1) where text="' + forminput+ '") and u="c"'
        yql_query = yql1+yql2+yql3
        yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        forecast  =   data['query']['results']['channel']['item']['forecast']
        location = data['query']['results']['channel']['location']
        today = data['query']['results']['channel']['item']['condition']


        return render(request,'index.html', {
            "forecast":forecast,
            "city":location['city'],
            "country": location['country'],
            "region": location['region'],
            "date":today['date'],
            "temp":today['temp'],
            "text":today['text'],
            'code':today['code'],
            'form': form
        })

    return render(request,'index.html',{'form':form})