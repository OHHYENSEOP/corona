#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install tkcalendar


# In[5]:


import tkinter # for use ui
import pymysql # for use database
import tkcalendar # for use calendar
from datetime import datetime
import corona
import openapi_vaccination

# DB 매일 갱신
corona.main()
openapi_vaccination.run()


# 함수를 익명함수로 넣어서 def UI() 안에 다 넣어버릴지

def getConnection() : 
    conn = pymysql.connect(host='127.0.0.1',user ='root',password='root',db='proj1',charset='utf8')
    return conn 


def getData():
    #date =  # get date from calendar    
    conn = conn = pymysql.connect(host='127.0.0.1',user ='root',password='root',db='proj1',charset='utf8')
    cur = conn.cursor()
    
    # initialization
    data_S_HJ.config(text = "")
    data_SN_HJ.config(text = "")
    data_T_HJ.config(text = "")
    data_N_HJ.config(text = "")
    data_FIR_INC.config(text = "")
    data_SCD_INC.config(text = "")
    data_ADD_INC.config(text = "")
    data_FIR_INC_RATE.config(text = "")
    data_SCD_INC_RATE.config(text = "")
    data_ADD_INC_RATE.config(text = "")
    
    date = get_date()
    
    cur.execute("SELECT * FROM corona3 where 서울기준일 LIKE '"+ date +"%'")
    while True:
        row = cur.fetchone()
        if row == None:
            break
        else:
            data_S_HJ.config(text = str(row[1]) + "명")
            data_SN_HJ.config(text = str(row[2]) + "명")
            data_T_HJ.config(text = str(row[11]) + "명")
            data_N_HJ.config(text = str(row[12]) + "명")
    
    cur.execute("SELECT * from vaccinate WHERE S_VC_DT='" + date + "'")
    count = 0
    while True:
        row = cur.fetchone()
        if row == None:
            break
        else:
            data_FIR_INC.config(text = str(row[3]) + "명")
            data_SCD_INC.config(text = str(row[6]) + "명")
            data_ADD_INC.config(text = str(row[9]) + "명")
            data_FIR_INC_RATE.config(text = str(row[4]) + "%")
            data_SCD_INC_RATE.config(text = str(row[7]) + "%")
            data_ADD_INC_RATE.config(text = str(row[10]) + "%")
    
    conn.close()
    
    
def get_date():
    caldate = cal.get_date()
    temp = caldate.split('/')

    YY = "20" + temp[2]
    
    if len(temp[0]) == 1:
        MM = '0' + temp[0]
    else:
        MM = temp[0]
    
    if len(temp[1]) == 1:
        DD = '0' + temp[1]
    else: 
        DD = temp[1]
    
    date = YY + "." + MM + "." + DD
    
    return date
    

window = tkinter.Tk()
window.title("")
window.geometry("500x250+100+100")
frame = tkinter.Frame(window) # make frame
frame.pack()

# view: frame for calendar
frame_cal = tkinter.Frame(frame)
frame_cal.grid(row = 0, column = 0, padx = 20, pady = 20)

# start date = today
cal = tkcalendar.Calendar(frame_cal, selectmode = "day", year = datetime.today().year, month = datetime.today().month, day = datetime.today().day)
cal.pack()

button = tkinter.Button(frame_cal, width = 20, height = 1, text = "조회하기", command = lambda:getData())
button.pack()


# view: frame for show data
frame_show = tkinter.Frame(frame)
frame_show.grid(row = 0, column = 1, padx = 20, pady = 20)

