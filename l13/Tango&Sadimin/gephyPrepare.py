import pandas as pd
import re

#opens file
with open("networkParagraph.csv", "r") as f1:
    raw = f1.read()
    #splits list by lines
    characterlist = raw.split("\n")

#creates empty dataframe with three columns
df = pd.DataFrame(columns=["source", "target", "weight"])
#creates empty dataframe with one column
df1 = pd.DataFrame(columns=["source"])

#iterates through lines from index 1
for row in characterlist[1:]:
    #splits the lines at a tab
    splittedrow = row.split("\t")
    #assigns the second items to var connection and converts it to string
    connection = str(splittedrow[1:2])
    #cleans the string
    connectionClean = re.sub("\(|\)|\[|\]|\"", "", connection)
    #assigns part of the string to var source
    source = re.sub("(, \'\w* ?\w*?\')", "", connectionClean)
    #cleans var source
    source = re.sub("\'", "", source)
    #assigns part of the string to var target
    target = re.sub("(\'\w* ?\w*?\'\, )", "", connectionClean)
    #cleans var target
    target = re.sub("\'", "", target)
    #assigns third item to var weight and transforms it into string
    weight = str(splittedrow[2:3])
    #cleans string
    weight = re.sub("\'|\[|\]", "", weight)
    #if clause gets active is isdigit function returns true
    if weight.isdigit():
        #converts string weight into integer and assigns value to var a
        a = int(weight)
    #creates format for new row
    newrow = {"source":source, "target": target, "weight": a}
    #creates format for new row
    newrow1= {"character":source}
    #appends new row
    df = df.append(newrow, ignore_index=True)
    #appends new row
    df1 = df1.append(newrow1, ignore_index=True)
  
#writes dataframe to a file
df = df.to_csv('Tango&Sadimin_NetworkParagraph.csv',sep='\t', index=False)

#df1 = df1.to_csv('Tango&Sadimin_characters.csv',sep='\t')