# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 11:47:01 2018

@author: lkiss
"""

import sys
import numpy as np
import random
import pandas as pd
import os
import itertools

os.chdir('C:\\Users\\lkiss\\SYMBOLIC_DATAMINING\\PYTHON_PROJECT')

#file = sys.argv[1]
#min_supp = sys.argv[2]
#min_supp = int(min_supp)


file = 'out.rcf'
min_supp = 3


def get_freq(itemset):

    x = ''.join(str(e) for e in itemsets.loc[itemsets['Itemset'] == itemset]['Freq'])

    x = int(x)

    return x
    

    
def create_rules_from_itemset(itemset):

    def create_second_tag(itemset,rule_str):
        for i in range(0,len(rule_str)):
            right_tag = itemset.replace(rule_str[i],'')
            itemset = right_tag

        return right_tag
    list_rule = list()
    list_rule_right_tag = list() 
    ass_rules = pd.DataFrame()
    
    current_len = 1
    while current_len < len(itemset)+1:
        current_rule_list = list()
        current_rule_list = list(itertools.combinations(itemset, current_len))
        length = len(current_rule_list)
        for i in range(0,length):
            str_rule = ''
            for j in range(0,len(current_rule_list[0])):
                str_rule += current_rule_list[i][j]
                if (len(str_rule) == current_len) & (len(str_rule) != len(itemset)):
                    list_rule.append(str_rule)
                    list_rule_right_tag.append(create_second_tag(itemset,str_rule))
        current_len += 1

    se = pd.Series(list_rule)
    ass_rules['left_tag'] = se.values

    se = pd.Series(list_rule_right_tag)
    ass_rules['right_tag'] = se.values

    ass_rules['itemset'] = itemset

    return ass_rules

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

    
itemsets = pd.DataFrame(columns = ['Itemset','Len','Freq'])


for i in range(len(freq_itemset)):
    itemsets.loc[i] = [freq_itemset[i],len(freq_itemset[i]),count_freq(freq_itemset[i])]
    
valid_itemsets = itemsets.loc[itemsets['Freq'] >= min_supp]

all_rules = pd.DataFrame(columns = ['left_tag','right_tag','itemset','conf','supp','suppL','suppR'])

for i in range(len(valid_itemsets)):
#    print(valid_itemsets.iloc[i]['Itemset'])
    all_rules = all_rules.append(create_rules_from_itemset(valid_itemsets.iloc[i]['Itemset']))

all_rules = all_rules.reset_index()
del all_rules['index']

for i in range(len(all_rules)):
    all_rules.loc[i]['conf'] = get_freq(all_rules.loc[i]['itemset'])/get_freq(all_rules.loc[i]['left_tag'])
    all_rules.loc[i]['supp'] = get_freq(all_rules.loc[i]['itemset'])/(max_item_set_name_len+1)        
    all_rules.loc[i]['suppL'] = get_freq(all_rules.loc[i]['left_tag'])/(max_item_set_name_len+1)        
    all_rules.loc[i]['suppR'] = get_freq(all_rules.loc[i]['right_tag'])/(max_item_set_name_len+1)        
    
