from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder="templates")
RECORDINGS_FOLDER = "recordings"

@app.route("/")
def home():
    """Displays all recorded audio files on the website."""
    files = sorted(os.listdir(RECORDINGS_FOLDER), reverse=True)  # Show latest first
    return render_template("index.html", files=files)

@app.route("/recordings/<filename>")
def play_audio(filename):
    """Serves the recorded audio file."""
    return send_from_directory(RECORDINGS_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
