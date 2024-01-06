
#outsude pip install packageName
import cowsay
import requests

#local library
import sys

cowsay.cow("hi "+sys.argv[1])
i=1
# response = requests.get("http://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])
response = requests.get(f"http://itunes.apple.com/search?entity=song&limit={sys.argv[2]}&term={sys.argv[1]}")
output = response.json()
for result in output["results"] :
    print(i,result["trackName"])
    i+=1
