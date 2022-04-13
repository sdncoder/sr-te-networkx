import csv
#f = open('sr-te-variables.csv')
#csv_f = csv.reader(f)
#for row in csv_f:
#    jada=row
#    print(row)


with open("sr-te-variables.csv") as csvFile:   #open the file
  CSVdata = csv.reader(csvFile, delimiter=',')  #read the data
  for row in CSVdata:   #loop through each row
    weight = row[1]
#GA.add_edge('ja', 'da', weight=row[1])
#GA.add_edge('ja', 'ta', weight=row[2])
#GA.add_edge('la', 'da', weight=row[3])
    print (weight)   #print the data
csvFile.close()   #close the file

#    GA.add_edge('ja', 'da', weight=10)
#    GA.add_edge('ja', 'ta', weight=200)
#    GA.add_edge('la', 'da', weight=10)
