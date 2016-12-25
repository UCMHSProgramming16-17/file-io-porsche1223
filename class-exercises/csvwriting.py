#import module
import csv

#create a file
file = open('morecsvwriting.csv', 'w')

#create csvwriter
csvwriter = csv.writer(file, delimiter=',')

#write information
csvwriter.writerow(['amanda', 'richard', 'kayleen', 'ktong', 'sabina', 'nika'])

#close file
file.close()