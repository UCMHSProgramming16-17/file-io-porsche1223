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
csvwriter.writerow(['Date', 'Weather', 'Location = ' + place])

#making life slightly easier
answer = input("Would you like to keep the time the same? ")

if answer == "yes":
    time1 = input("Insert time in the following format: [HH]:[MM]:[SS]. ")
    time1 = time1.lower()
    
else:
    time1 = input("Too bad. What is the time you would like to use? Same format applies. ")
    
time2 = input("What is your birthdate? Exclude the year. The format is: [MM]-[DD]. ")
time3 = int(input("Pick a start year. "))
time4 = int(input("How many years' worth of data would you like to see? "))

#making life extremely easy
for x in range(time4):
    endpoint = "https://api.darksky.net/forecast/"
    key_darksky = "5b9e1c711f845dcbd163771bfa1793a7"
    darkskyurl = endpoint + key_darksky + '/' + str(lat) + ',' + str(lon) + ',' + str(time3) + '-' + str(time2) + 'T' + str(time1)
    darkskyrequest = requests.get(darkskyurl)
    weather = darkskyrequest.json()
    csvwriter.writerow([time2 + '-' + str(time3), weather["hourly"]["icon"]])
    time3 += 1
   
#close file
file.close()

