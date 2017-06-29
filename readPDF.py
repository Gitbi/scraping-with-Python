from io import StringIO
import urllib
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import open


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams)
    process_pdf(rsrcmgr, device,pdfFile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = urllib.urlopen("http://pythonscraping.com/pages/warandpeace/charpter1.pdf")
outputString = readPDF(pdfFile)
print outputString
pdfFile.close()