label_S_HJ = tkinter.Label(frame_show, text = "서울시 확진자: ")
label_S_HJ.grid(row = 0, column = 0)
data_S_HJ = tkinter.Label(frame_show, textvariable = "")
data_S_HJ.grid(row = 0, column = 1)
label_SN_HJ = tkinter.Label(frame_show, text = "서울시 추가 확진:")
label_SN_HJ.grid(row = 1, column = 0)
data_SN_HJ = tkinter.Label(frame_show, textvariable = "")
data_SN_HJ.grid(row = 1, column = 1)
label_T_HJ = tkinter.Label(frame_show, text = "전국 확진: ")
label_T_HJ.grid(row = 2, column = 0)
data_T_HJ = tkinter.Label(frame_show, textvariable = "")
data_T_HJ.grid(row = 2, column = 1)
label_N_HJ = tkinter.Label(frame_show, text = "전국 추가 확진: ")
label_N_HJ.grid(row = 3, column = 0)
data_N_HJ = tkinter.Label(frame_show, textvariable = "")
data_N_HJ.grid(row = 3, column = 1)

label_FIR_INC = tkinter.Label(frame_show, text = "1차 접종 누계: ")
label_FIR_INC.grid(row = 4, column = 0)
data_FIR_INC = tkinter.Label(frame_show, textvariable = "")
data_FIR_INC.grid(row = 4, column = 1)
label_SCD_INC = tkinter.Label(frame_show, text = "2차 접종 누계: ")
label_SCD_INC.grid(row = 5, column = 0)
data_SCD_INC = tkinter.Label(frame_show, textvariable = "")
data_SCD_INC.grid(row = 5, column = 1)
label_ADD_INC = tkinter.Label(frame_show, text = "추가 접종 누계: ")
label_ADD_INC.grid(row = 6, column = 0)
data_ADD_INC = tkinter.Label(frame_show, textvariable = "")
data_ADD_INC.grid(row = 6, column = 1)
label_FIR_INC_RATE = tkinter.Label(frame_show, text = "1차 접종률: ")
label_FIR_INC_RATE.grid(row = 7, column = 0)
data_FIR_INC_RATE = tkinter.Label(frame_show, textvariable = "")
data_FIR_INC_RATE.grid(row = 7, column = 1)
label_SCD_INC_RATE = tkinter.Label(frame_show, text = "2차 접종률: ")
label_SCD_INC_RATE.grid(row = 8, column = 0)
data_SCD_INC_RATE = tkinter.Label(frame_show, textvariable = "")
data_SCD_INC_RATE.grid(row = 8, column = 1)
label_ADD_INC_RATE = tkinter.Label(frame_show, text = "추가 접종률: ")
label_ADD_INC_RATE.grid(row = 9, column = 0)
data_ADD_INC_RATE = tkinter.Label(frame_show, textvariable = "")
data_ADD_INC_RATE.grid(row = 9, column = 1)

window.mainloop()


# In[4]:


import tkinter
import pymysql
import pandas as pd # for use data

window = tkinter.Tk()



    
def get_date():
    caldate = cal.get_date()
    # 1 / 1 9 / 2 2
    # 0 1 2 3 4 5 6
    temp = caldate.split('/')

    YY = "20" + temp[2]
    
    if len(temp[0]) == 1:
        MM = '0' + temp[0]
    else:
        MM = temp[0]
    
    if len(temp[1]) == 1:
        DD = '0' + temp[1]
    else: 
        DD = temp[1]
    
    date = YY + "." + MM + "." + DD
    
    return date
        
    
def click2(message):
    date = get_date()
    conn = getConnection() 
    cur = conn.cursor()
    print(data1)
    
    # load data at table 'corona3'
    cur.execute("SELECT * FROM corona3 where 서울기준일 LIKE '"+date+"%'")
#     result = [ ] 
    result = ""
    while (True ) :
        row = cur.fetchone()
        if row == None :
            break; 
#         print(row[0])
        result = result+"\n" + str(row[1])+"\n" + str(row[2])+"\n" +                  str(row[11])+"\n" +  str(row[12])
#         result.append(row[0]) 

    # load data at table 'vaccinate'
    cur.execute("SELECT * from vaccinate WHERE S_VC_DT='" + date + "'")
    while True:
        row = cur.fetchone()
        if row == None:
            break;
        result = result +"\n" +str(row[3])+"\n"  + str(row[6])+"\n" + str(row[9]) + "\n"
        
    message.set( result )
    conn.close()
    return result 

