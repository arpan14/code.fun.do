import numpy as np
import pandas as pd
import csv
#import querycsv.py as qu

#just reading a file in csv format with specified headers
print pd.read_csv('sample.csv')

#reading a file in csv format with unspecified headers
#print pd.read_csv('sample2.csv',header=None)

#reading a file in csv format with user specified headers
#print pd.read_csv('sample.csv',names=['name','ID','Department','Ins','Hobby'])


#a=DataFrame.from_csv('sample.csv')
#a.head()

#(a.assign(new_id=a['id']+2).head())
#print a