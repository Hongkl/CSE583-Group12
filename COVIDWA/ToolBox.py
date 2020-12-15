import pandas as pd
months = {'March', 'April', 'May', 'June', 'July', 'August', 'September'}
counties = {"Adams", "Asotin", "Benton", "Chelan", "Clallam", "Clark",
            "Columbia", "Cowlitz", "Douglas", "Ferry", "Franklin",
            "Garfield", "Grant", "Grays Harbor", "Island", "Jefferson",
            "King", "Kitsap", "Kittitas", "Klickitat", "Lewis",
            "Lincoln", "Mason", "Okanogan", "Pacific", "Pend Oreille",
            "Pierce", "SanJuan", "Skagit", "Skamania", "Snohomish",
            "Spokane", "Stevens", "Thurston", "Wahkiakum",
            "Walla Walla", "Whatcom", "Whitman", "Yakima"}


def unemploy_text_parser(county, month):
    if month not in months:
        raise ValueError("Wrong month value input")

    if county not in county:
        raise ValueError("Wrong county value input")

    data = pd.read_csv("../data/Unemployed/Unemployment.csv")
    countyName = county + " " + "County"
    searchCounty = data[data['County Name/State Abbr'] == countyName]
    # Here should insert an exceptioncatch, if we don't have a dic
    searchFinal = searchCounty[searchCounty['Period'] == month]
    # Here should insert an exceptioncatch
    text = "County Name: " +\
        searchFinal['County Name/State Abbr'].item()+'     '
    "Period: " + searchFinal['Period'].item() + '     '
    "Unemployment Rate: " + str(searchFinal['Rate'].item())
    return text


def plot(county):
    county = county + " " + "County"
    covid_data = pd.read_csv(
        "../data/COVID19/COVID19-Rate and Unemployment.csv")
    df_covid = pd.DataFrame(covid_data.loc[covid_data['County'] == county,
                                           ['March',
                                            'April',
                                            'May',
                                            'June',
                                            'July',
                                            'August',
                                            'September']].T)
    df_unemployment = pd.DataFrame(
        covid_data.loc[covid_data['County'] == county,
                       ['March_umemployment',
                        'April_umemployment',
                        'May_umemployment',
                        'June_umemployment',
                        'July_umemployment',
                        'August_umemployment',
                        'Septembe_umemployment']].T)
    df_unemployment.rename({'March_umemployment': 'March'},
                           axis='index', inplace=True)
    df_unemployment.rename({'April_umemployment': 'April'},
                           axis='index', inplace=True)
    df_unemployment.rename({'May_umemployment': 'May'},
                           axis='index', inplace=True)
    df_unemployment.rename({'June_umemployment': 'June'},
                           axis='index', inplace=True)
    df_unemployment.rename({'July_umemployment': 'July'},
                           axis='index', inplace=True)
    df_unemployment.rename({'August_umemployment': 'August'},
                           axis='index', inplace=True)
    df_unemployment.rename({'Septembe_umemployment': 'September'},
                           axis='index', inplace=True)
    df_covid.plot(title=county + ' infection rate',
                  xlabel='Month',
                  ylabel='Rate %')
    df_unemployment.plot(title=county + ' unemployment rate',
                         xlabel='Month',
                         ylabel='Rate %')
