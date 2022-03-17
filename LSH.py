import io 
import pandas as pd 
from random import shuffle
from sklearn.metrics import jaccard_score
import difflib
from scipy import spatial


def lshSimilarity(text1,text2):
    #Data 
    a = "Earnings and revenue expectations for European companies for the third quarter have improved very slightly, although the region is still expected to be in a corporate recession, according to data on Tuesday.'"
    b = "Marks & Spencer will be relegated from London's FTSE 100 <.FTSE> index for the first time since the inception of the blue-chip index in 1984, according to Reuters calculations based on Tuesday's closing prices."
    #Data

    def shingle(text:str, k:int):
        shingle_set=[]
        #Divide text in k Characters per String 
        for i in range(len(text) - k + 1):
            shingle_set.append(text[i:i+k])
        return set(shingle_set)
    '''
    DIVIDE TEXT IN TWO CHAR STRINGS
    '''

    #Call function shingle
    k =2 
    a = shingle(a,k)#print(a)
    b = shingle(b,k)#print(b)

    vocab= list(a.union(b))



    #One encoding
    a1 = [1 if x in a else 0 for x in vocab]
    b1 = [1 if x in b else 0 for x in vocab]
    #print(a1)
    #One encoding


    def create_hash_func(size:int):
        '''
        function for creating the hash vecs
        '''
        hash_ex = list(range(1,len(vocab)+1))
        shuffle(hash_ex)#print(hash_ex)
        return hash_ex

    def minHash(vocabSize: int, nbits:int):
        '''
        function for building multiple minHash vecs
        '''
        hashes = []
        for _ in range (nbits):
            hashes.append(create_hash_func(vocabSize))
        return hashes

    #creation of 20 minhash vecs
    minhash = minHash(len(vocab), 20)

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

    aSig = createHash(a1)
    bSig = createHash(b1)



    def signatureInfo(x,y):
        return len(x.intersection(y)) / len(x.union(y)) 



    def split_vec(signature,b):
        assert len(signature) % b == 0
        r = int(len(signature)/b)
        subVectors =[]
        for i in range (0,len(signature),r):
            subVectors.append(signature[i:i+r])
        return subVectors

    band_a = split_vec(aSig,10)
    band_b = split_vec(bSig,10)

    band_a_jacc = [item for sublist in band_a for item in sublist]
    band_b_jacc = [item for sublist in band_b for item in sublist]
    a_jacc = set(band_a_jacc)
    b_jacc = set(band_b_jacc)
    similarity = float(len(a_jacc.intersection(b_jacc))) / len(a_jacc.union(b_jacc))

    return similarity




    