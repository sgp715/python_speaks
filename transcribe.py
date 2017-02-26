import sr
from os import path


def audio_to_text(file_path):

    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), file_path)

    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    BING_KEY = "2b422f588ba74f6a91b58108579a42a6"
    text = None
    try:
        text = r.recognize_bing(audio, key=BING_KEY)
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

    return text
