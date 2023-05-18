#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project: no show dataset
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# This dataset collects information
# from 100k medical appointments in
# Brazil and is focused on the question
# of whether or not patients show up
# for their appointment. A number of
# characteristics about the patient are
# included in each row.
# ● ‘ScheduledDay’ tells us on
# what day the patient set up their
# appointment.
# ● ‘Neighborhood’ indicates the
# location of the hospital.
# ● ‘Scholarship’ indicates
# whether or not the patient is
# enrolled in Brasilian welfare
# program Bolsa Família.
# ● Be careful about the encoding
# of the last column: it says ‘No’ if
# the patient showed up to their
# appointment, and ‘Yes’ if they
# did not show up.
# 
# 
# 
# ## importing libraries

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

import seaborn as snb
get_ipython().run_line_magic('matplotlib', 'inline')
# to show plots in jupyter notebook
# libraries that i will use 


# In[ ]:





# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# 
# 

# In[2]:


# Loading the data 

df= pd.read_csv("noshowappointments-kagglev2-may-2016.csv")
df.head()


# # reading data

# # here is a mathmatical summary of data 

# In[3]:



df.describe()



# min year is -1 and this is impossible ,so that is a wrong value so i will deal with that later


# Average age is 37-38 , Oldest age is 115 

# In[4]:


df.duplicated().sum()


# that is mean that there is no duplicate values

# In[5]:


df["PatientId"].duplicated().sum()


# means there is 48228 duplicated ID  

# In[6]:


df['PatientId'].nunique()


# there is 62299 unique values out of 110527

# In[7]:


df.duplicated(["PatientId","No-show"]).sum()


# mean that there is a number 38710 of duplicated tries for patients to attend
#  so , i will drop these

# In[8]:


df.drop_duplicates(['PatientId','No-show'],inplace= True)
df.shape


# I had dropped the duplicated tries for the patients.
#  the dataset contains 71817 appointments.

# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:


df.drop(['PatientId','AppointmentID','ScheduledDay','AppointmentDay'],axis=1,inplace=True)
#checking
df.head()


# Iam dropping these columns ( patient id ,appointmentid,ScheduledDay,AppointmentDay) As it will not help me in my analysis

# In[10]:


df.info()
# here  i found that there is no empty cell


# # there is no missing values

# # note 
# There Is a wrong value in age=-1 so I will delete that appointment

# In[11]:


wrong_Ans=df.query("Age==-1")
wrong_Ans


# In[12]:


df.drop(index=99832,inplace=True)
# here i found that there is only one appointment containing -1 age so i will drop that
# checking
wrong_Ans=df.query("Age==-1")
wrong_Ans


# In[ ]:





# # I will rename No-show to No_show
# 

# In[13]:


df.rename(columns={"No-show":"No_show"},inplace=True)
df.rename(columns={"Hipertension":"Hypertension"},inplace=True)
df.head()


# 
# 
# 
# 
# ### Research Question 1 (Age of customers , get to know customers)

# 
#  here is a describe of the customer that we deal with 
# 

# most of them are not taking alcohol or diabetes

# most of them are not HANDCAP

# most of them are not hipertension but there is a percent of hipertension(15000)

#  most of them have received sms

# In[14]:


df.hist(figsize=(16,10));


# # i will divide appointments into two group, the group that had attend and the group that hadnot

# In[15]:



noshow = df.No_show == 'Yes'
show = df.No_show == 'No'


df[show].count(),df[noshow].count()
   


# there is a 54153 patients that had attend

# there is a 17663 patients that had not attend
# 

# which means patients that had attend is 3 times that hadnot

# In[16]:


def AGE_vs_attend(df,col_name,attend,apsent):
    plt.figure(figsize=[13,8])
    df[col_name][show].hist(alpha=.5,bins=10,color='red',label='attend')
    df[col_name][noshow].hist(alpha=.5,bins=10,color='black',label='apsent')
    plt.legend()
    plt.title('Relation bet. age and attendence')
    plt.xlabel('AGE')
    plt.ylabel('numbers of patients');
AGE_vs_attend(df,'Age',show,noshow)


# Age from(0-8) are most showing, which means that there is a lot of parents showing up

# Age from(45-55) are the second showing patients

# the least attending patients is at Age (65-85)
# 

# In[ ]:





# ### Research Question 2  (Factors affecting attendence)

# In[ ]:





# In[ ]:





# In[20]:


def Gender_vs_attend(df,col_name,attend,apsent):
    plt.figure(figsize=[8,5])
    df[col_name][show].value_counts(normalize=True).plot(kind='pie',label='show')
    plt.legend()
    plt.title('Relation bet. Gender and attendence')
    plt.xlabel('Gender')
    plt.ylabel('numbers of patients');
    
