# 使用深度学习分类对象 (Image Analyst)

ArcGIS Pro 3.1|其他版本|[ 帮助归档](https://pro.arcgis.com/zh-cn/pro-app/latest/get-started/archived-arcgis-pro-help.htm)

获得 Image Analyst 许可后可用。

## 摘要

用于运行输入栅格和可选要素类上的训练深度学习模型，以生成要素类或表，其中每个输入对象或要素均具有一个分配的类或类别标注。

该工具需要包含经过训练的模型信息的模型定义文件。 可以使用训练深度学习模型工具或第三方训练软件（例如 TensorFlow、PyTorch 或 Keras）训练模型。 模型定义文件可以是 Esri 模型定义 JSON 文件 (.emd) 或深度学习模型包，它必须包含为处理每个对象调用的 Python 栅格函数的路径以及经过训练的二进制深度学习模型文件的路径。

## 使用情况

- 您必须在 ArcGIS Pro Python 环境中安装适当的深度学习框架 Python API（PyTorch 或 Keras）；否则在将 Esri 模型定义文件添加至工具时会发生错误。 Esri 模型定义文件的创建者应提供相应的框架信息。

  要设置计算机以在 ArcGIS Pro 中使用深度学习框架，请参阅[安装 ArcGIS 的深度学习框架](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/analysis/deep-learning/install-deep-learning-frameworks.htm)。

- 该工具将调用第三方深度学习 Python API（例如 PyTorch 或 Keras），并使用指定的 Python 栅格函数来处理每个对象。

- 您可以在 [Esri Python 栅格函数 GitHub 页面](https://links.esri.com/Anatomy_of_a_PRF)![Python 栅格函数解析](https://pro.arcgis.com/zh-cn/pro-app/latest/tool-reference/image-analyst/GUID-BBE867AF-47B6-432F-8AC1-E3220E808B03-web.png)上找到此工具的使用案例示例。 您还可以按照以下示例和说明编写自定义 Python 模块。

- **模型定义**参数值可以是 Esri 模型定义 JSON 文件 (.emd)、JSON 字符串或深度学习模型包 (.dlpk)。 当在服务器上使用此工具时，JSON 字符串十分有用，因为您可以直接粘贴 JSON 字符串，而无需上传 .emd 文件。 .dlpk 文件必须存储在本地。

- 以下示例适用于 .emd 文件：

  ```
  {
      "Framework": "Keras",
      "ModelConfiguration":"KerasClassifier",
      "ModelFile":"C:\\DeepLearning\\Damage_Classification_Model_V7.h5",
      "ModelType":"ObjectClassification",
      "ImageHeight":256,
      "ImageWidth":256,
      "ExtractBands":[0,1,2],
      "CropSizeFixed": 1,
      "BlackenAroundFeature": 1,
      "ImageSpaceUsed": "MAP_SPACE", 
      "Classes": [
      {
         "Value": 0,
         "Name": "Damaged",
         "Color": [255, 0, 0]
      },
      {
         "Value": 1,
         "Name": "Undamaged",
         "Color": [76, 230, 0]
      }
      ]
  }
  ```

- CropSizeFixed 属性可定义每个对象周围的栅格切片的裁剪模式。 值 1 表示将使用由 .emd 文件内的 ImageHeight 和 ImageWidth 属性定义的固定栅格切片。 对象位于固定切片大小的中心。 值 0 表示将使用可变切片大小，其中栅格切片将使用对象周围的最小边界框进行裁剪。

- BlackenAroundFeature 属性指定是否掩膜每个对象外部的像素。 值 0 表示不会掩膜对象外部的像素。 值 1 表示将掩膜对象外部的像素。

- 该工具可以处理地图空间或像素空间中的输入影像。 地图空间中的影像位于基于地图的坐标系中。 像素空间中的影像位于原始影像空间中，没有旋转和变形。 可以在导出训练数据进行深度学习工具中使用**参考系统**参数生成训练数据时指定参考系统。 如果使用第三方训练软件对模型进行训练，则必须在 .emd 文件中使用 ImageSpaceUsed 参数指定参考系统， 该参数可以设置为 MAP_SPACE 或 PIXEL_SPACE。

- 输入栅格可以是单个栅格、多个栅格或附加影像的要素类。 有关附件的详细信息，请参阅[添加或移除文件附件](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/editing/edit-file-attachments.htm)。

- 增加批量大小可以提高工具性能；但是随着批量大小增加，所用内存也将随之增加。 如果出现内存不足错误，则降低批量大小。 可以使用**自变量**参数调整 batch_size 值。

- 批量大小为平方数，例如 1、4、9、16、25、64 等。 如果输入值不是完全平方值，将使用可能的最高平方值。 例如，如果指定的值为 6，表示可以将批量大小设置为 4。

- 有关运行此工具的要求以及您可能遇到的问题的信息，请参阅[深度学习常见问题](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/analysis/deep-learning/deep-learning-faq.htm)。

- 有关深度学习的详细信息，请参阅 [ArcGIS Image Analyst 扩展模块中的深度学习](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/analysis/image-analyst/deep-learning-in-arcgis-pro.htm).

## 参数

对话框Python



| 标注               | 说明                                                         | 数据类型                                                     |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 输入栅格           | 用于分类对象的输入图像。输入可以是镶嵌数据集、影像服务或影像文件夹中的一个或多个栅格，或者具有影像附件的要素类。 | Raster Dataset; Raster Layer; Mosaic Layer; Image Service; Map Server; Map Server Layer; Internet Tiled Layer; Folder; Feature Layer; Feature Class |
| 输出分类对象要素类 | 包含输入要素类中对象或要素周围几何的输出要素类，以及用于存储分类标注的字段。 | Feature Class                                                |
| 模型定义           | **模型定义**参数值可以是 Esri 模型定义 JSON 文件 (.emd)、JSON 字符串或深度学习模型包 (.dlpk)。 当在服务器上使用此工具时，JSON 字符串十分有用，因为您可以直接粘贴 JSON 字符串，而无需上传 .emd 文件。 .dlpk 文件必须存储在本地。其中包含深度学习二进制模型文件的路径、待使用的 Python 栅格函数的路径以及其他参数，例如首选切片大小或填充。 | File; String                                                 |
| 输入要素(可选)     | 用于标识要分类或要标注的每个对象或要素位置的点、线或面输入要素类。 输入要素类中的每一行表示一个对象或要素。如果未指定输入要素类，将假设每个输入影像包含单个待分类对象。 如果一个或多个输入影像使用空间参考，则工具的输出为要素类，其中每个影像的范围将用作每个标注要素类的边界几何。 如果一个或多个输入影像没有使用空间参考，则工具的输出为包含影像 ID 值和每个影像类标注的表。 | Feature Class; Feature Layer                                 |
| 类标注字段(可选)   | 包含输出要素类中类或类别标注的字段名称。如果未指定字段名称，则会在输出要素类中生成一个 ClassLabel 字段。 | String                                                       |
| 处理模式(可选)     | 指定处理镶嵌数据集或影像服务中的所有栅格项目的方式。 当输入栅格是镶嵌数据集或影像服务时，将应用此参数。以镶嵌影像方式处理—将镶嵌在一起并处理镶嵌数据集或影像服务中的所有栅格项目。 这是默认设置。单独处理所有栅格项目—将作为独立影像处理镶嵌数据集或影像服务中的所有栅格项目。 | String                                                       |
| 模型参数(可选)     | Python 栅格函数类中定义的函数参数。 可以在此列出其他深度学习参数和用于试验和优化的参数，例如用于调整灵敏度的置信度阈值。 参数名称将通过 Python 模块进行填充。 | Value Table                                                  |
| 说明文字(可选)     | 包含输出要素类中文本或标题的字段名称。 仅当使用“影像描述生成器”模型时才支持此参数。如果未指定字段名称，则会在输出要素类中生成一个 Caption 字段。注：此参数不会出现在**地理处理**窗格中。 要更改默认字段名称，请使用**类标注字段**参数。 | String                                                       |