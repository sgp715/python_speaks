import pyaudio
import wave


CHUNK = 1024
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 2
RATE = 16000 #sample rate
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"


def record_and_save(file_path):

    p = pyaudio.PyAudio()

    frames = []
    stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data) # 2 bytes(16 bits) per channel

    stream.stop_stream()
    stream.close()
    p.terminate()

    # TODO: make a temp file
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
