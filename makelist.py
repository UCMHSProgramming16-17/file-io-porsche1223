#open a file
file = open('mylist.txt', 'w')

#add items to file
for x in range(10):
    file.write(str(x + 1) + '. ' + input("What should I add to list? ") + '\n')

#close file    
file.close()