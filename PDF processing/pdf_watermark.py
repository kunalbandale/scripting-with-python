import PyPDF2
import sys

template = PyPDF2.PdfFileReader(open('super.pdf' , 'rb'))
watermark = PyPDF2.PdfFileReader(open('watermark.pdf' , 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(1)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output' , 'wb') as file:
        output.write(file)