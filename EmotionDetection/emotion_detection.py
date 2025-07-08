import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)
    
    # Convert response text to dict
    emotion_data = json.loads(response.text)
    
    # Extract emotions dictionary from nested structure
    emotion_predictions = emotion_data.get('emotionPredictions', [])
    if not emotion_predictions:
        return {}
    
    emotions = emotion_predictions[0].get('emotion', {})
    
    # Find dominant emotion (highest score)
    dominant_emotion = max(emotions, key=emotions.get) if emotions else None
    
    # Build formatted output dict
    result = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }
    
    return result
