import urllib, json

url = "https://data.worldbank.org/indicator/SH.IMM.MEAS?locations=PA&start=2000&end=2019&view=chart"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print (data)