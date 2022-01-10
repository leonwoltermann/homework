import re
import os
import json

directory = "./data/"

#iterate through all files
files = os.listdir(directory)

#sort files 
filesSorted = sorted(files)

globalCounter = 0

tagFreqArticle = {}
tagFreqFile = {}

for filename in filesSorted: #start from 1 because of the ds_store file
    print(filename)

    #skips invisible files
    if filename.startswith("dltext"): #or: if not filename.startswith("."): 

        with open(f"{directory}{filename}", "r") as file:
        
            #to check that the script goes through every file

            #the raw data of every file
            raw = file.read()

            tagFreqFile[filename] = {}
            with open("simpleTags.csv", "r") as tagsFile:
                tagsRaw = tagsFile.read()
                tags = tagsRaw.split("\n")
                for tagFile in tags:
                    freqFile = raw.count(tagFile)
                    tagFreqFile[filename][tagFile] = freqFile
            
            #extract the date
            date = re.search(r'<date value="([-\d]+)"', raw).group(1)
            
            #counts the iterations
            counter = 0

            #splits the raw data in articles (or items)
            for article in re.split("<div3", raw)[1:]:
                

                globalCounter += 1

                article = "<div3" + article

                #id:
                articleID = date + "-" + str(globalCounter)
                
                tagFreqFile[filename][articleID] = {}
                

                for tagArticle in tags:
                    freqArticle = article.count(tagArticle)
                    tagFreqFile[filename][articleID][tagArticle] = freqArticle


with open("tagsFreq1.json", "w") as output:  
    json.dump(tagFreqFile, output, indent=4)


                        

