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

                #type:
                typeRaw = re.search("<div3[^<]+>", article).group(0)
                if re.search(r'type="([^"]+)"', typeRaw) == None:
                    textType = "none"
                    countMissedTypes += 1
                else:
                    textType = re.search(r'type="([^"]+)"', typeRaw).group(1)
        
                #header
                if re.search(r'<head(.*)?>(.*)</head>', article) != None:
                    header = re.search(r'<head(.*)?>(.*)</head>', article).group(0)
                    header = re.sub("<[^<]+>", " ", header)
                    header = re.sub(" +", " ", header)
                    header = re.sub(" \.", ".", header)
                else:
                    header = "none"

                #if re.search(r'<head(.*)?>(.*)</head>', article).group(0) == None:
                #header = "none"
                #countMissedHeaders += 1


                #article cleaning:
                article = re.sub("<[^<]+>", " ", article)
                article = re.sub("\n*", "", article)
                article = re.sub("/\s\s+/g", "", article)
                article = re.sub("type=\"(article|advert|news)\" n=\".*\" org=\"(composite|uniform)\" sample=\"complete\">", 
                "", article)
                article = re.sub(" +", " ", article)
            
                #create dict for article
                #articleDict = {}

                #add filename, header, date, texttype, and text to the articleDict
                #articleDict.update({"file": filename, "header": header, "date": date, "type": textType, "text": article})

                dispatchDict[articleID] = {"file": filename, "header": header, "date": date, "type": textType, "text": article}

                #add the article dict with the articleID to the main dict
                #dispatchDict.update({articleID: articleDict})
                
with open("dispatch.json", "w") as jsonFile:
    json.dump(dispatchDict, jsonFile, indent=4)

print("splitted elements: ", globalCounter)
elementsinDict = len(dispatchDict.keys())
print("dict entries: ", elementsinDict)
print("Difference between splitted elements and dictionary entries: ", globalCounter - elementsinDict)

