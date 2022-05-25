import os
import pandas as pd
import numpy as np

file_dir='D:/论文数据/SPEI指数数据集/penman方程及站点数据计算SPEI不用python包/15单站点每月SPEI24时间序列(1981-2020)'
file_to='D:/论文数据/SPEI指数数据集/penman方程及站点数据计算SPEI不用python包/20每月所有站点SPEI24提取(1981-2020)'
all_csv_list=os.listdir(file_dir)

years=list(range(1981,2021,1))
months=list(range(1,13,1))


for year in years:
    for month in months:
        List=[]
        for file_csv in all_csv_list:
            data=pd.read_csv(os.path.join(file_dir,file_csv),thousands=',')
            data=data[['Station','Lat','Lon','Altitude','Year','Month','SPEI24']]
            row=data.loc[data['Year'].astype(str)==str(year)+'.0']
            row=row.loc[row['Month'].astype(str)==str(month)+'.0']
            List.append(np.array(row.values).flatten().tolist())
        dataframe=pd.DataFrame(List,columns=['Station','Lat','Lon','Altitude','Year','Month','SPEI_24'])
        dataframe.dropna(axis=0,how='all',inplace=True)
        if month<10:
            dataframe.to_csv(os.path.join(file_to,str(year)+'0'+str(month)+'.csv'),index=False)
        else:
            dataframe.to_csv(os.path.join(file_to,str(year)+str(month)+'.csv'),index=False)
    print(str(year)+'写入成功')
print('所有文件已写入成功')