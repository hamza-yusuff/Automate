import pyttsx3
import PyPDF2
text=open("code.pdf","rb")
reader=PyPDF2.PdfFileReader(text)
pages=reader.getNumPages()
page=reader.getPage(0)
text=page.extractText()

speaker=pyttsx3.init()
speaker.say(text)
speaker.runAndWait()