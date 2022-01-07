import pandas as pd

df = pd.read_csv('articles_data.csv')

articlesDataframe = df[['source_name','author','title','description']]


articlesDataframe.dropna(inplace=True)
print(articlesDataframe)


