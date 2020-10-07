# dumpPDFTotxt.py dump PDF data text into a .txt file.
# Get filename from console.

import PyPDF2,sys

if len(sys.argv) > 1:
    # Get arguments from command line.
    dataPdf = sys.argv[1:][0]
else:
    print("Please, introduce existing filename in command lines")
    sys.exit(1)

pdfFileObj = open(dataPdf, "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
stream=''
for numPage in range(0, pdfReader.getNumPages()):
    pageObj = pdfReader.getPage(numPage)
    stream+=pageObj.extractText()+'\n'

dumpDataFile= open('dump.txt','w')
# write txt file
dumpDataFile.write(stream)
dumpDataFile.close()
