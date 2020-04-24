import pandas as pd
import numpy as np
from math import *

#creating dataframes from csv's
df1 = pd.read_csv('D:\COLLEGE SEM 4\Pointer Analysis\CalPoint\FSM.csv')
df2 = pd.read_csv('D:\COLLEGE SEM 4\Pointer Analysis\CalPoint\SSM.csv')
df3 = pd.read_csv('D:\COLLEGE SEM 4\Pointer Analysis\CalPoint\TSM.csv')

#list of columns of dataframe and credits for respective subjects.
lc1 = ['SrNo','RollNo','Name','AM1-ese','AM1','AM1-tw','EC','EC-ca','ED','ED-ca','EEEE','CS','ECL','EDL','EEEEL','WP1']
ds1 = {'AM1':4,'AM1-tw':1,'EC':4,'ED':3,'EEEE':3,'CS':2,'ECL':1,'EDL':1,'EEEEL':1,'WP1':2}
lc2 = ['SrNo','RollNo','Name','AM2-ese','AM2','AM2-tw','EP','EP-ca','EMC','PROGC','ES','INDAP','EPL','EMCL','PROG','WP2']
ds2 = {'AM2':4,'AM2-tw':1,'EP':4,'EMC':3,'PROGC':3,'ES':2,'INDAP':2,'EPL':1,'EMCL':1,'PROG':1,'WP2':2}
lc3 = ['SrNo','RollNo','Name','C3ITVC','C3ITVC-tw','C3DTS','C3COA','C3OOPM','C3DM-ese','C3DM','C3DM-tw','C3DDL','C3DTSL','C3COAL','C3OOPML']
ds3 = {'C3ITVC':3,'C3ITVC-tw':1,'C3DTS':3,'C3COA':3,'C3OOPM':3,'C3DM':3,'C3DM-tw':1,'C3DDL':2,'C3DTSL':1,'C3COAL':1,'C3OOPML':1}

#function for dropping unecessecary rows even though function is named coulmns
def dropcolumns(df):
    df=df.drop(df.index[0:3])
    df=df.drop(df.index[23:27])
    df=df.drop(df.index[46:49])
    df=df.drop(df.index[46])
    df=df.drop(df.index[69:73])
    df=df.drop(df.index[92:96])
    df=df.drop(df.index[115:119])
    df=df.drop(df.index[138:142])
    return df
df1 = dropcolumns(df1)
df2 = dropcolumns(df2)
df3 = dropcolumns(df3)

#functin for renaming columns
def renamecol(df1,lc1):
    df1.rename( columns={'Unnamed: 0':lc1[0]}, inplace=True )
    df1.rename( columns={'Unnamed: 1':lc1[1]}, inplace=True )
    df1.rename( columns={'Unnamed: 2':lc1[2]}, inplace=True )
    df1.rename( columns={'Unnamed: 3':lc1[3]}, inplace=True )
    df1.rename( columns={'Unnamed: 4':lc1[4]}, inplace=True )
    df1.rename( columns={'Unnamed: 5':lc1[5]}, inplace=True )
    df1.rename( columns={'Unnamed: 7':lc1[7]}, inplace=True )
    df1.rename( columns={'Unnamed: 8':lc1[8]}, inplace=True )
    df1.rename( columns={'Unnamed: 9':lc1[9]}, inplace=True )
    df1.rename( columns={'Unnamed: 10':lc1[10]}, inplace=True )
    return df1

#function call for renaming columns
df1 = renamecol(df1,lc1)
df2 = renamecol(df2,lc2)
df3 = renamecol(df3, lc3)


#function for removing sem from the roll no of candidate and / from name of girl candidate
def changerollandname(df):
    df['RollNo'] = df['RollNo'].astype(str)
    df['RollNo'] = df['RollNo'].map(lambda x: str(x)[1:])
    df['Name'] = df['Name'].astype(str)
    df['Name'] = df['Name'].map(lambda x: str(x)[3:] if x[0] == '/' else str(x))
    return df

#function call for changing rollno and name of candidate
df1 = changerollandname(df1)
df2 = changerollandname(df2)
df3 = changerollandname(df3)

#function for converting string into int for respective columns
def cstoint(df,lc):
    def calSumCol(x):
        sumval = int(x[0]) + int(x[1])
        return sumval
    def calSumColnew(x):
        sumval = ceil(int(x[0])/2) + int(x[1])
        return sumval
    for i in range(3,len(lc)):
        var = lc[i]
        if str(df[var].values[0]).find('.') == -1:
            df[var].astype(int)
        else:
            df[var] = df[var].astype(str)
            df[var] = df[var].map((lambda x: str(x)[:-1]))
            df[var] = df[var].apply(lambda x: x.split('. '))
            if var[-1] == 'L' or var[-1] == 'l':
                df[var] = df[var].apply(calSumCol)
            else:
                df[var] = df[var].apply(calSumColnew)
    return df

