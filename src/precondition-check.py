from user_relationship import RelationshipScore
import pandas as pd
import numpy as np
from pathlib import Path
import argparse

##### Define paths to data and output #####
data_folder = Path("data/csv/")
output_folder = Path("output/analysis-0.1/")

##### Initialise ArgParse #####
parser = argparse.ArgumentParser()
parser.add_argument("--filename", help="File name in data/csv/")
parser.add_argument("--var", help="Variability of relationship score")
args = parser.parse_args()

##### Initialise Relationship Score #####
if args.var:
    relationship_variability = args.var
else:
    relationship_variability = 0.1
relationship_score = RelationshipScore(relationship_variability)

##### Get the conversation file #####
if args.filename:
    conversation_fn = args.filename
else:
    conversation_fn = input("Conversation file name: ")

##### Parse the data #####
df = pd.read_csv(data_folder / conversation_fn)

length_conversation = len(df.index)
print("Number of rows imported: " + str(length_conversation))
scores = np.empty(length_conversation)
for index, row in df.iterrows():
    scores[index] = relationship_score.update(row['utterance'])

df['relationship'] = scores

print(df)

##### Output the data #####
df.to_csv(output_folder / conversation_fn)