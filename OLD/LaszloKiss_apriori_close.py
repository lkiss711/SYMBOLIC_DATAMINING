# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:18:22 2018

@author: lkiss
"""

import sys
import numpy as np
import random
import pandas as pd
import os

os.chdir('C:\\Users\\lkiss\\SYMBOLIC_DATAMINING\\PYTHON_PROJECT')

file = sys.argv[1]
min_supp = sys.argv[2]
min_supp = int(min_supp)


#file = 'out.rcf'
#min_supp = 2

def get_indexes(itemset):
    df_temp = pd.DataFrame()
    
    for i in itemset:
        df_temp[i] = df[i]
        
    
    df_temp['sum'] = df_temp.sum(axis=1)
    
    df_temp = df_temp.loc[df_temp['sum'] == len(itemset)]    

    return(list(df_temp.index.values))


def isclosed_itemset(itemset,min_supp):
    isclosed = 1
    for i in range(len(itemsets)):
        count = 0
        for j in range(len(itemsets)):
            if(itemsets.loc[i,'Indexes'] == itemsets.loc[j,'Indexes']):
                count += 1
        if(count < 2):
            print('Index: ',i, ' ',count)
        
    return isclosed
    
def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

def count_freq (colnamelist):
    "It can decide is this a frequent itemset"
    df_temp = pd.DataFrame
    df_temp = df.loc[:,list(colnamelist)]
    df_temp['sum'] = pd.Series(df_temp.sum(axis = 1),index = df_temp.index)
    return(df_temp['sum'].loc[df_temp['sum'] == len(colnamelist)].count())

my_file=open(file,'r')
txt = my_file.read()

start_pos = find_str(txt, 'ARRAY_START')
end_pos = find_str(txt, 'ARRAY_END')
start_pos += len('ARRAY_START\n')

txt = txt[start_pos:end_pos]
my_file=open('temp.rcf','w')
my_file.write(txt)
my_file.close()


df = pd.read_csv('temp.rcf',sep = ' ')
df = df.iloc[:, :-1]

freq_itemset = []

for colname in df.columns:
    freq_item = df[colname].loc[df[colname] == 1].count()
    if(freq_item >= min_supp):
        freq_itemset.append(colname)

item_set_name_len = 1
max_item_set_name_len = len(freq_itemset)



while item_set_name_len < max_item_set_name_len:
    for i in range(0,len(freq_itemset)):
        for j in range(i,len(freq_itemset)):
            if(i != j) and (freq_itemset[i][:-1] == freq_itemset[j][:-1]) and len(freq_itemset[i]) == item_set_name_len:
                freq_itemset.append(freq_itemset[i]+freq_itemset[j][-1])
    item_set_name_len += 1

    
itemsets = pd.DataFrame(columns = ['Itemset','Len','Freq','Indexes','Isclosed'])


for i in range(len(freq_itemset)):
    itemsets.loc[i] = [freq_itemset[i],len(freq_itemset[i]),count_freq(freq_itemset[i]),get_indexes(freq_itemset[i]),1]
    itemsets.loc[i,'Indexes'] = ''.join(str(e) for e in itemsets.loc[i,'Indexes'])


itemsets['Isclosed'] = itemsets.groupby(['Len','Indexes'])['Itemset'].transform("count")


valid_itemsets = pd.DataFrame()

valid_itemsets = itemsets.loc[itemsets['Freq'] >= min_supp]

valid_itemsets = valid_itemsets.loc[valid_itemsets['Isclosed'] == 1]

valid_itemsets.to_csv('valid_closeditemsets.rcf',sep = '\t')


        
    


