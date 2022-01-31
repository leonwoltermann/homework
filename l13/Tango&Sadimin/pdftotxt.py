#from pdfminer.high_level import extract_text
import PyPDF2

#opens file
pdffileobj=open('Tango & Sadimin.220219.pdf','rb')

#reads file
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
#method which returns amount of pages is assigned to var x
x=pdfreader.numPages
#gets the code from pdf for every page
pageobj=pdfreader.getPage(x+1)
#extract text from page
text=pageobj.extractText()


#file = "Tango & Sadimin.220219.pdf"
#text = extract_text(file)

#writes string to file
with open("tango&sadimin2.txt", "w") as f:
    f.write(text)

