from flask import Flask, request, jsonify
from main import recognize_speech, speech_to_text
from nlp import preprocess_text, recognize_intent
from tasks import set_reminder, get_weather, general_query
from voice_output import speak

app = Flask(__name__)


@app.route('/process', methods=['POST'])
def process_audio():
    audio = recognize_speech()
    text = speech_to_text(audio)
    tokens = preprocess_text(text)
    intent = recognize_intent(tokens)

    if intent == 'set_reminder':
        response = set_reminder(text)
    elif intent == 'get_weather':
        response = get_weather()
    elif intent == 'general_query':
        response = general_query(text)
    else:
        response = "I didn't understand that."

    speak(response)
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)
