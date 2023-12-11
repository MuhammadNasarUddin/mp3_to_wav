import streamlit as st
from pydub import AudioSegment

def mp3_to_wav(input_file, output_file):
    audio = AudioSegment.from_mp3(input_file)
    audio.export(output_file, format="wav")

def main():
    st.title("MP3 to WAV Converter")
    uploaded_file = st.file_uploader("Upload an MP3 file", type=["mp3"])

    if uploaded_file is not None:
        with open("temp.mp3", "wb") as f:
            f.write(uploaded_file.getvalue())

        output_file = "converted.wav"
        mp3_to_wav("temp.mp3", output_file)
        st.success("Download your WAV file:")
        st.download_button(label="Download WAV", data=open(output_file, "rb").read(), file_name=output_file)

if __name__ == "__main__":
    main()
