import pyttsx3
import PyPDF2
book = open('object_oriented_python_tutorial.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
Mamun = pyttsx3.init()
page = pdfReader.getPage(7)
text = page.extractText()
Mamun.say(text)
Mamun.say = ('How are you Mamun')
Mamun.runAndWait()