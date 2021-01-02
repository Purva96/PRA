{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5714\n",
      "[{'TagName': '5714_WGC_2nd Stage Head_Flow', 'Value': 16770.0, 'TimeStamp': '2020-11-11T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Head', 'Value': 14610.0, 'TimeStamp': '2020-11-11T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Efficiency', 'Value': 75.47, 'TimeStamp': '2020-11-11T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Flow', 'Value': 18270.0, 'TimeStamp': '2020-11-12T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Head', 'Value': 14370.0, 'TimeStamp': '2020-11-12T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Efficiency', 'Value': 76.3, 'TimeStamp': '2020-11-12T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Flow', 'Value': 19660.0, 'TimeStamp': '2020-11-13T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Head', 'Value': 13990.0, 'TimeStamp': '2020-11-13T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Efficiency', 'Value': 77.14, 'TimeStamp': '2020-11-13T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Flow', 'Value': 20970.0, 'TimeStamp': '2020-11-14T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Head', 'Value': 13440.0, 'TimeStamp': '2020-11-14T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Efficiency', 'Value': 77.51, 'TimeStamp': '2020-11-14T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Flow', 'Value': 22130.0, 'TimeStamp': '2020-11-15T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Head', 'Value': 12780.0, 'TimeStamp': '2020-11-15T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Efficiency', 'Value': 77.03, 'TimeStamp': '2020-11-15T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Flow', 'Value': 22830.0, 'TimeStamp': '2020-11-16T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Head', 'Value': 12130.0, 'TimeStamp': '2020-11-16T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Efficiency', 'Value': 76.0, 'TimeStamp': '2020-11-16T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Flow', 'Value': 23670.0, 'TimeStamp': '2020-11-17T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Head', 'Value': 10970.0, 'TimeStamp': '2020-11-17T00:00:00'}, {'TagName': '5714_WGC_2nd Stage Head_Efficiency', 'Value': 73.48, 'TimeStamp': '2020-11-17T00:00:00'}]\n"
     ]
    }
   ],
   "source": [
    "import openpyxl\n",
    "import xlsxwriter\n",
    "import xlrd\n",
    "from xlutils.copy import copy\n",
    "from xlwt import easyxf\n",
    "import csv\n",
    "import win32com.client\n",
    "from datetime import datetime,timedelta\n",
    "Main_list=[]\n",
    "FlowValue_list=[]\n",
    "HeadValue_list=[]\n",
    "EffValue_list=[]\n",
    "Date='2020-11-10'\n",
    "path_of_file = \"WGC Stage2.xlsx\"\n",
    "\n",
    "rb = xlrd.open_workbook(path_of_file)\n",
    "sheet = rb.sheet_by_index(0)\n",
    "\n",
    "for i in range(sheet.nrows):\n",
    "    Col_A_Cellvalues=sheet.cell_value(i,0)\n",
    "    Col_B_Cellvalues=sheet.cell_value(i,1)\n",
    "    Col_C_Cellvalues=sheet.cell_value(i,2)\n",
    "    try:\n",
    "        if \"Name in legend\" in Col_A_Cellvalues:\n",
    "            legend_name=sheet.cell_value(i,1).split()[0]\n",
    "            print(legend_name)\n",
    "            Eff_Tag_Name= legend_name+\"_WGC_2nd Stage Head_Efficiency\"\n",
    "            Flow_Tag_Name=legend_name+\"_WGC_2nd Stage Head_Flow\"\n",
    "            Head_Tag_Name=legend_name+\"_WGC_2nd Stage Head_Head\"\n",
    "#             print(Eff_Tag_Name,Flow_Tag_Name,Head_Tag_name,sep=\"\\n\")\n",
    "    except:\n",
    "        pass\n",
    "    if type(Col_A_Cellvalues)==float or type(Col_A_Cellvalues)==int :\n",
    "        FlowValue_list.append(Col_A_Cellvalues)\n",
    "    if type(Col_B_Cellvalues)==float or type(Col_B_Cellvalues)==int:\n",
    "        HeadValue_list.append(Col_B_Cellvalues)\n",
    "    if type(Col_C_Cellvalues)==float or type(Col_C_Cellvalues)==int:\n",
    "        EffValue_list.append(Col_C_Cellvalues)   \n",
    "        \n",
    "\n",
    "for i in range(len(FlowValue_list)):\n",
    "    Date=(datetime.strptime(Date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')\n",
    "    mab_flow_dict={'TagName': Flow_Tag_Name,\n",
    "                   'Value': FlowValue_list[i],\n",
    "                  'TimeStamp':Date+\"T00:00:00\"                 \n",
    "                 }     \n",
    "    Main_list.append(mab_flow_dict)\n",
    "    mab_head_dict={'TagName': Head_Tag_Name,\n",
    "                   'Value': HeadValue_list[i],\n",
    "                  'TimeStamp':Date+\"T00:00:00\"                 \n",
    "                 } \n",
    "    Main_list.append(mab_head_dict)\n",
    "    mab_Eff_dict={'TagName': Eff_Tag_Name,\n",
    "                   'Value': EffValue_list[i],\n",
    "                  'TimeStamp':Date+\"T00:00:00\"                 \n",
    "                 } \n",
    "    Main_list.append(mab_Eff_dict)\n",
    "print(Main_list)\n",
    "with open(\"Jsonformat.txt\",mode=\"w\") as f:\n",
    "    f.write(str(Main_list))\n",
    "   \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
