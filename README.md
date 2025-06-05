# 🎧 VisionWaveAI

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Live App](https://img.shields.io/badge/Try%20Live%20App-Click%20Here-00bfff?logo=streamlit)](https://visionwaveai.streamlit.app/)

> 🎨 A lightweight and interactive MP3 Audio Visualizer made with Python + Streamlit  
> 🧠 Designed for creative audio insights on minimal systems (4GB RAM, Kali Linux tested)

---

## 🔥 Features

- 🎵 MP3 Upload support (no WAV required)
- 🎚️ Dropdown menu with 6 real-time visualizations
- 📊 Interactive plots using Matplotlib + Librosa
- 💻 Runs smoothly on low-resource systems

---

## 🔍 Available Visualizations

| Visualization     | Description                                  |
|-------------------|----------------------------------------------|
| 📈 Waveform        | Raw audio amplitude over time                |
| 🌊 Spectrogram     | Frequency over time in dB scale              |
| 🎹 Mel Spectrogram | Perceptual scale of pitches (log-spaced)     |
| 🎼 Chromagram      | Intensity of each pitch class                |
| 🔔 Onset Strength  | Beat energy detection                        |
| ⏱ Tempogram       | Tempo variations over time                   |

---

## 🚀 Live Demo

Click below to try it instantly:

👉 [**Launch VisionWaveAI**](https://visionwaveai.streamlit.app/)

---

## 🛠️ Local Setup

1. **Clone this repository**:

```bash
git clone https://github.com/aymnsk/VisionWaveAI.git
cd VisionWaveAI/VisionWav
````

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

> Make sure `ffmpeg` is installed (required by Librosa):

```bash
sudo apt install ffmpeg
```

3. **Run the app**:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
VisionWaveAI/
└── VisionWav/
    ├── app.py             # Main Streamlit App
    ├── requirements.txt   # Python dependencies
    └── README.md          # This file
```

---

## 🤖 Tech Stack

* Python 3.10
* Streamlit
* Librosa
* Matplotlib
* NumPy

---

## 🙌 Author

Made with ❤️ by [Ayman](https://github.com/aymnsk)
Feel free to ⭐ the repo and share your feedback!

---

## 📄 License

MIT License — free to use, modify & distribute.
