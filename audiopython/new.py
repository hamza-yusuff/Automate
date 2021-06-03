import pyttsx3
import PyPDF2
text=open('code.pdf','rb')
reader=PyPDF2.PdfFileReader(text)
pages=reader.getNumPages()

for i in range(0,pages):
    page=reader.getPage(i)
    t=page.extractText()

    speaker=pyttsx3.init()
    speaker.say(t)
    speaker.runAndWait()