def getConnection() : 
    conn = pymysql.connect(host='127.0.0.1',user ='root',password='root',db='proj1',charset='utf8')
    return conn 


# view: frame for calendar
frame_cal = tkinter.Frame(window)
frame_cal.pack(side = "left", padx = 15)

# 오늘 날짜 받아와서 시작일 지정
cal = tkcalendar.Calendar(frame_cal, selectmode = "day", year = 2022, month = 1, day = 26)
cal.pack()

#temp = tkinter.StringVar()
#entry = tkinter.Entry(frame_cal, textvariable = temp)
#entry.grid(row = 0, column = 0)
button = tkinter.Button(frame_cal, text = "Enter", command = lambda:getData())
#button = tkinter.Button(frame_cal, text = "Enter", command)
#button.grid(row = 0, column = 1)
button.pack()

frame = tkinter.Frame(window)
frame.pack()
var1 = tkinter.StringVar()
var2 = tkinter.StringVar() 

# label1 = tkinter.Label(frame, text='달력정보를 입력하세요(yyyy.mm.dd) ')
# #label1.pack()
# label1.grid(row=0,column=0)
# entry1 = tkinter.Entry(frame,textvariable=var1)
# entry1.grid(row=0,column=1)
# #entry1.pack() 

message = tkinter.StringVar()

label2 = tkinter.Label(frame, text="서울시 확진자: \n서울시 추가 확진:\n전국확진:\n전국추가확진:\n1차접종 누계:\n2차접종 누계:\n추가접종 누계:")
label2.grid(row=2,column=0)
#label2.pack()

label3 = tkinter.Label(frame, textvariable=message)
label3.grid(row=2,column=1)

frame2 = tkinter.Frame(window)
frame2.pack()

button = tkinter.Button(frame2, text="조회", command=lambda : click2(message), height=2, width=30) 
#button.grid(row=10,column=0)
button.pack()

window.mainloop()


# In[3]:


import tkinter # for use ui
import pymysql # for use database
import tkcalendar # for use calendar
from datetime import datetime

# 함수를 익명함수로 넣어서 def UI() 안에 다 넣어버릴지

def getData():
#date =  # get date from calendar    
conn = pymysql.connect(host='127.0.0.1',user ='root',password='root',db='proj1',charset='utf8')
cur = conn.cursor()

# initialization
data_S_HJ.config(text = "")
data_SN_HJ.config(text = "")
data_T_HJ.config(text = "")
data_N_HJ.config(text = "")
data_FIR_INC.config(text = "")
data_SCD_INC.config(text = "")
data_ADD_INC.config(text = "")
data_FIR_INC_RATE.config(text = "")
data_SCD_INC_RATE.config(text = "")
data_ADD_INC_RATE.config(text = "")

#date = get_date()
caldate = cal.get_date()
temp = caldate.split('/')

YY = "20" + temp[2]

if len(temp[0]) == 1:
    MM = '0' + temp[0]
else:
    MM = temp[0]

if len(temp[1]) == 1:
    DD = '0' + temp[1]
else: 
    DD = temp[1]

date = YY + "." + MM + "." + DD


cur.execute("SELECT * FROM corona3 where 서울기준일 LIKE '"+ date +"%'")
while True:
    row = cur.fetchone()
    if row == None:
        break
    else:
        data_S_HJ.config(text = str(row[1]))
        data_SN_HJ.config(text = str(row[2]))
        data_T_HJ.config(text = str(row[11]))
        data_N_HJ.config(text = str(row[12]))

cur.execute("SELECT * from vaccinate WHERE S_VC_DT='" + date + "'")
count = 0
while True:
    row = cur.fetchone()
    if row == None:
        break
    else:
        data_FIR_INC.config(text = str(row[3]))
        data_SCD_INC.config(text = str(row[6]))
        data_ADD_INC.config(text = str(row[9]))
        data_FIR_INC_RATE.config(text = str(row[4]))
        data_SCD_INC_RATE.config(text = str(row[7]))
        data_ADD_INC_RATE.config(text = str(row[10]))

