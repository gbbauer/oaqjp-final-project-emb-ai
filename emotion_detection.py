import requests
import json

# Function to pass text to AI service
def emotion_detector(text_to_analyze) :
    #Format JSON Object
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text_obj = { "raw_document": { "text": text_to_analyze } }

    #Post request set to response
    response = requests.post(url, json=text_obj, headers=header)
    
    #format response
    formatted_response = json.loads(response.text)

    anger_score = float(formatted_response['emotionPredictions'][0]['emotion']['anger'])
    disgust_score = float(formatted_response['emotionPredictions'][0]['emotion']['disgust'])
    fear_score = float(formatted_response['emotionPredictions'][0]['emotion']['fear'])
    joy_score = float(formatted_response['emotionPredictions'][0]['emotion']['joy'])
    sadness_score = float(formatted_response['emotionPredictions'][0]['emotion']['sadness'])

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }
    
    #set high score variable & dominant emotion out of for loop
    high_score = 0
    dominant_emotion = "None"
    
    #iternate through all scores in dictionary, find highest one

    for key, value in emotion_scores.items() :

        if value > high_score : 
            high_score = value
            dominant_emotion = key

    #set dominant emotion in emotion scores
    emotion_scores['dominant_emotion'] = dominant_emotion

    return(formatted_response)


# Response Structure
# {'emotionPredictions': 
# [{'emotion': {'anger': 0.010783353, 'disgust': 0.0057280147, 'fear': 0.012159394, 
# 'joy': 0.9787635, 'sadness': 0.023557507}, 
# 'target': '', 'emotionMentions': [{'span': {'begin': 0, 'end': 20, 'text': 'I love this new tech'},
#  'emotion': {'anger': 0.010783353, 'disgust': 0.0057280147, 'fear': 0.012159394, 
# 'joy': 0.9787635, 'sadness': 0.023557507}}]}], 
# 'producerId': {'name': 'Ensemble Aggregated Emotion Workflow', 'version': '0.0.1'}}
