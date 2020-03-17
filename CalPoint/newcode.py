# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:00:35 2020

@author: Dell
"""

import pandas as pd
import numpy as np
df1=pd.read_csv('D:\COLLEGE SEM 4\Pointer Analysis\CalPoint\FSM.csv')

#deleting extra rows
df1=df1.drop(df1.index[0:3])
df1=df1.drop(df1.index[23:27])
df1=df1.drop(df1.index[46:49])
df1=df1.drop(df1.index[46])
df1=df1.drop(df1.index[69:73])
df1=df1.drop(df1.index[92:96])
df1=df1.drop(df1.index[115:119])


#rename columns
df1.rename( columns={'Unnamed: 0':'SrNo'}, inplace=True )
df1.rename( columns={'Unnamed: 1':'RollNo'}, inplace=True )
df1.rename( columns={'Unnamed: 2':'Name'}, inplace=True )
df1.rename( columns={'Unnamed: 3':'AM1-ese'}, inplace=True )
df1.rename( columns={'Unnamed: 5':'AM1-tw'}, inplace=True )
df1.rename( columns={'Unnamed: 7':'EC-ca'}, inplace=True )
df1.rename( columns={'Unnamed: 9':'ED-ca'}, inplace=True )

#Am1
df1['AM1-ese']=df1['AM1-ese'].astype(str)
df1['AM1-ese'] = df1['AM1-ese'].map(lambda x: str(x)[:-1])
df1['AM1-ese'] = df1['AM1-ese'].astype(int)
df1['AM1']=df1['AM1'].astype(str)
df1['AM1'] = df1['AM1'].map(lambda x: str(x)[:-1])
df1['AM1'] = df1['AM1'].astype(int)
df1['AM1-ese']=df1['AM1-ese']/2
df1['AM1-sc']=df1['AM1']+df1['AM1-ese']
df1['AM1-sc'] = df1['AM1-sc'].apply(np.ceil)
df1=df1.drop(['AM1'],axis=1)
df1=df1.drop(['AM1-ese'],axis=1)
df1.rename( columns={'AM1-sc':'AM1'}, inplace=True )

#Am1-tw
df1['AM1-tw']=df1['AM1-tw'].astype(str)
df1['AM1-tw'] = df1['AM1-tw'].map(lambda x: str(x)[:-1])
df1['AM1-tw'] = df1['AM1-tw'].astype(int)


df1['ECL'] = df1['ECL'].astype(str)
df1['ECL'] = df1['ECL'].map(lambda x: str(x)[:-1])
"""
df1['ECL-TW'], df1['ECL-O'] = df1['ECL'].str.split('. ', 1).str
df1['ECL-TW'] = df1['ECL-TW'].astype(int)
df1['ECL-O'] = df1['ECL-O'].astype(int)
df1['ECL-sc']=df1['ECL-TW']+df1['ECL-O']
df1=df1.drop(['ECL'],axis=1)
df1=df1.drop(['ECL-TW'],axis=1)
df1=df1.drop(['ECL-O'],axis=1)
df1.rename( columns={'ECL-sc':'ECL'}, inplace=True )

#EC
df1['EC']=df1['EC'].astype(str)
df1['EC'] = df1['EC'].map(lambda x: str(x)[:-1])
df1['EC'] = df1['EC'].astype(int)
df1['EC']=df1['EC']/2
df1['EC-ca']=df1['EC-ca'].astype(str)
df1['EC-ca'] = df1['EC-ca'].map(lambda x: str(x)[:-1])
df1['EC-ca'] = df1['EC-ca'].astype(int)
df1['ec-sc']=df1['EC']+df1['EC-ca']
df1['ec-sc'] = df1['ec-sc'].apply(np.ceil)
df1=df1.drop(['EC'],axis=1)
df1=df1.drop(['EC-ca'],axis=1)
df1.rename( columns={'ec-sc':'EC'}, inplace=True )

#Ed
df1['ED']=df1['ED'].astype(str)
df1['ED'] = df1['ED'].map(lambda x: str(x)[:-1])
df1['ED'] = df1['ED'].astype(int)
df1['ED']=df1['ED']/2
df1['ED-ca']=df1['ED-ca'].astype(str)
df1['ED-ca'] = df1['ED-ca'].map(lambda x: str(x)[:-1])
df1['ED-ca'] = df1['ED-ca'].astype(int)
df1['ED-sc']=df1['ED']+df1['ED-ca']
df1['ED-sc'] = df1['ED-sc'].apply(np.ceil)
df1=df1.drop(['ED'],axis=1)
df1=df1.drop(['ED-ca'],axis=1)
df1.rename( columns={'ED-sc':'ED'}, inplace=True )

