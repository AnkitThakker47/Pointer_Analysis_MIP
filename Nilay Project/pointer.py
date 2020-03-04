import csv
import pandas as pd
f = open('it.csv')
csv_f=csv.reader(f)
def gradepoint(esem,ca,j):

	if(j==1):
		esem=esem/2
	gp=esem+ca
	if(gp>=85 and gp<=100):
		return 10
	elif(gp>=75 and gp<85):
		return 9
	elif(gp>=70 and gp<75):
		return 8
	elif(gp>=60 and gp<70):
		return 7
	elif(gp>=50 and gp<60):
		return 6
	elif(gp>=45 and gp<50):
		return 5
	elif(gp>=40 and gp<45):
		return 4
	else:
		return 0

#maths_gp,phy_gp,mech_gp,pic_gp,evs_gp,indap_gp,mathstw_gp,epl_gp,eml_gp,pictw_gp,wp2_gp=[]
roll_no=[]
name=[]
maths_ese=[]
maths_ca=[]
maths_gp=[]
maths_tw=[]
ep_ese=[]
ep_ca=[]
em_ese=[]
em_ca=[]
pic_ese=[]
pic_ca=[]
ep_lab=[]
ep_tw=[]
em_lab=[]
em_tw=[]
es=[]
pic_tw=[]
indap=[]
wp=[]
maths_tw_gp=[]
ep_ese_gp=[]

em_ese_gp=[]

pic_ese_gp=[]

ep_lab_gp=[]

em_lab_gp=[]

es_gp=[]
pic_tw_gp=[]
indap_gp=[]
wp_gp=[]
maths_ese_cr=[]
maths_tw_cr=[]
ep_ese_cr=[]
em_ese_cr=[]
pic_ese_cr=[]
ep_lab_cr=[]
em_lab_cr=[]
es_cr=[]
pic_tw_cr=[]
indap_cr=[]
wp_cr=[]
tc=[]
finalcredits=[]
for row in csv_f:
	t18=int(row[1])
	roll_no.append(t18)
	name.append(row[2])
	try:

		t1=float(row[3])
		t2=float(row[4])
		t3=float(row[5])
		t4=float(row[6])
		t5=float(row[7])
		t6=float(row[8])
		t7=float(row[9])
		t8=float(row[10])
		t9=float(row[11])
		t10=float(row[12])
		t11=float(row[13])
		t12=float(row[14])
		t13=float(row[15])
		t14=float(row[16])
		t15=float(row[17])
		t16=float(row[18])
		t17=float(row[19])
		

		maths_ese.append(t1)
		maths_ca.append(t2)
		maths_tw.append(4.0*t3)
		ep_ese.append(t4)
		ep_ca.append(t5)
		em_ese.append(t6)
		em_ca.append(t7)
		pic_ese.append(t8)
		pic_ca.append(t9)
		es.append(t10)
		indap.append(2.0*t11)
		ep_lab.append(2.0*t12)
		ep_tw.append(2.0*t13)
		em_lab.append(2.0*t14)
		em_tw.append(2.0*t15)
		pic_tw.append(2.0*t16)
		wp.append(2.0*t17)
	
	except ValueError:
		maths_ese.append(0.0)
		maths_ca.append(0.0)
		ep_ese.append(0.0)
		ep_ca.append(0.0)
		em_ese.append(0.0)
		em_ca.append(0.0)
		pic_ese.append(0.0)
		pic_ca.append(0.0)
		es.append(0.0)
		indap.append(0.0)
		ep_lab.append(0.0)
		ep_tw.append(0.0)
		em_lab.append(0.0)
		em_tw.append(0.0)
		pic_tw.append(0.0)
		wp.append(0.0)
		maths_tw.append(0.0)
i=0
while(i<len(roll_no)):
	maths_gp.append(gradepoint(maths_ese[i],maths_ca[i],1))
	maths_tw_gp.append(gradepoint(maths_tw[i],0.0,0))
	ep_ese_gp.append(gradepoint(ep_ese[i],ep_ca[i],1))
	em_ese_gp.append(gradepoint(em_ese[i],em_ca[i],1))
	pic_ese_gp.append(gradepoint(pic_ese[i],pic_ca[i],1))
	ep_lab_gp.append(gradepoint(ep_lab[i],ep_tw[i],0))
	em_lab_gp.append(gradepoint(em_lab[i],em_tw[i],0))
	es_gp.append(gradepoint(es[i],0.0,0))
	pic_tw_gp.append(gradepoint(pic_tw[i],0.0,0))
	indap_gp.append(gradepoint(indap[i],0.0,0))
	wp_gp.append(gradepoint(wp[i],0.0,0))
	i=i+1
i=0
while(i<len(roll_no)):
	maths_ese_cr.append(4.0*maths_gp[i])
	maths_tw_cr.append(1.0*maths_tw_gp[i])
	ep_ese_cr.append(4.0*ep_ese_gp[i])
	em_ese_cr.append(3.0*em_ese_gp[i])
	pic_ese_cr.append(3.0*pic_ese_gp[i])
	ep_lab_cr.append(1.0*ep_lab_gp[i])
	em_lab_cr.append(1.0*em_lab_gp[i])
	es_cr.append(2.0*es_gp[i])
	pic_tw_cr.append(1.0*pic_tw_gp[i])
	indap_cr.append(2.0*indap_gp[i])
	wp_cr.append(2.0*wp_gp[i])
	tc.append(maths_ese_cr[i]+ep_ese_cr[i]+em_ese_cr[i]+pic_ese_cr[i]+ep_lab_cr[i]+em_lab_cr[i]+es_cr[i]+pic_tw_cr[i]+indap_cr[i]+wp_cr[i]+maths_tw_cr[i])
	finalcredits.append(round(tc[i]/24,2))
	i=i+1
#print(maths_tw_cr[120],maths_tw_gp[120],maths_tw[120])

# j=0
# while(j<len(roll_no)):
# 	print(roll_no[j],name[j],round(finalcredits[j],2),em_ese_gp[j])
# 	j+=1
dl=pd.DataFrame(list(zip(roll_no,name,finalcredits)),columns=['Roll Number','Name','Credits'])
export_csv=dl.to_csv(r'.\sendit.csv',index=False,header=True)