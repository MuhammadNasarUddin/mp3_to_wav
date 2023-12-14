from flask import Flask, render_template, request, send_file
from pydub import AudioSegment
import os

mp3towav = Flask(__name__)

def mp3_to_wav(input_file, output_file):
    audio = AudioSegment.from_mp3(input_file)
    audio.export(output_file, format="wav")

@mp3towav.route('/')
def index():
    return render_template('index.html')

@mp3towav.route('/convert', methods=['POST'])
def convert():
    try:
        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            raise ValueError("No file selected")
        
        input_file = "audio/audio.mp3"
        uploaded_file.save(input_file)
        
        output_file = "wav/converted.wav"
        mp3_to_wav(input_file, output_file)

        return send_file(output_file, as_attachment=True)

    except Exception as e:
        error_message = "An error occurred: " + str(e)
        return render_template('index.html', error=error_message)


if __name__ == "__main__":
    mp3towav.run(debug=True)
