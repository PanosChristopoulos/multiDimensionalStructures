import pandas as pd
from sklearn.datasets import fetch_20newsgroups

categories = ['alt.atheism', 'soc.religion.christian']
twenty_train = fetch_20newsgroups(subset='train',categories=categories, shuffle=True, random_state=30)
print(len(twenty_train.data))