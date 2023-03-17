from django.shortcuts import render
import json
from upcoming.models import Concert, CoPerformers
from datetime import datetime, timezone
import dateutil.parser
from upcoming.utils import *
from bson.objectid import ObjectId

# Create your views here.
def upcoming_concerts(request):

    
    dbname = get_db_connection()
    collection = dbname['concert']

    cop = collection.find_one({'_id': ObjectId("64140e0fb0487363ec8dd9aa")})

    print(cop['_id']['band1'])

    '''for concert in concerts:
        if dateutil.parser.parse(concert['fields']['performance_date']) < datetime.now(timezone.utc):
            collection2.delete_one({'pk': concert['fields']['coperformersId']})
            collection.delete_one({'pk': concert['pk']})'''

    return render(request, 'upcoming/upcoming-concerts.html') 


def concerts(request):

    dbname = get_db_connection()

    concert_coll = dbname['concert']
    coperformers_coll = dbname['coperformers']
    
    searched_artist = request.GET['artist']

    if searched_artist == "":
        pass
    elif concert_coll.count_documents({'artist': searched_artist}) == 0:

        insert_data_from_api(searched_artist, coperformers_coll, concert_coll)
        print("Data was inserted successfully")

    empty = ''

    concert_count = concert_coll.count_documents({'artist': searched_artist})

    if concert_count >= 5:
        concerts = concert_coll.find({'artist': searched_artist})
    elif concert_count < 5 and concert_count > 0:
        concert_coll.delete_many({'artist': searched_artist})
        insert_data_from_api(searched_artist, coperformers_coll, concert_coll)
    else:
        concerts = ''
        empty = "No records found"

    return render(request, 'upcoming/concerts.html', {
        'title': 'Home',
        'concerts': concerts, 
        'empty': empty,
        })

def saved_concerts(request):

    return render(request, 'upcoming/saved.html', {'title': 'Saved Concerts'})




