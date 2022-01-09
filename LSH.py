import io
import numpy as np 
import pandas as pd 
from random import shuffle
from sklearn.metrics.pairwise import cosine_similarity,cosine_distances
from numpy import dot
from numpy.linalg import norm
from scipy import spatial
from importArticles import articlesDataframe

#Data 
a = "flying fish flew by the space station"
b = "he will not allow you to bring your sticks of dynamite and pet armadillo "
c = "he figured a few sticks of dynamite were easier than a fishing pot"
#Data


def shingle(text:str, k:int):

    '''
    DIVIDE TEXT IN TWO CHAR STRINGS
    '''

    shingle_set=[]

    #Divide text in k Characters per String 
    for i in range(len(text) - k + 1):
        shingle_set.append(text[i:i+k])

    return set(shingle_set)

#Create shingle set and vocabulary list for all text data
vocab = []
final_vocab=[]
final_set = []
for i in range(len(articlesDataframe)):
    
    try:
        #Make the shingle of our texts
        shingle_title = shingle(articlesDataframe['title'][i],3) #Call function shingle
        final_set.extend(shingle_title)
        #Make the shingle of our texts
        
        vocab.extend(list(shingle_title))#Make the vocabulary of our texts

    except KeyError:
        pass

vocab = list(set(vocab))#Make unique 3 characters in vocab 

#One encoding

shingleOne = [1 if x in final_set else 0 for x in vocab]

#One encoding


def create_hash_func(size:int):
    '''
    function for creating the hash vecs
    '''
    hash_ex = list(range(1,len(vocab)+1))
    shuffle(hash_ex)
    #print(hash_ex)
    return hash_ex

def minHash(vocabSize: int, nbits:int):
    '''
    function for building multiple minHash vecs
    '''
    hashes = []
    for _ in range (nbits):
        hashes.append(create_hash_func(vocabSize))
    return hashes


minhash = minHash(len(vocab), 100)#creation of 100 minhash vecs

def createHash(vector:list):
    '''
    use this func for creating our signatures
    '''
    signature = []

    for func in minhash:

        for i in range(1, len(vocab)+1):
            idx = func.index(i)
            sign_value = vector[idx]

            if sign_value == 1:
                signature.append(idx)
                break

    return signature

shingleSignature = createHash(shingleOne)# Create Signature

print(shingleSignature)#List

'''#Signature info
def signatureInfo(x,y):
    return len(x.intersection(y)) / len(x.union(y)) 

#print(signatureInfo(c,b))
'''

def split_vec(signature,b):
    assert len(signature) % b == 0
    r = int(len(signature)/b)
    #Split signature in b parts
    subVectors =[]
    for i in range (0,len(signature),r):
        subVectors.append(signature[i:i+r])
    return subVectors

bandShingle = split_vec(shingleSignature,50)#Call function split_vec

print(bandShingle) #List of Lists

'''
for aRows ,bRows in bandShingle:
    
    if aRows == bRows :
        #print (f"Pair:{aRows} = {bRows}")
        #print('a=b')
        break

for aRows ,cRows in bandShingle:
    
    #dot(aRows,cRows)/(norm(aRows)*norm(cRows))#cosine_similarity(aRows.reshape(1,-1),cRows.reshape(1,-1))
    if aRows == cRows :
        #print (f"Pair:{aRows} = {cRows}")
        #print('a=c')
        break


for bRows ,cRows in bandShingle:
    
    if bRows == cRows :
        #print (f"Pair:{bRows} = {cRows}")
        #print('b=c')
        break
'''


'''
COSINE SIMILARITY FOR NEXT 
for aRows, bRows , cRows in bandShingle:
    #aArr = np.asarray(aRows)
    #cArr = np.asarray(cRows) 
    aRows == aRows
    bRows == bRows
    cRows == cRows

resultAB = 1 - spatial.distance.cosine(aRows,bRows)
resultAC = 1 - spatial.distance.cosine(aRows,cRows) #resultAC = cosine_similarity(aArr.reshape(1,-1),cArr.reshape(1,-1))
resultBC = 1 - spatial.distance.cosine(bRows,cRows)
'''  