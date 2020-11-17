"""
Author: William Zhiwei Ye

Generate conversations between two agents
"""

# Import python libraries

# Import local libraries
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

# Record output in these variables
names = []
lines = []

numTurns = 20
agent = 1
prompt = "What's up Rick!"
generativeModel.add_to_history(prompt)
print("Agent: " + prompt)
names.append("Agent")
lines.append(prompt)
for counter in range(numTurns):
    if (counter % 2 == 0):
        agent = 2
        name = "Rick"
    else: 
        agent = 1
        name = "Agent"
    nextline = generativeModel.get_response()
    print_response(agent, nextline)

    # Save the results
    names.append(name)
    lines.append(nextline)

# Output the results to a csv
df = pd.DataFrame({'name': names, 'line': lines})
print(df)
df.to_csv('./output/agent-conversations/' + args.outfn, index=False)
