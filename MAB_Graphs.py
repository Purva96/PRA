#####################################################################################################################
"""
# coding: utf-8
Developed By 
"""
#################################################################################################################### 


import openpyxl
import xlsxwriter
import xlrd
from xlutils.copy import copy
from xlwt import easyxf
import csv
import win32com.client
from datetime import datetime,timedelta
import pandas as pd
import json


# In[122]:


def mab_main_funct(path,Date):
    xlrd.xlsx.ensure_elementtree_imported(False, None)
    xlrd.xlsx.Element_has_iter = True
    main_list = []
    xls = pd.ExcelFile(path,engine ="openpyxl")
    df = pd.read_excel(xls,"MAB Graphs", usecols = "A:D")
    print(df)
    df = df.dropna()
    dfj= df.to_json(orient= "records")
    print(dfj)
    obj = json.loads(dfj)
    print(obj)

    rb = xlrd.open_workbook(path)
    sheet = rb.sheet_by_name("MAB Graphs")
    
    
    for rec in obj:

        TagName = rec["Name in legend"].split()[0]
        flow_TagName = TagName+sheet.cell_value(1,5)
        head_TagName = TagName+sheet.cell_value(1,6)
        Eff_TagName = TagName +sheet.cell_value(1,7)
        Date1=(datetime.strptime(Date, '%Y-%m-%d'))
        flow_dict = {"TagName" : flow_TagName,
            "Value" : rec['Flow'],
            "TimeStamp": str(Date1).split()[0]+"T00:00:00"
        }
        main_list.append(flow_dict) 
        head_dict = {"TagName" : head_TagName,
            "Value" : rec['Head'],
            "TimeStamp": str(Date1).split()[0]+"T00:00:00"
        }
        main_list.append(head_dict) 
        Eff_dict = {"TagName" : Eff_TagName,
            "Value" : rec['Efficiency'],
            "TimeStamp": str(Date1).split()[0]+"T00:00:00"
        }
        main_list.append(Eff_dict)
        Date=(datetime.strptime(Date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
        
    mab_json_fmt = json.dumps(main_list,indent =4)
#     print(pd.DataFrame.from_dict(main_list).head(20))
#     print(mab_json_fmt)  
    return mab_json_fmt
    
    
    


# In[123]:


# main_func(r'C:/Users/H373302/Documents/Local Github Repository/Configuration3.xlsx', '2020-11-10')


# In[ ]:




