import pyttsx3
import PyPDF2
print(dir(PyPDF2))
book = open('.pdf', 'rb')
# PdfReader = PyPDF2.PdfFileReader(book)
# pages = pdfReader.numPages
# print(pages)
speaker = pyttsx3.init()
speaker.say(book)
speaker.runAndWait()
