import sr
from os import path


def audio_to_text(file_path, type='Sphinx'):

    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), file_path)

    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    text = None
    if type == "Sphinx":
        try:
            text = r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
    elif type == "Google":
        print "GOOGLE"
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use ``
            # instead of `r.recognize_google(audio)`
            text = r.recognize_google(audio, key="AIzaSyDK6Lj3_Hqhf_HEFdBm0F6kFrQY-eLx-RY")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    else:
        print "Type not supported"


    return text