#function for combining columns
def combinecol(df):
    col1 = ['AM1','EC','ED']
    col2 = ['AM2','EP']
    col3 = ['C3DM']
    dflist = list(df.columns.values)
    for i in dflist:
        if i in col1:
            if i == 'AM1':
                tempstr = i+'-ese'
                df[i] = df[i].astype(float)
                df[tempstr] = df[tempstr].astype(float)
                df[i] = df[tempstr]/2 + df[i]
                df[i] = df[i].apply(lambda x: ceil(x))
                df = df.drop([tempstr],axis=1)
            elif i == 'EC' or i == 'ED':
                tempstr = i+'-ca'
                df[i] = df[i].astype(float)
                df[tempstr] = df[tempstr].astype(float)
                df[i] = df[i]/2 + df[tempstr]
                df[i] = df[i].apply(lambda x: ceil(x))
                df = df.drop([tempstr],axis=1)
        elif i in col2:
            if i in 'AM2':
                tempstr = i+'-ese'
                df[i] = df[i].astype(float)
                df[tempstr] = df[tempstr].astype(float)
                df[i] = df[tempstr]/2 + df[i]
                df[i] = df[i].apply(lambda x: ceil(x))
                df = df.drop([tempstr],axis=1)
            elif i == 'EP':
                tempstr = i+'-ca'
                df[i] = df[i].astype(float)
                df[tempstr] = df[tempstr].astype(float)
                df[i] = df[i]/2 + df[tempstr]
                df[i] = df[i].apply(lambda x: ceil(x))
                df = df.drop([tempstr],axis=1)
        elif i in col3:
            if i == 'C3DM':
                tempstr = i+'-ese'
                df[i] = df[i].astype(float)
                df[tempstr] = df[tempstr].astype(float)
                df[i] = df[tempstr]/2 + df[i]
                df[i] = df[i].apply(lambda x: ceil(x))
                df = df.drop([tempstr],axis=1)
    return df

#function call for converting string to integers so calculation can be done
df1 = cstoint(df1,lc1)
df2 = cstoint(df2,lc2)
df3 = cstoint(df3,lc3)

#function call for combie columns of ese and ca marks for respective subjects
df1 = combinecol(df1)
df2 = combinecol(df2)
df3 = combinecol(df3)

#function for calculating the pointer
def pointer(df,ds):
    def pcal(x,maxm):
        if x>0.84*maxm:
            return 10
        elif x>0.74*maxm:
            return 9
        elif x>=0.70*maxm:
            return 8
        elif x>=0.60*maxm:
            return 7
        elif x>=0.50*maxm:
            return 6
        elif x>=0.45*maxm:
            return 5
        elif x>=0.40*maxm:
            return 4
        else:
            return 0
    collist = list(df.columns.values)
    collist.remove('SrNo')
    collist.remove('RollNo')
    collist.remove('Name')
    #collist.remove('SrNo')
    cred = 0
    tot_cred = 0
    for i in collist:
        df[i] = df[i].astype(float)
        if 'DDL' in i:
            cred = cred + (df[i].apply(pcal,maxm=75)) * ds[i]
        elif i[-1] == 'L' or i == 'WP1' or i == 'WP2' or i == 'INDAP' or i == 'PROG':
            cred = cred + (df[i].apply(pcal,maxm=50)) * ds[i]
        elif i[-1:-3:-1] == 'wt':
            cred = cred + (df[i].apply(pcal,maxm=25)) * ds[i]
        else:
            cred = cred + (df[i].apply(pcal,maxm=100)) * ds[i]
        tot_cred = tot_cred + ds[i]
    point = cred/tot_cred
    df['Pointer'] = point
    df['Pointer'] = df['Pointer'].round(2)
    return df

# function call for calculating the pointer
df1 = pointer(df1,ds1)
df2 = pointer(df2,ds2)
df3 = pointer(df3,ds3)

#df1.to_csv('D:\COLLEGE SEM 4\Pointer Analysis\CalPoint\sem1.csv')
#df2.to_csv('D:\COLLEGE SEM 4\Pointer Analysis\CalPoint\sem2.csv')
#df3.to_csv('D:\COLLEGE SEM 4\Pointer Analysis\CalPoint\sem3.csv')