#analyzes character relationships


import re, itertools
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import csv


#open cleaned text file
with open("tango&sadimin_Clean.md", "r", encoding="utf8") as f1:
    text = f1.read()

#split chapters 
chapters = re.split("\#\#|\n\n", text)



#define the nodes or characters for the network
characterlist = ["nini randa","tango","sadimin","nah","dana","samijan","ozog","mono","misbah","nyai", "salamah", "karim","nyonya samijan"]

#var which counts chapters in the loops
chaptercount = 0

#creating a dictionary
character_assoc_dictionary = dict()

#loop which iterates through all elements in the list named chapters begining from index 1
for chapter in chapters[1:]:
    #crates list which will include appearances of characters in chapter
    appears = []
    #adds one to integer var chaptercount
    chaptercount += 1
    #counts appearances of all characters in a chapter
    counter = 0
    #iterates through all characters in characterlist
    for character in characterlist:
        #regex function which searches for matches of the character (also if character appears for of after certain symbols)
        match = re.search(rf"[ |,|.|?|!|\"]{character}[ |,|.|?|!|\"]", chapter)
        #if statement gets active when regex function returns true
        if match:
            #appends character name to appears list
            appears.append(character)
        #if statement gets active when regec function returs False
        elif match == None:
            #adds 1 to counter from line 33
            counter += 1
            #nested if clause which gets activated when the counter is 13 which implies that none of the characters in the list appear in the chapter
            if counter == 13:
                #appends none to appears list
                appears.append("None")
    #creater a list with all possible combination between all characters
    relationships = itertools.combinations(sorted(appears),2)
    #print(list(relationships))

    #loop which iterates trough all possible relationships
    for relationship in relationships:
        #if clause gets active when there already is an entry of current relationship in the dict
        if relationship in character_assoc_dictionary:
            #adds an entry to the dict with relationship as key and +=1 as value
           character_assoc_dictionary[relationship] += 1
        #clause gets active when there is no entry of the currect relationship
        else:
            #adds entry to dict with realtionship as key and =1 as value
            character_assoc_dictionary[relationship] = 1

#assigns g to function
g = nx.Graph()

#iterates through all characters in list
for character in characterlist:
    #adds node for all characters to network
   g.add_node(character)

#iterates through all relationships (as edges) and their weight
for edge, weight in character_assoc_dictionary.items():
    #adds edge for all relationships and weigths to network
   g.add_edge(edge[0], edge[1], weight=weight)



#creates dataframe of the dict character_assoc_dictionary
df = pd.DataFrame(list(character_assoc_dictionary.items()),columns=["connection", "weight"])

#exports dataframe to csv
df = df.to_csv('networkParagraph.csv',sep='\t')




