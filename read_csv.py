import pandas as pd


df = pd.read_csv(r"C:\Users\antony.samarawickrem\projects\dfo\dfo3.csv", usecols=[
                 'Date','Title', 'Text','Link'])

df=df[df['Title'].str.contains('british|pacific| haida|vancouver|campbell|fraser|bc|b.c.', na=False, case=False)]

df = df[['Date', 'Title', 'Text', 'Link']]
print(len(df))

df.to_csv(r'C:\Users\antony.samarawickrem\projects\dfo\small3.csv', index = False)
