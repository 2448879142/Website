# 笔记

----------------

> [Python教程](https://www.runoob.com/python/python-tutorial.html)  
> [Python3教程](https://www.runoob.com/python3/python3-tutorial.html)


## 影像按地区覆盖整理分类

-----------------------

> 基于Python语言的arcpy模块包，对多景影像进行分类整理.

----------------

### 应用场景

每期影像处理后的成果，名称冗长，景数繁多，整体镶嵌又太费时间，业务上又常常需要查看各县区影像，整期影像加载，软件负荷较大.

--------------

### 涉及软件

- ArcGIS Pro(建议使用Pro)
- ArcGIS

--------------------

### 操作流程

#### 新建工程文档，打开Python脚本框

- 打开ArcGIS Pro，新建地图文档，一般建议新建新文档，避免旧文档中默认的空间参考系与当前处理影像坐标系存在冲突.
- 点击分析→python→python窗口
- 输入python脚本代码

#### 文件目录说明

```menu
- 1_image_classifcation
    - 1_in_layer                 # 输入文件
        - *.tif
    - 2_select_features          # 分类整理的区域矢量数据
        - *.shp
    - 3_result_move_folder
        - "分类成果文件夹1"       # 按照自己需求进行修改 
        - "分类成果文件夹2"       # 按照自己需求进行修改
    - 4_spatialReference         # 空间参考文件
    - 代码.txt                   # python代码文件
    - ReadMe.txt                # 使用说明
```

### Python代码

#### 参数

```python
''' 
param:
in_layer:文件夹，待整理分类影像'.tif'的集合
select_features:文件夹，进行整理分类的区域矢量数据'.shp'的集合
result_move_folder:文件夹，输出分类后的成果
spatialReference:文件夹，读取栅格转换矢量后的坐标系
'''
```

#### 导入模块
```python
import os
import arcpy
```

#### 栅格转矢量函数
```python
def GetVectorFromTIFF(in_ras_path,out_vector_path,spatialReference):
    arcpy.env.workspace=os.path.dirname(in_ras_path)
    sr = arc.SpatialReference(spatialReference)
    arcpy.CreateFeatureclass_management(os.path.dirname(out_vector_path),os.path.basename(out_vector_path),geometry_type="POLYGON",spatial_reference=sr)
    arcpy.AddField_management(in_table=out_vector_path,field_name="RasterName",field_type="TEXT",field_length=200)
    cursor = arcpy.InsertCursor(out_vector_path)
    point = arcpy.Point()
    array = arcpy.Array()
    corners = ["lowerLeft","lowerRight","upperRight","upperLeft"]
    feat = cursor.newRow()
    r = arcpy.Raster(in_ras_path)
    for corner in corners:
        point.X = getattr(r.extent,"%s" % corner).X
        point.Y = getattr(r.extent,"%s" % corner).Y
        array.add(point)
    array.add(array.getObject(0))
    polygon=arcpy.Polygon(array)
    feat.shape =polygon
    feat.setValue("RasterName",os.path.basename(in_ras_path))
    cursor.insertRow(feat)
    array.removeAll()
```

#### 按位置相交获得影像名称函数

```python
def GetNameBySelectLocation(in_layer,select_features,overlap_type='INTERSECT',selection_type='NEW_SELECTION'):
    arcpy.env.workspace = in_layer
    arcpy.MakeFeatureLayer_management(in_layer,'lyr')
    selection = arcpy.SelectLayerByLocation_management(in_layer='lyr',select_features=select_features,overlap_type=overlap_type,selection_type=selection_type)
    arcpy.MakeFeatureLayer_management(selection,'select_shp')
    num = arcpy.GetCount_management('select_shp')
    if not num == '0':
        rows= arcpy.SearchCursor('select_shp',fields='RasterName')
        value=[]
        for row in rows:
            value.append(row.getValue("RasterName"))
        return value
    else:
        return ''
```

#### 保存栅格名称到文件
```python
def SaveNameToTXT(wait_move_folder,result_folder):
    with open(result_folder+'re.txt',mode='a',encoding='utf-8') as f:
        f.write('move ' + wait_move_folder + '* '+result_folder)
        f.write('\n')
```
#### Main函数
```python
in_layer = 栅格数据文件夹路径
vector = 临时矢量文件存放路径
select_features=筛选栅格数据的矢量文件
result_move_folder = 成果文件夹
spatialReference =空间坐标系参数文件夹
sum = 0 # 计数器
for f in os.listdir(in_layer):
    if f.endswith('tif'):
        GetVectorFromTIFF(in_layer+f,vector,spatialReference)
        for shp in os.listdir(select_features):
            if shp.endswith('shp'):
                for v in GetNameBySelectLocation(vector,select_features+shp):
                    SaveNameToTXT(in_layer+v,result_move_folder+shp.split('.')[0][0:3]+'\\')
        sum = sum + 1
        print("已完成"+str(num)+"景")
print("任务完成")
```


