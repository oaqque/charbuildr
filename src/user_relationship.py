"""
Author: William Zhiwei Ye

This object contains a ChatBot which will keep track of the relationship-score between the User and Conversational AI
"""
from sentiment import authenticate_client, sentiment_analysis, Sentiment

class RelationshipScore:

    def __init__(self, variability):
        self.sentiment_client = authenticate_client() 
        self.variability = variability
        self.user_relationship = 0

    def update(self, msg):
        sentiment = sentiment_analysis(self.sentiment_client, [msg.lower()])
        self.user_relationship = self.user_relationship + (sentiment.neu * 0.3 + sentiment.pos - sentiment.neg) * self.variability
        if (self.user_relationship > 1): self.user_relationship = 1 
        if (self.user_relationship < 0): self.user_relationship = 0
        return self.user_relationship

    def get_relationship(self):
        return round(self.user_relationship, 3)
