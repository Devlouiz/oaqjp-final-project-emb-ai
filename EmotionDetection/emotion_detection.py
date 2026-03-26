import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = my_obj, headers = headers)
    response_str = response.text
    formatted_response = json.loads(response_str)

    emotion_obj = {}
    for emotion, score in formatted_response['emotionPredictions'][0]['emotion'].items():
        emotion_obj[emotion] = score
    dominant_emotion = max(emotion_obj, key=emotion_obj.get)
    emotion_obj["dominant_emotion"] = dominant_emotion

    return emotion_obj
