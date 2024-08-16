import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_merger(inputs)


# with open('Resume.pdf' , 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     # output number of pages
#     print(reader.numPages)
#     # page object
#     page = reader.getPage(0)
#     print(page)
#     print(page.rotateCounterClockwise(90))
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)

#     with open('new.pdf' , 'wb') as file:
#         writer.write(file)





