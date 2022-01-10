import re
import os

source = "./data/"
target = "./processedData/"  # needs to be created beforehand!

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

for f in lof:
    if f.startswith("dltext"):  # fileName test
        newF = f.split(":")[-1] + ".yml"  # in fact, yml-like

        issueVar = []
        c = 0  # technical counter
        with open(source + f, "r", encoding="utf8") as f1:
            text = f1.read()
            date = re.search(r'<date value="([\d-]+)"', text).group(1)
            split = re.split("<div3 ", text)

            for s in split[1:]:
                c += 1
                s = "<div3 " + s  # a step to restore the integrity of items

                try:
                    unitType = re.search(r'type="([^\"]+)"', s).group(1)
                except:
                    unitType = "noType"

                try:
                    header = re.search(r'<head.*</head>', s).group(0)
                    header = re.sub("<[^<]+>", "", header)

                except:
                    header = "NO HEADER"

                text = s
                text = re.sub("<[^<]+>", " ", text)
                text = re.sub(" +\n|\n +", "\n", text)
                text = text.strip()
                text = re.sub("\n+", ";;; ", text)
                text = re.sub(" +", " ", text)
                text = re.sub(r" ([\.,:;!])", r"\1", text)

                itemID = date + "_" + unitType + "_%03d" % c

                if len(re.sub("\W+", "", text)) != 0:
                    itemIdvar = "ID: " + itemID
                    dateVar = "DATE: " + date
                    unitType = "TYPE: " + unitType
                    header = "HEADER: " + header
                    # @§@ is used to replace ":", because in YML : is used as a divider between the key and value
                    text = "TEXT: " + text.replace(":", "@§@") + "\n\n"
                    var = "\n".join(
                        [itemIdvar, dateVar, unitType, header, text])

                    issueVar.append(var)

                    # NOW, WE CAN ADD SOME CODE TO PROCESS EACH ITEM AND COLLECT ALL INTO OUR TIDY DATA FORMAT
                    # STRUCTURE: itemID, dateVar, EXTRACTED_ITEM (type, unified_form, id)
                    # ADDING TO: entities (list)

                    for i in re.findall(r"(<\w+[^>]+>)", s):
                        if "persName" in i and "authname" in i and "n=" in i:
                            # input(i)
                            itemType = "persName"
                            itemUnified = re.search(r'n="([^"]+)"', i).group(1)
                            itemId = re.search(
                                r'authname="([^"]+)"', i).group(1)

                            tempVar = "\t".join(
                                [itemID, date, itemType, itemUnified, itemId])
                            entities.append(tempVar)

                            # print(i)
                            # input(tempVar)

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
                        else:
                            pass

        issueNew = "".join(issueVar)
        with open(target + newF, "w", encoding="utf8") as f9:
            f9.write(issueNew)

        # count processed issues and print progress counter at every 100
        counter += 1  # counter = counter + 1
        # if counter is divisible by 100 (i.e., no remainder), then print it
        if counter % 100 == 0:
            print(counter)

header = "\t".join(["itemID", "date", "itemType", "itemUnified", "itemId"])
entitiesTest = header + "\n" + "\n".join(entities).lower()
with open("entities.csv", "w", encoding="utf8") as f9:
    f9.write(entitiesTest)

print("Done!")