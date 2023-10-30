import pandas as pd
import numpy as np
import icecream as ic

def get_player_data(column, df):
    if column not in df.columns:
        raise ValueError(f'{column} is not a valid column name')
    else:
        # create a new object that contains playerid, fname, lname, and the column
        player_data = df[['playerid', 'fname', 'lname', column]]        
        return player_data