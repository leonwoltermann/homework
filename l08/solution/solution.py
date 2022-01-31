import re
import os

source = "./Data/"
target = "./Dispatch_Processed/"  # needs to be created beforehand!

lof = os.listdir(source)
counter = 0  # general counter to keep track of the progress

#iterates through list of items in folder "source"
for f in lof:
    #gets active when item starts with dltext
    if f.startswith("dltext"):  # fileName test
        #splits string at ":"
        newF = f.split(":")[-1] + ".yml"  # in fact, yml-like
        
        #creates list
        issueVar = []
        #opens file with path
        with open(source + f, "r", encoding="utf8") as f1:
            text = f1.read()
            #extract the date from date value tag
            date = re.search(r'<date value="([\d-]+)"', text).group(1)
            #splits xml at div3 tag
            split = re.split("<div3 ", text)

            #iterates through the elements which were splitted on the div3 tag
            for s in split[1:]:
                #restores the div3 tag
                s = "<div3 " + s  # a step to restore the integrity of each item
                #if regex function returns true it assigns the type of the item to var unittype
                try:
                    unitType = re.search(r'type="([^\"]+)"', s).group(1)
                #if regex function returns false then there is no type and the string "noType is assigned to va unittype"
                except:
                    unitType = "noType"

                #if there is a header then it is assignes to header
                try:
                    header = re.search(r'<head.*</head>', s).group(0)
                    header = re.sub("<[^<]+>", "", header)

                #if there is no header string "no header" is assignes instead
                except:
                    header = "NO HEADER"

                #cleans text
                text = s
                text = re.sub("<[^<]+>", " ", text)
                text = re.sub(" +\n|\n +", "\n", text)
                text = text.strip()
                text = re.sub("\n+", ";;; ", text)
                text = re.sub(" +", " ", text)
                text = re.sub(r" ([\.,:;!])", r"\1", text)

                #creates itemID for every unit
                itemID = "ID: " + date + "_" + unitType + "_%03d" 

                #gets active when unit has some characters
                if len(re.sub("\W+", "", text)) != 0:
                    #preperation for yaml conversion
                    #adds string to item id
                    itemIdvar = "ID: " + itemID
                    #adds string to date
                    dateVar = "DATE: " + date
                    #adds string to type
                    unitType = "TYPE: " + unitType
                    #adds string to header
                    header = "HEADER: " + header
                    # @§@ is used to replace ":", because in YML : is used as a divider between the key and value
                    text = "TEXT: " + text.replace(":", "@§@") + "\n\n"
                    #every part of the unit is merged and assigned to var "var"
                    var = "\n".join(
                        [itemIdvar, dateVar, unitType, header, text])

                    #var "var" is assigned to issueVar
                    issueVar.append(var)

        issueNew = "".join(issueVar)
        with open(target + newF, "w", encoding="utf8") as f9:
            f9.write(issueNew)

        counter += 1
        if counter % 100 == 0:
            print(counter)