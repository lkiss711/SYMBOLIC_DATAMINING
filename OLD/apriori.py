# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:16:59 2018

@author: lkiss
"""

import sys
import numpy as np
import random
import pandas as pd

#rownum = sys.argv[1]
#colnum= sys.argv[2]
#density = sys.argv[3]
#min_supp = 3
#
#rownum = int(rownum)
#colnum = int(colnum)
#density = float(density)

rownum = 10
colnum= 5
density = 0.75
min_supp = 3


print(sys.argv[0])

def count_freq (colnamelist):
    "It can decide is this a frequent itemset"
    df_temp = pd.DataFrame
    df_temp = df.loc[:,list(colnamelist)]
    df_temp['sum'] = pd.Series(df_temp.sum(axis = 1),index = df_temp.index)
    return(df_temp['sum'].loc[df_temp['sum'] == len(colnamelist)].count())

#create a dataframe
indexes = random.sample(range(1,rownum*colnum),int(rownum*colnum*density))
array = np.zeros(rownum*colnum)
columns = ["" for x in range(colnum)]
array[indexes] = 1
array = array.reshape(rownum,colnum)
df = pd.DataFrame(array)
df_apriori = pd.DataFrame()


for i in range(colnum):
        columns[i] = chr(i+97)

df.columns = columns


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

    
itemsets = pd.DataFrame(columns = ['Itemset','Len','Freq'])


for i in range(len(freq_itemset)):
    itemsets.loc[i] = [freq_itemset[i],len(freq_itemset[i]),count_freq(freq_itemset[i])]

valid_itemsets = pd.DataFrame()

valid_itemsets = itemsets.loc[itemsets['Freq'] >= min_supp]