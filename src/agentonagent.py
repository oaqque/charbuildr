"""
Author: William Zhiwei Ye

Generate conversations between two agents
"""

# Import python libraries

# Import local libraries
from user_relationship import RelationshipScore
from utils import generate_rs_threshold
from generativeModel import GenerativeModel
from retrievalModel import RetrievalModel
import os
import argparse
import pandas as pd
##########################################################################
# Arguments #
parser = argparse.ArgumentParser()
parser.add_argument('--model')
parser.add_argument('--outfn')
args = parser.parse_args()

##########################################################################
def print_response(agent, response):
    if agent == 1:
        print("Agent: " + response)
    else: 
        print("Rick : " + response)
##########################################################################
# Main #
print("Loading generative model...")
generativeModel = GenerativeModel(args.model)
print("Establishing relationship score...")
relationshipScore = RelationshipScore(0.1)
rs_threshold = round(generate_rs_threshold(), 3)

print(f"\nRelationship Score Threshold: {rs_threshold}\n")

# Record output in these variables
names = []
lines = []
relationship_scores = []

numTurns = 20
agent = 1
prompt = "What's up Rick!"
generativeModel.add_to_history(prompt)
relationshipScore.update(prompt)
print("Agent: " + prompt)
print(f"[Relationship Score: {relationshipScore.get_relationship()}, Relationship Score Threshold: {rs_threshold}")
names.append("Agent")
lines.append(prompt)
relationship_scores.append(relationshipScore.get_relationship())
for counter in range(numTurns):
    if (counter % 2 == 0):
        agent = 2
        name = "Rick"
    else: 
        agent = 1
        name = "Agent"
    nextline = generativeModel.get_response()
    relationshipScore.update(nextline)
    print_response(agent, nextline)
    print(f"[Relationship Score: {relationshipScore.get_relationship()}, Relationship Score Threshold: {rs_threshold}")

    # Save the results
    names.append(name)
    lines.append(nextline)
    relationship_scores.append(relationshipScore.get_relationship())

# Output the results to a csv
df = pd.DataFrame({'name': names, 'line': lines, 'rs_score': relationship_scores})
print(df)
df.to_csv('./output/agent-conversations/' + args.outfn, index=False)