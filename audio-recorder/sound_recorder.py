import pyaudio
import wave
import threading
import tkinter as tk
import os
from datetime import datetime
from flask import Flask, render_template, send_from_directory

# Create Flask App
app = Flask(__name__, template_folder="templates")

# Audio Settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # Sampling rate
CHUNK = 1024  # Buffer size
RECORDINGS_FOLDER = "recordings"

# Ensure the recordings folder exists
os.makedirs(RECORDINGS_FOLDER, exist_ok=True)

# Global Variables
recording = False
current_filename = ""

def start_recording():
    """Starts recording audio in a separate thread."""
    global recording, current_filename
    recording = True
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    current_filename = os.path.join(RECORDINGS_FOLDER, f"recording_{timestamp}.wav")
    
    record_thread = threading.Thread(target=record_audio, args=(current_filename,))
    record_thread.start()
    status_label.config(text="🎤 Recording... Speak now!", fg="green")

def stop_recording():
    """Stops recording audio."""
    global recording
    recording = False
    status_label.config(text=f"⏹️ Recording Saved! Access it on the website.", fg="red")

def record_audio(filename):
    """Records audio until manually stopped and saves it."""
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []
    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop & Save
    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))

# 🎨 Create GUI Window
root = tk.Tk()
root.title("Audio Recorder 🎙️")
root.geometry("400x300")
root.configure(bg="#f4f4f4")

status_label = tk.Label(root, text="Click Start to Record", font=("Arial", 14), fg="black", bg="#f4f4f4")
status_label.pack(pady=20)

start_button = tk.Button(root, text="▶ Start Recording", font=("Arial", 14), bg="green", fg="white",
                         command=start_recording, width=20)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="⏹ Stop Recording", font=("Arial", 14), bg="red", fg="white",
                        command=stop_recording, width=20)
stop_button.pack(pady=10)

open_website_button = tk.Button(root, text="🌐 Open Website", font=("Arial", 14), bg="blue", fg="white",
                                command=lambda: os.system("start http://127.0.0.1:5000"), width=20)
open_website_button.pack(pady=10)

exit_button = tk.Button(root, text="❌ Exit", font=("Arial", 14), bg="gray", fg="white",
                        command=root.quit, width=20)
exit_button.pack(pady=10)

#  Run Flask server in a separate thread
def run_flask():
    app.run(debug=True, use_reloader=False)

flask_thread = threading.Thread(target=run_flask, daemon=True)
flask_thread.start()

# Run the GUI
root.mainloop()
