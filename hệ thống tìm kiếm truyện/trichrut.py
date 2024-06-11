from tkinter import *
import tkinter
from tkinter import ttk
import glob, os
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import pandas as pd
import fitz
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
from tkinter import Tk, Label, Text, font
import json


#doc file
def readfiles(path, pdfs):
   os.chdir(path)
#    pdfs = []
   for file in glob.glob("*.pdf"):
       # print(file)
       pdfs.append(file)
pdfs = []
readfiles('C:/Users/DELL G7/BTL-HCSDLDPT/data2',pdfs)

def dummy_fun(doc):
    return doc
# tạo danh sách trống để lưu nội dung các file PDF
documents = []

#doc pdf
for fname in pdfs:
    doc = fitz.open(fname)
    text = ''
    for page in doc:
        text += page.get_text()
    documents.append(text)

#chuyen text sang chu thuong và bo dau cau
lower_documents = []
i = 0
for document in documents:
    i+=1
    new_string = document.lower().translate(str.maketrans('', '', string.punctuation))
    lower_documents.append(new_string)

#token doan van ban # tách nội dung các văn bản thành các từ riêng lẻ

list_of_tokens_without_sw = []
i = 0
print("Dang token doan van ban")
for lower_document in lower_documents:
    text_tokens = word_tokenize(lower_document)
    list_of_tokens_without_sw.append(text_tokens)
    i += 1
    print(i, end = ' ')

preprocess_token_list = []
i = 0

print("\nDang tien xu ly")

for tokens in list_of_tokens_without_sw:
    i+=1
    print(i,end = ' ')
    tmp = []
    for token in tokens:
        if token.isalpha() and len(token) > 1:
            tmp.append(token)
    preprocess_token_list.append(tmp)

filter_preprocess_token_list = []
i = 0

stopwords = nltk.corpus.stopwords.words('english')
print('\nDang loai bo stopwords')
for token_list in preprocess_token_list:
    filtered_words = [word for word in token_list if word not in stopwords]
    filter_preprocess_token_list.append(filtered_words)
    i+= 1
    print(i,end = ' ')

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)

# Lưu danh sách vào tệp JSON
save_to_json(filter_preprocess_token_list, 'C:/Users/DELL G7/BTL-HCSDLDPT/filter_preprocess_token_list.json')





