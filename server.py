"""
server.py
Flask server for the Emotion Detection web application.
Handles HTTP requests and returns emotion analysis results.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detector import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the home page.
    
    Returns:
        HTML template for the home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detection_route():
    """
    Process the emotion detection request.
    
    Retrieves the 'textToAnalyze' query parameter from the request,
    sends it to the emotion detection function, and formats the response.
    
    Returns:
        JSON response with the formatted emotion analysis or error message.
    """
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
    # Run the Flask application in debug mode.
    app.run(debug=True)
