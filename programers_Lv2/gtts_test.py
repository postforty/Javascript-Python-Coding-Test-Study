from gtts import gTTS

read_file = "Hi!"

tts = gTTS(text=read_file, lang="en")
tts.save(r"hi.mp3")
