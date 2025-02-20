"""This is the Flask server to run Emotion Detection"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def run_emotion_detector() :
    """Runs emotion detector from package on click"""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None :
        return "Invalid Text! Please Try Again"

    formatted_response = "For the given statement, the system response is 'anger' : "
    formatted_response += f"{response['anger']}, "
    formatted_response += f"'disgust' : {response['disgust']}, 'fear' : {response['fear']}, "
    formatted_response += f"'joy' : {response['joy']}, and 'sadness' : "
    formatted_response += f"{response['sadness']}. "
    formatted_response += f"The dominant emotion is <b>{response['dominant_emotion']}<b>"

    return formatted_response

@app.route("/")

def render_index_page() :
    """Renders Index page at server root"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
