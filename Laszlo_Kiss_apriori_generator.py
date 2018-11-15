# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:08:48 2018

@author: lkiss
"""

import sys
import numpy as np
import random
import pandas as pd

rownum = sys.argv[1]
colnum= sys.argv[2]
density = sys.argv[3]
min_supp = 3

rownum = int(rownum)
colnum = int(colnum)
density = float(density)

#rownum = 10
#colnum= 5
#density = 0.33
#min_supp = 3



#create a dataframe
indexes = random.sample(range(1,rownum*colnum),int(rownum*colnum*density))
array = np.zeros(rownum*colnum)
columns = ["" for x in range(colnum)]
array[indexes] = 1
array = array.reshape(rownum,colnum)
df = pd.DataFrame(array)

for i in range(colnum):
    columns[i] = chr(i+97)
    
df.columns = columns
df_col = pd.DataFrame(columns)


file = open('C:\\SYMBOLIC_DATAMINING\\out.rcf','w')
file.write('#Laszlo Kiss\n')
file.write('[Relational Context]\n')
file.write('Default Name\n')
file.write('[Binary Relation]\n')
file.write('Name_of_dataset\n')
#np.savetxt('C:\\SYMBOLIC_DATAMINING\\out.rcf', array,fmt = '%i')
file.close()


for i in range(rownum):
    if(i == rownum-1):
        file = open('C:\\SYMBOLIC_DATAMINING\\out.rcf','a')
        file.write('o'+str(i+1)+'\n')
        file.close()
    else:
        file = open('C:\\SYMBOLIC_DATAMINING\\out.rcf','a')
        file.write('o'+str(i+1)+' | ')
        file.close()


for i in range(colnum):
    if(i == colnum-1):
        file = open('C:\\SYMBOLIC_DATAMINING\\out.rcf','a')
        file.write(chr(i+97)+'\n')
        file.close()
    else:
        file = open('C:\\SYMBOLIC_DATAMINING\\out.rcf','a')
        file.write(chr(i+97)+' | ')
        file.close()

file = open('C:\\SYMBOLIC_DATAMINING\\out.rcf','a')
file.write('ARRAY_START\n')
file.close()

file = open('C:\\SYMBOLIC_DATAMINING\\out.rcf','a')
np.savetxt(file,df_col,fmt = '%s',newline = ' ')
file.write('\n')
file.close()


file = open('C:\\SYMBOLIC_DATAMINING\\out.rcf','ab')
np.savetxt(file,array,fmt = '%d',delimiter = ' ',newline='\r\n')
file.close()

file = open('C:\\SYMBOLIC_DATAMINING\\out.rcf','a')
file.write('ARRAY_END\n')
file.close()


file = open('C:\\SYMBOLIC_DATAMINING\\out.rcf','a')
file.write('[END Relational Context]')
file.close()



