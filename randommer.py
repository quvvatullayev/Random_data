import requests
import json

def test():
    url = 'https://randommer.io/api/Card'
    r = requests.get(url, headers={'X-API-KEY':'3ad41b2a1ece4d749d0e240af917af2d'})
    r1 = r.json()
    return r1

x = test()
with open('json_file.json', 'w') as f:
    json.dump(x, f, indent=2)