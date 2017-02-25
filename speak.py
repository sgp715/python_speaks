import os
import record
import transcribe
import keyboard


r = record.Recorder()

frames = r.recorde_audio()
SAVE_FILE = "output.wav"
r.save_audio(frames, SAVE_FILE)

text = transcribe.audio_to_text(SAVE_FILE)
os.remove(SAVE_FILE)

keyboard.write_text(text)
