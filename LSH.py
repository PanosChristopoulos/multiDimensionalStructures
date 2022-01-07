import io 
import pandas as pd 
from random import shuffle
#Data 
#try
a = "flying fish flew by the space station"
b = "he will not allow you to bring your sticks of dynamite and pet armadillo "
c = "he figured a few sticks of dynamite were easier than a fishing pot"
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
c = shingle(c,k)#print(c)
#Call function shingle

#Make the vocabulary of our texts
vocab= list(a.union(b).union(c))
#print(vocab)
#Make the vocabulary of our texts


#One encoding
a1 = [1 if x in a else 0 for x in vocab]
b1 = [1 if x in b else 0 for x in vocab]
c1 = [1 if x in c else 0 for x in vocab]
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
# Create Signatures
aSig = createHash(a1)
bSig = createHash(b1)
cSig = createHash(c1)

#print(aSig)
#print(bSig)
#print(cSig)


#Signature info
def signatureInfo(x,y):
    return len(x.intersection(y)) / len(x.union(y)) 

#print(signatureInfo(c,b))


def split_vec(signature,b):
    assert len(signature) % b == 0
    r = int(len(signature)/b)
    #Split signature in b parts
    subVectors =[]
    for i in range (0,len(signature),r):
        subVectors.append(signature[i:i+r])
    return subVectors
band_a = split_vec(aSig,10)
band_b = split_vec(bSig,10)
band_c = split_vec(cSig,10)
#print(band_b)
for aRows ,bRows in zip(band_a,band_b):
    if aRows == bRows :
        print (f"Pair:{aRows} = {bRows}")
        print('a=b')
        break

for aRows ,cRows in zip(band_a,band_c):
    if aRows == cRows :
        print (f"Pair:{aRows} = {cRows}")
        print('a=c')
        break

for bRows ,cRows in zip(band_b,band_c):
    if bRows == cRows :
        print (f"Pair:{bRows} = {cRows}")
        print('b=c')
        break
 
    '''
import pandas as pd
 import io 

 url =''

text = request.get(url).text 

data = pd.read_csv(io.StringIO(text),sep='\t')
data.head() 
    '''

 
