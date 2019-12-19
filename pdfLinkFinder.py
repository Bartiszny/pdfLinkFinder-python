import PyPDF2
import re

def find(string):
    """source: https://www.geeksforgeeks.org/python-check-url-string/"""
    # findall() has been used  
    # with valid conditions for urls in string 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                     string) 
    return url


pdf = PyPDF2.PdfFileReader('Maciej_Aniserowicz-Zawod_Programista.pdf')

num =pdf.getNumPages()

print("Total number of pages : ",num)
print("URLs with correspodning page numbers: ")

for i in range(num):
    page = pdf.getPage(i)
    txt = page.extractText()
    url = find(txt)
    if url:
        print(url,i)


    
