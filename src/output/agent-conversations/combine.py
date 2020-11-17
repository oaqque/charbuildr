import os 
import pandas as pd
import numpy as np

for filename in os.listdir(os.getcwd()):
    df = pd.read_csv(os.path.join(os.getcwd(), filename))
    outfn = filename - '.csv' + '.txt'
    np.savetxt(outfn, df['line'].values, fmt='%s')
