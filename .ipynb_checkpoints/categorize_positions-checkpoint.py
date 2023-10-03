import pandas as pd
"""
We will treat true guards as backcourt, since there is so much double position
of guard-forward and forward-guard in this dataset.
If we made everyone with a forward a frontcourt player the numbers would be skewed.
So we create a wing position type to equalize the applied positions
"""
def categorize_positions(pos):
    pos_type = ''
    if pos == 'guard':
        pos_type = 'backcourt'
    elif pos == 'guard-forward':
        pos_type = 'wing'        
    elif pos == 'forward-guard':
        pos_type = 'wing'        
    elif pos == 'forward':
        pos_type = 'wing'        
    elif pos == 'forward-center':
        pos_type = 'frontcourt'
    elif pos == 'center-forward':
        pos_type = 'frontcourt'
    elif pos == 'center':
        pos_type = 'frontcourt'
    else:
        return 'Unknown'
    return pos_type
