##Extracting Text from PDFs
'''
PyPDF2 does not have a way to extract images, charts, or other media
from PDF documents, but it can extract text and return it as a Python string.
'''

import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb') #read binary mode since Pdf is binary data
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
19
pageObj = pdfReader.getPage(0)
pageObj.extractText()
'''
   OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of March 7,
   2015        \n     The Board of Elementary and Secondary Education shall
   provide leadership and create policies for education that expand opportunities
   for children, empower families and communities, and advance Louisiana in an
   increasingly competitive global market. BOARD  of ELEMENTARY and  SECONDARY
   EDUCATION
'''
pdfFileObj.close()

##Decrypting PDFs

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted
True
pdfReader.getPage(0)
'''
Traceback (most recent call last):
    File "<pyshell#173>", line 1, in <module>
       pdfReader.getPage()
    File "C:\Python34\lib\site-packages\PyPDF2\pdf.py", line 1173, in getObject
       raise utils.PdfReadError("file has not been decrypted")
   PyPDF2.utils.PdfReadError: file has not been decrypted
'''
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.decrypt('rosebud')
1
pageObj = pdfReader.getPage(0)

## Creating PDFs

'''
PyPDF2’s counterpart to PdfFileReader is PdfFileWriter, which can create new PDF files.
But PyPDF2 cannot write arbitrary text to a PDF like Python can do with plaintext files.

PyPDF2 doesn’t allow you to directly edit a PDF. Instead, you have to create a new PDF and then copy content over from an existing document.
The examples in this section will follow this general approach:

    Open one or more existing PDFs (the source PDFs) into PdfFileReader objects.
    Create a new PdfFileWriter object.
    Copy pages from the PdfFileReader objects into the PdfFileWriter object.
    Finally, use the PdfFileWriter object to write the output PDF.

Creating a PdfFileWriter object creates only a value that represents a PDF document in Python.
It doesn’t create the actual PDF file. For that, you must call the PdfFileWriter’s write() method.

The write() method takes a regular File object that has been opened in write-binary mode.
You can get such a File object by calling Python’s open() function with two arguments:
the string of what you want the PDF’s filename to be and 'wb' to indicate the file should be opened in write-binary mode.
'''

## Copying Pages

pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

## Rotating Pages

import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
{'/Contents': [IndirectObject(961, 0), IndirectObject(962, 0),}
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()


## Overlaying Pages

'''
Useful for adding a logo, timestamp, or watermark to a page.
'''

import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()

## Encrypting PDFs

import PyPDF2
pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('swordfish')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()

