import os
import record
import transcribe
import keyboard
# import Tkinter as tk


# def on_return(event):
#
    # SAVE_FILE = "output.wav"
    #
    # record.record_and_save(SAVE_FILE)
    #
    # trans = transcribe.audio_to_text(SAVE_FILE)
    # text.insert('end', 'text understood: %s\n' % (trans, ))
    # os.remove(SAVE_FILE)
    #
    # keyboard.write_text(trans)

# def on_key(event):
#     text.insert('end', 'You pressed %s\n' % (event.char, ))
#
#
# root = tk.Tk()
# root.geometry('300x200')
# text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
# text.pack()
# root.bind('<Return>', on_return)
# root.bind('<KeyPress>', on_key)
# root.mainloop()

SAVE_FILE = "output.wav"

while True:

    print "recording"
    record.record_and_save(SAVE_FILE)

    print "transcribing"
    trans = transcribe.audio_to_text(SAVE_FILE)

    print "saving"
    print "text understood:" + trans + '\n'
    os.remove(SAVE_FILE)

    keyboard.write_text(trans)
