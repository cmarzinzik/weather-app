from datetime import datetime, timedelta
import requests
import json
#my API key
apiToken = '508a278f88f9373234be3942c8748ee5/'
#base API url
apiUrl = 'https://api.darksky.net/forecast/'
#Longitude and Latitude for Sooke BC
longatude = '48.3742576,'
latitude = '-123.7388384'

apiUrl = apiUrl + apiToken +longatude + latitude

#Get information from API and turn it into a dictionary so we can search the json object
r = requests.get(url=apiUrl)
jsonOutput = json.loads(r.text)

#Parse time and date from the API and minus seven hours to account for the time zone difference
time = jsonOutput['currently']['time']
timeOutput = (datetime.fromtimestamp(time) - timedelta(hours=7)).strftime('%I:%M %p')
date = (datetime.fromtimestamp(time)- timedelta(hours=7)).strftime('%A %d %B')

#Parse weather data from the json
summary = jsonOutput['currently']['summary']
icon = jsonOutput['currently']['icon']
temp = jsonOutput['currently']['temperature']

#convert temperature to celcius
temp = (int(temp) - 32) * .5556

#display the data
print("On " + date + " at " + timeOutput + " it is currently " + summary + " and " + str(round(temp)) + " degrees celcius in Sooke BC Canada")