import json
from geojson import Feature, Point, FeatureCollection
import geopandas as gpd
from shapely.geometry import shape

# input and output file that must be fixed
input_file = 'ObrasPROD20210317_GRAF.json'
output_file = 'geojson_aysa_salida.geojson'

with open(input_file, 'r') as file:
    datatxt = file.read().replace('\n', '')

# fixes!
for r in (("\\", ""), ("\"{", "{"), ("\"null,", "\"null\",")):
    datatxt = datatxt.replace(*r)

# not as featurecollection/features yet! but now its a valid json file
datajson = json.loads(datatxt)

for data in datajson:
    if data['geojson'] != 'null':
        print(data['geojson'])
        print(data['IDENTIFICADOR_OBRA'])
        print(data['UPDATED'])

geojs= {"type": "FeatureCollection", "features": []}

for g in datajson:
        a=g['geojson']
        b=g['IDENTIFICADOR_OBRA']        

        if a != 'null' and a != None and b != 'null'and b != None:
            
            geojs['features'].append(a)
            geojs['features'].append(b)
            
feature_collection = FeatureCollection(geojs['features'])
geopandas_df=gpd.GeoDataFrame.from_features(feature_collection)

# saves output geojson fixed
geopandas_df.to_file(output_file, driver='GeoJSON')

# geom = [shape(i) for i in geojs['features']]
# gpd.GeoDataFrame({'geometry':geom})
