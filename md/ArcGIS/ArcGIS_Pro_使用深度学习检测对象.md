# 使用深度学习检测对象 (Image Analyst)

ArcGIS Pro 3.1|其他版本|[ 帮助归档](https://pro.arcgis.com/zh-cn/pro-app/latest/get-started/archived-arcgis-pro-help.htm)

获得 Image Analyst 许可后可用。

## 摘要

用于运行输入栅格上的训练深度学习模型，以生成包含其找到对象的要素类。 这些要素可以是所找到对象周围的边界框或面，也可以是对象中心的点。

该工具需要包含经过训练的模型信息的模型定义文件。 可以使用训练深度学习模型工具或第三方训练软件（例如 TensorFlow、PyTorch 或 Keras）训练模型。 模型定义文件可以是 Esri 模型定义 JSON 文件 (.emd) 或深度学习模型包，它必须包含为处理每个对象调用的 Python 栅格函数的路径以及经过训练的二进制深度学习模型文件的路径。

## 使用情况

- 您必须在 ArcGIS Pro Python 环境中安装适当的深度学习框架 Python API（例如 TensorFlow、PyTorch 或 Keras）；否则在将 Esri 模型定义文件添加至工具时会发生错误。 向 Esri 模型定义文件的创建者索取相应的框架信息。

  要设置计算机以在 ArcGIS Pro 中使用深度学习框架，请参阅[安装 ArcGIS 的深度学习框架](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/analysis/deep-learning/install-deep-learning-frameworks.htm)。

- 该工具将调用第三方深度学习 Python API（例如 TensorFlow、PyTorch 或 Keras），并使用指定的 Python 栅格函数来处理每个对象。

- 可以在 [Esri Python 栅格函数 GitHub 页面](https://links.esri.com/Anatomy_of_a_PRF)中找到此工具的示例用例。 您还可以按照 GitHub 资料档案库中的示例和说明编写自定义 Python 模块。

- **模型定义**参数值可以是 Esri 模型定义 JSON 文件 (.emd)、JSON 字符串或深度学习模型包 (.dlpk)。 当在服务器上使用此工具时，JSON 字符串十分有用，因为您可以直接粘贴 JSON 字符串，而无需上传 .emd 文件。 .dlpk 文件必须存储在本地。

- 请参阅下面的 .emd 文件示例。

  ```
  {
      "Framework" :"TensorFlow",
      "ModelConfiguration": "ObjectDetectionAPI",
      
      "ModelFile": ".\\CoconutTreeDetection.model",
      "ModelType": "ObjectDetection",
      "ImageHeight": 850,
      "ImageWidth": 850,
      "ExtractBands": [0,1,2],
      "ImageSpaceUsed": "MAP_SPACE"
      "Classes": [
      {
          "Value": 0,
          "Name": "CoconutTree",
          "Color": [0, 255, 0]
      }
      ]
  }
  ```

- 该工具可以处理地图空间或像素空间中的输入影像。 地图空间中的影像位于基于地图的坐标系中。 像素空间中的影像位于原始影像空间中，没有旋转和变形。 可以在导出训练数据进行深度学习工具中使用**参考系统**参数生成训练数据时指定参考系统。 如果使用第三方训练软件对模型进行训练，则必须在 .emd 文件中使用 ImageSpaceUsed 参数指定参考系统， 该参数可以设置为 MAP_SPACE 或 PIXEL_SPACE。

- 增加批量大小可以提高工具性能；但是随着批量大小增加，所用内存也将随之增加。 如果出现内存不足错误，则降低批量大小。 可以使用**自变量**参数调整 batch_size 值。

- 批量大小为平方数，例如 1、4、9、16、25、64 等。 如果输入值不是完全平方值，将使用可能的最高平方值。 例如，如果指定的值为 6，表示可以将批量大小设置为 4。

- 使用**非极大值抑制**参数标识和移除对象检测中重复的要素。

- 输入栅格可以是单个栅格、多个栅格或附加影像的要素类。 有关附件的详细信息，请参阅[添加或移除文件附件](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/editing/edit-file-attachments.htm)。

- 有关运行此工具的要求以及您可能遇到的问题的信息，请参阅[深度学习常见问题](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/analysis/deep-learning/deep-learning-faq.htm)。

- 有关深度学习的详细信息，请参阅 [ArcGIS Pro 中的深度学习](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/analysis/image-analyst/deep-learning-in-arcgis-pro.htm)。

## 参数

对话框Python



| 标注                 | 说明                                                         | 数据类型                                                     |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 输入栅格             | 用于检测对象的输入图像。 输入可以是镶嵌数据集、影像服务或影像文件夹中的单个栅格或多个栅格。 还支持具有影像附件的要素类。 | Raster Dataset; Raster Layer; Mosaic Layer; Image Service; Map Server; Map Server Layer; Internet Tiled Layer; Folder; Feature Layer; Feature Class |
| 输出检测到的对象     | 此输出要素类中包含围绕输入图像中检测到的一个或多个对象的几何。 | Feature Class                                                |
| 模型定义             | 此参数可以是 Esri 模型定义 JSON 文件 (.emd)、JSON 字符串或深度学习模型包 (.dlpk)。 当在服务器上使用此工具时，JSON 字符串十分有用，因为您可以直接粘贴 JSON 字符串，而无需上传 .emd 文件。 .dlpk 文件必须存储在本地。其中包含深度学习二进制模型文件的路径、待使用的 Python 栅格函数的路径以及其他参数，例如首选切片大小或填充。 | File; String                                                 |
| 参数(可选)           | Python 栅格函数类中定义的函数参数。 可以在此列出其他深度学习参数和用于试验和优化的参数，例如用于调整灵敏度的置信度阈值。 参数名称将通过 Python 模块进行填充。 | Value Table                                                  |
| 非极大值抑制(可选)   | 指定是否将执行非极大值抑制，其中将标识重复的对象，并移除置信度值较低的重复要素。未选中 - 不执行非极大值抑制。 所有检测到的对象都将位于输出要素类中。 这是默认设置。选中 - 将执行非极大值抑制，并且将移除检测到的重复对象。 | Boolean                                                      |
| 置信度得分字段(可选) | 要素类中包含将由对象检测方法输出的置信度得分的字段的名称。当选中了**非最大抑制**参数时需要用到该参数。 | String                                                       |
| 类值字段(可选)       | 输入要素类中类值字段的名称。如果未指定字段名称，则将使用 Classvalue 或 Value 字段。 如果这些字段不存在，则会将所有记录标识为属于一个类。 | String                                                       |
| 最大重叠比(可选)     | 两个重叠要素的最大重叠比，其定义为交集区域与并集区域之比。 默认值为 0。 | Double                                                       |
| 处理模式(可选)       | 指定处理镶嵌数据集或影像服务中的所有栅格项目的方式。 当输入栅格是镶嵌数据集或影像服务时，将应用此参数。以镶嵌影像方式处理—将镶嵌在一起并处理镶嵌数据集或影像服务中的所有栅格项目。 这是默认设置。单独处理所有栅格项目—将作为独立影像处理镶嵌数据集或影像服务中的所有栅格项目。 | String                                                       |

### 派生输出

| 标注         | 说明                                                         | 数据类型       |
| ------------ | ------------------------------------------------------------ | -------------- |
| 输出分类栅格 | 用于像素分类的输出分类栅格。 栅格数据集的名称将与**输出检测对象**参数值相同。该参数仅在模型类型为全景分割时才可用。 | Raster Dataset |