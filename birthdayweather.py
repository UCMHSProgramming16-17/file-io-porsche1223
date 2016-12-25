#import module
import csv

#create a file
file = open('birthdayweather.csv', 'w')

#create csvwriter
csvwriter = csv.writer(file, delimiter=',')

#import requests
import requests

#other api stuff
place = input("Pick a place in the world. Be absolutely sure of this place, because you can't change it later. ")

gmapsurl = "https://maps.googleapis.com/maps/api/geocode/json"
payload = {"key":"", "address":place}

rgmaps = requests.get(gmapsurl, params = payload)
gmapsdata = rgmaps.json()


lat = gmapsdata['results'][0]['geometry']['location']['lat']
lon = gmapsdata['results'][0]['geometry']['location']['lng']

#api stuff
csvwriter.writerow(['Date', 'Weather'])

endpoint = "https://api.darksky.net/forecast/"
key_darksky = "5b9e1c711f845dcbd163771bfa1793a7"
time = input("Pick any point in time in the past. The format is [YYYY]-[MM]-[DD]. ")
darkskyurl = endpoint + key_darksky + '/' + str(lat) + ',' + str(lon) + ',' + time

for x in range(10):
    darkskyrequest = requests.get(darkskyurl, params = payload)
    weather = darkskyrequest.json()
    print(weather)
   
#close file
file.close()

