import sr
from os import path


def audio_to_text(file_path):

    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), file_path)

    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    text = None
    try:
        text = r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    return text
