#python code for converting text file to speech
#use Python 3.7 to run this code
import pyttsx3
import PyPDF2

txtfile=open('testing.pdf','rd')
pdf_reader=PyPDF2.PdfFileReader(txtfile)
pgnum=pdf_reader.numPages
play = pyttsx3.init()

for n in range(0,pgnum):
    page=pdf_reader.getPage(n)
    data=page.extractText()
    play.say(data)
    play.runAndWait()
