import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import io

def load_audio(file: io.BytesIO) -> tuple[np.ndarray, int]:
    y, sr = librosa.load(file, sr=None)
    return y, sr

def plot_waveform(y: np.ndarray, sr: int) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.plot(np.linspace(0, len(y)/sr, len(y)), y, color='purple')
    ax.set_title("Waveform")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    return fig

def plot_spectrogram(y: np.ndarray, sr: int) -> plt.Figure:
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    fig, ax = plt.subplots()
    img = librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', cmap='magma', ax=ax)
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    ax.set_title("Spectrogram (dB)")
    return fig

def plot_mel_spectrogram(y: np.ndarray, sr: int) -> plt.Figure:
    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    mel_db = librosa.power_to_db(mel, ref=np.max)
    fig, ax = plt.subplots()
    img = librosa.display.specshow(mel_db, sr=sr, x_axis='time', y_axis='mel', cmap='viridis', ax=ax)
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    ax.set_title("Mel Spectrogram")
    return fig

def plot_chromagram(y: np.ndarray, sr: int) -> plt.Figure:
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    fig, ax = plt.subplots()
    librosa.display.specshow(chroma, x_axis='time', y_axis='chroma', cmap='coolwarm', ax=ax)
    ax.set_title("Chromagram")
    return fig

def plot_onset_strength(y: np.ndarray, sr: int) -> plt.Figure:
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    fig, ax = plt.subplots()
    ax.plot(np.linspace(0, len(onset_env)/sr, len(onset_env)), onset_env, label='Onset Strength', color='green')
    ax.set_title("Onset Strength (Beat Energy)")
    ax.set_xlabel("Time (s)")
    ax.legend()
    return fig

def plot_tempogram(y: np.ndarray, sr: int) -> plt.Figure:
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempo = librosa.feature.tempogram(onset_envelope=onset_env, sr=sr)
    fig, ax = plt.subplots()
    img = librosa.display.specshow(tempo, sr=sr, x_axis='time', y_axis='tempo', cmap='plasma', ax=ax)
    fig.colorbar(img, ax=ax)
    ax.set_title("Tempogram (Tempo Over Time)")
    return fig

# Streamlit UI
def main() -> None:
    st.set_page_config(page_title="VisionWav", layout="centered")
    st.title("🎧 VisionWav - MP3 Audio Visualizer")

    uploaded_file = st.file_uploader("Upload your MP3 file", type=["mp3"])

    if uploaded_file:
        audio_data = io.BytesIO(uploaded_file.read())
        y, sr = load_audio(audio_data)

        st.success(f"Audio Loaded - Duration: {len(y)/sr:.2f}s, Sample Rate: {sr} Hz")

        options = [
            "Waveform",
            "Spectrogram",
            "Mel Spectrogram",
            "Chromagram",
            "Onset Strength",
            "Tempogram"
        ]

        choice = st.selectbox("Choose Visualization Type", options)

        fig = None
        if choice == "Waveform":
            fig = plot_waveform(y, sr)
        elif choice == "Spectrogram":
            fig = plot_spectrogram(y, sr)
        elif choice == "Mel Spectrogram":
            fig = plot_mel_spectrogram(y, sr)
        elif choice == "Chromagram":
            fig = plot_chromagram(y, sr)
        elif choice == "Onset Strength":
            fig = plot_onset_strength(y, sr)
        elif choice == "Tempogram":
            fig = plot_tempogram(y, sr)

        if fig:
            st.pyplot(fig)
            plt.close(fig)

if __name__ == "__main__":
    main()
