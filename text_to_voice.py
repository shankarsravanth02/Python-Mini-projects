from gtts import gTTS
import os
myt='welcome shankar sravanth'
language='en'
myobj=gTTS(text=myt,lang=language,slow=False)
myobj.save("firstvoice.mp3")
os.system("firstvoice.mp3")
