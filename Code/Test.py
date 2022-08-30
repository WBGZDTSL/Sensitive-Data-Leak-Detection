# Library
import numpy as np
import pandas as pd
import string
from datetime import datetime
from pathlib import Path

path='C:\\Users\\jweiban\\OneDrive - Johnson Controls\\Desktop\\work\\Work_Record_Bannguo Wei\\sensitive data leak detection\\'
#%%
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.corpus import stopwords
import re
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

def wordprocess(s):
    #s=str(s)
    s = str(s).lower()
    cleanr = re.compile('<.*?>')# string
    cleantext = re.sub(cleanr, '', s)# transform string to
    tokenizer = RegexpTokenizer(r'p&l|m&a|[\u4e00-\ufaff]+|[0-9]+|[a-zA-Z]+\'*[a-z]*')
    #tokenizer = RegexpTokenizer(r"\s|[\.,;'/\\\-:\(\)_]", gaps=True)
    tokens = tokenizer.tokenize(cleantext)
    #print(tokens)
    return tokens

#%%
Data = pd.read_csv(path+'Data\\Data_file_name_copy.csv', encoding='utf-8')
File_Suffix= pd.read_csv(path+'Data\\File_Suffix.csv')
Data_filename = Data['File_Name']
Data['File_size'] = [x.rpartition('-')[2] for x in Data['File_Name']]
Data['Suffix_File'] = [x.rpartition('-')[0].rpartition('.')[2] for x in Data['File_Name']]
List_suffix = File_Suffix['Suffix'].tolist()
Suffix = Data['Suffix_File'].tolist()
Data['File_suffix'] = [x if x in List_suffix else None for x in Suffix]
Data['word_list']=Data['File_Name'].map(lambda s:wordprocess(s))
#Data_Keywords = pd.read_csv(path+'Data\\key_words_collection.csv',encoding='utf-8' )
Data_Keywords = pd.read_excel(path+'Data\\key_words_collection.xlsx', sheet_name="Sheet1")
