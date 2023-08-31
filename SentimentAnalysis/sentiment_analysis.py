import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header)
    new_response = json.loads(response.text)
    if response.status_code == 200:
        label = new_response['documentSentiment']['label']
        score = new_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {'label': label, 'score': score}


"""
After successful import, test your application with the text “I love this new technology.”
sentiment_analyzer("I love this new technology.")'{"documentSentiment":{"score":0.996586, "label":"SENT_POSITIVE", "mixed":false, "sentimentMentions":[{"span":{"begin":0, "end":27, "text":"I love this new technology."}, "sentimentprob":{"positive":0.9934198, "neutral":0.0030947884, "negative":0.0034853641}}]}, "targetedSentiments":{"targetedSentiments":{}, "producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}, "producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}'
"""