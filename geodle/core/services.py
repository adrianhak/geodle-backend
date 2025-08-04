import math
from shapely.geometry import shape, Point
import shapefile
import re
import random
import urllib.request

from geodle.settings import HERE_API_KEY

def getRandomCoordsInLocation(locationName):
    """
    Returns a random coordinate in a given location.
    """
    shapes = shapefile.Reader('shapefiles/World_Countries_v3.shp')
    locationFeatures = [s for s in shapes.records() if locationName in s][0]
    features_id = int(re.findall(r'\d+',str(locationFeatures))[0])

    shapeRecs = shapes.shapeRecords()
    feature = shapeRecs[features_id].shape.__geo_interface__

    shp_geom = shape(feature)

    minx, miny, maxx, maxy = shp_geom.bounds
    while True:
        p = Point(random.uniform(minx,maxx), random.uniform(miny,maxy))
        if shp_geom.contains(p):
            return p.y, p.x
    
def getSatImage(lat, long, level=16, show_labels=False):
    """
    Returns a satellite image for a given location using the HERE API
    """
    url = "https://image.maps.hereapi.com/mia/v3/{}/mc/center:{},{};zoom={}/512x512/jpeg?style=satellite.day&apiKey={}".format('base' if show_labels else 'background', lat, long, level, HERE_API_KEY)
    print('Requesting sat image from url: {}', url)
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    return response.read()

