from importArticles import *
from sklearn.model_selection import train_test_split
from kdTree import *
import time

df = articlesDataframe

trainDf, testDf = train_test_split(df, test_size=0.1)

print('Executing KD Tree, Quad Tree, Range Tree, R Tree functions using data from',len(df),'articles')
time.sleep(0.5)
print('Data has been split to',len(trainDf),'train articles to be added to Trees and',len(testDf),'articles for queries')
time.sleep(0.5)

print('--------------KD Tree Demo--------------')

start_time = time.time()

col_one_list = trainDf['vectors'].tolist()

kdTreeDemo = kdTree(col_one_list)

timeElapsed = time.time() - start_time

print(timeElapsed,"seconds elapsed to insert",len(trainDf),"train articles to KD Tree. Average insertion time:",(timeElapsed/len(trainDf)))

rowToQuery = testDf.sample()

print('Randomly selected article:',rowToQuery.iloc[0]['description'])


closestNeighbor = kdTreeClosest(kdTreeDemo,rowToQuery['vectors'].tolist()[0])
print(closestNeighbor)
print(trainDf['vectors'])
print(trainDf.index[trainDf['vectors'] != closestNeighbor].tolist())