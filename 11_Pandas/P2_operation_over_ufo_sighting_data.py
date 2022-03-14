import pandas as pd
import numpy as np

ufo_data = pd.read_csv('/home/wot-aksh/Desktop/Python_Training/11_Pandas/ufo_sighting_data.csv')

#----------------------------------------------------------------------------------------------------------------------------
"""Write a Pandas program to create today's date"""

# print(pd.datetime.now())

#----------------------------------------------------------------------------------------------------------------------------
"""Write a Pandas program to calculate all the sighting days of the unidentified flying object (ufo) from the current date."""

print(ufo_data['Date_time'])
