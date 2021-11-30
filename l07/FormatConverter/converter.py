import csv

def csv_to_dict_1(file):
    with open(file, mode="r") as file:
        reader = csv.reader(file, delimiter = "\t")
        next(reader)
        settlements = {}
        for row in reader:
            settlements[row[0]] = {"settlement_id":row[0], "languages":row[1], "names_ara_common":row[2],
            "names_ara_common_other":row[3], "names_eng_search":row[4], "names_eng_translit":row[5], 
            "names_eng_translit_other":row[6], "region_URI":row[7], "source":row[8], "top_type":row[9],
            "coordinates":row[10]}
        return(settlements)

def csv_to_dict_2(file):
    with open(file) as file:
        reader = csv.DictReader(file, delimiter = "\t")
        settlements = {}
        for row in reader:
            settlements[row["settlement_id"]] = row
    return(settlements)

def createXml1(file):
    with open(file, "r") as f1:
        data = f1.read().strip().split("\n")

        header = data[0].split("\t")

        allData = []

        for d in data[1:]:
            tags = d.split("\t") 
            tempVar = ["<"+tags[0]+">"]
            
            for i in range(1, len(header)):
                item = "\t<%s>%s</%s>" % (header[i], tags[i], header[i])
                tempVar.append(item)
            
            tempVar.append("</"+tags[0]+">")
            tempVarFinal = "\n".join(tempVar)

            allData.append(tempVarFinal)
    reallyfinaldata = "\n\n".join(allData)
    with open (file.replace(".csv", ".xml"), "w", encoding="utf8") as f9:
        f9.write(reallyfinaldata)

def createXml2(file):
    with open(file, "r") as f1:
        data = f1.read().strip().split("\n")

        header = data[0].split("\t")

        allData = []

        for d in data[1:]:
            tags = d.split("\t") 
            tempVar = ["<settlement>"]
            
            for i in range(0, len(header)):
                item = "\t<%s>%s</%s>" % (header[i], tags[i], header[i])
                tempVar.append(item)
            
            tempVar.append("</settlement>")
            tempVarFinal = "\n".join(tempVar)

            allData.append(tempVarFinal)
    reallyfinaldata = "\n\n".join(allData)
    with open ("settlements1.xml", "w", encoding="utf8") as f9:
        f9.write(reallyfinaldata)

def createJson(dict):
    import json 
    with open("sample.json", "w") as jsonFile:
        json.dump(dict, jsonFile, indent=4, ensure_ascii=False)

def createYaml(file):
    with open(file, "r") as f1:
        data = f1.read().strip().split("\n")

        header = data[0].split("\t")

        allData = []

        for d in data[1:]:
            temp = d.split("\t")
            tempVar = [temp[0]+":"]
            


            for i in range(1, len(header)):
                item = "\t%s: %s" % (header[i], temp[i])
                tempVar.append(item)

            tempVarFinal = "\n".join(tempVar)

            allData.append(tempVarFinal)
    reallyfinaldata = "\n\n".join(allData)
    with open (file.replace(".csv", ".yml"), "w", encoding="utf8") as f9:
        f9.write(reallyfinaldata)

def main():
    csv_to_dict_1("settlements.csv")
    csv_to_dict_2("settlements.csv")
    createXml1("settlements.csv")
    createXml2("settlements.csv")
    createJson(csv_to_dict_2("settlements.csv"))
    createYaml("settlements.csv")

main()