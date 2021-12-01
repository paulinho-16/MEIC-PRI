from pathlib import Path
import pandas as pd
import numpy as np

datasets_folder = Path("./datasets")

Path("plots/").mkdir(parents=True, exist_ok=True)

df = pd.read_csv(datasets_folder/'final_netflix_list.csv', sep=",", low_memory=True)

for x in range(0, len(df)):
    df['popularRank'][x] = (df['popularRank'][x]).replace(',', '')
    df['popularRank'][x] = int(df['popularRank'][x])

df = df.replace('Not available', np.nan)

df.to_csv(datasets_folder/"final_netflix_list_1.csv", index=False)