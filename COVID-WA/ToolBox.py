import pandas as pd
months = {'March','April','May','June','July','August','September'}
counties = {"Adams","Asotin","Benton","Chelan","Clallam","Clark","Columbia",
            "Cowlitz","Douglas","Ferry","Franklin","Garfield","Grant", "Grays Harbor",
            "Island","Jefferson","King","Kitsap","Kittitas","Klickitat","Lewis",
            "Lincoln","Mason","Okanogan","Pacific","Pend Oreille","Pierce","SanJuan",
            "Skagit","Skamania","Snohomish","Spokane","Stevens","Thurston","Wahkiakum",
            "Walla Walla","Whatcom","Whitman","Yakima"}

def unemploy_text_parser(county,month):
    if month not in months:
        raise ValueError("Wrong month value input")
    if county not in county:
        raise ValueError("Wrong county value input")
    data = pd.read_csv("../data/Unemployed/Unemployment.csv")
    countyName = county + " " + "County" 
    searchCounty = data[data['County Name/State Abbr'] == countyName]# Here should insert an exceptioncatch, if we don't have a dic
    searchFinal = searchCounty[searchCounty['Period'] == month] # Here should insert an exceptioncatch
    text = "County Name: " + searchFinal['County Name/State Abbr'].item()+'     '\
    "Period: " + searchFinal['Period'].item()+ '     ' \
    "Unemployment Rate: " + str(searchFinal['Rate'].item())                 
    return text