Gender_vs_attend(df,'Gender',show,noshow)


# In[19]:


def Gender_vs_attend(df,col_name,attend,apsent):
    plt.figure(figsize=[8,5])
    df[col_name][noshow].value_counts(normalize=True).plot(kind='pie',label='show')
    plt.legend()
    plt.title('Relation bet. Gender and attendence')
    plt.xlabel('Gender')
    plt.ylabel('numbers of patients');
    
Gender_vs_attend(df,'Gender',show,noshow)


# there is no relation bet attendence and gender

# In[21]:


plt.figure(figsize=[16,5])
df[show].groupby(['Hypertension','Diabetes']).mean()['Age'].plot(kind='bar',color='red',label='show')
df[noshow].groupby(['Hypertension','Diabetes']).mean()['Age'].plot(kind='bar',color='blue',label='noshow')
plt.legend();
plt.title("Relation bet. age and diseases")
plt.xlabel('diseases')
plt.ylabel('Average Age');


# In[22]:


df[noshow].groupby(["Hypertension","Diabetes"]).mean()['Age']


# mean age of non choronic diseases  that had not attend is 28 years

# mean age of Hypertension   patients that hadnot attend is 58 , and 49 of diabetes patients

# In[23]:


df[show].groupby(["Hypertension","Diabetes"]).mean()['Age']


# mean age of non choronic diseases that had  attend is 30 years

# mean age of Hypertension patients that had attend is 60 , and 53 of diabetes patients
# 

# that means there is a relation bet age and choronic disease 

# In[34]:


def Sms_vs_attend(df,col_name,attend,apsent):
    plt.figure(figsize=[13,8])
    df[col_name][show].hist(alpha=.5,bins=10,color='red',label='attend')
    df[col_name][noshow].hist(alpha=.5,bins=10,color='black',label='apsent')
    plt.legend()
    plt.title('Relation bet. sms messages and attendence')
    plt.xlabel('sms')
    plt.ylabel('numbers of patients');
Sms_vs_attend(df,'SMS_received',show,noshow)


# looks like there is alot of patients(double) that attend without receiving sms , so we need to change the way of writing sms

# In[ ]:





# In[ ]:





# In[ ]:





# In[35]:



plt.figure(figsize=[13,8])
df.Neighbourhood[show].value_counts().plot( kind= 'bar', color='blue', label='show')
df.Neighbourhood[noshow].value_counts().plot( kind= 'bar', color='red', label='noshow')
plt.legend()
plt.title("comparison bet Neighbourhood and attendence")
plt.xlabel("Neighbourhood")
plt.ylabel("attendence")
plt.show();


# there is a huge effect bet Neighbourhood and attendence , jardim camburi has the greatest showing rate and appointments

# note: there is no a dataset that tells me the census of each city to get the percentage more acurate

# In[ ]:





# In[ ]:





# In[ ]:





# In[36]:


plt.figure(figsize=(13,8))
df[show].groupby('Neighbourhood').SMS_received.mean().plot(kind= 'bar',color='red',label='show')
df[noshow].groupby('Neighbourhood').SMS_received.mean().plot(kind= 'bar',color='blue',label='noshow')
plt.legend()
plt.title("comparison bet Neighbourhood and sms ")
plt.xlabel("Neighbourhood")
plt.ylabel("attendence");


# only 5 response to sms in Neighbourhoods ,ilhas oceanicas de trindade has the most rate of reponse 

# the 5 regions that shows response has the least attending rate 

# which means there is a huge issue with sms senders ,maybe they donot send to the other regions

# In[ ]:





# In[ ]:





# In[ ]:





# <a id='conclusions'></a>
# ## Conclusions
# 
# > **Tip**: there is a huge relation bet.  Neighbourhood and attendence, jardim camburi has the greatest showing rate and appointments
# note: there is no a dataset that tells me the census of each city to get the percentage more acurate
# 
# 
# 
# > **Tip**: there is a huge issue with the sms senders technique, as most of patients had attend without receiving sms 
# , the number of showing patients without receiving sms is double the number of patients that attend by the sms 
# 
# 
# > **Tip**: Age has clear effect on attendence as the patients with (0-8) is the most showing ,and for sure with there parents.
# Age from(45-55) are the second showing patients.
# the least attending patients is at Age (65-85)
# so there is an inversaly propotional relation bet age and attendence.
# 
# 
# > **Tip**: to increase the amount of patients showing:
# fix the sms issue as patients are not giving attention to it 
# give attention to regions or Neighbourhood  
# ### Limitations
# > **Tip**: there is no relation bet. gender and attendence
# 
# 
# 
# 

# In[25]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




