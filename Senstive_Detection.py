#Library
import numpy as np
import pandas as pd
import os
import spacy
import pytextrank
#%%Data
Data = pd.read_excel(r'C:\Users\jweiban\OneDrive - Johnson Controls\Documents\GitHub\Sensitive-Data-Leak-Detection\File_Location_Template.xlsx',sheet_name='Sheet1',index_col='Num')
#%% List Extraction
# Storage_List = []
# for i in Data['File_Location']:
#     a = os.path.split(i)
#     Storage_List.extend(a)
#     print (Storage_List)

Storage_List2= []
for i in Data['File_Location']:
    Storage_List2.extend(i.split('\\',-1))
    print (Storage_List2)
#Display
for i in Storage_List2:
    print(i)

#%%pytextrank
# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_sm")
# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")
nlp.analyze_pipes(pretty=True)# check details
doc = nlp('C:\\Users\\jweiban\\OneDrive - Johnson Controls\\Documents\\GitHub\\Sensitive-Data-Leak-Detection')# just Example

# examine the top-ranked phrases in the document
for phrase in doc._.phrases:
    print(phrase.text)
    print(phrase.rank, phrase.count)
    print(phrase.chunks)