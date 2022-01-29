#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests # for use api
import pandas as pd # for use data
import pymysql # for use DB

# key / url
API_AUTH_KEY = "616e56516c656a6937365a62686a4c"
url = "http://openapi.seoul.go.kr:8088/{}/json/tvCorona19VaccinestatNew/1/500/".format(API_AUTH_KEY)


# read data use api
# make list with open api data
def seoul_open_api_data(url, service):
    data_list = None
    try:
        result_dict = requests.get(url).json()
        result_data = result_dict[service]
        code = result_data['RESULT']['CODE']
        if code == 'INFO-000':
            data_list = result_data['row']
    except:
        pass
    return data_list


# make data frame with list of open api data
def make_data_frame(data_list):
    # S_VC_DT 접종일
    # FIR_SUB 접종대상자
    # FIR_INC1 당일 1차접종자 수
    # FIR_INC 1차접종 누계
    # FIR_INC_RATE 1차접종률
    # SCD_INC1 당일 2차접종자 수
    # SCD_INC 2차접종 누계
    # SCD_INC_RATE 2차접종률
    # ADD_INC1 당일 추가접종자 수
    # ADD_INC 추가접종 누계
    # ADD_INC_RATE 추가접종률
    # ADD_SUB 추가접종대상자
    columns = ['S_VC_DT', 'FIR_SUB', 'FIR_INC1',
               'FIR_INC', 'FIR_INC_RATE', 'SCD_INC1',
               'SCD_INC', 'SCD_INC_RATE', 'ADD_INC1',
               'ADD_INC', 'ADD_INC_RATE', 'ADD_SUB']
    data_df = pd.DataFrame(data = data_list, columns=columns)
    data_df.fillna(0)
    return data_df


# connect with database
def dbconnect():
    conn = pymysql.connect(host='127.0.0.1', user ='root', password='root', db ='proj1', charset='utf8')
    return conn 


# check if data already exist
def checkData(conn, row):
    cur2 = conn.cursor()
    cur2.execute("SELECT * from vaccinate WHERE S_VC_DT='" + row[0] + "'")
    temp = cur2.fetchone()
    if temp == None: 
        return True
    else:
        return False

    
# insert data in DB
def insertData(cur, row):
    # query for save DB
    sql = "INSERT INTO vaccinate VALUES ('"             + row[0] + "', " + str(row[1]) + ", " + str(row[2])+ ", "             + str(row[3]) + ", " + row[4] + ", " + str(row[5]) + ", "             + str(row[6]) + ", " + row[7] + ", " + str(row[8]) + ", "             + str(row[9]) + ", " + row[10] + ", " + str(row[11]) + ")"
    cur.execute(sql)

    
# save data in DB
def save_data(data_df):
    conn = dbconnect() # connect DB
    cur = conn.cursor()
    for i in range(len(data_df)):
        row = [] # temp list 
        for j in range(len(data_df.columns)):
            data = data_df.iloc[i, j]
            if data == '':
                data = '0'
            row.append(data)
        
        # check if data already exist
        check = checkData(conn, row)
        
        # query for save DB
        if check == True: # if there is no data already exists
            insertData(cur, row)
            conn.commit()

    conn.close() # close DB
    

data_list = seoul_open_api_data(url, 'tvCorona19VaccinestatNew')
data_df = make_data_frame(data_list)
save_data(data_df)
print("Succeed")

