# 使用深度学习分类像素 (Image Analyst)

ArcGIS Pro 3.1|其他版本|[ 帮助归档](https://pro.arcgis.com/zh-cn/pro-app/latest/get-started/archived-arcgis-pro-help.htm)

获得 Image Analyst 许可后可用。

## 摘要

用于运行输入栅格上的训练深度学习模型，以生成分类栅格，其中每个有效像素都被分配了一个类标注。

该工具需要包含经过训练的模型信息的模型定义文件。 可以使用训练深度学习模型工具或第三方训练软件（例如 TensorFlow、PyTorch 或 Keras）训练模型。 模型定义文件可以是 Esri 模型定义 JSON 文件 (.emd) 或深度学习模型包，它必须包含为处理每个对象调用的 Python 栅格函数的路径以及经过训练的二进制深度学习模型文件的路径。

## 使用情况

- 您必须在 ArcGIS Pro Python 环境中安装适当的深度学习框架 Python API（例如 TensorFlow 或 PyTorch）；否则在将 Esri 模型定义文件添加至工具时会发生错误。 向 Esri 模型定义文件的创建者索取相应的框架信息。

  要设置计算机以在 ArcGIS Pro 中使用深度学习框架，请参阅[安装 ArcGIS 的深度学习框架](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/analysis/deep-learning/install-deep-learning-frameworks.htm)。

- 该工具将调用第三方深度学习 Python API（例如 TensorFlow、PyTorch 或 Keras），并使用指定的 Python 栅格函数来处理每个对象。

- 可以在 [Esri Python 栅格函数 GitHub 页面](https://links.esri.com/Anatomy_of_a_PRF)中找到此工具的示例用例。 您还可以按照 GitHub 资料档案库中的示例和说明编写自定义 Python 模块。

- **模型定义**参数值可以是 Esri 模型定义 JSON 文件 (.emd)、JSON 字符串或深度学习模型包 (.dlpk)。 当在服务器上使用此工具时，JSON 字符串十分有用，因为您可以直接粘贴 JSON 字符串，而无需上传 .emd 文件。 .dlpk 文件必须存储在本地。

- 有关深度学习的详细信息，请参阅 [ArcGIS Pro 中的深度学习](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/analysis/image-analyst/deep-learning-in-arcgis-pro.htm)。

- 以下代码示例使用 Esri 模型定义 (.emd) 文件：

  ```
  {
      "Framework":"TensorFlow",
      "ModelConfiguration":"deeplab",
  
      "ModelFile":"\\Data\\ImgClassification\\TF\\froz_inf_graph.pb",
      "ModelType":"ImageClassification",
      "ExtractBands":[0,1,2],
      "ImageHeight":513,
      "ImageWidth":513,
  
      "Classes" : [
          {
              "Value":0,
              "Name":"Evergreen Forest",
              "Color":[0, 51, 0]
           },
           {
              "Value":1,
              "Name":"Grassland/Herbaceous",
              "Color":[241, 185, 137]
           },
           {
              "Value":2,
              "Name":"Bare Land",
              "Color":[236, 236, 0]
           },
           {
              "Value":3,
              "Name":"Open Water",
              "Color":[0, 0, 117]
           },
           {
              "Value":4,
              "Name":"Scrub/Shrub",
              "Color":[102, 102, 0]
           },
           {
              "Value":5,
              "Name":"Impervious Surface",
              "Color":[236, 236, 236]
           }
      ]
  }
  ```

- 输入栅格可以是单个栅格、多个栅格或附加影像的要素类。 有关附件的详细信息，请参阅[添加或移除文件附件](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/editing/edit-file-attachments.htm)。

- 增加批量大小可以提高工具性能；但是随着批量大小增加，所用内存也将随之增加。 如果出现内存不足错误，则降低批量大小。 可以使用**自变量**参数调整 batch_size 值。

- 批量大小为平方数，例如 1、4、9、16、25、64 等。 如果输入值不是完全平方值，将使用可能的最高平方值。 例如，如果指定的值为 6，表示可以将批量大小设置为 4。

- 有关运行此工具的要求以及您可能遇到的问题的信息，请参阅[深度学习常见问题](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/analysis/deep-learning/deep-learning-faq.htm)。

## 参数

对话框Python



| 标注             | 说明                                                         | 数据类型                                                     |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 输入栅格         | 将分类的输入栅格数据集。输入可以是镶嵌数据集、影像服务或影像文件夹中的一个或多个栅格，或者具有影像附件的要素类。 | Raster Dataset; Raster Layer; Mosaic Layer; Image Service; Map Server; Map Server Layer; Internet Tiled Layer; Folder; Feature Layer; Feature Class |
| 模型定义         | **模型定义**参数值可以是 Esri 模型定义 JSON 文件 (.emd)、JSON 字符串或深度学习模型包 (.dlpk)。 当在服务器上使用此工具时，JSON 字符串十分有用，因为您可以直接粘贴 JSON 字符串，而无需上传 .emd 文件。 .dlpk 文件必须存储在本地。其中包含深度学习二进制模型文件的路径、待使用的 Python 栅格函数的路径以及其他参数，例如首选切片大小或填充。 | File; String                                                 |
| 参数(可选)       | 函数参数在 Python 栅格函数类中进行定义。 您可以在此列出其他深度学习参数和用于试验和优化的参数，例如用于调整灵敏度的置信度阈值。 参数名称将通过读取 Python 模块进行填充。 | Value Table                                                  |
| 处理模式         | 指定处理镶嵌数据集或影像服务中的所有栅格项目的方式。 当输入栅格是镶嵌数据集或影像服务时，将应用此参数。以镶嵌影像方式处理—将镶嵌在一起并处理镶嵌数据集或影像服务中的所有栅格项目。 这是默认设置。单独处理所有栅格项目—将作为独立影像处理镶嵌数据集或影像服务中的所有栅格项目。 | String                                                       |
| 输出文件夹(可选) | 将存储输出分类栅格的文件夹。 将使用此文件夹中的分类栅格来生成镶嵌数据集。当输入栅格是要单独处理所有项目的影像文件夹或镶嵌数据集时，此参数为必需项。 默认为工程文件夹中的文件夹。 | Folder                                                       |
| 输出要素(可选)   | 将存储输出分类栅格的要素类。当输入栅格为图像要素类时，此参数为必需参数。 | Feature Class                                                |

### 返回值

| 标注           | 说明                               | 数据类型       |
| -------------- | ---------------------------------- | -------------- |
| 输出栅格数据集 | 包含结果的栅格或镶嵌数据集的名称。 | Raster Dataset |