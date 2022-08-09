import requests

KEY = '7b88e90dfad2f86bf250b0ac388176ec'
LINK_1 = 'http://136.244.93.168/admin_api/v1/clicks/log'

headers = {'Api-Key': f"{KEY}", 'accept': 'application/json'}

a = {
    "limit": 2,
    "offset": 0,
    # "filters": [
    #   {
    #     "name": "ID",
    #     "operator": "bogdan",
    #   }
    # ],
}

r = requests.post(LINK_1, headers=headers, data=a)
print(r.json())
clicks_dict = r.json()
total = clicks_dict.get('total')
print(total)
