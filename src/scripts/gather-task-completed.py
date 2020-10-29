from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from statistics import mean

##### Define paths to data and output #####
data_folder = Path("../data/csv/")
output_folder = Path("../output/analysis-0.1/")
graph_folder = Path("../graphs/0.1")

filename = "task-completed-manual.csv"
df = pd.read_csv(data_folder / filename)

relationship_scores_pre = []
relationship_scores_post = []
conversation_length = []
for task_id in df.task_id:
    tmp_fn = "taskmaster-" + str(task_id) + ".csv"
    tmp_df = pd.read_csv(output_folder / tmp_fn)

    task_completed_line = df.task_completed_line[task_id]

    relationship_scores_post.append(tmp_df.relationship[task_completed_line])
    relationship_scores_pre.append(tmp_df.relationship[task_completed_line - 1])
    conversation_length.append(len(tmp_df))

df['relationship_score_pre'] = relationship_scores_pre
df['relationship_score_post'] = relationship_scores_post

# Print Statistics
print(f"Post Mean: {df['relationship_score_post'].mean()}")
print(f"Post STD: {df['relationship_score_post'].std()}")
print(f"Pre Mean: {df['relationship_score_pre'].mean()}")
print(f"Pre STD: {df['relationship_score_pre'].std()}")
print(f"Average Length of Conversation: {mean(conversation_length)}")

# Scatter Plot Post
plt.figure(0)
plt.scatter(df['task_id'], df['relationship_score_post'])
plt.title('Relationship Scores Post Task Completion Scatterplot')
plt.xlabel('task_id')
plt.ylabel('Relationship Score') 
plt.savefig(graph_folder / 'scatterplot-post.png')

# Normal Distribution Post
h = sorted(relationship_scores_post)
fit = stats.norm.pdf(h, np.mean(h), np.std(h)) 
plt.figure(1)
plt.plot(h, fit, '-o')
plt.title('Relationship Scores Post Task Completion Histogram')
plt.xlabel('Relationship Score')
plt.hist(h, density=True) 
plt.savefig(graph_folder / 'hist-norm-post.png')

# Scatter Plot Pre
plt.figure(2)
plt.scatter(df['task_id'], df['relationship_score_pre'])
plt.title('Relationship Scores Pre Task Completion Scatterplot')
plt.xlabel('task_id')
plt.ylabel('Relationship Score') 
plt.savefig(graph_folder / 'scatterplot-pre.png')

# Normal Distribution Pre
h = sorted(relationship_scores_pre)
fit = stats.norm.pdf(h, np.mean(h), np.std(h)) 
plt.figure(3)
plt.plot(h, fit, '-o')
plt.title('Relationship Scores Pre Task Completion Histogram')
plt.xlabel('Relationship Score')
plt.hist(h, density=True) 
plt.savefig(graph_folder / 'hist-norm-pre.png')