import PyPDF2
pdfreader= PyPDF2.PdfFileReader(open("(your_pdf_name_here",'rb'))

import pyttsx3
speaker=pyttsx3.init()

for p in range(pdfreader.numPages):
    t=pdfreader.getPage(p).extractText()
    speaker.say(t)
    speaker.runAndWait()
speaker.stop()

speaker.save_to_file(t,'audio.mp3')
speaker.runAndWait()
