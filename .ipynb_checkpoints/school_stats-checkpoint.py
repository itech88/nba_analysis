import pandas as pd
import numpy as np
import icecream as ic
from get_player_data import get_player_data
from config import school_dict

def check_school_player_count(player_data, df):

    schools = df['school'].unique()
    # ic.ic(schools)
    

    # using player_data object, find the number of players from each school
    school_count = player_data['school'].value_counts()
    school_check = input(f'What school would you like to know how many active players are from?')
    if school_check in schools:
        print(f'There are {school_count[school_check]} active players from {school_check}')
    

def school_stats(school_dict, df):
    
    ic.ic(f'Number of players from each school: \n {school_count}')
    print(f'Top 10 list of schools with the most players in the NBA: \n {school_count.head(10)}')


