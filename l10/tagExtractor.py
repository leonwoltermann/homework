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

textList = []  # we will collect all extracted data here

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
                text = re.sub(r"\t", " ", text)

                if len(re.sub("\W+", "", text)) != 0:
                    
                 
                    itemID = date + "_" + unitType + "_%03d" % c

                    #wordsArticle = re.split("[,. -]", text)    
                    #for word in wordsArticle:
                    var = "\n".join([itemID, date, text])
                    issueVar.append(var)
                    tempVar = "\t".join([itemID, date, text])
                    textList.append(tempVar)
                        
        # count processed issues and print progress counter at every 100
        counter += 1  # counter = counter + 1
        # if counter is divisible by 100 (i.e., no remainder), then print it
        if counter % 100 == 0:
            print(counter)

headerList = "\t".join(["itemID", "date", "text"])
textListTest = headerList + "\n" + "\n".join(textList).lower()

with open("textList.csv", "w", encoding="utf8") as f9:
    f9.write(textListTest)

print("Done!")