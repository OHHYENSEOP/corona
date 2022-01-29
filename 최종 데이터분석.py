#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import numpy as np
import load_data
from datetime import datetime
plt.rcParams['font.family'] = "Malgun Gothic" #폰트


# In[2]:


l = load_data.LoadData('root')  #데이터베이스 불러오기


# In[3]:


v= l.getData_vaccinate() #백신접종데이터
b= l.getData_corona() #코로나 확진자 데이터


# In[4]:


b2 = b.iloc  [441:722, : ]  #2021.04.21이후 확진자
result1=b2.reset_index()


# In[5]:


v #백신
result2=v.reset_index()


# In[6]:


#서울기준일을 접종일로 변경
r_new = []
for n in result1["서울기준일"] : 
    r_new.append( n[0:10] ) 
# r_new


# In[7]:


#코로나 확진데이터에 접종일 칼럼추가
result1_new  =  [  n[0:10]  for n in  result1["서울기준일"] ]
# result1_new
result1["S_VC_DT"] = result1_new 


# In[8]:


#21.04.21접종일 이후 확진자 합병
r = pd.merge( result1, result2, on="S_VC_DT") 


# In[9]:


d1= b.iloc[0:441,:] #2020.02.05 ~ 2021.04.20 접종 전  
d2 = b.iloc[441:722,:] #2021.04.21 ~ 2022.01.26 접종 후


# In[10]:


#전국확진자수
b.plot(x='서울기준일' ,y='전국확진',figsize=(10, 6))


# In[11]:


v1 = v.copy()


# In[12]:


# #특정날짜 추출
v1["S_VC_DT"] = [ pd.to_datetime ( n )   for n in v1["S_VC_DT"] ]
b["서울기준일"] = [ pd.to_datetime ( n )   for n in b["서울기준일"] ]
r["서울기준일"] = [ pd.to_datetime ( n )   for n in r["서울기준일"] ]


# In[13]:


#초창기 거리두기 전국확진자
ax= b.plot(x="서울기준일", y="전국확진" )
ax.set_xlim(["2020.03.22.00","2020.06.27.00"])
ax.set_ylim([8700,12800])


# In[14]:


# 초창기 거리두기에 따른 서울확진자
ax= b.plot(x="서울기준일", y="서울시확진자" )
ax.set_xlim(["2020.03.22.00","2020.06.27.00"])
ax.set_ylim([200,1300])


# In[15]:


# 21년 중반~지금(코로나 예방접종 시작)
# 백신접종이후 서울시확진자(2021.04.21.00 ~ 2021.05.31.00)
ax= b.plot(x="서울기준일", y="서울시추가확진" )
ax.set_xlim(["2021.04.21.00","2021.05.31.00"])
ax.set_ylim([0,1400])
# 백신접종이후 서울시확진자(2021.06.01.00 ~ 2021.09.30.00)
ax= b.plot(x="서울기준일", y="서울시추가확진" )
ax.set_xlim(["2021.06.01.00","2021.09.30.00"])
ax.set_ylim([0,1400])
# 백신접종이후 서울시확진자(2021.10.01.00 ~ 2022.01.26.00)
ax= b.plot(x="서울기준일", y="서울시추가확진" )
ax.set_xlim(["2021.10.01.00","2022.01.26.00"])
ax.set_ylim([0,3500])


# In[16]:


v2 = v.copy()
Series(v2.S_VC_DT)[v1.S_VC_DT.map(lambda x:type(x)==type(1))]
v2.loc[:,"월"]= v2.S_VC_DT.map(lambda x:".".join(x.split(".")[:2]))


# In[17]:


#1달로 묶기
v_month=v2.pivot_table(index="월", values=["FIR_INC1","SCD_INC1","ADD_INC1","FIR_INC","SCD_INC","ADD_INC","FIR_INC_RATE","SCD_INC_RATE","ADD_INC_RATE"], aggfunc="sum")


# In[18]:


#월별 1,2,3,차 당일 접종자 수
plt.figure(figsize=(15,7))
sns.lineplot(x="월", y="FIR_INC1", data=v_month, marker='o', color='r', linestyle='solid') #빨강
sns.lineplot(x="월", y="SCD_INC1", data=v_month, marker='o', color='b', linestyle='solid') #파랑
sns.lineplot(x="월", y="ADD_INC1", data=v_month, marker='o', color='y', linestyle='solid') #노랑

v.plot(x="S_VC_DT" ,y=['FIR_INC_RATE', 'SCD_INC_RATE','ADD_INC_RATE'],figsize=(10, 6)) #"FIR_INC : 1차접종률     
plt.xlabel("접종일")                                                                   # SCD_INC : 2차접종률
plt.ylabel("접종률")  


# In[19]:


