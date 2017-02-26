import os
import record
import transcribe
import keyboard
import stt
import time
import evaluate


SAVE_FILE = "output.wav"


simple_rules = {
                "declare":["variable","list","class","function"],
                "control":["if", "for", "while"]
                }

declared = []

time.sleep(2)

while True:

    print "recording"
    # stt.listen_for_speech(SAVE_FILE)
    record.record_and_save(SAVE_FILE)

    print "transcribing"
    trans = transcribe.audio_to_text(SAVE_FILE)

    if trans == None:
        print "No text found"
        continue

    print "saving"
    print "text understood:" + trans + '\n'
    os.remove(SAVE_FILE)

    text = evaluate.evaluate(trans)

    """

    words = trans.split(' ')
    text = ''
    if words[0] == "declare":
        if words[1] in simple_rules["declare"]:
            if words[1] == "variable":
                text += (words[2].lower() + ' = ' + '"' + words[4]) + '"'
    # elif words[0] == "control":
    #
    elif words[0] == "print":
        text = "print "
        for r in words[1:]:
            text += r
    elif words[0] == "hello":
        keyboard.new_line()

    else:
        print "Didn't get that please try again"
        continue """


    keyboard.write_text(text)
