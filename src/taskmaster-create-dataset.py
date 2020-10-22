from pathlib import Path
import json
import pandas as pd
import numpy as np
from tqdm import tqdm 

##### Define paths to data and output #####
data_folder = Path("data/json/")
output_folder = Path("data/csv/")

with open(data_folder / "self-dialogs.json") as file:
    data = json.load(file)

counter = 0
for conversation in tqdm(data):
    # conversation_len = len(conversation['utterances'])
    speakers = []
    texts = []
    filename = "taskmaster-" + str(counter) + ".csv"
    df = pd.DataFrame()

    for utterance in conversation['utterances']:
        speakers.append(utterance['speaker'])
        texts.append(utterance['text'])

    df['name'] = speakers
    df['utterance'] = texts 
    df.to_csv(output_folder / filename)
    counter += 1