#당일 1차접종자 수 0 인 날짜
plt.figure(figsize=(27,7)) #기준일 부터 土3일씩 적용
ax= v1.plot(x="S_VC_DT", y="FIR_INC1" )
ax.set_xlim([ "2021.07.01.00","2021.07.06.00"]) #2021.07.01 ~ 2021.07.06
ax.set_ylim([0,15000])

#당일 1차접종자 수 0 인 날짜
plt.figure(figsize=(27,7)) #기준일 부터 土3일씩 적용
ax= v1.plot(x="S_VC_DT", y="FIR_INC1" )
ax.set_xlim([ "2021.06.23.00","2021.06.29.00"]) #2021.06.23 ~ 2021.06.29
ax.set_ylim([0,8000])

#당일 1차접종자 수 0 인 날짜
plt.figure(figsize=(20,5)) #기준일 부터 土3일씩 적용
ax= v1.plot(x="S_VC_DT", y="FIR_INC1" )
ax.set_xlim([ "2021.05.18.00","2021.05.25.00"]) #2021.05.18 ~ 2021.05.25
ax.set_ylim([0,10000])

#당일 1차접종자 수 0 인 날짜
plt.figure(figsize=(27,7)) #기준일 부터 土3일씩 적용
ax= v1.plot(x="S_VC_DT", y="FIR_INC1" )
ax.set_xlim([ "2021.05.12.00","2021.05.18.00"]) #2021.05.12 ~ 2021.05.18
ax.set_ylim([0,5000])


# In[20]:


# 2021.09.13 ~ 2021.09.14 접종률이 64.4 > 67.4  ` 3% 상승 전일 비례 2.6% 더 상승
ax= r.plot(x="서울기준일", y=["FIR_INC_RATE", "SCD_INC_RATE"]) 
ax.set_xlim(["2021.09.12.00","2021.09.14.00"])
ax.set_ylim([38,75])


# In[21]:


#서울시확진자와 접종누계 상관계수
sns.heatmap(data = r.loc[:, ('서울시확진자', 'FIR_INC','SCD_INC','ADD_INC') ].corr(), annot=True,  fmt = '.2f', linewidths=.6, cmap='Reds')


# In[22]:


#서울시확진과 백신접종누계 상관계수
sns.heatmap(data = r.loc[:, ('서울시추가확진', 'FIR_INC','SCD_INC','ADD_INC') ].corr(), annot=True,  fmt = '.2f', linewidths=.6, cmap='Reds')


# In[23]:


#서울시 사망률 칼럼추가
r.loc[:,"서울시 사망률"]=0
for n in range(0,281):
    r.loc[n,"서울시사망률"]=r.loc[n,"서울시사망"]/r.loc[n,"서울시확진자"]


# In[24]:


#백신 접종이후 서울시 사망률
ax= r.plot(x="서울기준일", y="서울시사망률" )
ax.set_xlim(["2021.04.21.00","2022.01.26.00"])


# In[25]:


#백신접종누계와 사망자 상관계수
sns.heatmap(data = r.loc[:, ('FIR_INC','SCD_INC','ADD_INC','서울시사망') ].corr(), annot=True,  fmt = '.2f', linewidths=.6, cmap='Reds')


# In[26]:


# 추석, 델타변이, 위드 코로나, 오미크론이라는 범주형 변수를 추가하고 
 # 특정 사건 발생 이전을 0, 발생 이후를 1로 두고 데이터를 추가함
r.loc[:,("추석","델타변이","위드 코로나","오미크론")]=0
# r["서울기준일"] = [ pd.to_datetime ( n )   for n in r["서울기준일"] ]
r.loc[r.서울기준일>datetime.strptime("2021.09.21.00","%Y.%m.%d.%H"),"추석"]=1
r.loc[r.서울기준일>datetime.strptime("2021.11.01.00","%Y.%m.%d.%H"),"위드 코로나"]=1
r.loc[r.서울기준일>datetime.strptime("2021.06.28.00","%Y.%m.%d.%H"),"델타변이"]=1
r.loc[r.서울기준일>datetime.strptime("2021.11.24.00","%Y.%m.%d.%H"),"오미크론"]=1


# In[27]:


#요인들과 확진자 상관계수
sns.heatmap(data = r.loc[:, ('추석','델타변이','위드 코로나','오미크론','서울시추가확진','전국추가확진') 
                ].corr(), annot=True,fmt = '.2f', linewidths=.6, cmap='Reds')


# In[28]:


#백신접종누계와 사망자 상관계수
sns.heatmap(data = r.loc[:, ('FIR_INC','SCD_INC','ADD_INC','서울시사망률') ].corr(), annot=True,  fmt = '.2f', linewidths=.6, cmap='Reds')

