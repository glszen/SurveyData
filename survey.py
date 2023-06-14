# -*- coding: utf-8 -*-
"""
**********Product Impact of Fitness Data Analysis**********
**********@author: gulsen************
"""
""" *********************************************************************** """
""" 

Libraries
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

""" *********************************************************************** """
"""
Data import
"""

data=pd.read_csv(r'C:\Users\LENOVO\Desktop\data_science\Survey_Data\survey.csv')

data.head()


""" *********************************************************************** """

"""
Data Preparation
"""

data.shape

data.size

data.columns

data.isnull().sum()

data.duplicated().value_counts()

data.info()

data.drop(['Timestamp'], axis=1, inplace=True)

data.rename(columns={'What is your age?':'Age', 'What is your gender?':'Gender', 
'What is your highest level of education?':'Education', 'What is your current occupation?':'Occupation', 
'How often do you exercise in a week?':'Workout Freq per Week', 
'How long have you been using a fitness wearable?':'Usage Duration', 
'How frequently do you use your fitness wearable?':'Freq Usage', 
'How often do you track fitness data using wearable?':'Tracking data', 
'How has the fitness wearable impacted your fitness routine?':'Fitness Routine', 
'Has the fitness wearable helped you stay motivated to exercise?':'Motivation', 
'Do you think that the fitness wearable has made exercising more enjoyable?':'Enjoyment', 
'How engaged do you feel with your fitness wearable?':'Engagement', 
'Does using a fitness wearable make you feel more connected to the fitness community?':'Connection', 
'How has the fitness wearable helped you achieve your fitness goals?':'Fitness Goals', 
'How has the fitness wearable impacted your overall health?':'Health', 
'Has the fitness wearable improved your sleep patterns?':'Sleep', 
'Do you feel that the fitness wearable has improved your overall well-being?':'Well Being', 
'Has using a fitness wearable influenced your decision? [To exercise more?]':'Exercise More', 
'Has using a fitness wearable influenced your decision? [To purchase other fitness-related products?]':'Purchase Products', 
'Has using a fitness wearable influenced your decision? [To join a gym or fitness class?]':'Join Gym', 
'Has using a fitness wearable influenced your decision? [To change your diet?]':'Change Diet'}, inplace=True)

""" *********************************************************************** """

"""
VISUALIZE
"""


gender_count=data['Gender'].value_counts()
fig, ax=plt.subplots()
ax.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%')
ax.set_title('Gender Distribution')
plt.show()

age_count=data['Age'].value_counts()
fig, ax=plt.subplots()
ax.pie(age_count, labels=age_count.index, autopct='%1.1f%%')
ax.set_title('Age Distribution')
plt.show()

fig,ax=plt.subplots()
education_count=data['Education'].value_counts()
ax.pie(education_count, labels=education_count.index, autopct='%1.1f%%')
ax.set_title('Education Distribution')
plt.show()

fig, ax=plt.subplots()
occupation_count=data['Occupation'].value_counts()
ax.pie(occupation_count, labels=occupation_count.index, autopct='%1.1f%%')
ax.set_title('Occupation Distibution')
plt.show()

workout_week=data['Workout Freq per Week'].value_counts()
ax=workout_week.plot(kind='barh', color='deeppink')
ax.set_xlabel('Workout Freq per Week')
ax.set_ylabel('Count')
ax.set_title('Workout frequency in a week')

for i, count in enumerate(workout_week):
    ax.text(count+0.4, i-0.1, str(count),fontsize=10)
plt.show()



usage_duration=data['Usage Duration'].value_counts()
ax=usage_duration.plot(kind='bar', color='purple')
ax.set_xlabel('Usage Duration')
ax.set_ylabel('Count')
ax.set_title('Use of Fitness Wearable')

for i, count in enumerate(usage_duration):
     ax.text(i, count+0.1, str(count),ha='center', fontsize=10)
plt.show()


freq_usage=data['Freq Usage'].value_counts()
ax=freq_usage.plot(kind='bar', color='darkgreen')
ax.set_xlabel('Freq Usage')
ax.set_ylabel('Count')
ax.set_title('Frequent Use of Fitness Wearable')

for i, count in enumerate(freq_usage):
    ax.text(i, count+0.1, str(count), ha='center', fontsize=10)
plt.show()

tracking_data=data['Tracking data'].value_counts()
ax=tracking_data.plot(kind='bar', color='red')
ax.set_xlabel('Tracking data')
ax.set_ylabel('Count')
ax.set_title('Tracking data using Fitness Wearable')

for i, count in enumerate(tracking_data):
    ax.text(i, count+0.1, str(count), ha='center', fontsize=9)
plt.show()

fitness_goals=data['Fitness Goals'].value_counts()
ax=fitness_goals.plot(kind='bar', color='pink')
ax.set_xlabel='Fitness Goals'
ax.set_ylabel='Count'
ax.set_title('Achieved Fitness Goals')

for i, count in enumerate(fitness_goals):
    ax.text(i, count+0.1, str(count), ha='center', fontsize=10)
plt.show()

purchase_products=data['Purchase Products'].value_counts()
ax=purchase_products.plot(kind='bar', color='yellowgreen')
ax.set_xlabel('Purchase Products')
ax.set_ylabel=('Count')
ax.set_title('Purchase Products')

for i, count in enumerate(purchase_products):
    ax.text(i, count+0.1,str(count), ha='center', fontsize=10)
plt.show()

health=data['Health'].value_counts()
ax=health.plot(kind='bar', color='brown')
ax.set_xlabel=('Health')
ax.set_ylabel=('Count')
ax.set_title('Impact on Health')

for i, count in enumerate(health):
    ax.text(i, count+0.1, str(count), ha='center', fontsize=10)
plt.show()



change_diet=data['Change Diet'].value_counts()
ax=change_diet.plot(kind='bar', color='violet')
ax.set_xlabel=('Change Diet')
ax.set_ylabel=('Count')
ax.set_title('Change Diet')

for i, count in enumerate(change_diet):
    ax.text(i, count+0.1, str(count), ha='center', fontsize=10)


fig, ax=plt.subplots()    
join_gym=data['Join Gym'].value_counts()
ax=join_gym.plot(kind='bar', color='indigo')
ax.set_xlabel=('Join Gym')
ax.set_ylabel=('Count')
ax.title('Join Gym')

for i, count in enumerate(join_gym):
    ax.text(i, count+0.1, str(count), ha='center', fontsize=10)