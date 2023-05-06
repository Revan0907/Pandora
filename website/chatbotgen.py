import tensorflow as tf     
import numpy as np
import pandas as pd
import json 
import nltk
import matplotlib.pyplot as plt
import string
import random
import re
import os, sys
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

def cbinteraction(query):
    tokenizer = Tokenizer(lower=True)


    model = tf.keras.models.load_model(os.path.join(sys.path[0],"website","tensorflow_model"))

    with open(os.path.join(sys.path[0],"website", "intents.json"), "r") as file:
        data = json.load(file)
    tags=[]
    patterns=[]
    responses={}
    for i in data['intents']:
        responses[i['tag']]=i['responses']
        for j in i['patterns']:
            patterns.append(j)
            tags.append(i['tag'])

    frame = pd.DataFrame({"tags":tags, "patterns":patterns})

    #Data Preprocessing - Requires removal of whitespace & punctuation, Tokenization and encoding

        #remove puctuation & whitespace
    frame['patterns'] = frame['patterns'].apply(lambda word:[l.lower() for l in word if l not in string.punctuation])
    frame['patterns'] = frame['patterns'].apply(lambda word: ''.join(word))

        #Tokenize data
    tokenizer = Tokenizer(lower=True)
    tokenizer.fit_on_texts(frame['patterns'])
    train = tokenizer.texts_to_sequences(frame['patterns'])
    x_train = pad_sequences(train)  #padding for data to be of same length for a rnn layer
        #Encoding
    le = LabelEncoder()
    y_train = le.fit_transform(frame['tags'])

    vocab = len(tokenizer.word_index)
    ptrn2seq = tokenizer.texts_to_sequences(frame['patterns'])
    X = pad_sequences(ptrn2seq, padding='post')
    ol = le.classes_.shape[0]


    #query = user input
    print(query) 
    text = []
    txt = re.sub('[^a-zA-Z\']', ' ', query)
    txt = txt.lower()
    txt = txt.split()
    txt = " ".join(txt)
    text.append(txt)
        
    x_test = tokenizer.texts_to_sequences(text)
    x_test = np.array(x_test).reshape(-1)
    x_test = pad_sequences([x_test], padding='post', maxlen=X.shape[1])
    y_pred = model.predict(x_test)
    y_pred = y_pred.argmax()
    tag = le.inverse_transform([y_pred])[0]
    response = random.choice(responses[tag])

    u_msg = "{}".format(query)
    cb_msg = "{}".format(response)
    return u_msg, cb_msg

