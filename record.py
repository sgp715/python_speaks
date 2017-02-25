import pyaudio
import wave


CHUNK = 1024
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 2
RATE = 16000 #sample rate
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"

class Recorder(object):

    def __init__(self):
        self.p = pyaudio.PyAudio()

    def recorde_audio(self):

        stream = self.p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK) #buffer

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data) # 2 bytes(16 bits) per channel

        print("* done recording")

        stream.stop_stream()
        stream.close()
        self.p.terminate()

        return frames

    def save_audio(self, frames, file_path):

        # TODO: make a temp file
        wf = wave.open(file_path, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
