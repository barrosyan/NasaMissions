import pandas as pd
columns=['Mission', 'url', 'htmlpagecontent', 'Company']
df = pd.read_csv('nasamissions.csv', names=columns)
df.drop(["Unnamed: 0", 0, 1, 2, "Comapny"], inplace=True)
rows_dropped_df.head()=df.drop(df.index[0])
df.head()

rows_dropped_df.to_csv(r'C:\Users\Usuario\Downloads\nasamissions.csv')