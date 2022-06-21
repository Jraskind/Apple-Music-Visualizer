import pandas as pd
import matplotlib as plt
import sys
csv_dir = sys.argv[1] 
df = pd.read_csv(csv_dir)
#Top X artists
NUM_ARTISTS = 10
artist_names = df["Artist Name"].unique()
times = {}
for name in artist_names:
    if name != "Rain Sounds" and name != "Nature Sounds":
        times[name] = df[df["Artist Name"] == name]["Play Duration Milliseconds"].sum() * (10 ** -3) * (1/60)
times = pd.DataFrame.from_dict(times, orient="index", columns=["play time"])
print(times.sort_values(by=["play time"], ascending=False)[:NUM_ARTISTS] )