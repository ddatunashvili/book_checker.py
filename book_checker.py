#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
განსაზღვროს წიგნის გავლენიანობა
• შეიქმნას გავლენიანი სიტყვების სია csv (ძლიერ ემოციური სიტყვები, ჟანრის სიტყვები) : +
• ააგოს წინადადებების dataframe: +
• შეამოწმოს რამდენი გავლენიანი სიტყვაა წინადადებაში: +
• გავლენიანი სიტყვების ოდენობა გაყოს წინადადების ყველა სიტყვაზე(IPS) : +
• აიჯამოს გავლენიანი წინადადებების ოდენობა
• გავლენიანი წინადადებების ოდდენობა გაყოს ყველა წინადადების ოდენობაზე
• თუ განაყოფი მეტია 50% დააბრუნოს True თუ არა False
'''
import  pandas as pd
# შეიქმნას გავლენიანი სიტყვების სია(ძლიერ ემოციური სიტყვები)
filter_name= input('შეიყვანეთ ფილტრის ფაილის path .csv: ')
filt = pd.read_csv(filter_name)
#-------------------------------------------------

import re
import  csv
path = input('შეიყვანეთ წიგნიის path/to/name.txt: ')
book =  open(path,'r', encoding='utf-8')

text = ''.join(book.readlines())
sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
# print(type(sentences))
data = []
for i in sentences:    
    data.append(f'{i}')
import  csv

# წინადადებების დატა
sentences = pd.DataFrame()
sentences['sentences'] = data
IPS_base=[]
word_IPS=[]
for srow in sentences['sentences']:
    filtered=0
    for frow in filt['scienceFilter']:
        words = srow.split()
        for word in words:
            if str(word) == str(frow):
                filtered = filtered+1
                
            else:
                pass
    # count IPS (true sum) / (word sum)
    if len(words) !=0 : 
        IPS =filtered/len(words)
        if IPS !=0:
            IPS_base.append(IPS)
#create base
base = pd.DataFrame()
base['influence'] =  IPS_base 
#-------------------------------------------------
# ამ კოეფიციენტების ჯამის კვადრატის გასაშუალოება ხდება
# მერე  იყოფა ფესვი საერთო წინადადებების რაოდენობაზე
import pandas as pd
import numpy as np
# root mean square
rms = lambda d: d.sum ()
index = sentences. index

influence =  rms(base.influence)/len(sentences.index)*100
if influence > 50:
    print(f'This book has a {influence}% influence')
else:
    print(f'This book has a no influence')