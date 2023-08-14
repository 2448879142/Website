# Parameter对象

| 属性              | 说明                                                         |
| ----------------- | ------------------------------------------------------------ |
| **displayName**   | 工具对话框中显示的参数名称。                                 |
| **name**          | Python 中的工具语法中显示的参数名称。                        |
| **datatype**      | 每个 Python 工具箱的工具参数都有关联的数据类型。打开脚本工具对话框后，地理处理使用数据类型检查参数值。数据类型也可用于浏览数据 - 只有与参数数据类型匹配的数据才会显示在浏览对话框中。要获取参数数据类型的列表，请参阅[在 Python 工具箱中定义参数数据类型](https://desktop.arcgis.com/zh-cn/arcmap/10.3/analyze/creating-tools/defining-parameter-data-types-in-a-python-toolbox.htm)。可用的数据类型有许多种，最常用的数据类型包括字符串型、双精度型、布尔型、要素图层和栅格数据集。 |
| **parameterType** | 提供三种 **parameterType** 选项：**必选** - 必须提供值才能执行工具。**可选** - 不需要为参数提供值。**派生** - 参数只适用于输出参数（请参阅下文的方向参数）。派生的输出参数不显示在工具对话框中。 |
| **direction**     | 该属性定义参数是工具的输入参数还是工具的输出参数。如果将 **parameterType** 设置为“派生”，则应将参数 **direction** 设置为“输出”。 |

详细查看 **[Parameter](https://desktop.arcgis.com/zh-cn/arcmap/10.3/analyze/arcpy-classes/parameter.htm)** 对象。

## datatype

| 数据类型                                                     | **datatype** 关键字               | 说明                                                         |
| ------------------------------------------------------------ | --------------------------------- | ------------------------------------------------------------ |
| 地址定位器                                                   | **DEAddressLocator**              | 用于地理编码的数据集，存储地址属性、关联的索引以及用于定义将地点的非空间描述转换为空间数据这一过程的规则。 |
| 地址定位器样式                                               | **GPAddressLocatorStyle**         | 用于创建新地址定位器的模板。                                 |
| 分析像元大小                                                 | **analysis_cell_size**            | 栅格工具使用的像元大小。                                     |
| 任何值                                                       | **GPType**                        | 接受任何值的数据类型。                                       |
| ArcMap 文档                                                  | **DEMapDocument**                 | 包含一个地图、它的布局以及它的关联图层、表格、图表和报表的文件。 |
| 面积单位                                                     | **GPArealUnit**                   | 面积单位类型和值，例如平方米或英亩。                         |
| 布尔型                                                       | **GPBoolean**                     | 布尔值。                                                     |
| CAD 工程图数据集                                             | **DECadDrawingDataset**           | 与多种要素类型和符号系统混合的矢量数据源。此数据集不适用于基于要素类的查询或分析。 |
| 计算器表达式                                                 | **GPCalculatorExpression**        | 计算器表达式。                                               |
| 目录根                                                       | **DECatalogRoot**                 | 目录树中的顶级结点。                                         |
| 像元大小                                                     | **GPSACellSize**                  | ArcGIS Spatial Analyst 扩展模块 使用的像元大小。             |
| 像元大小 XY                                                  | **GPCellSizeXY**                  | 定义栅格像元的两侧。                                         |
| 复合图层                                                     | **GPCompositeLayer**              | 对多个子图层的引用，包括符号系统和渲染属性。                 |
| 压缩                                                         | **GPSAGDBEnvCompression**         | 指定用于栅格的压缩类型。                                     |
| 坐标系                                                       | **GPCoordinateSystem**            | 参考框架，例如 UTM 系统，由一组点、线和/或面，以及一组用于定义二维和三维空间中点的位置的规则组成。 |
| 坐标系文件夹                                                 | **DESpatialReferencesFolder**     | 磁盘上用于存储坐标系的文件夹。                               |
| Coverage                                                     | **DECoverage**                    | coverage 数据集，用于存储地理要素，如点、弧线和面以及相关要素属性表的专有数据模型。 |
| Coverage 要素类                                              | **DECoverageFeatureClasses**      | coverage 要素类，例如点、弧线、节点、路线、路线系统、弧段、面和区域。 |
| 数据元素                                                     | **DEType**                        | ArcCatalog 中可见的数据集。                                  |
| 数据文件                                                     | **GPDataFile**                    | 数据文件。                                                   |
| 数据库连接                                                   | **DERemoteDatabaseFolder**        | ArcCatalog 中的数据库连接文件夹。                            |
| 数据集                                                       | **DEDatasetType**                 | 相关数据的集合，通常被分组或存储在一起。                     |
| 日期                                                         | **GPDate**                        | 日期值。                                                     |
| dBASE 表                                                     | **DEDbaseTable**                  | 以 dBASE 格式存储的属性数据。                                |
| 抽取                                                         | **GP3DADecimate**                 | 指定 TIN 的节点子集，以创建该 TIN 的概化版本。               |
| 磁盘连接                                                     | **DEDiskConnection**              | 数据存储设备的访问路径。                                     |
| 双精度                                                       | **GPDouble**                      | 所有浮点数都存储为双精度 64 位值。                           |
| 加密字符串                                                   | **GPEncryptedString**             | 密码加密的字符串。                                           |
| 包络                                                         | **GPEnvelope**                    | 定义数据源所在的最小外接矩形的坐标对。                       |
| 评估级别                                                     | **GPEvaluationScale**             | 加权叠加操作中应用于输入值的级别值范围和增量值。             |
| 范围                                                         | **GPExtent**                      | 指定定义数据源的最小外接矩形的坐标对（x 最小值、y 最小值、x 最大值、y 最大值）。所有数据源的坐标都在此边界内。 |
| 提取值                                                       | **GPSAExtractValues**             | 提取值参数。                                                 |
| 要素类                                                       | **DEFeatureClass**                | 形状类型相同的空间数据的集合：点、多点、折线和面。           |
| 要素数据集                                                   | **DEFeatureDataset**              | 共享公共的地理区域和相同的空间参考系统的要素类集合。         |
| 要素图层                                                     | **GPFeatureLayer**                | 对要素类的引用，包括符号系统和渲染属性。                     |
| 要素集                                                       | **GPFeatureRecordSetLayer**       | 工具运行时绘制要素的交互式要素。                             |
| 字段                                                         | **Field**                         | 表中的列，用于存储单个属性的值。                             |
| 字段信息                                                     | **GPFieldInfo**                   | FieldMap 中字段的详细信息。                                  |
| 字段映射                                                     | **GPFieldMapping**                | 一个或多个输入表中的字段集合。                               |
| 文件                                                         | **DEFile**                        | 磁盘上的文件。                                               |
| 文件夹                                                       | **DEFolder**                      | 指定数据在磁盘上的存储位置。                                 |
| 格式化栅格                                                   | **GPRasterFormulated**            | 栅格表面，其像元值由公式或常量表示。                         |
| 模糊函数                                                     | **GPSAFuzzyFunction**             | 指定用于模糊化输入栅格的算法。                               |
| 地理数据集                                                   | **DEGeodatasetType**              | 地理数据库中具有共同主题的数据集合。                         |
| GeoDataServer                                                | **DEGeoDataServer**               | 引用地理数据库的粗粒度对象。                                 |
| 几何网络                                                     | **DEGeometricNetwork**            | 由拓扑连接的边和交汇点要素表示的线状网络。要素连通性以它们的几何重叠为基础。 |
| 地统计图层                                                   | **GPGALayer**                     | 对地理统计数据源的引用，包括符号系统和渲染属性。             |
| 地理统计搜索邻域                                             | **GPGASearchNeighborhood**        | 定义地统计图层的搜索邻域参数。                               |
| 地理统计值表                                                 | **GPGAValueTable**                | 定义地理统计图层的数据源和字段的集合。                       |
| GlobeServer                                                  | **DEGlobeServer**                 | Globe 服务器。                                               |
| GPServer                                                     | **DEGPServer**                    | 地理处理服务器。                                             |
| 图表                                                         | **GPGraph**                       | 图表。                                                       |
| 图表数据表                                                   | **GPGraphDataTable**              | 图表数据表。                                                 |
| 图层组                                                       | **GPGroupLayer**                  | 显示为单个图层，并按照单个图层处理的图层集合。图层组使组织地图、指定高级绘制顺序选项和分享图层以用于其他地图变得更加容易。 |
| 水平系数                                                     | **GPSAHorizontalFactor**          | 水平成本系数和水平相对移动角度之间的关系。                   |
| 影像服务                                                     | **DEImageServer**                 | 影像服务。                                                   |
| Index                                                        | **Index**                         | 用于加快在地理数据集和数据库中搜索记录的速度的数据结构。     |
| INFO 表达式                                                  | **GPINFOExpression**              | 定义和操纵 INFO 表中数据的语法。                             |
| INFO 项目                                                    | **GPArcInfoItem**                 | INFO 表中的项目。                                            |
| INFO 表                                                      | **DEArcInfoTable**                | INFO 数据库中的表格。                                        |
| LAS 数据集                                                   | **DELasDataset**                  | LAS 数据集存储对磁盘上一个或多个 LAS 文件以及其他表面要素的引用。LAS 文件是一个二进制文件，存储机载激光雷达数据。 |
| LAS 数据集图层                                               | **GPLasDatasetLayer**             | 引用磁盘上的 LAS 数据集的图层。此图层可将过滤器应用于 LAS 数据集引用的雷达文件和表面约束。 |
| 图层                                                         | **GPLayer**                       | 对数据源的引用，例如 shapefile、coverage、地理数据库要素类或栅格，包括符号系统和渲染属性。 |
| 图层文件                                                     | **DELayer**                       | 图层文件存储图层定义，包括符号系统和渲染属性。               |
| 线                                                           | **GPLine**                        | 由一系列相连的唯一 x,y 坐标对定义的笔直或弯曲的形状。        |
| 线性单位                                                     | **GPLinearUnit**                  | 线性单位类型和值，例如米或英尺。                             |
| 长                                                           | **GPLong**                        | 一个整数值。                                                 |
| M 值域                                                       | **GPMDomain**                     | M 坐标的最低和最高可能值的范围。                             |
| MapServer                                                    | **DEMapServer**                   | 地图服务器。                                                 |
| 镶嵌数据集                                                   | **DEMosaicDataset**               | 栅格和影像数据的集合，可以存储、查看和查询数据。镶嵌数据集是地理数据库中的数据模型，用于管理一组以目录形式存储并以镶嵌影像方式查看的栅格数据集（影像）。 |
| 镶嵌图层                                                     | **GPMosaicLayer**                 | 引用镶嵌数据集的图层。                                       |
| 邻域                                                         | **GPSANeighborhood**              | 用于计算统计数据的各像元周围区域的形状。                     |
| 网络分析类 FieldMap                                          | **NAClassFieldMap**               | 在网络分析图层（如中转点、设施点和事故点）和点要素类中的位置属性之间建立映射。 |
| 网络分析等级设置                                             | **GPNAHierarchySettings**         | 使用两个整数将网络数据集的等级值分成三组的等级属性。第一个整数设置第一组的结束值；第二个数值设置第三组的起始值。 |
| 网络分析图层                                                 | **GPNALayer**                     | 用于表达和解决网络路径问题的特殊图层组。Network Analyst 图层中存储的各子图层代表路径问题和解决方案的某些方面。 |
| 网络数据集                                                   | **DENetworkDataset**              | 拓扑连接网络元素的集合（边、交汇点和转弯），源于网络源并与网络属性的集合相关联。 |
| 网络数据集图层                                               | **GPNetworkDatasetLayer**         | 对网络数据集的引用，包括符号系统和渲染属性。                 |
| 宗地结构                                                     | **DECadastralFabric**             | 宗地结构是存储、维护和编辑相连宗地或宗地网络的连续表面的数据集。 |
| 宗地结构图层                                                 | **GPCadastralFabricLayer**        | 引用磁盘上宗地结构的图层。此图层作为图层组，将一组相关图层组织到单个图层下。 |
| 点                                                           | **GPPoint**                       | x,y 坐标对。                                                 |
| 面                                                           | **GPPolygon**                     | 一系列相连的 x,y 坐标对，其中，第一个坐标对和最后一个坐标对相同。 |
| 投影文件                                                     | **DEPrjFile**                     | 存储空间数据的坐标系统信息的文件。                           |
| 金字塔                                                       | **GPSAGDBEnvPyramid**             | 指定是否构建金字塔。                                         |
| 半径                                                         | **GPSARadius**                    | 指定用于插值的周围点。                                       |
| 随机数生成器                                                 | **GPRandomNumberGenerator**       | 指定创建随机值时使用的种子和生成器。                         |
| 栅格波段                                                     | **DERasterBand**                  | 栅格数据集中的图层。                                         |
| 栅格计算器表达式                                             | **GPRasterCalculatorExpression**  | 栅格计算器表达式。                                           |
| 栅格目录                                                     | **DERasterCatalog**               | 以表形式定义的栅格数据集的集合。每个表记录定义目录中的一个单独栅格数据集。 |
| 栅格目录图层                                                 | **GPRasterCatalogLayer**          | 对栅格目录的引用，包括符号系统和渲染属性。                   |
| 栅格数据图层                                                 | **GPRasterDataLayer**             | 栅格数据图层。                                               |
| 栅格数据集                                                   | **DERasterDataset**               | 根据一个或多个栅格构建的单个数据集。                         |
| 栅格图层                                                     | **GPRasterLayer**                 | 对栅格的引用，包括符号系统和渲染属性。                       |
| 栅格统计                                                     | **GPSAGDBEnvStatistics**          | 指定是否构建栅格统计。                                       |
| 栅格数据类型                                                 | **GPRasterBuilder**               | 栅格数据是通过指定栅格类型的方式添加到镶嵌数据集中的。栅格类型可与栅格格式一起识别元数据，例如地理配准、采集日期和传感器类型。 |
| 记录集                                                       | **GPRecordSet**                   | 交互表；工具运行时输入表值。                                 |
| 关系类                                                       | **DERelationshipClass**           | 地理数据库中对象间关系的详细信息。                           |
| 重映射                                                       | **GPSARemap**                     | 定义栅格像元值重分类方法的表。                               |
| 路径测量事件属性                                             | **GPRouteMeasureEventProperties** | 在表中指定一个字段来描述由线性参考路径系统测量的事件。       |
| 逻辑示意图数据集                                             | **DESchematicDataset**            | 逻辑示意图数据集中包含同一应用领域（例如水网或电网）中的逻辑示意图模板和逻辑示意图要素类的集合。 |
| 逻辑示意图                                                   | **DESchematicDiagram**            | 逻辑示意图。                                                 |
| 逻辑示意图文件夹/Schematic 文件夹                            | **DESchematicFolder**             | 逻辑示意图文件夹。                                           |
| 逻辑示意图图层                                               | **GPSchematicLayer**              | 逻辑示意图图层是复合图层，由基于与创建逻辑示意图时使用的模板相关联的逻辑示意图要素类的要素图层组成。 |
| 半变异函数                                                   | **GPSASemiVariogram**             | 指定用于量化自相关的两个地点的距离和方向。                   |
| ServerConnection                                             | **DEServerConnection**            | 服务器连接。                                                 |
| Shapefile                                                    | **DEShapefile**                   | shapefile 格式的空间数据。                                   |
| 空间参考                                                     | **GPSpatialReference**            | 用于存储空间数据集（包括空间域）的坐标系。                   |
| SQL 表达式                                                   | **GPSQLExpression**               | 定义和操纵关系数据库中的数据的语法。                         |
| 字符串                                                       | **GPString**                      | 文本值。                                                     |
| 隐藏字符串                                                   | **GPStringHidden**                | 以 * 字符掩膜的字符串。注:在脚本中使用时，文本不会加密。     |
| 表                                                           | **DETable**                       | 表格数据。                                                   |
| 表视图                                                       | **GPTableView**                   | 用于查看和编辑的表格数据表现形式，存储在内存或磁盘中。       |
| Terrain 图层                                                 | **GPTerrainLayer**                | 对 terrain 的引用，包括符号系统和渲染属性。它用于绘制 terrain。 |
| 文本文件                                                     | **DETextfile**                    | 以 ASCII 格式存储的数据。                                    |
| 分块大小                                                     | **GPSAGDBEnvTileSize**            | 指定存储在块中的数据的宽度和高度。                           |
| 时间配置                                                     | **GPSATimeConfiguration**         | 指定用于计算特定位置太阳辐射的时间段。                       |
| TIN                                                          | **DETin**                         | 一种将地理空间分割为连续的不重叠三角形的矢量数据结构。每个三角形的折点都是具有 x、y 和 z 值的采样数据点。 |
| TIN 图层                                                     | **GPTinLayer**                    | 对 TIN 的引用，包括拓扑关系、符号系统和渲染属性。            |
| 工具                                                         | **DETool**                        | 地理处理工具。                                               |
| 工具箱                                                       | **DEToolbox**                     | 地理处理工具箱。                                             |
| 拓扑要素                                                     | **GPSATopoFeatures**              | 输入到插值中的要素。                                         |
| 拓扑                                                         | **DETopology**                    | 定义并强制空间数据的完整性规则的拓扑。                       |
| 拓扑图层                                                     | **GPTopologyLayer**               | 对拓扑的引用，包括符号系统和渲染属性。                       |
| [值表](https://desktop.arcgis.com/zh-cn/arcmap/10.3/analyze/creating-tools/defining-parameters-in-a-python-toolbox.htm#ESRI_SECTION1_E2BAA5D4440D41D6AAB948922186905A) | **GPValueTable**                  | 值列的集合。                                                 |
| 变量                                                         | **GPVariant**                     | 可以包含任意基本类型的数据值：布尔型、日期型、双精度型、长整型和字符串型。 |
| 垂直系数                                                     | **GPSAVerticalFactor**            | 指定垂直成本系数和垂直相对移动角度之间的关系。               |
| VPF Coverage                                                 | **DEVPFCoverage**                 | 以矢量产品格式存储的空间数据。                               |
| VPF 表                                                       | **DEVPFTable**                    | 以矢量产品格式存储的属性数据。                               |
| WCS Coverage                                                 | **DEWCSCoverage**                 | 网络覆盖服务 (WCS) 是网络上共享栅格数据集的开放式规范。      |
| 加权叠加表                                                   | **GPSAWeightedOverlayTable**      | 包含数据的表，可以通过对每一个栅格值使用同一测量尺度并根据其重要性对其进行加权来合并多个栅格。 |
| 加权总和                                                     | **GPSAWeightedSum**               | 指定用于通过将栅格各自乘以指定的权重并合计在一起来叠加多个栅格的数据。 |
| WMS 地图                                                     | **DEWMSMap**                      | WMS 地图。                                                   |
| 工作空间                                                     | **DEWorkspace**                   | 容器，例如地理数据库或文件夹。                               |
| XY 值域                                                      | **GPXYDomain**                    | x,y 坐标的最低和最高可能值的范围。                           |
| Z 值域                                                       | **GPZDomain**                     | z 坐标的最低和最高可能值的范围。                             |