from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import requests
import json
from concerts.settings import API_KEY
from upcoming.models import Concert, CoPerformers
import datetime

# Create your views here.
def upcoming_concerts(request):

    return render(request, 'upcoming/upcoming-concerts.html') 


def concerts(request):
    
    get_artist = request.GET['artist']

    if get_artist == "":
        pass
    elif not Concert.objects.filter(artist=get_artist).exists():

        url = "https://concerts-artists-events-tracker.p.rapidapi.com/artist"

        querystring = {"name": get_artist,"page":"1"}  #add perameter <artist> where 'Ed Sheeran' is

        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": "concerts-artists-events-tracker.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        concerts_data = response.text
        concerts_input = json.loads(concerts_data)  

        try:

            for concert in concerts_input['data']:
                try:
                    
                    coperformers = CoPerformers(
                        band1 = check_performers(concert['performer'], 0),
                        band2 = check_performers(concert['performer'], 1),
                        band3 = check_performers(concert['performer'], 2)
                    )
                    coperformers.save()

                    con = Concert(
                        artist = concert['name'],
                        venue = concert['location']['name'],
                        location = f"{concert['location']['address']['addressLocality']}, {check_region(concert['location']['address'])} {concert['location']['address']['addressCountry']}",
                        performance_date = concert['startDate'],
                        coperformersId = coperformers
                    )
                    con.save()
                    

                except TypeError as t:
                    con.delete()
                    try:
                        coperformers.delete()
                    except UnboundLocalError:
                        print("coperformers do not exist")

                    print("There was a server error")
                    raise t

                else:
                    print("Something else happened")
        except KeyError:
            print("There was an error processing the request.")
    empty = ''

    if Concert.objects.all().filter(artist=get_artist).exists():
        concerts = Concert.objects.all().filter(artist=get_artist)
    else:
        concerts = ''
        empty = "No records found"

    return render(request, 'upcoming/concerts.html', {
        'title': 'Home',
        'concerts': concerts, #['data'],
        'empty': empty,
        })

def saved_concerts(request):

    return render(request, 'upcoming/saved.html', {'title': 'Saved Concerts'}) 


def check_region(address):
    if "addressRegion" in address:
        return address["addressRegion"]
    else:
        return ""

def check_performers(list, index):
    if 0 <= index < len(list):
        return list[index]['name']
    else:
        return ""