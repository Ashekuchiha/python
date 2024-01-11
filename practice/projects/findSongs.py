import requests
import sys

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={sys.argv[2]}&term={sys.argv[1]}")
#print(response.json())
output = response.json()
for result in output["results"] :
    print(f"{result['trackName']}")