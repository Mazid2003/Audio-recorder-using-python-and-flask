# 🎙️ Sound Recorder & Web Playback

This project is a Python-based sound recorder with a Tkinter GUI & Flask Web Interface, allowing users to record, save, play, and download audio files directly from a web browser.

**🌟 Features**

✅ Record Audio via GUI (Tkinter)

✅ Save & Store Multiple Recordings

✅ Web Interface to Play & Download Audio (Flask)

✅ Auto-Lists All Recordings on Website

**📂 Folder Structure**

📁 SoundRecorderProject

│── 📁 recordings          # Stores all recorded audio files

│── 📁 templates           # HTML files for Flask web app

│   │── index.html         # Webpage to display & play recordings

│── app.py                 # Flask backend to serve recordings

│── sound_recorder.py      # Tkinter-based sound recorder GUI

│── requirements.txt       # Dependencies list for easy setup

│── README.md              # Project description & usage guide

**📥 Installation & Setup**

**1️⃣ Clone the Repository**

git clone https://github.com/Mazid2003/sound-recorder-using-python-and-flask.git

cd <directory name or project_folder name>

**2️⃣ Install Dependencies**

pip install -r requirements.txt

**3️⃣ Run the Sound Recorder (Tkinter GUI)**

python sound_recorder.py

Click "Start Recording" 🎙️

Click "Stop Recording" ⏹

**4️⃣ Run the Flask Web Server**

python app.py

Open in browser: http://127.0.0.1:5000

🎶 Play & download recorded files.

**🛠 Technologies Used**

Python 🐍

Tkinter (GUI for Recording) 🎛️

Flask (Web App for Playback) 🌐

pyaudio (Audio Recording) 🎤

wave (Audio Processing) 🎵

**💡 Future Improvements**

🚀 Add Real-time Audio Visualization📂 Cloud Storage for Recordings🔊 Noise Reduction & Audio Enhancements

**📜 License**

This project is open-source under the MIT License.

