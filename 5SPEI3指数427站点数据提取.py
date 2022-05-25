import pandas as pd
import os


file_dir = 'D:/站点SPEI指数/daily_SPEI_data_multi-scale_by_each_station_and_each_scale/monthly_spei_GEV_3monthscale'
all_csv_list = os.listdir(file_dir)
file_from = 'D:/论文数据/SPEI指数数据集/penman方程及站点数据计算SPEI不用python包/4单站点每月SPEI3时间序列(1981-2020)'
file_to = 'D:/论文数据/SPEI指数数据集/penman方程及站点数据计算SPEI不用python包/8SPEI3指数427站点数据提取'


file_list = []
for file_name in all_csv_list:
    stationid = file_name[0:5]
    new_file_name = str(stationid) + '.csv_pre_pet.csv_spei3.csv'
    data = pd.read_csv(os.path.join(file_from, new_file_name), thousands=',')
    data.to_csv(os.path.join(file_to, new_file_name))
    print(str(stationid) + '写入成功')
print('所有文件写入成功')