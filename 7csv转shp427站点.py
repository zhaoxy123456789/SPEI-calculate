import shapefile as shp
import pandas as pd
from osgeo import gdal
from osgeo import osr
import csv,os

file_dir="D:/论文数据/SPEI指数数据集/penman方程及站点数据计算SPEI不用python包/9每月427站点SPEI3提取"
file_to="D:/论文数据/SPEI指数数据集/penman方程及站点数据计算SPEI不用python包/10每月SPEI3指数shp文件(427站点)"
all_csv_list=os.listdir(file_dir)
for signal_csv in all_csv_list:
    df=pd.read_csv(os.path.join(file_dir,signal_csv))
    data_address = os.path.join(file_to,signal_csv) # 新建数据存放位置 data_address = "./output/point05.shp" # 新建数据存放位置
    file = shp.Writer(data_address)
    #创建字段
    columns_list=list(df.head(0))#获取字段列名
    #添加字段
    for i in range(len(columns_list)):
        if columns_list[i] in ['Station','Year','Month']:
            file.field(columns_list[i],'N','10')
        else:
            file.field(columns_list[i],'N','30',decimal=4)
    for num in range(len(df['Station'])):
        file.point(df['Lon'][num],df['Lat'][num])
        file.record(df['Station'][num],df['Lat'][num],df['Lon'][num],df['Altitude'][num],df['Year'][num],df['Month'][num],
                    df['SPEI_3'][num])
    file.close()
    # 定义投影
    proj = osr.SpatialReference() 
    proj.ImportFromEPSG(4326) # 4326-GCS_WGS_1984; 4490- GCS_China_Geodetic_Coordinate_System_2000
    wkt = proj.ExportToWkt()
    # 写入投影
    f = open(data_address.replace(".shp", ".prj"), 'w') 
    f.write(wkt)#写入投影信息
    f.close()#关闭操作流'''
    print(str(signal_csv)+'写入成功')
print('全部文件转化成功')