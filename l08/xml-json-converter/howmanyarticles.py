import re
import os
import json

directory = "./data/"

#iterate through all files
files = os.listdir(directory)

#sort files 
filesSorted = sorted(files)

counter = 0

for filename in filesSorted: #start from 1 because of the ds_store file
    
    #skips invisible files
    if filename.startswith("dltext"): #or: if not filename.startswith("."): 

        with open(f"{directory}{filename}", "r") as file:
        
            #to check that the script goes through every file
            print(filename)

            #the raw data of every file
            raw = file.read()
            
            for article in re.split("<div3", raw)[1:]:
                counter += 1


print(counter)