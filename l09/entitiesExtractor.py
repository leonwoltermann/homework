import re
import os
import json

directory = "./xml-json-converter/data/"

#iterate through all files
files = os.listdir(directory)

#sort files 
filesSorted = sorted(files)

#the final dict which contains all the information for the export
dispatchDict = {}

globalCounter = 0

for filename in filesSorted: #start from 1 because of the ds_store file
    
    #skips invisible files
    if filename.startswith("dltext"): #or: if not filename.startswith("."): 

        with open(f"{directory}{filename}", "r") as file:
        
            #to check that the script goes through every file
            print(filename)

            #the raw data of every file
            raw = file.read()
            
            #extract the date
            date = re.search(r'<date value="([-\d]+)"', raw).group(1)
            
            #counts the iterations
            counter = 0

            countMissedTypes = 0
            countMissedHeaders = 0

            #splits the raw data in articles (or items)
            for article in re.split("<div3", raw)[1:]:
                
                globalCounter += 1
                
                counter += 1

                article = "<div3" + article

                #id:
                articleID = date + "-" + str(globalCounter)
