"""
Author: William Zhiwei Ye

Chatbot based on 
https://github.com/parulnith/Building-a-Simple-Chatbot-in-Python-using-NLTK/blob/master/chatbot.py

Harry Potter script from
https://www.kaggle.com/eward96/harry-potter-and-the-philosophers-stone-script
"""

# Import python libraries

# Import local libraries
from user_relationship import RelationshipScore
from utils import generate_rs_threshold
from generativeModel import GenerativeModel
from retrievalModel import RetrievalModel
import os

##########################################################################
# Main #
print("Loading generative model...")
generativeModel = GenerativeModel()
print("Loading retrieval model...")
retrievalModel = RetrievalModel()
print("Establishing relationship score...")
relationshipScore = RelationshipScore(0.1)
rs_threshold = round(generate_rs_threshold(), 3)

print(f"\nRelationship Score Threshold: {rs_threshold}\n")

flag = True
welcomeMsg = "Hi, how can I help you today?"
generativeModel.add_to_history(welcomeMsg)
relationshipScore.update(welcomeMsg)
print("AI: " + welcomeMsg)
print(f"[Relationship Score: {relationshipScore.get_relationship()}")

while (flag == True):
    # Get a response from the user
    user_response = input("User: ").lower()
    relationshipScore.update(user_response)
    generativeModel.add_to_history(user_response)
    print(f"[Relationship Score: {relationshipScore.get_relationship()}")

    # Get a response from the models
    if (relationshipScore.get_relationship() < rs_threshold):
        ai_response = generativeModel.get_response()
    else:
        similarity = retrievalModel.calculate_similarity(user_response)
        if (similarity > 0.2):
            ai_response = retrievalModel.get_response(user_response)
            generativeModel.add_to_history(ai_response)
        else:
            ai_response = generativeModel.get_response()
    relationshipScore.update(ai_response)
    print("AI: " + ai_response)
    print(f"[Relationship Score: {relationshipScore.get_relationship()}")

    if (user_response.lower() == "bye"):
        flag = False 

