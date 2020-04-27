from flask import Flask,render_template,request,redirect,flash
app=Flask(__name__)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import sklearn.preprocessing as sp


df1=pd.read_csv('sem1.csv')
df2=pd.read_csv('sem2.csv')
df3=pd.read_csv('sem3.csv')

dfm1=df1[df1.columns[4:14]]
dfm2=df2[df2.columns[4:15]]
dfm3=df3[df3.columns[4:15]]

courses1=['AM1','AM1-TW','EC','ED','EEEE','CS','EC-LAB','ED-LAB','EEEE-LAB','WP-1']
courses2=['AM-2','AM2-TW','EP','EM','PIC', 'EVS','IAP','EP-Lab','EM-Lab','PIC-Lab','WP-2']
courses3=['ITVS','ITVC-TW','DS','COA','OOPM', 'DSGT','DSGT-TW',
          'DD-Lab','DS-Lab','COA-Lab','OOPM-Lab']

c1 = {'AM1':[0,1],'EC':[2,6],'ED':[3,7],'EEEE':[4,8],'CS':[5,100],'WP1':[9,50]}
c2 = {'AM2':[0,1],'EP':[2,7],'EM':[3,8],'PIC':[4,9],'EVS':[5,100],'IAP':[6,50],'WP-2':[10,50]}
c3 = {'ITVS':[0,1],'DS':[2,8],'COA':[3,9],'OOPM':[4,10],'DSGT':[5,6],'DD-Lab':[7,75]}

ds1 = {'AM1':[100,4],'AM1-tw':[25,1],'EC':[100,4],'ED':[100,3],'EEEE':[100,3],'CS':[100,2],'ECL':[50,1],'EDL':[50,1],'EEEEL':[50,1],'WP1':[50,2]}
ds2 = {'AM2':[100,4],'AM2-tw':[25,1],'EP':[100,4],'EMC':[100,3],'PROGC':[100,3],'ES':[50,2],'INDAP':[50,2],'EPL':[50,1],'EMCL':[50,1],'PROG':[50,1],'WP2':[50,2]}
ds3 = {'ITVC':[100,3],'ITVC_TW':[25,1],'DS':[100,3],'COA':[100,3],'OOPM':[100,3],'DSGT':[100,3],'DSGT-TW':[25,1],'DD-LAB':[75,2],'DS-LAB':[50,1],'COA-LAB':[50,1],'OOPML-LAB':[50,1]}

sem1_courses=list(c1.keys())
sem2_courses=list(c2.keys())
sem3_courses=list(c3.keys())

l=[]
ind_pie=[]

df1_mean=np.array(dfm1.mean(axis=0))
df2_mean=np.array(dfm2.mean(axis=0))
df3_mean=np.array(dfm3.mean(axis=0))

df1_max=np.array(dfm1.max())
df2_max=np.array(dfm2.max())
df3_max=np.array(dfm3.max())

name="student name"
sem=0
rno=0
pointer=0
count=0
scount=0
data=0
cr=0

#find student as per rno
def find(rno,df):
    global name, pointer
    stud=np.array(df[df['RollNo']==rno])
    name=stud[0][3]
    stud = np.delete(stud, [0,1,2,3])
    return stud

#graph individual progress    
def student_prog_graph(stud,courses):
    global l
    index = np.arange(len(courses))
    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5,forward=True)
    plt.bar(index, stud,color="teal")
    plt.xlabel('Courses', fontsize=20,fontweight='bold')
    plt.ylabel('Score', fontsize=20,fontweight='bold')
    plt.xticks(index, courses, fontsize=20, rotation=90)
    plt.title('Your Progress',fontsize=20,fontweight='bold')
    fig.savefig('static/img/student_progress.png',dpi=100)
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    l.insert(0,figdata_png)

#student v/s mean
def stud_vs_mean(stud,df_mean,courses):
    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5,forward=True)
    barWidth = 0.40
    r1 = np.arange(len(stud))
    r2 = [x + barWidth for x in r1]
    index = np.arange(len(courses))
    plt.bar(r1, stud, color='cornflowerblue', width=barWidth, edgecolor='white', label='Self')
    plt.bar(r2, df_mean, color='coral', width=barWidth, edgecolor='white', label='Average')
    plt.title('Your Progress V/S Class Average Performance ',fontsize=20,fontweight='bold')
    plt.xlabel('courses', fontsize=20,fontweight='bold')
    plt.ylabel('score',fontsize=20,fontweight='bold')
    plt.xticks(index,courses,fontsize=20, rotation=90)
    plt.legend()
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    l.insert(1,figdata_png)
    
#student v/s max    
def stud_vs_max(stud,df_max,courses):
    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5,forward=True)
    barWidth = 0.40
    r1 = np.arange(len(stud))
    r2 = [x + barWidth for x in r1]
    index = np.arange(len(courses))
    plt.bar(r1, stud, color='chartreuse', width=barWidth, edgecolor='white', label='Self')
    plt.bar(r2, df_max, color='crimson', width=barWidth, edgecolor='white', label='Maximum')
    plt.title('Your Progress V/S Class Best Performance ',fontsize=20,fontweight='bold')
    plt.xlabel('courses',fontsize=20,fontweight='bold')
    plt.ylabel('score', fontsize=20,fontweight='bold')
    plt.xticks(index,courses,fontsize=20, rotation=90)
    plt.legend()
    fig.savefig('static/img/student_vs_max.png',dpi=100)
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    l.insert(2,figdata_png)
   
