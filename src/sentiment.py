"""
Author: William Zhiwei Ye

Sentiment analysis of user_response
Built using Microsoft Text Analytics API 
"""

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from keys import azure_key, azure_endpoint

def authenticate_client():
    ta_credential = AzureKeyCredential(azure_key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=azure_endpoint, credential=ta_credential)
    return text_analytics_client

def sentiment_analysis(client, user_response):
    response = client.analyze_sentiment(documents = user_response)[0]
    return Sentiment(response.sentiment, response.confidence_scores.positive, response.confidence_scores.neutral, response.confidence_scores.negative)
    
class Sentiment:

    def __init__(self, sentiment, pos, neu, neg):
        self.sentiment = sentiment
        self.pos = pos
        self.neu = neu
        self.neg = neg           
