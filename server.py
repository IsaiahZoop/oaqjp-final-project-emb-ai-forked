from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detector import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detection_route():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    # Check if the result has valid emotion data
    if result['dominant_emotion'] is None:
        return jsonify({'response': 'Invalid text! Please try again!'})

    # Format the response
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({'response': formatted_response})

if __name__ == '__main__':
    app.run(debug=True)
