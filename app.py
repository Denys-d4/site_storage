from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Директорія для збереження MP3-файлів
AUDIO_FOLDER = os.path.join(app.root_path, 'static/audio')

@app.route('/')
def home():
    return '<h1>Головна сторінка</h1><a href="/audio">Слухати MP3</a>'

# Сторінка, що напряму повертає MP3-файл
@app.route('/audio')
def get_audio():
    return send_from_directory(AUDIO_FOLDER, 'sample.mp3')

if __name__ == '__main__':
    app.run(debug=True)
