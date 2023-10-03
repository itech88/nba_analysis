import pandas as pd
import numpy as np
import icecream as ic
from get_player_data import get_player_data
from school_stats import school_stats

data = pd.read_csv("players.csv")
# data.info()
# data.describe()
# ic.ic(data.head())

player_names = data[['fname', 'lname']]
name_sorted = player_names.sort_values(by=['lname','fname'], ascending=True)
ic.ic(name_sorted.head())

# Find the count of all players under 25 years old

"""
1. Generate the lists of all colleges in: 
ACC, SEC, Big 10, Big 12, Pac-12, HBCU, International, Other US Colleges
2. Find the percentage of active players that went to each type of college
3. Find which type of colleges 
i. score the most points, 
ii. produce the most all stars
iii. make the most salary
iv. produce the most championship
"""

def choose_column(df):
    col_to_associate = (input(f'What column would you like to associate with?: \n {data.columns}\n'))
    player_data = get_player_data(col_to_associate, df)
    print(f'New object type: \n {player_data}')
    print('Find how many players from each school are in the NBA')
    school_stats(player_data, df)

def main():
    print("Welcome to the Active NBA Player Data Analysis Tool")
    print("What would you like to do?")
    print("1. Choose a column to associate with")
    choose_column(data)
    

main()



    
