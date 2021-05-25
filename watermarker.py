import PyPDF2
import sys
# python .\watermarker.py super.pdf wtr.pdf watermarked_output.pdf


templete = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))
watermark = PyPDF2.PdfFileReader(open(sys.argv[2], 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(templete.getNumPages()):
    page = templete.getPage(i)
    watermark_page = watermark.getPage(0)
    page.mergePage(watermark_page)
    output.addPage(page)

    with open(sys.argv[3], 'wb') as file:
        output.write(file)
