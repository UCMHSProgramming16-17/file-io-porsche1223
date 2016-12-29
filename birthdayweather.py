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

answer = input("Would you like to keep the time the same? ")

if answer == "yes":
    time1 = input("Insert time in the following format: [HH]:[MM]:[SS]. ")
    
else:
    time1 = input("Too bad. What is the time you would like to use? Same format applies. ")

for x in range(10):
    endpoint = "https://api.darksky.net/forecast/"
    key_darksky = "5b9e1c711f845dcbd163771bfa1793a7"
    time2 = input("Pick any point in time in the past. The format is [YYYY]-[MM]-[DD]. Brackets are not required. ")
    darkskyurl = endpoint + key_darksky + '/' + str(lat) + ',' + str(lon) + ',' + str(time2 + 'T' + time1)
    darkskyrequest = requests.get(darkskyurl)
    weather = darkskyrequest.json()
    csvwriter.writerow([time2, weather["hourly"]["summary"]])
   
#close file
file.close()

