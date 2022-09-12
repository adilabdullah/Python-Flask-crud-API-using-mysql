import mysql.connector
import os
import json

mysqldb=mysql.connector.connect(host="localhost",user="root",password="Contour@1234")#established connection   


def sample(data):
    try:
       
       return {"First_Name":data.fname,"Last_Name":data.lname,
       "Age":data.age,"Email":data.email,"Cell":data.cell};
    except Exception as e:
       return {"ResponseCode":95,"ResponseDesc":str(x)}; 


def create(data):
    try:
       mycursor=mysqldb.cursor();
       statement='insert into ibm_ace.person (SNO,F_NAME,L_NAME,EMAIL,CELL,AGE,SALARY,GRADE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)';
       tuple1 =(int(data["sno"]),data["fname"],data["lname"],data["email"],data["cell"],int(data["age"]),float(data["salary"]),data["grade"]);
       mycursor.execute(statement,(tuple1));
       mysqldb.commit();
       return {"ResponseCode":100,"ResponseDesc":"Success"};
    except Exception as e:
       mysqldb.rollback()  
       mysqldb.close()
       return {"ResponseCode":95,"ResponseDesc":str(e)}; 

def update(data,sno):
    try:
       mycursor=mysqldb.cursor();

       tuple1=(data["fname"],data["lname"],data["email"],data["cell"],int(data["age"]),float(data["salary"]),sno);
       mycursor.execute('update ibm_ace.person set F_NAME=%s,'+
       'L_NAME=%s,EMAIL=%s,CELL=%s,AGE=%s,SALARY=%s'+
       'where sno=%s',(data["fname"],data["lname"],data["email"],data["cell"],int(data["age"]),float(data["salary"]),sno));
       mysqldb.commit();
       return {"ResponseCode":100,"ResponseDesc":"Success"};
    except Exception as e:
       mysqldb.rollback()  
       mysqldb.close()
       return {"ResponseCode":95,"ResponseDesc":str(e)}; 

def delete(sno):
    try:
       mycursor=mysqldb.cursor();
       mycursor.execute('delete from ibm_ace.person where sno='+sno);
       mysqldb.commit();
       return {"ResponseCode":100,"ResponseDesc":"Success"};
    except Exception as e:
       mysqldb.rollback()  
       mysqldb.close() 
       return {"ResponseCode":95,"ResponseDesc":str(e)}; 
def AllData():
    try:
       mycursor=mysqldb.cursor();
       statement = 'select * from ibm_ace.person';
       mycursor.execute(statement)
       res = mycursor.fetchall()
       return res;
    except Exception as e:
       mysqldb.rollback()  
       mysqldb.close()
       return str(e); 


def specific(sno):
    try:
       mycursor=mysqldb.cursor();
       mycursor.execute('select * from ibm_ace.person where sno='+sno);
       return mycursor.fetchone();
    except Exception as e:
       mysqldb.rollback()  
       mysqldb.close()
       return str(e); 