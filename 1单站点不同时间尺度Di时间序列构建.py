from cmath import sqrt
import pandas as pd
import numpy as np
from scipy.special import gamma
import datetime,os


file_dir = 'D:/论文数据/SPEI指数数据集/penman方程及站点数据计算SPEI不用python包/1单站点每月降水和pet时间序列(1981-2020)'
all_csv_list = os.listdir(file_dir)
file_to = 'D:/论文数据/SPEI指数数据集/penman方程及站点数据计算SPEI不用python包/2单站点每月不同时间尺度Di时间序列(1981-2020)'


for file in all_csv_list:
    data = pd.read_csv(os.path.join(file_dir,file), thousands=',')

    pre_list1=data['prectotal']
    pet_list1=data['pet']

    pre_list3=[np.nan]*2
    pet_list3=[np.nan]*2

    pre_list6=[np.nan]*5
    pet_list6=[np.nan]*5

    pre_list9=[np.nan]*8
    pet_list9=[np.nan]*8

    pre_list12=[np.nan]*11
    pet_list12=[np.nan]*11

    pre_list24=[np.nan]*23
    pet_list24=[np.nan]*23

    data['D1']=np.array(pre_list1)-np.array(pet_list1)

    for i in range(3,len(data)+1):
        number_pre3, number_pet3 = data['prectotal'][i-3:i].sum(), data['pet'][i-3:i].sum()
        pre_list3.append(number_pre3)
        pet_list3.append(number_pet3)
    data['D3']=np.array(pre_list3)-np.array(pet_list3)

    for i in range(6,len(data)+1):
        number_pre6, number_pet6 = data['prectotal'][i-6:i].sum(), data['pet'][i-6:i].sum()
        pre_list6.append(number_pre6)
        pet_list6.append(number_pet6)
    data['D6']=np.array(pre_list6)-np.array(pet_list6)

    for i in range(9,len(data)+1):
        number_pre9, number_pet9 = data['prectotal'][i-9:i].sum(), data['pet'][i-9:i].sum()
        pre_list9.append(number_pre9)
        pet_list9.append(number_pet9)
    data['D9']=np.array(pre_list9)-np.array(pet_list9)
    
    for i in range(12,len(data)+1):
        number_pre12, number_pet12 = data['prectotal'][i-12:i].sum(), data['pet'][i-12:i].sum()
        pre_list12.append(number_pre12)
        pet_list12.append(number_pet12)
    data['D12']=np.array(pre_list12)-np.array(pet_list12)

    for i in range(24,len(data)+1):
        number_pre24, number_pet24 = data['prectotal'][i-24:i].sum(), data['pet'][i-24:i].sum()
        pre_list24.append(number_pre24)
        pet_list24.append(number_pet24)
    data['D24']=np.array(pre_list24)-np.array(pet_list24)


    data.to_csv(os.path.join(file_to,file+'_pre_pet.csv'))
    print(file+'写入成功')
print('所有文件写入成功')