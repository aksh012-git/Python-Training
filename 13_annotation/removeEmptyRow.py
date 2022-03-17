import pandas as pd


df = pd.read_csv("/home/wot-aksh/Desktop/Python_Training/lable_part_1.csv")
df = pd.DataFrame(df)
print(df)

df = df[df.iloc[:,1].notna()]
print(df.head())

df.to_csv('/home/wot-aksh/Desktop/Python_Training/lable_part_1.csv', index=False)