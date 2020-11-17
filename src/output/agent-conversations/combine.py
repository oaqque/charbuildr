import os 
import pandas as pd
import numpy as np

for filename in os.listdir(os.getcwd()):
	try:
		df = pd.read_csv(os.path.join(os.getcwd(), filename))
		outfn = filename + '.txt'
		np.savetxt(outfn, df['line'].values, fmt='%s')
	except:
		continue
