import PyPDF2

marksPDF = open('FIRSTSEMMARKS.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(marksPDF)

print(pdfReader.numPages)
pageObj = pdfReader.getPage(0) 
print(pageObj.extractText()) 
marksPDF.close() 
