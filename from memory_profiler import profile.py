from memory_profiler import profile
import json
import pandas as pd
from pandas import json_normalize
 
@profile
def load_data(path):
    with open(path) as f:
        data = json.load(f)
    #Branch Dataframe
    branch_df= json_normalize(data)
    del data
    return branch_df
 
def main():
    df= load_data(r"C:\Users\ibrahim.aneesulla\Downloads\fd7a1a13-b84d-4ef9-afc0-a5d594041241_83d04ac6-cb74-4a96-a06a-e0d5442aa126_transactions (1).json")
    print(df.head())

main()