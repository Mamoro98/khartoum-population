import geemap
import json 
import os 
import requests
from geemap import geojson_to_ee, ee_to_geojson
from ipyleaflet import GeoJSON
from ipywidgets import Text , HTML 
from ipyleaflet import WidgetControl, GeoJSON
import ipywidgets as widgets
from ipywidgets import Button, Layout
from ipywidgets import * 


Map = geemap.Map()

html1 = HTML(
    value = '''
    '''
)

html2 = HTML(
    value = '''   
    '''
)

control1 = WidgetControl(widget=html1, position = 'bottomright')
control2 = WidgetControl(widget=html2, position = 'topright')

Map.add_control(control1)
Map.add_control(control2)

def update_html1(feature,**kwargs):
#     html1.value =  '''
#     <div>
    
#     males from 80_84  population {} 
#     <br>
#     males from 75_79  population {}
#     <br>
#     males from 70_74  population {}
#     <br>
#     males from 65_69  population {}
#     <br>
#     males from 60_64  population {}
#     <br>
#     males from 55_59 population {}
#     <br>
#     males from 50_54  population {}
#     <br>
#     males from 45_49  population {}
#     <br>
#     males from 40-44  population {}
#     <br>
#     males from 35-39  population {}
#     <br>
#     males from 30-34  population {}
#     <br>
#     males from 25-29  population {}
#     <br>
#     males from 20-24  population {}
#     <br>
#     males from 15-19  population {}
#     <br>
#     males from 10-14 population {}
#     <br>
#     males from 5-9  population {}
#     <br>
#     males from 0-4  population {}
#     <br>
#     females from 80_84  population {} 
#     <br>
#     females from 75_79  population {}
#     <br>
#     females from 70_74  population {}
#     <br>
#     females from 65_69  population {}
#     <br>
#     females from 60_64  population {}
#     <br>
#     females from 55_59 population {}
#     <br>
#     females from 50_54  population {}
#     <br>
#     females from 45_49  population {}
#     <br>
#     females from 40-44  population {}
#     <br>
#     females from 35-39  population {}
#     <br>
#     females from 30-34  population {}
#     <br>
#     females from 25-29  population {}
#     <br>
#     females from 20-24  population {}
#     <br>
#     females from 15-19  population {}
#     <br>
#     females from 10-14 population {}
#     <br>
#     females from 5-9  population {}
#     <br>
#     females from 0-4  population {}
   
