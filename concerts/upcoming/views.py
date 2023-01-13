from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import requests
import json
from concerts.settings import API_KEY

# Create your views here.
def upcoming_concerts(request):

    return render(request, 'upcoming/upcoming-concerts.html') 


def concerts(request):
    
    artist = request.GET['artist']


    url = "https://concerts-artists-events-tracker.p.rapidapi.com/artist"

    querystring = {"name": artist,"page":"1"}  #add perameter <artist> where 'Ed Sheeran' is

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "concerts-artists-events-tracker.p.rapidapi.com"
    }

    #response = requests.request("GET", url, headers=headers, params=querystring)

    concerts_data = response.text
    concerts = json.loads(concerts_data)            

    #concerts = [
    #       {
    #           'name': 'Ed Sheeran',
    #           'location': {
    #               'address': {
    #                   'addressCountry': 'US',
    #                   'addressLocality': 'Salt Lake City, UT'
    #                   },
    #                   'name': 'USANA'
    #           },
    #            'startDate': '2022-07-22T20:00:00-0700'
    #        }
    #]

    return render(request, 'upcoming/concerts.html', {
        'title': 'Home',
        'concerts': concerts['data']
        })

def saved_concerts(request):

    return render(request, 'upcoming/saved.html', {'title': 'Saved Concerts'}) 