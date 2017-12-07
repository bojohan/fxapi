import requests
from pprint import pprint


def fxload():
    response = requests.get('https://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/json?start_date=2017-01-03')
    data = response.json()

    print 'log: get files'

    return data['observations'][-1]


def fxdata():

    try:
        jsondata = fxdata.data
    except AttributeError:
        fxdata.data = fxload()
        jsondata = fxdata.data


    return jsondata



