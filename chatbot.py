"""
Author: William Zhiwei Ye
"""

class ChatBot:

    def __init__(self, script):
        self.user_relationship = 0
        self.char_profile = get_char_profile(script)
        self.extraversion = get_extraversion(self.char_profile)
        self.agreeableness = get_agreeableness(self.char_profile)
        self.neuroticism = get_neuroticism(self.char_profile)

    def calculate_user_relationship(user_sentiment):
        return self.user_relationship + (self.neuroticism * -user_sentiment.neg + user_sentiment.neu * 0.3 + self.agreeableness * user_sentiment.pos)

def get_char_profile(script):
    return 0

def get_extraversion(profile):
    return 0.7

def get_agreeableness(profile):
    return 0.5

def get_neuroticism(profile):
    return 0.1