conn.close()

window = tkinter.Tk()
window.title("")
window.geometry("500x250+100+100")
frame = tkinter.Frame(window) # make frame
frame.pack()

# view: frame for calendar
frame_cal = tkinter.Frame(frame)
frame_cal.grid(row = 0, column = 0, padx = 20, pady = 20)

# start date = today
cal = tkcalendar.Calendar(frame_cal, selectmode = "day", year = datetime.today().year, month = datetime.today().month, day = datetime.today().day)
cal.pack()

button = tkinter.Button(frame_cal, width = 20, height = 1, text = "조회하기", command = lambda:getData())
button.pack()


# view: frame for show data
frame_show = tkinter.Frame(frame)
frame_show.grid(row = 0, column = 1, padx = 20, pady = 20)

label_S_HJ = tkinter.Label(frame_show, text = "서울시 확진자: ")
label_S_HJ.grid(row = 0, column = 0)
data_S_HJ = tkinter.Label(frame_show, textvariable = "")
data_S_HJ.grid(row = 0, column = 1)
label_SN_HJ = tkinter.Label(frame_show, text = "서울시 추가 확진:")
label_SN_HJ.grid(row = 1, column = 0)
data_SN_HJ = tkinter.Label(frame_show, textvariable = "")
data_SN_HJ.grid(row = 1, column = 1)
label_T_HJ = tkinter.Label(frame_show, text = "전국 확진: ")
label_T_HJ.grid(row = 2, column = 0)
data_T_HJ = tkinter.Label(frame_show, textvariable = "")
data_T_HJ.grid(row = 2, column = 1)
label_N_HJ = tkinter.Label(frame_show, text = "전국 추가 확진: ")
label_N_HJ.grid(row = 3, column = 0)
data_N_HJ = tkinter.Label(frame_show, textvariable = "")
data_N_HJ.grid(row = 3, column = 1)

label_FIR_INC = tkinter.Label(frame_show, text = "1차 접종 누계: ")
label_FIR_INC.grid(row = 4, column = 0)
data_FIR_INC = tkinter.Label(frame_show, textvariable = "")
data_FIR_INC.grid(row = 4, column = 1)
label_SCD_INC = tkinter.Label(frame_show, text = "2차 접종 누계: ")
label_SCD_INC.grid(row = 5, column = 0)
data_SCD_INC = tkinter.Label(frame_show, textvariable = "")
data_SCD_INC.grid(row = 5, column = 1)
label_ADD_INC = tkinter.Label(frame_show, text = "추가 접종 누계: ")
label_ADD_INC.grid(row = 6, column = 0)
data_ADD_INC = tkinter.Label(frame_show, textvariable = "")
data_ADD_INC.grid(row = 6, column = 1)
label_FIR_INC_RATE = tkinter.Label(frame_show, text = "1차 접종률: ")
label_FIR_INC_RATE.grid(row = 7, column = 0)
data_FIR_INC_RATE = tkinter.Label(frame_show, textvariable = "")
data_FIR_INC_RATE.grid(row = 7, column = 1)
label_SCD_INC_RATE = tkinter.Label(frame_show, text = "2차 접종률: ")
label_SCD_INC_RATE.grid(row = 8, column = 0)
data_SCD_INC_RATE = tkinter.Label(frame_show, textvariable = "")
data_SCD_INC_RATE.grid(row = 8, column = 1)
label_ADD_INC_RATE = tkinter.Label(frame_show, text = "추가 접종률: ")
label_ADD_INC_RATE.grid(row = 9, column = 0)
data_ADD_INC_RATE = tkinter.Label(frame_show, textvariable = "")
data_ADD_INC_RATE.grid(row = 9, column = 1)

window.mainloop()

