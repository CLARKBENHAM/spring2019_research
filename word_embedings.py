# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 13:09:55 2019

@author: Clark Benham
"""


import re
commands = [i for i in """“Hey Google, set the <room> thermostat to 22.”

To set thermostat using the thermostat's name
"Hey Google, set <thermostat> to 20°C."

To hear the ambient temperature on the thermostat
“Hey Google, what’s the <room> temperature inside?”

To hear what the temperature is set to on the thermostat
“Hey Google, what’s the <room> thermostat set to?”

Increase/Decrease the temperature on all thermostats
"Hey Google, make it warmer/cooler.”
(on Alexa for 1 degree, on Google Assistant for 3 degrees)

Increase/Decrease the temperature using the thermostat's room name
"Hey Google, raise/lower the temperature in the <room>." 

Increase/Decrease the temperature using the thermostat's name
"Hey Google, raise/lower the temperature of <thermostat>."

Increase/Decrease the temperature in all rooms for X degrees
“Hey Google, raise/lower the temperature by 2 degrees.”

Increase/Decrease the temperature of thermostat for X degrees
"Hey Google, raise/lower the temperature of <thermostat> by 2 degrees.” 

To switch heating or cooling for all rooms modes¹
“Hey Google, turn on the heating/cooling."
"Hey Google, turn on the heat." 

To switch heating or cooling for a specific room/thermostat¹
"Hey Google, set <thermostat> to heating/cooling/automatic.”
"Hey Google, turn the <thermostat> to heat/cool/automatic (mode)."
"Hey Google, make it warmer/cooler in the <room>" """.split("\n") if len(i) >0 and (i[0] == '“' or i[0] == '"')]

#%%
import pandas as pd
import sys
import csv
maxInt = sys.maxsize
import numpy as np
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
        
#embedings = pd.read_csv()
                        #, engine='python', error_bad_lines=False, sep=" ", header = None)
import os
embeddings_index = {}
file_loc = "glove_word_embeddings\glove.6B.100d.txt"
with open(file_loc, encoding="utf8") as f:
    for line in f:
        word, coefs = line.split(maxsplit=1)
        try:
            coefs = np.fromstring(coefs, 'f', sep=' ')
            embeddings_index[word] = coefs
        except:
            pass
#%%
words = set([re.search("[cxa-zA-Z]+",j).group().lower() for i in commands for j in i.split(" ") if re.search("[a-zA-Z]+",j)])
vecs = pd.DataFrame(data = {w:embeddings_index[w] for w in words if w in embeddings_index})

from sklearn.decomposition import PCA
pca = PCA(n_components = 5)
pca.fit(vecs.iloc[:,1:])
print(f"Word Variance explained: {pca.explained_variance_ratio_}")
#%%m,
#ToDo get Elmo to measure the complexity of words in context
import h5py
pth = "glove_word_embeddings\elmo_2x1024_128_2048cnn_1xhighway_weights.hdf5"
f = h5py.File("glove_word_embeddings\elmo_2x1024_128_2048cnn_1xhighway_weights.hdf5")
data = f['char_embed']
# data = pd.read_hdf("glove_word_embeddings\elmo_2x1024_128_2048cnn_1xhighway_weights.hdf5", key="char_embed")
pca.fit(data)
print(f"Word Variance explained: {pca.explained_variance_ratio_}")


#%%
#Todo get measure of syntatical complexity

print("""
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out
out""".count("out"))
