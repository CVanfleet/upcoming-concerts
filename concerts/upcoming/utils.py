from pymongo import MongoClient
import requests
from concerts.settings import API, DATABASES
from bson.objectid import ObjectId
import json

def get_db_connection():

    client = MongoClient(DATABASES['default']['CLIENT']['host'])
    dbname = client[DATABASES['default']['NAME']]
    return dbname

def get_api_connection(searched_artist):
    url = API['concerts']['URL']

    querystring = {"name": searched_artist,"page":"1"}  #add perameter <artist> where 'Ed Sheeran' is

    headers = {
        "X-RapidAPI-Key": API['concerts']['API_KEY'],
        "X-RapidAPI-Host": API['concerts']['API_HOST']
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response


def insert_data_from_api(searched_artist, coperformers_coll, concert_coll):
        
    # Connect to the api to get concert information
        response = get_api_connection(searched_artist)

        concerts_data = response.text
        concerts_input = json.loads(concerts_data)  

        try:

            for concert in concerts_input['data']:
                try:

                    cop = coperformers_coll.insert_one({
                        'band1' : check_performers(concert['performer'], 0), 
                        'band2' : check_performers(concert['performer'], 1), 
                        'band3' : check_performers(concert['performer'], 2)})
                    
                    
                    copObjId = ObjectId(cop.inserted_id)

                    con = concert_coll.insert_one({
                        'artist' : concert['name'],
                        'venue' : concert['location']['name'],
                        'location' : f"{concert['location']['address']['addressLocality']}, {check_region(concert['location']['address'])} {concert['location']['address']['addressCountry']}",
                        'performance_date' : concert['startDate'],
                        'coperformersId' : copObjId
                    })
                    
                    conObjId = ObjectId(con.inserted_id)

                except TypeError as t:
                    concert_coll.delete_one({'_id': conObjId})                    
                    try:
                        coperformers_coll.delete_one({'_id': copObjId})   
                    except UnboundLocalError:
                        print("coperformers do not exist")

                    print("There was a server error")
                    raise t

        except KeyError:
            print("There was an error processing the request.")

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