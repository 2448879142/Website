# XY转线工具

## 摘要

创建新要素类，其中包含基于表的起点 x 坐标字段、起点 y  坐标字段、终点 x 坐标字段和终点 y 坐标字段中的值构建的大地测量线要素。 

## 用法

- 如果输入的是文本文件和 .csv（逗号分隔值）文件，请确保其符合关于表格数据源中指定的文件结构。
- 每条大地测量线均通过一组特定的表示起点 x 和 y 坐标以及终点  x 和 y 坐标的字段值构建。这些字段和值将包含在输出中。
- 测地线是地球表面上的曲线。但在输出时，测地线要素不是以参数（真）曲线形式存储的，而是以表示测地线路径的增密折线形式进行存储。如果测地线的长度相对较短，则在输出中可能由直线表示。随着线长度的增加，需要使用更多的折点来表示路径。
- 如果输出的是文件地理数据库或个人地理数据库中的要素类，则  Shape_Length 字段中的值始终使用由空间参考参数所指定的输出坐标系的单位；并且该值表示折线的平面长度。要测量测地线的长度或距离，请使用 ArcMap  测量工具；在测量之前，请确保相应地选择了“测地线”、“等角航线”或“大椭圆”选项。

## 语法

XYToLine_management  (in_table, out_featureclass, startx_field, starty_field, endx_field, endy_field,  {line_type}, {id_field}, {spatial_reference})

| 参数                     | 说明                                                         | 数据类型          |
| ------------------------ | ------------------------------------------------------------ | ----------------- |
| in_table                 | 输入表，可以是文本文件、CSV 文件、Excel  文件、dBASE 表或地理数据库表。 | Table View        |
| out_featureclass         | 包含增密测地线的输出要素类。                                 | Feature Class     |
| startx_field             | 输入表中的数值字段，其中包含在 spatial_reference 参数所指定的输出坐标系中进行定位的线的起点 x  坐标（或经度）。 | Field             |
| starty_field             | 输入表中的数值字段，其中包含在 spatial_reference 参数所指定的输出坐标系中进行定位的线的起点 y  坐标（或纬度）。 | Field             |
| endx_field               | 输入表中的数值字段，其中包含在 spatial_reference 参数所指定的输出坐标系中进行定位的线的终点 x 坐标（或经度）。 | Field             |
| endy_field               | 输入表中的数值字段，其中包含在 spatial_reference 参数所指定的输出坐标系中进行定位的线的终点 y 坐标（或纬度）。 | Field             |
| line_type (可选)         | 要构造的测地线的类型。  GEODESIC —  测地线类型，可以最准确地表示地球表面任意两点之间的最短距离。测地线的数学定义十分复杂冗长，因此此处略去该定义。这种线类型是默认类型。 GREAT_CIRCLE —测地线类型，可以表示地球表面与通过地心的平面的相交线上任意两点之间的路径。根据“空间参考”参数所指定的输出坐标系，在基于椭球体的坐标系中，该线表示大椭圆；在基于球体的坐标系中，该线表示唯一的大圆（球面上最大半径的圆）。 RHUMB_LINE —测地线类型，又称为等角航线 (loxodrome  line)，可以表示通过以极点为起点的等方位角所定义的椭球体表面上的任意两点之间的路径。等角航线在墨卡托投影中显示为直线。 NORMAL_SECTION —测地线类型，可以表示由椭球体表面与通过椭球体表面上两点并垂直于两点起点处椭球面的平面相交而定义的椭球面上任意两点之间的路径。因此，从  A 点到 B 点与从 B 点到 A 点的法向截面线不同。 | String            |
| id_field (可选)          | 输入表中的字段；此字段和值均包含在输出中，可用于连接输出要素和输入表中的记录。 | Field             |
| spatial_reference (可选) | 输出要素类的空间参考。可通过多种方式指定空间参考：  输入 .prj 文件的路径，如 C:/workspace/watershed.prj。  引用包含要应用的空间参考的要素类或要素数据集，例如 C:/workspace/myproject.gdb/landuse/grassland。  在使用此工具之前定义空间参考对象，例如之后要用作空间参考参数的 sr =  arcpy.SpatialReference("C:/data/Africa/Carthage.prj")。 | Spatial Reference |

## 代码示例

XYToLine 示例（独立脚本）

下面的示例用于将 DBF  表转换为两点大地测量线。

```python
# Import system modules
import arcpy
from arcpy import env

# Set local variables
input_table = r"c:\workspace\city2city.dbf"
out_lines = r"c:\workspace\flt4421.gdb\routing001"

#XY To Line
arcpy.XYToLine_management(input_table,out_lines,
                         "LOND1","LATD1","LOND2",
                         "LATD2","GEODESIC","idnum")
```

## 工具箱

![1692021930671.png](https://img1.imgtp.com/2023/08/14/7qbF99EG.png)