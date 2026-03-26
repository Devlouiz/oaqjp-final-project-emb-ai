"""
This module contains the Flask application for the Emotion Detection service.

It exposes a web service where users can input a text string, and the system
will analyze the emotions expressed in the text. The system returns emotion 
scores for emotions such as anger, joy, fear, sadness, and disgust, along 
with the dominant emotion identified in the text.

Routes:
    - /emotionDetector: Analyzes the input text and returns the emotion scores.
    - /: The index page with a form for users to input text to be analyzed.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_function():
    """
    Analyzes the emotion of the provided text input.

    Retrieves the emotion analysis for the given text from the `emotion_detector`
    function, and returns a string with the predicted emotions and the dominant emotion.

    Args:
        None

    Returns:
        str: A formatted string with emotion predictions or an error message if invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    joy = response['joy']
    fear = response['fear']
    sadness = response['sadness']
    disgust = response['disgust']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"""
    For the given statement, the system response is 
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 
    'joy': {joy}, and 'sadness': {sadness}. 
    The dominant emotion is {dominant_emotion}.
    """

@app.route("/")
def render_index_page():
    """
    Renders the index (home) page with a form for text input.

    This function serves the homepage where users can enter the text that they want to analyze.

    Args:
        None

    Returns:
        render_template: The rendered `index.html` page with the form.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    