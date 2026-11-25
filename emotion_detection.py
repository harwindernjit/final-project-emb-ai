"""Emotion detection using the Watson NLP EmotionPredict service."""
import requests, json

# Constant Variables
URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
EMOTIONS = ["anger", "disgust", "fear", "joy", "sadness"]

def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for the given text."""
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers = header)
    
    # Task 7: blank or invalid input returns status 400
    if response.status_code == 400 :
        result = {emotion: None for emotion in EMOTIONS}
        result["dominant_emotion"] = None
        return result
    
    # Task 3: extract the scores and find the dominant emotion
    data = json.loads(response.text)
    scores = data["emotionPredictions"][0]["emotion"]
    scores["dominant_emotion"] = max(EMOTIONS, key=lambda e: scores[e])
    return scores