#eeee
df1['EEEE'] = df1['EEEE'].astype(str)
df1['EEEE'] = df1['EEEE'].map(lambda x: str(x)[:-1])
df1['EEEE-ese'], df1['EEEE-ca'] = df1['EEEE'].str.split('. ', 1).str
df1['EEEE-ca'] = df1['EEEE-ca'].astype(int)
df1['EEEE-ese'] = df1['EEEE-ese'].astype(int)
df1['EEEE-ese']=df1['EEEE-ese']/2
df1['EEEE-sc']=df1['EEEE-ese']+df1['EEEE-ca']
df1['EEEE-sc'] = df1['EEEE-sc'].apply(np.ceil)
df1=df1.drop(['EEEE'],axis=1)
df1=df1.drop(['EEEE-ca'],axis=1)
df1=df1.drop(['EEEE-ese'],axis=1)
df1.rename( columns={'EEEE-sc':'EEEE'}, inplace=True )

#CS
df1['CS']=df1['CS'].astype(str)
df1['CS'] = df1['CS'].map(lambda x: str(x)[:-1])
df1['CS'] = df1['CS'].astype(int)

#WP1
df1['WP1']=df1['WP1'].astype(str)
df1['WP1'] = df1['WP1'].map(lambda x: str(x)[:-1])
df1['WP1'] = df1['WP1'].astype(int)

#ecL
df1['ECL'] = df1['ECL'].astype(str)
df1['ECL'] = df1['ECL'].map(lambda x: str(x)[:-1])
df1['ECL-TW'], df1['ECL-O'] = df1['ECL'].str.split('. ', 1).str
df1['ECL-TW'] = df1['ECL-TW'].astype(int)
df1['ECL-O'] = df1['ECL-O'].astype(int)
df1['ECL-sc']=df1['ECL-TW']+df1['ECL-O']
df1=df1.drop(['ECL'],axis=1)
df1=df1.drop(['ECL-TW'],axis=1)
df1=df1.drop(['ECL-O'],axis=1)
df1.rename( columns={'ECL-sc':'ECL'}, inplace=True )

#eeel
df1['EEEEL'] = df1['EEEEL'].astype(str)
df1['EEEEL'] = df1['EEEEL'].map(lambda x: str(x)[:-1])
df1['EEEEL-TW'], df1['EEEEL-O'] = df1['EEEEL'].str.split('. ', 1).str
df1['EEEEL-TW'] = df1['EEEEL-TW'].astype(int)
df1['EEEEL-O'] = df1['EEEEL-O'].astype(int)
df1['EEEEL-sc']=df1['EEEEL-TW']+df1['EEEEL-O']
df1=df1.drop(['EEEEL'],axis=1)
df1=df1.drop(['EEEEL-TW'],axis=1)
df1=df1.drop(['EEEEL-O'],axis=1)
df1.rename( columns={'EEEEL-sc':'EEEEL'}, inplace=True )

#EDL
df1['EDL']=df1['EDL'].astype(str)
df1['EDL'] = df1['EDL'].map(lambda x: str(x)[:-1])
df1['EDL'] = df1['EDL'].astype(int)

def range_calc(x):
    if x>84:
        return 10
    elif x>74:
        return 9
    elif x>=70:
        return 8
    elif x>=60:
        return 7
    elif x>=50:
        return 6
    elif x>=45:
        return 5
    elif x>=40:
        return 4
    else:
        return 0
   
   
df1['AM1-tw']=df1['AM1-tw']*4
df1['EDL']=df1['EDL']*2
df1['ECL']=df1['ECL']*2
df1['EEEEL']=df1['EEEEL']*2
df1['WP1']=df1['WP1']*2
     
def pointer(df):
    creds={3:1,4:2,5:1,6:2,7:4,8:4,9:3,10:3,11:1,12:1}
    cred=0
    for i in range(3,13):
        cred=cred+(range_calc(df[i]))*creds.get(i)
    pointer=cred/22
    return pointer
   
df1['Pointer']=df1.apply(pointer,axis=1)
df1['Pointer']=df1['Pointer'].round(2)

#df1.to_csv('sem1.csv')
"""
