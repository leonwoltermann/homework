#imports csv library
import csv
#imports json librabry
import json

#defines the function which converts tsv to json
def converter_tsv_to_json(file):
    #opens the file (which takes the place of the variable 'file') an gives it the variable name 'f1'
    with open(file) as f1:
        #the csv.DictReader function automatically reads the csv/tsv as a dictionary
        #reader is the variable name for the csv.DictReader
        #f1 is the variable name for the file
        #delimiter is the sign which is used to split columns and here is defines as a tab
        reader = csv.DictReader(f1, delimiter="\t")
        #creates a the dictionary with the variable name settlements
        settlements = {}
        #loop which iterates through every row in the reader (which is the variable for the csv.DictReader of the file which is assignes to the variable 'file')
        for row in reader:
            #since the csv.DictReader already reads the file as a dictctionary, every row is already a dictionary itself
            #this line makes of every row an entry (with the id settlement_id) of the dictionary named 'settlements'
            #this all is assigned to the variable row which then represents the row as an entry of the dictionary 'settlements' where every column is an entry of the dictionary of the row
            #a dictionary of dictionaries
            settlements[row["settlement_id"]] = row
    #opens the file with the variable 'file' in the writing modus ('w'), replaces the .csv extension with a .json extension and assigns the renamed file to the variable f9
    with open(file.replace(".csv", ".json"), "w") as f9:
        #json.dump function (from json library) transforms the dictionary 'settlements' into the json format and writes it into the file with the variable f9
        #indent makes it more human readable but takes memory as well
        #ensure_ascii is set to false, so that the unicode characters are also deciphered  
        json.dump(settlements, f9, indent=4, ensure_ascii=False)

#defines the function which converts tsv to yml
def converter_tsv_to_yml(file):
    #opens the file (which takes the place of the variable 'file') an gives it the variable name 'f1'
    with open(file) as f1:
    #does the same thing as previous line, the difference is that the encoding and the opening method are defined
    with open(file, "r", encoding="utf8") as f1:
        #the read() function reads the file as a plain text
        #the strip() function deletes whitespace at the beginning and the end
        #the split() function splits the plain text at the definied value which here is '\n' (a new line) and creates a list of the splitted elements
        data = f1.read().strip().split("\n")
        #date[0] is the first line in the file which is then splitted at the ’\t‘ (tab) 
        #every column then is a element of a list called 'header'
        header = data[0].split("\t")
        #creates a list with the name 'allData'
        allData = []
        #loop which iterates through all lines in the file, except the first line
        for d in data[1:]:
            #splits the line at the '\t' and creates a list of the splitted elements
            temp = d.split("\t")
            #takes the first element of the list 'temp' adds a colon and assign it to the list named 'tempVar'
            tempVar = [temp[0]+":"]
            #loop which iterates through a range of integers from zero to the length of the header (which is the number of columns in the file)
            for i in range(0, len(header)):
                #formats the ith element of the list header and the ith element of the list temp and assign it to the variable 'item'
                item = "\t%s: %s" % (header[i], temp[i])
                #appends the value of the variable 'item' to the list 'tempVar'
                tempVar.append(item)
                #combines all items of the list 'tempVar', puts a new line between every element and creates a string
            tempVarFinal = "\n".join(tempVar)
            #appends the string with the variable 'tempVarFinal to the list named 'allData'
            allData.append(tempVarFinal)
    #creates a string of the list 'allData' and puts two lines between every element
    ReallyFinalData = "\n\n".join(allData)

    #opens the file 'file', replaces the .csv with a .yml extension and assigns it to the variable f9
    #w stands for writing method
    with open(file.replace(".csv", ".yml"), "w", encoding="utf8") as f9:
        #writes the string ReallyFinalData into the openend file
        f9.write(ReallyFinalData)


#defines the function converter_tsv_to_xml
def converter_tsv_to_xml(file):
    #opens 'file' and assigns to the variable f1
    with open(file) as f1:
        #the csv.DictReader function automatically reads the csv/tsv as a dictionary
        #reader is the variable name for the csv.DictReader
        #f1 is the variable name for the file
        #delimiter is the sign which is used to split columns and here is defines as a tab
        reader = csv.DictReader(f1, delimiter="\t")
        #creates a list named 'data'
        data = []
        #iterates through every row in the value assigned to reader (which is already a dictionary because of the DictReader function)
        for row in reader:
            #creates a list named 'temp'
            temp = []
            #the .items() method returns a list of tuple pairs (key, value) of a dictionary
            #therefore it iterates through keys 'k' and values 'v' of every row
            for k, v in row.items():
                #formats the keys and values and appends it to the list 'temp'
                temp.append("<%s>%s</%s>" % (k, v, k))
            #combines elements of list 'temp' to a string
            #formats it and assigns it to the variable tempComplete
            tempComplete = "<settlement>\n\t%s\n</settlement>" % "\n\t".join(
                temp)
            #appens the value of the variable tempComplete to the list named 'data'
            data.append(tempComplete)
    #combined all elements of the list data to a string with the variable ReallyFinalData and puts two blank lines between every element
    ReallyFinalData = "\n\n".join(data)
    #opens file 'file' and replaces .csv with a .xml extension
    #assigns it to the variable f9
    with open(file.replace(".csv", ".xml"), "w", encoding="utf8") as f9:
        #writes the string assigned to ReallyFinalData into the file assigned to F9
        f9.write(ReallyFinalData)

#calls the function named converter_tsv_to_json where 'settlements.csv' is the value assigned to the variable 'file' inside the function
converter_tsv_to_json("settlements.csv")
#same as above but different function
converter_tsv_to_yml("settlements.csv")
#same as above but different function
converter_tsv_to_xml("settlements.csv")