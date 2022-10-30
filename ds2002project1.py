#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:46:44 2022

@author: skyejung
"""

#%%

'''
Import Packages
'''

import json
import csv
import pandas as pd
import numpy as np

## url: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams


#%%

'''
Benchmark 1.1 : Retrieve data file
'''

file = '/Users/skyejung/Desktop/ds 2002/StudentsPerformance.csv'

## url: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

scores = pd.read_csv(file)
print(scores.head(10))


#%%

'''
Benchmark 1.2 : Converting general format and data structure of the data source
'''

## CSV to JSON

examscsv = open('/Users/skyejung/Desktop/ds 2002/StudentsPerformance.csv','r')
examsjson = open('/Users/skyejung/Desktop/ds 2002/examsjson.json','w')

variables = ("Gender","Race/Ethnicity","Parental Level of Education","Lunch",
             "Test Preparation Course","Math Score","Reading Score","Writing Score")

reader = csv.DictReader(examscsv,variables)

for each in reader:
    json.dump(each,examsjson)
    examsjson.write('\n')
    json.dumps(each,sort_keys=False,indent=4,separators=(',',': '))


#%%

'''
Benchmark 1.3 : Modifying the number of columns from the source to the destination
'''

## New column for total average score among math, reading, and writing scores
## New column if observation's total average score is above or below average of all observations

scores_mod = scores.copy()

scores_mod['avg'] = scores_mod[['math score', 'reading score','writing score']].mean(axis=1)

total_avg = np.mean(scores_mod['avg'])

condition = [scores_mod['avg']>total_avg]

value=[1]

scores_mod['above average'] = np.select(condition,value)

scores_mod.to_csv('/Users/skyejung/Desktop/ds 2002/scores_mod.csv')


#%%

'''
Benchmark 1.5 : Generate a brief summary of the data file ingestion
'''

cols = len(scores_mod.columns)
rows = len(scores_mod)

print("Number of Records:",rows)  
print("Number of Columns:",cols)  
print("")
print("First Five Rows of Modified Data Set:")
print(scores_mod.head(10))   


#%%

'''
Benchmark 2 : Processor produces informative errors should it be unable to complete an operation
'''

## Input gender and race group and processor outputs total average of all observations that meet the demographic requirements
## if input invalid, outputs error

scores_mod2 = scores_mod.copy()
scores_mod2['race/ethnicity'] = scores_mod['race/ethnicity'].str.lower()

try:
    gender_input = input("Input Gender: ")
    race_input = input("Input Race Group: ")
    gender_input2 = gender_input.lower().strip()
    race_input2 = race_input.lower().strip()# lower case and strip white space off the input
    if (scores_mod2['gender'] == gender_input2).any():
        gender = scores_mod2[scores_mod2['gender']==gender_input2]
        race = gender[gender['race/ethnicity']==race_input2]
        mean = np.mean(race['avg'])
        print("Average Score: ",np.round(mean,3))
    elif (scores_mod2['gender'] != gender_input2).any():
        raise Exception("ERROR: Gender/Race combination not in system or input is invalid")  # raising an exception for error line
except Exception:
    print("ERROR: Gender/Race combination not in system or input is invalid")









