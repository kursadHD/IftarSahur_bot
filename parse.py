import requests
import json
import sys

if len(sys.argv) > 1:
    country = sys.argv[1]
else:
    country = input('Ülke giriniz: ')

_resp = requests.get('https://namazvakitleri.diyanet.gov.tr/assets/locations/countries.json')
country_list = [c['CountryName'] for c in _resp.json()]
print(country_list)
if country.upper() not in country_list:
    print('Ülke bulunamadı!')
    sys.exit(1)

resp = requests.get('https://namazvakitleri.diyanet.gov.tr/assets/locations/{}.json'.format(country))
_dict = {i['City']: str(i['CityID']) for i in resp.json()}

idjson = json.load(open('ilceid.json'))
idjson.update({country.upper(): _dict})

json.dump(idjson, open('ilceid.json', 'w'), indent=4)

print('İşlem tamamlandı!')