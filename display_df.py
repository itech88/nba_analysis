import pandas as pd
from IPython.display import display

def display_df(df, num_records=5, part = 'head'):
    if part == 'head':
        display(df.head(num_records).style.hide(axis="index"))
    elif part == 'tail':
        display(df.tail(num_records).style.hide(axis="index"))
    elif part == 'middle':
        middle_start = len(df) // 2 # find the middle row, round down
        middle_end = middle_start + num_records # find ending row
        display(df.iloc[middle_start:middle_end].style.hide(axis="index"))
    elif part == 'random':
        display(df.sample(n=num_records).style.hide(axis="index"))
    else:
        print("Invalid value for 'part': Should be 'head', 'tail' or 'middle'")
        
""" Example usage
df = pd.DataFrame({'A': range(1, 21), 'B': range(21, 41)})

Display first 5 rows
display_df(df)

Display last 3 rows
display_df(df, num_records=3, part='tail')

Display 4 rows from the middle
display_df(df, num_records=4, part='middle')
"""