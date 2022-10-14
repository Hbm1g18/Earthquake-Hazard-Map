import requests
import pandas as pd
import urllib
import json
from pprint import pprint
from flask import Flask, render_template, request, flash
import os
import datetime


app = Flask(__name__)
port = os.environ.get("PORT", 5000)

@app.route("/", methods=['GET'])
def index():
    title = "Home"
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    # above is above 2.5
    urllatest = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    # Above is most recent no change
    url2 = "https://volcanoes.usgs.gov/hans2/apiv2/volcanoApi/allWithNotice"
    url3 = "https://volcview.wr.usgs.gov/vv-api/volcanoApi/wwvolcanoes"

# https://webservices.volcano.si.edu/geoserver/GVP-VOTW/wfs?request=GetCapabilities&service=WFS&AcceptFormats=application/json

    r = requests.get(url.format()).json()
    v = requests.get(url2.format()).json()
    vmap = requests.get(url3.format()).json()
    latest = requests.get(urllatest.format()).json()
    listeq = requests.get(urllatest.format()).json()
    # print(r)
    # print(v)

    earthquake = {
        'Place' : r['features'][0]['properties']['place'],
        'Mag' : r['features'][0]['properties']['mag'],
        'Time' : r['features'][0]['properties']['time'],
        'Lat' : r['features'][0]['geometry']['coordinates'][1],
        'Lon' : r['features'][0]['geometry']['coordinates'][0]
    }

    latestearthquake = {
        'Place' : latest['features'][0]['properties']['place'],
        'Mag' : latest['features'][0]['properties']['mag'],
        'Time' : latest['features'][0]['properties']['time'],
        'Lat' : latest['features'][0]['geometry']['coordinates'][1],
        'Lon' : latest['features'][0]['geometry']['coordinates'][0]
    }

    listeqdict = [{'Place2':i['properties']['place'], 
            'Mag2':i['properties']['mag'],
            'Lat2':i['geometry']['coordinates'][1],
            'Lon2':i['geometry']['coordinates'][0],
            'Time2':i['properties']['time']} 
                for i in listeq['features']]

    
    # volcano_threats = {
    #     x['volcName']: x['threat'] for x in v
    #     }

    volcano_threats = [{'name':i['volcName'], 'threat':i['threat']} for i in v]


    volcanoinfo = [{
        'name':i['vn'], 
        'vlat':i['lat'],
        'vlng':i['lng'],
        'elev':i['elevM'],
        'obs':i['obsAbbr']} 
            for i in vmap]

    print(volcano_threats)
    # print(volcanoinfo)
    # print(earthquake)
    # print(latestearthquake)
    print(listeqdict)



    # int(earthquake['Mag'])
    # round(earthquake['Mag'])

    # print(earthquake['Mag'])

    return render_template("index.html", title=title, earthquake=earthquake, volcanoinfo=volcanoinfo, volcano_threats=volcano_threats, latestearthquake=latestearthquake, listeqdict=listeqdict)


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=port)

# Run the app in powershell
# $env:FLASK_APP = "app.py"
# $env:FLASK_DEBUG = "1"
# flask run 

# For pushing to github
# git add -A
# git commit -m "some text"
# git push