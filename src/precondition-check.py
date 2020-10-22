from user_relationship import RelationshipScore
import pandas as pd
import numpy as np
from pathlib import Path

##### Define paths to data and output #####
data_folder = Path("data/csv/")
output_folder = Path("output/analysis/")

##### Initialise Relationship Score #####
relationship_variability = 0.2
relationship_score = RelationshipScore(relationship_variability)

##### Get the conversation file #####
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