"""
Flask server for emotion detection web app.
Handles routes and communicates with the emotion detector module.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the home page with the input form."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Handle GET request to detect emotions in the given text.
    Returns JSON with emotion scores or error message.
    """
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)

    if result.get("dominant_emotion") is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
