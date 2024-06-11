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

def load_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# # Lưu danh sách vào tệp JSON
# save_to_json(filter_preprocess_token_list, 'C:/Users/DELL G7/BTL-HCSDLDPT/filter_preprocess_token_list.json')

# Đọc từ tệp JSON và khôi phục lại danh sách
filter_preprocess_token_list = load_from_json('C:/Users/DELL G7/BTL-HCSDLDPT/filter_preprocess_token_list.json')


#giao dien
window = Tk()
window.title('Tìm kiếm')
window.geometry('1000x1000')

# Thiết lập font chữ
custom_font = font.Font(family="Helvetica", size=10, weight="bold")
# Label
lbl = Label(window, text='Nhập nội dung tìm kiếm:', font=custom_font, fg='black', bg='#FFB6C1')  
lbl.grid(column=0, row=0, pady=20, sticky='N')
# Thiết lập màu nền và màu chữ cho cửa sổ
window.configure(bg='#FFB6C1')
# #label
# lbl = Label(window, text= 'Input searching string:', font=('Arial', 10))
# lbl.grid(column=0,row=0)
#o tim kiem
input_txt = tkinter.Text(window,width=90,height=30)
input_txt.grid(column=5,row = 1)

query = ''





#function nut search
def retrieve_input():
    inputValue=input_txt.get("1.0","end-1c")
    print(inputValue)
    querry = inputValue
    new_querry = querry.lower().translate(str.maketrans('', '', string.punctuation))
    text_token = word_tokenize(new_querry)
    filtered_querry = list(text_token)
    tfidf = TfidfVectorizer(
        analyzer='word',
        tokenizer=dummy_fun,
        preprocessor=dummy_fun,
        token_pattern=None)
    filter_preprocess_token_list.append(filtered_querry)
    X = tfidf.fit_transform(filter_preprocess_token_list)

    cosine_similarities = linear_kernel(X[0:199], X[X.shape[0]-1]).flatten()
    idx_top_k_score = (-cosine_similarities).argsort()[:3]


    # root de show data
    root = Tk()

    frm = Frame(root)
    frm.pack(padx=0, pady=0, anchor=NW)

    tv = ttk.Treeview(frm, columns=(1, 2), show='headings')
    tv.grid(row=0, column=0)
    
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("Treeview", rowheight=40)
    
    tv.column("# 1", anchor=CENTER, width=30)
    tv.heading("# 1", text="Độ tương đồng")
    tv.column("# 2", anchor=W, width=500)
    tv.heading("# 2", text="Tên")
    root.title('Kết quả')
    root.geometry('500x230')
    root.resizable(True, TRUE)

    for i in idx_top_k_score:
        print(
            f"Top {i} match ({cosine_similarities[i]}):\n\n", pdfs[i] + "..." + "\n"
        )
        tv.insert(parent='', index='end', text='Parent', values=(cosine_similarities[i], pdfs[i]))
    root.mainloop()

search_btn = Button(window,text='Search',command=retrieve_input)
search_btn.grid(column=5, row = 20, pady=30)

window.mainloop()




