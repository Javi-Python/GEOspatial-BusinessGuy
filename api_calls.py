import os
import requests
import json
from dotenv import load_dotenv
from functools import reduce
import operator
from pymongo import MongoClient
import pandas as pd
import os
load_dotenv()

def call_4square (coordinates, query):
    '''calls the 4square api with central coordinates and query type'''
    tok1= os.getenv("Client_Id")
    tok2= os.getenv("Client_Secret")
    url_query = 'https://api.foursquare.com/v2/venues/explore'
    
    params = {
    'client_id': tok1,
    'client_secret': tok2,
    'v' : "20200323",
    'll' : f"{coordinates.get('coordinates')[0]}, {coordinates.get('coordinates')[1]}",
    'query' : query
    }

    return requests.get(url= url_query, params = params).json()


def get_response(request):
    '''dives down the api response to the part that we are interested in working with'''
    return request.get("response").get("groups")[0].get("items")


def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)

def name_lat_lon(lista_response, query):
    '''extracts latitude, longitud, and venue type from a json response'''
    mapa_nombre = ['venue', 'name']
    mapa_lat = ['venue', 'location', 'lat']
    mapa_long = ['venue', 'location', 'lng']
    lista1 = []
    for dicc in lista_response:
        lista2 = {}
        lista2["name"] = getFromDict(dicc, mapa_nombre)
        lista2["latitud"]= getFromDict(dicc, mapa_lat)
        lista2["longitud"] = getFromDict(dicc,mapa_long)
        lista2['venue'] = str(query)
        lista1.append(lista2)
    return lista1

def to_point(api_list):
    '''turns coordinates into type point, takes in a list of the response'''
    documentos_ = []
    for diccionario in api_list:
        temporal = {
            "name": diccionario.get("name"),
            "location": {"type": "Point", "coordinates": [diccionario.get("longitud"), diccionario.get("latitud")]},
            'venue': diccionario.get('venue'),
            'latitud' : diccionario.get('latitud'),
            'longitud': diccionario.get('longitud')
        }
        documentos_.append(temporal)
    return documentos_

def near_point(point, radius):
    '''checks what is near each business location within our chosen radius and business location type point'''
    client = MongoClient('localhost:27017')
    db = client.get_database("ironhack")
    geo = db.get_collection("Geobusinesses")
    x = {"location": {"$near": {"$geometry": point, "$maxDistance": radius}}}
    return list(geo.find(x))
