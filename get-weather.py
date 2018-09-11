import requests
#my API key
apiToken = '508a278f88f9373234be3942c8748ee5/'
#base API url
apiUrl = 'https://api.darksky.net/forecast/'
#Longitude and Latitude for Sooke BC
longatude = '48.3742576,'
latitude = '-123.7388384'

apiUrl = apiUrl + apiToken +longatude + latitude
#Get information from API
r = requests.get(url=apiUrl)
#print the info
print(r.json())