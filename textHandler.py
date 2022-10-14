from gtts import gTTS


def speech_creator(text):
    obj = gTTS(text=text, lang="ru")
    obj.save(r"file.mp3")
