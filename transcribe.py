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

def bing_audio_to_text(file_path):
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), file_path)
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    BING_KEY = "2b422f588ba74f6a91b58108579a42a6" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    try:
        print(r.recognize_bing(audio, key=BING_KEY))
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
