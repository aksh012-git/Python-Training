import pandas as pd

ufo_data = pd.read_csv('/home/wot-aksh/Desktop/Python_Training/11_Pandas/ufo_sighting_data.csv')


#----------------------------------------------------------------------------------------------------------------------------
"""Write a Pandas program to create today's date"""

print('Current date and time: ',pd.datetime.now(),'\n')


#----------------------------------------------------------------------------------------------------------------------------
"""Write a Pandas program to calculate all the sighting days of the unidentified flying object (ufo) from the current date."""

end_date = '10/11/2005'

# ufo_data['Date_time'] = ufo_data['Date_time'].str.replace('24:00','0:00')

ufo_data['Date_time'] = pd.to_datetime(ufo_data['Date_time']).dt.date

print('ufo appeared {0} days till date {1}'.format(ufo_data.loc[ufo_data['Date_time'] <= pd.to_datetime(end_date)].shape[0],end_date))

