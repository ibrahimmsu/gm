from memory_profiler import profile
import json
import pandas as pd
from pandas import json_normalize

@profile
def load_data(path):
    with open(path) as f:
        for line in f:
            data = json.loads(line)
            yield json_normalize(data)

@profile
def main():
    generator = load_data(r"C:\Users\ibrahim.aneesulla\Downloads\fd7a1a13-b84d-4ef9-afc0-a5d594041241_83d04ac6-cb74-4a96-a06a-e0d5442aa126_transactions (1).json")
    for df in generator:
        print(df.head())

main()