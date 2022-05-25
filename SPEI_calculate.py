import pandas as pd
import numpy as np
from scipy.special import gamma
import datetime,os

file_dir = 'D:/论文数据/SPEI指数数据集/penman方程及站点数据计算SPEI不用python包/2单站点每月不同时间尺度Di时间序列(1981-2020)'
all_csv_list = os.listdir(file_dir)
file_to = 'D:/论文数据/SPEI指数数据集/penman方程及站点数据计算SPEI不用python包/15单站点每月SPEI24时间序列(1981-2020)'

c0,c1,c2,d1,d2,d3=2.515517,0.802853,0.010328,1.432788,0.189269,0.001308



for file in all_csv_list:
    data = pd.read_csv(os.path.join(file_dir,file), thousands=',')
    data = data[['Station','Lat','Lon','Altitude','Year','Month','prectotal','pet','D24']]
    dataframe=pd.DataFrame()
    for i in range(1,13):
        SPEI_list=[]
        dataDay_Di1 = data[data['Month']==i]['D24']
        dataDay_Di_sort1 = sorted(dataDay_Di1)
        Fi=[(x-0.35)/len(dataDay_Di_sort1) for x in range(1,len(dataDay_Di_sort1)+1)]
        Fi1=[(1-Fi[ind])*v for ind,v in enumerate(dataDay_Di_sort1)]
        Fi2=[(1-Fi[ind])**2*v for ind,v in enumerate(dataDay_Di_sort1)]
        w0=np.nanmean(dataDay_Di_sort1)
        w1=np.nanmean(Fi1)
        w2=np.nanmean(Fi2)
        b_=(2*w1-w0)/(6*w1-w0-6*w2)
        a_=(w0-2*w1)*b_/(gamma(1+1/b_)*gamma(1-1/b_))
    #        b_=round(b_,2)
    #        a_=round(a_,2)
        r=w0-a_*gamma(1+1/b_)*gamma(1-1/b_)
        Fx=[(1+abs(a_/(v-r))**b_)**-1  for v in dataDay_Di1 ]
    #        Fx=[(1+(a_/(v-r))**b_)**-1 if a_/(v-r)>=0 else (1-abs(a_/(v-r))**b_)**-1 for v in dataDay_Di ]
    #        Fx=[]
    #        for v in dataDay_Di:
    #            print((1+(a_/(dataDay_Di[5]-r))**b_)**-1)
        
        
        P=[]
        for v in Fx:
            if v<=0.5:
                P.append(v)
            else:
                P.append(1-v)
        w=[(-2*np.log(v))**0.5 for v in P]
        for ind,v in enumerate(Fx):
            if v<=0.5:
                SPEI_list.append(-(w[ind]-(c0+c1*w[ind]+c2*w[ind]**2)/(1+d1*w[ind]+d2*w[ind]**2+d3*w[ind]**3)))
            else:
                SPEI_list.append(w[ind]-(c0+c1*w[ind]+c2*w[ind]**2)/(1+d1*w[ind]+d2*w[ind]**2+d3*w[ind]**3))
        data1=data[data['Month']==i]
        data1['SPEI24']=SPEI_list
        #print(data1)
        dataframe=dataframe.append(data1)
        dataframe.sort_values(['Year', 'Month'], inplace=True, ascending=True)
    #print(dataframe)
        #dataframe['SPEI3'].replace(list(dataframe[dataframe['SPEI3'].lt(-3)]['SPEI3']), dataframe[dataframe['SPEI3'].lt(-3)]['SPEI3']*0.3, inplace=True)
        #dataframe['SPEI3'].replace(list(dataframe[dataframe['SPEI3'].gt(3)]['SPEI3']), dataframe[dataframe['SPEI3'].gt(3)]['SPEI3']*0.3, inplace=True)
    dataframe.to_csv(os.path.join(file_to,file+'_spei24.csv'))
    print(file+'写入成功')
print('所有文件写入成功')
