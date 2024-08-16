import PyPDF2

with open('Resume.pdf' , 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    # output number of pages
    print(reader.numPages)
    # page object
    page = reader.getPage(0)
    print(page)
    print(page.rotateCounterClockwise(90))
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('new.pdf' , 'wb') as file:
        writer.write(file)




