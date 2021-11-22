import pandas as pd
from pathlib import Path
from pathlib import Path

datasets_folder = Path("./datasets")
Path("plots/").mkdir(parents=True, exist_ok=True)
df = pd.read_csv(datasets_folder/'final_netflix_list.csv', sep=",", low_memory=True)

# TODO: Fill Database