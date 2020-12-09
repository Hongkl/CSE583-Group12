import pandas as pd
import panel as pn
import folium
import json
import param
import os
import webbrowser

pn.extension()

class CovidWeb(param.Parameterized):
    Months = param.ObjectSelector(default='March', objects = ['March','April','May','June','July','August','September'])
    Counties = param.ObjectSelector(default='Clark',objects = ["Adams","Asotin","Benton","Chelan","Clallam","Clark","Columbia",
                                                                  "Cowlitz","Douglas","Ferry","Franklin","Garfield","Grant", "Grays Harbor",
                                                                  "Island","Jefferson","King","Kitsap","Kittitas","Klickitat","Lewis",
                                                                  "Lincoln","Mason","Okanogan","Pacific","Pend Oreille","Pierce","SanJuan",
                                                                  "Skagit","Skamania","Snohomish","Spokane","Stevens","Thurston","Wahkiakum",
                                                                  "Walla Walla","Whatcom","Whitman","Yakima"])
    #Map = folium.Map(location=[47.751076, -120.740135], zoom_start=7)
    
    @param.depends('Counties','Months')
    def unemploy_text(self):
        data = pd.read_csv("../data/Unemployed/Unemployment.csv")
        County = self.Counties
        countyName = County + " " + "County" 
        searchCounty = data[data['County Name/State Abbr'] == countyName]# Here should insert an exceptioncatch, if we don't have a dic
        searchFinal = searchCounty[searchCounty['Period'] == self.Months] # Here should insert an exceptioncatch
        text = "County Name: " + searchFinal['County Name/State Abbr'].item()+'     '\
        "Period: " + searchFinal['Period'].item()+ '     ' \
        "Unemployment Rate: " + str(searchFinal['Rate'].item())                 
        return text
    
    def getGeoAndData(self):
        state_geo = json.load(open("../data/WA_County_Boundaries.geojson"))
        state_data = pd.read_csv("../data/COVID19/COVID19-Rate.csv")
        return state_geo, state_data
    
    @param.depends('Counties','Months')                                            
    def popup(self):
        Map = folium.Map(location=[47.351076, -120.640135], zoom_start=7.5)
        
        #popup Unemployment data    
        searchCounty = '../data/WA_County_json/'+ self.Counties + '.json' 
        Text = self.unemploy_text()
        layer1 = folium.features.GeoJson(data = json.load(open(searchCounty)), tooltip = folium.map.Tooltip(text = Text)).add_to(Map)
        
        #popup Covid data                    
        state_geo,state_data = self.getGeoAndData()
        month = self.Months
        layer2 = folium.Choropleth(
            geo_data=state_geo,
            name='choropleth',
            data=state_data,
            columns=['County', month],
            key_on='feature.properties.JURISDICT_NM',
            fill_color='OrRd',
            fill_opacity=0.7,
            line_opacity=0.2,
            threshold_scale=[0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.2, 1.8],
            legend_name='Covid19 Infect Rate (%)',
        ).add_to(Map)
        Map.keep_in_front(layer2, layer1)
        folium.LayerControl().add_to(Map)
        return Map
    
    @param.depends('Counties','Months')   
    def view(self): 
        return pn.pane.HTML(self.popup(), sizing_mode="scale_both")

    
viewer = CovidWeb(name='Group-12 Map Viewer')

pn.Row(viewer.param, viewer.view).servable()
os.popen('panel serve --show CovidWeb.py').read() 
