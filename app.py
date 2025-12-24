from flask import Flask, request, send_file, jsonify
from gtts import gTTS

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def text_to_speech():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "Text is required"}), 400

    text = data['text']
    language = data.get('lang', 'en')

    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")

    return send_file("output.mp3", mimetype="audio/mpeg")

app.run(debug=True)
