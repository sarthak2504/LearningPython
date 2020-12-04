import pandas as pd

# Reading of different kinds of files using Pandas

df = pd.read_csv('pokemon_data.csv')

df_xlsx = pd.read_excel('pokemon_data.xlsx')

df_tab = pd.read_csv('pokemon_data.txt', delimiter='\t')

#print(df.head(5))

#print(df[['Name','Type 1','#']])

#print(df.iloc[1])

#print(df.iloc[0,1])

# TO ITERATE THROUGH THE DATA

#for index,rows in df.iterrows():
#    print(index,rows['Name'])

print(df.loc[df['Type 1'] == "Water"][df['Type 2'] == "Flying"])

#Added a line to test GIT