#     <br>
#     total from 80_84  population {} 
#     <br>
#     total from 75_79  population {}
#     <br>
#     total from 70_74  population {}
#     <br>
#     total from 65_69  population {}
#     <br>
#     total from 60_64  population {}
#     <br>
#     total from 55_59 population {}
#     <br>
#     total from 50_54  population {}
#     <br>
#     total from 45_49  population {}
#     <br>
#     total from 40-44  population {}
#     <br>
#     total from 35-39  population {}
#     <br>
#     total from 30-34  population {}
#     <br>
#     total from 25-29  population {}
#     <br>
#     total from 20-24  population {}
#     <br>
#     total from 15-19  population {}
#     <br>
#     total from 10-14 population {}
#     <br>
#     total from 5-9  population {}
#     <br>
#     total from 0-4  population {}
#    </div>
#     '''.format( 
#         feature['properties']['A80_84M'],
#         feature['properties']['A75_79M'],
#         feature['properties']['A70_74M'],
#         feature['properties']['A65_69M'],
#         feature['properties']['A60_64M'],
#         feature['properties']['A55_59M'],
#         feature['properties']['A50_54M'],
#         feature['properties']['A45_49M'],
#         feature['properties']['A40_44M'],
#         feature['properties']['A35_39M'],
#         feature['properties']['A30_34M'],
#         feature['properties']['A25_29M'],
#         feature['properties']['A20_24M'],
#         feature['properties']['A15_19M'],
#         feature['properties']['A10_14M'],
#         feature['properties']['A05_09M'],
#         feature['properties']['A00_04M'],
#         feature['properties']['A80_84F'],
#         feature['properties']['A75_79F'],
#         feature['properties']['A70_74F'],
#         feature['properties']['A65_69F'],
#         feature['properties']['A60_64F'],
#         feature['properties']['A55_59F'],
#         feature['properties']['A50_54F'],
#         feature['properties']['A45_49F'],
#         feature['properties']['A40_44F'],
#         feature['properties']['A35_39F'],
#         feature['properties']['A30_34F'],
#         feature['properties']['A25_29F'],
#         feature['properties']['A20_24F'],
#         feature['properties']['A15_19F'],
#         feature['properties']['A10_14F'],
#         feature['properties']['A05_09F'],
#         feature['properties']['A00_04F'],
#         feature['properties']['A80_84B'],
#         feature['properties']['A75_79B'],
#         feature['properties']['A70_74B'],
#         feature['properties']['A65_69B'],
#         feature['properties']['A60_64B'],
#         feature['properties']['A55_59B'],
#         feature['properties']['A50_54B'],
#         feature['properties']['A45_49B'],
#         feature['properties']['A40_44B'],
#         feature['properties']['A35_39B'],
#         feature['properties']['A30_34B'],
#         feature['properties']['A25_29B'],
#         feature['properties']['A20_24B'],
#         feature['properties']['A15_19B'],
#         feature['properties']['A10_14B'],
#         feature['properties']['A05_09B'],
#         feature['properties']['A00_04B'] 
#         )
    
    html2.value = '''
    Location : {} 
    <br>
    
    '''.format(feature['properties']['NAME2'])
    
    html1.value = '''
   <div style="overflow-x: scroll;
    max-width: 500px;">
    <table style="   
    border-collapse: collapse;
    border-spacing: 0;
    border: 1px solid #ddd;
    width: 100%;
    max-width: 500px;">
        <tr>
            <th
            style="    
            padding: 8px;
            white-space: nowrap;"
            ></th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 0 - 4</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 5 - 9</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 10 - 14</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 15 - 19</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 20 - 24</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 25 - 29</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 30 - 34</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 35 - 39</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 40 - 44</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 45 - 49</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 50 - 54</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 55 - 59</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 60 - 64</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 65 - 69</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 70 - 74</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 75 - 79</th>
            <th style="    
            padding: 8px;
            white-space: nowrap;">from 80 - 84</th>
          
           
            
        </tr>
        <tr>
            <td>Male</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>   
        </tr>
        
             <tr>
            <td>Female</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>   
        </tr>
        
            <tr>
            <td>Total</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>   
        </tr>
    </table>
    </div>
    '''.format(
        feature['properties']['A00_04M'],#1
        feature['properties']['A05_09M'],#2
        feature['properties']['A10_14M'],#3
        feature['properties']['A15_19M'],#4
        feature['properties']['A20_24M'],#5
        feature['properties']['A25_29M'],#6
        feature['properties']['A30_34M'],#7
        feature['properties']['A35_39M'],#8
        feature['properties']['A40_44M'],#9
        feature['properties']['A45_49M'],#10
        feature['properties']['A50_54M'],#11
        feature['properties']['A55_59M'],#12
        feature['properties']['A60_64M'],#13
        feature['properties']['A65_69M'],#14
        feature['properties']['A70_74M'],#15
        feature['properties']['A75_79M'],#16
        feature['properties']['A80_84M'],
        
        feature['properties']['A00_04F'],
        feature['properties']['A05_09F'],
        feature['properties']['A10_14F'],
        feature['properties']['A15_19F'],
        feature['properties']['A20_24F'],
        feature['properties']['A25_29F'],
        feature['properties']['A30_34F'],
        feature['properties']['A35_39F'],
        feature['properties']['A40_44F'],
        feature['properties']['A45_49F'],
        feature['properties']['A50_54F'],
        feature['properties']['A55_59F'],
        feature['properties']['A60_64F'],
        feature['properties']['A65_69F'],
        feature['properties']['A70_74F'],
        feature['properties']['A75_79F'],
        feature['properties']['A80_84F'],
        
        feature['properties']['A00_04B'],
        feature['properties']['A05_09B'],
        feature['properties']['A10_14B'],
        feature['properties']['A15_19B'],
        feature['properties']['A20_24B'],
        feature['properties']['A25_29B'],
        feature['properties']['A30_34B'],
        feature['properties']['A35_39B'],
        feature['properties']['A40_44B'],
        feature['properties']['A45_49B'],
        feature['properties']['A50_54B'],
        feature['properties']['A55_59B'],
        feature['properties']['A60_64B'],
        feature['properties']['A65_69B'],
        feature['properties']['A70_74B'],
        feature['properties']['A75_79B'],
        feature['properties']['A80_84B'],
    )

path =  r'C:\Users\Ammar\Downloads\oro\supermarket_geoJson.geojson'

with open(path) as f :
    json_data = json.load(f)

json_layer = GeoJSON(data=json_data, name="Sudan state",hover_style={'fillColor':'red','fillOpacity':0.5 })

Map.add_layer(json_layer)

json_layer.on_click(update_html1)