def student_ind_pie(stud,courses,c,cr):
    global l,ind_pie
    subjects = list(c.keys())
    colors = ['lightskyblue','gold','yellowgreen']
    for subject in subjects:
        i=cr.index(subject)
        temp = c[subject]
        if 'AM' in subject or 'DSGT' in subject or 'ITVS' in subject:
            explode = (0,0,0)
            val1,val2 = stud[temp[0]],stud[temp[1]]
            labels=[subject+" Theory",subject+" TermWork","125 - Acquired Marks"]
            values = [val1,val2,125-val1-val2]
            fig1, ax1 = plt.subplots()
            ax1.pie(values,explode=explode,labels=values,startangle = 90,colors = colors,autopct='%1.1f%%',textprops={'fontsize': 20})
            centre_circle = plt.Circle((0,0),0.70,color='black', fc='white',linewidth=1.25)
            fig = plt.gcf()
            fig.set_size_inches(18.5, 10.5,forward=True)
            fig.gca().add_artist(centre_circle)
            ax1.axis('equal')
            plt.tight_layout()
            plt.legend(labels,frameon=True,loc='center left',bbox_to_anchor=(0.75,0.5),fontsize=20)
            fig.savefig('static/img/'+subject+'.png',dpi=100)
            figfile = BytesIO()
            plt.savefig(figfile, format='png')
            figfile.seek(0)
            figdata_png = base64.b64encode(figfile.getvalue())
            figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
            ind_pie.insert(i,figdata_png)

        elif 'WP' in subject or subject in ['EVS','IAP','DD-Lab','CS']:
            labels = [subject, str(temp[1])+" - Acquired Marks"]
            val1=stud[temp[0]]
            values,explode = [val1,temp[1]-val1],(0,0)
            fig1, ax1 = plt.subplots()
            ax1.pie(values,explode=explode,labels=values,startangle = 90,colors = colors,autopct='%1.1f%%',textprops={'fontsize': 20})
            centre_circle = plt.Circle((0,0),0.70,color='black', fc='white',linewidth=1.25)
            fig = plt.gcf()
            fig.set_size_inches(18.5, 10.5,forward=True)
            fig.gca().add_artist(centre_circle)
            ax1.axis('equal')
            plt.tight_layout()
            plt.legend(labels,frameon=True,loc='center left',bbox_to_anchor=(0.75,0.5),fontsize=20)
            fig.savefig('static/img/'+subject+'.png',dpi=100)
            figfile = BytesIO()
            plt.savefig(figfile, format='png')
            figfile.seek(0)
            figdata_png = base64.b64encode(figfile.getvalue())
            figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
            ind_pie.insert(i,figdata_png)

        else:
            labels = [subject+" Theory",subject+" Practicals","150 - Acquired Marks"]
            val1,val2 = stud[temp[0]],stud[temp[1]]
            values,explode = [val1,val2,150-val1-val2],(0,0,0)
            fig1, ax1 = plt.subplots()
            ax1.pie(values,explode=explode,labels=values,startangle = 90,colors = colors,autopct='%1.1f%%',textprops={'fontsize': 20})
            centre_circle = plt.Circle((0,0),0.70,color='black', fc='white',linewidth=1.25)
            fig = plt.gcf()
            fig.set_size_inches(18.5, 10.5,forward=True)
            fig.gca().add_artist(centre_circle)
            ax1.axis('equal')
            plt.tight_layout()
            plt.legend(labels,frameon=True,loc='center left',bbox_to_anchor=(0.75,0.5),fontsize=20)
            fig.savefig('static/img/'+subject+'.png',dpi=100)
            l.append(subject)
            fig.savefig('static/img/'+subject+'.png',dpi=100)
            figfile = BytesIO()
            plt.savefig(figfile, format='png')
            figfile.seek(0)
            figdata_png = base64.b64encode(figfile.getvalue())
            figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
            ind_pie.insert(i,figdata_png)
        i+=1

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
d1 = [4,1,4,3,3,2,1,1,1,2]
d2 = [4,1,4,3,3,2,2,1,1,1,2]
d3 = [3,1,3,3,3,3,1,2,1,1,1]
mm1=[100,25,100,100,100,100,50,50,50,50]
mm2=[100,25,100,100,100,100,50,50,50,50,50]
mm3=[100,25,100,100,100,100,25,75,50,50,50]


