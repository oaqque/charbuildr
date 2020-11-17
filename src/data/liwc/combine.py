import numpy as np 
import pandas as pd

df = pd.read_csv("rick_script_clean.csv")
np.savetxt("rick_script.txt", df['line'].values, fmt='%s')