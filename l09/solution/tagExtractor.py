import re
import os
from typing import Text

from sympy import S

source = "./data/"
target = "./processedData/"  # needs to be created beforehand!

#function returns a list of the names of items in the folder "source" and assigns it to var lof
lof = os.listdir(source)
counter = 0  # general counter to keep track of the progress

"""
1. Analyze categories of tagged data:
    - <persName> (552,453); <placeName> (402,419); <orgName> (164,988); <rs> (353,521) /https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-rs.html/; 
    - How to determine these?!
        - Advice: always check whether the tagging is actually good;
        - if there is no tagging (or it is not reliable), alternative methods must be used to extract your data (named entity recognition)
2. Extract tagged data in those categories
    - data format: ID, date, item (item may take more than one column)
3. as a starting point, we can use the script with which we reformatted the data from the Dispatch into other formats
"""

entities = []  # we will collect all extracted data here

#iterates through list of items in folder "source"
for f in lof:
    #gets active when item starts with dltext
    if f.startswith("dltext"):  # fileName test
        #splits string at ":"
        newF = f.split(":")[-1] + ".yml"  # in fact, yml-like

        #creates list
        issueVar = []
        c = 0  # technical counter
        #opens file with path
        with open(source + f, "r", encoding="utf8") as f1:
            text = f1.read()
            #extract the date from date value tag
            date = re.search(r'<date value="([\d-]+)"', text).group(1)
            #splits xml at div3 tag
            split = re.split("<div3 ", text)

            #iterates through the elements which were splitted on the div3 tag
            for s in split[1:]:
                #adds 1 to counter in line 9
                c += 1
                #restores the div3 tag
                s = "<div3 " + s  # a step to restore the integrity of items

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
                text = re.sub("<[^<]+>", " ", text)
                text = re.sub(" +\n|\n +", "\n", text)
                text = text.strip()
                text = re.sub("\n+", ";;; ", text)
                text = re.sub(" +", " ", text)
                text = re.sub(r" ([\.,:;!])", r"\1", text)



                #creates itemID for every unit
                itemID = date + "_" + unitType + "_%03d" % c

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


                    # NOW, WE CAN ADD SOME CODE TO PROCESS EACH ITEM AND COLLECT ALL INTO OUR TIDY DATA FORMAT
                    # STRUCTURE: itemID, dateVar, EXTRACTED_ITEM (type, unified_form, id)
                    # ADDING TO: entities (list)

                    #iterates through all tags inside a unit (splitted on div3 tag)
                    for i in re.findall(r"(<\w+[^>]+>)", s):
                        #gets active when the three strings are inside element i
                        if "persName" in i and "authname" in i and "n=" in i:
                            # input(i)
                            #string assigned to var
                            itemType = "persName"
                            #regex function returns itemtype and assigns it to vat
                            itemUnified = re.search(r'n="([^"]+)"', i).group(1)
                            #regex function returns itemtype and assigns it to var
                            itemId = re.search(
                                r'authname="([^"]+)"', i).group(1)

                            #all values of vars are merged and assigned to one var
                            tempVar = "\t".join(
                                [itemID, date, itemType, itemUnified, itemId])
                            #var appended to entities list
                            entities.append(tempVar)

                            # print(i)
                            # input(tempVar)
                        
                        #same thing as before just with place instead of person
                        elif "placeName" in i and "authname" in i and "reg=" in i:
                            # input(i)
                            itemType = "placeName"
                            itemUnified = re.search(
                                r'reg="([^"]*)"', i).group(1)
                            itemId = re.search(
                                r'authname="([^"]+)"', i).group(1)

                            tempVar = "\t".join(
                                [itemID, date, itemType, itemUnified, itemId])
                            entities.append(tempVar)

                            # print(i)
                            # input(tempVar)

                        #same thing as before just with organization instead of place
                        elif "orgName" in i and "type" in i and "n=" in i:
                            # print(i)
                            itemType = "orgName"
                            itemUnified = re.search(r'n="([^"]+)"', i).group(1)
                            itemId = re.search(
                                r'type="([^"]+)"', i).group(1)

                            tempVar = "\t".join(
                                [itemID, date, itemType, itemUnified, itemId])
                            entities.append(tempVar)

                            # print(i)
                            # input(tempVar)
                        
                        # if there is no organization name inside the element then the else statement gets active goes on to next line
                        else:
                            pass

        #list issuevar is merged and assigned to new var
        issueNew = "".join(issueVar)
        #writes issuenew to file
        with open(target + newF, "w", encoding="utf8") as f9:
            f9.write(issueNew)

        # count processed issues and print progress counter at every 100
        counter += 1  # counter = counter + 1
        print(counter)
        # if counter is divisible by 100 (i.e., no remainder), then print it
        #if counter % 100 == 0:
         #   print(counter)

#merges all the string with a tab in between and assigns it to var
header = "\t".join(["itemID", "date", "itemType", "itemUnified", "itemId"])
#combines header with entities list and assigns everything to var
entitiesTest = header + "\n" + "\n".join(entities).lower()
#writes string to file
with open("entities.csv", "w", encoding="utf8") as f9:
    f9.write(entitiesTest)


print("Done!")