import re
import os

directory = "./data/"

#iterate through all files
files = os.listdir(directory)

#sort files 
filesSorted = sorted(files)

simpleTagsList = []

globalCounter = 0

for filename in filesSorted: #start from 1 because of the ds_store file
    print(filename)

    #skips invisible files
    if filename.startswith("dltext"): #or: if not filename.startswith("."): 

        with open(f"{directory}{filename}", "r") as file:
        
            #to check that the script goes through every file

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

                #< ?\w+ (\w+=\"(\w+|\d+)\"+)>

                #entities = re.findall(r"<[^<]+>", article)
                
                #simpleTags = re.findall(r"<[^<]+>", article)

                simpleTags = re.findall(r"<[^<> ]+(?= |>)", article)

                cleanSimpleTags = []  

                for i in simpleTags:
                    i = re.sub("<|/|>", "", i)
                    cleanSimpleTags.append(i)

                res = []

                [res.append(x) for x in cleanSimpleTags if x not in res]

                for i in res:
                    simpleTagsList.append(i)

    cleanedSimpleTagsList = []    
    [cleanedSimpleTagsList.append(x) for x in simpleTagsList if x not in cleanedSimpleTagsList]    
        

with open("simpleTags.csv", "w") as output:
    for tag in cleanedSimpleTagsList:
        output.write(tag + "\n")