def stu_credits_pie(stud_mks,courses,d,mm,creds):
    temp=[]
    explode=[]
    sum=0
    global l
    for i in range(len(stud_mks)):
        temp.insert(i,pcal(stud_mks[i],mm[i]))
        temp[i]=temp[i]*d[i]
        sum+=temp[i]
        explode.insert(i,0)
    explode=tuple(explode)
    colors=['green','gold','yellowgreen','blue','pink','yellow','maroon','orange','powderblue','red','grey']
    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5,forward=True)
    plt.pie(temp,explode=explode,labels=courses, colors=colors,pctdistance=0.85,autopct='%1.1f%%',textprops={'fontsize': 20}, shadow=True, startangle=90)
    centre_circle = plt.Circle((0,0),0.70,color='black',fc='white',linewidth=1.25)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.axis('equal')
    plt.legend(courses,frameon=True,loc='best',fontsize=20)
    msg="Total credits="+str(sum)+"/"+str(creds)
    plt.title(msg, fontsize='20')
    fig.savefig('static/img/student_ptr.png',dpi=100)
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    l.insert(3,figdata_png)
    
def pointers(df,ptr):
    color=['crimson','darkblue','yellowgreen']
    avg_ptr=df['Pointer'].mean()
    max_ptr=df['Pointer'].max()
    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5,forward=True)
    p=[avg_ptr,max_ptr,ptr]
    bars=('Average Pointer','Max Pointer','Your Pointer')
    y_pos = np.arange(len(bars))
    plt.barh(y_pos, p,color=color)
    plt.yticks(y_pos, bars)
    fig.savefig('static/img/pointersr.png',dpi=100)
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
    l.insert(4,figdata_png)

def predict_ptr(a,b,c,d,e):
    dataset = pd.read_csv("responses.csv")
    X=dataset.iloc[:,1:6]
    labelencoder= sp.LabelEncoder()
    X1=pd.DataFrame(X.iloc[:,0])
    X1['Travelling time']=labelencoder.fit_transform(X1)
    X['Travelling time']=X1['Travelling time'].values
    y=dataset.iloc[:,7]
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.3,random_state=0)
    from sklearn.linear_model import LinearRegression
    regressor=LinearRegression()
    regressor.fit(X_train,y_train)
    y_pred=regressor.predict([[a,b,c,d,e]])
    return float((y_pred).round(2))

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST','GET'])
def handle_data():
    if request.method=="POST":
        global sem, rno, pointer, count, scount, cr
        rno=request.form['rno']
        sem=request.form['sem']   
        rno=int(rno)

        if int(sem)==1:   
            stud=find(rno,df1)
            count=np.array(range(3,9))
            scount=np.array(range(6))
            cr=list(c1.keys())
            pointer=(stud[-1])
            stud_mks=np.delete(stud,-1)
            student_prog_graph(stud_mks,courses1)
            stud_vs_mean(stud_mks,df1_mean,courses1)
            stud_vs_max(stud_mks,df1_max,courses1)
            student_ind_pie(stud,courses1,c1,cr)
            stu_credits_pie(stud_mks,courses1,d1,mm1,220)
            pointers(df1,pointer)
            
            
        elif int(sem)==2:   
            stud=find(rno,df2)
            count=np.array(range(3,10))
            scount=np.array(range(7))
            cr=list(c2.keys())
            pointer=(stud[-1])
            count=np.array(range(3,10))
            stud_mks=np.delete(stud,-1)
            student_prog_graph(stud_mks,courses2)
            stud_vs_mean(stud_mks,df2_mean,courses2)
            stud_vs_max(stud_mks,df2_max,courses2)
            student_ind_pie(stud,courses2,c2,cr)
            stu_credits_pie(stud_mks,courses2,d2,mm2,240)
            pointers(df2,pointer)
            
        elif int(sem)==3:   
            stud=find(rno,df3)
            count=np.array(range(3,9))
            scount=np.array(range(6))
            cr=list(c3.keys())
            pointer=(stud[-1])
            count=np.array(range(3,9))
            stud_mks=np.delete(stud,-1)
            student_prog_graph(stud_mks,courses3)
            stud_vs_mean(stud_mks,df3_mean,courses3)
            stud_vs_max(stud_mks,df3_max,courses3)
            student_ind_pie(stud,courses3,c3,cr)
            stu_credits_pie(stud_mks,courses3,d3,mm3,220)
            pointers(df3,pointer)
    
    return redirect('/score')
        
@app.route('/score')
def score():
    return render_template('scores.html',name=name,sem=sem,r1=l[0],r2=l[1],count=count,scount=scount,cr=cr,
    ind_pie=ind_pie, pointer=pointer,r10=l[3])

@app.route('/peer')
def peer():
    return render_template('peer.html',name=name,sem=sem,l=l,r1=l[1],r2=l[2],r4=l[4])

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/handle_predict', methods=['POST','GET'])
def handle_predict():
    if request.method=="POST":
        tr=request.form['options']
        study_hrs=request.form['study_hrs']
        unprod=request.form['unprod']
        sleep=request.form['sleep']
        lect=request.form['lect']
        result=predict_ptr(int(tr),int(study_hrs),int(unprod),int(sleep),int(lect))
        return render_template('pred_result.html', result=result)

if __name__=='__main__':
    app.run(debug=True)