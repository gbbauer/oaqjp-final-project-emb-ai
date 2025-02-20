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

    return(formatted_response)
