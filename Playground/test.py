import pandas as pd

raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
'age': [20, 19, 22, 21],
'favorite_color': ['blue', 'red', 'yellow', "green"],
'grade': [88, 92, 95, 70],
'birth_date': ['10/10/1949 20:30', '08-05-1997', '04-28-1996', '12-16-1995']}

df = pd.read_csv('/home/wot-aksh/Desktop/Python_Training/11_Pandas/ufo_sighting_data.csv')

df['Date_time'] = pd.to_datetime(df['Date_time'])

print(df)

