# ArcGIS 深度学习

## 模型训练

在使用深度学习模型识别图像、点云或其他数据集中的要素或对象之前，必须先对其进行训练才能识别这些对象。 训练深度学习模型涉及的许多步骤与训练传统机器学习分类模型相同。 您必须收集并提供训练样本和输入数据，然后训练模型，以使其学习识别这些要素或对象。

## 准备训练数据

可使用[**标注对象以供深度学习**](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/analysis/image-analyst/label-objects-for-deep-learning.htm)窗格收集和生成标注影像数据集，以训练用于影像工作流的深度学习模型。 您可以交互方式识别和标注图像中的对象，并将训练数据导出为训练模型所需的影像片、标注和统计数据。 如果您具有已标注的矢量或栅格数据，可以使用[导出训练数据进行深度学习](https://pro.arcgis.com/zh-cn/pro-app/3.1/tool-reference/image-analyst/export-training-data-for-deep-learning.htm)地理处理工具生成下一步所需的训练数据。

[准备点云训练数据](https://pro.arcgis.com/zh-cn/pro-app/3.1/tool-reference/3d-analyst/prepare-point-cloud-training-data.htm)工具将创建用于训练和验证卷积神经网络以进行点云分类的数据。 该工具会创建未压缩 HDF5 文件的许多重叠块，用于训练点云。 有关准备和训练点云数据的详细信息，请参阅[训练用于点云分类的深度学习模型](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/data/las-dataset/train-a-point-cloud-model-with-deep-learning.htm)。

## 训练模型

[训练深度学习模型](https://pro.arcgis.com/zh-cn/pro-app/3.1/tool-reference/image-analyst/train-deep-learning-model.htm)工具会使用准备的训练数据训练用于影像工作流的深度学习模型。 许多模型类型和参数可用于配置训练过程。

[训练点云分类模型](https://pro.arcgis.com/zh-cn/pro-app/3.1/tool-reference/3d-analyst/train-point-cloud-classification-model.htm)工具会训练用于点云分类的深度学习模型。 有关准备和训练点云数据的详细信息，请参阅[训练用于点云分类的深度学习模型](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/data/las-dataset/train-a-point-cloud-model-with-deep-learning.htm)。

## 模型推断

模型推断指使用经过训练的模型从图像或点云中提取信息的过程。 ArcGIS Pro 中用于模型推断的选项如下：

- 检测对象 - 在图像中的对象或要素周围生成边界框以标识其位置。 使用[使用深度学习检测对象](https://pro.arcgis.com/zh-cn/pro-app/3.1/tool-reference/image-analyst/detect-objects-using-deep-learning.htm)工具。
- 分类对象 - 为图像中的要素生成标注以标识其类或类别。 使用[使用深度学习分类对象](https://pro.arcgis.com/zh-cn/pro-app/3.1/tool-reference/image-analyst/classify-objects-using-deep-learning.htm)工具。
- 分类像素 - 生成分类栅格，其中每个像素都属于一个类或类别。 使用[使用深度学习分类像素](https://pro.arcgis.com/zh-cn/pro-app/3.1/tool-reference/image-analyst/classify-pixels-using-deep-learning.htm)工具。
- 分类点云 - 生成分类点云，其中点根据特定的分类代码进行分类。 使用[使用训练模型分类点云](https://pro.arcgis.com/zh-cn/pro-app/3.1/tool-reference/3d-analyst/classify-point-cloud-using-trained-model.htm)工具。 有关详细信息，请参阅[通过深度学习对点云进行分类](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/data/las-dataset/classify-a-point-clould-with-deep-learning.htm)。



## 探索性分析

[**对象检测**探索性分析](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/mapping/exploratory-analysis/interactive-object-detection-basics.htm)工具使用经过训练的深度学习模型来识别当前地图或场景中显示的对象。 每个标识的要素都由一个点要素以及在地图坐标系中的位置、详细描述对象方向和范围的属性及其置信度值表示。 该工具可以与任何经过训练的 Faster R-CNN 模型以及 YOLO、SingleShotDetector (SSD) 和 RetinaNet 模型配合使用，专门用于按需检测活动视图中的对象。

![使用框符号系统的交互式对象检测](https://pro.arcgis.com/zh-cn/pro-app/latest/help/analysis/deep-learning/GUID-F1F3E6AF-3C44-40B7-A4AE-1C0485E1715B-web.png)

![使用十字形符号系统的交互式对象检测](https://pro.arcgis.com/zh-cn/pro-app/latest/help/analysis/deep-learning/GUID-FF925BDF-2238-4CB8-847B-482C8C0F8577-web.png)

## 查看结果

可在两个阶段查看深度学习模型的结果：训练模型之后以及运行推断工具之后。

### 查看模型训练结果

训练用于影像的深度学习模式时，训练深度学习模型工具的输出包含名为 model_metric.html 的文件。 该文件包含有关训练模型的信息，例如学习率、训练和验证损失以及平均精度得分。

训练用于点云的深度学习模型时，训练点云分类模型工具的输出会在工具结果窗口的消息部分中包含结果。 详细的报表包含每个时间的训练损失、验证损失和准确度，以及保存的深度学习模型的精度、召回率和 f1 得分。 该工具还将生成一个 CSV 表，其中包含每个时间每个类代码的精度、召回率和 F1 得分。 有关检查训练结果的详细信息，请参阅[评估点云训练结果](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/data/las-dataset/assessing-point-cloud-training-results.htm)。

### 查看模型推断结果

使用深度学习模型后，您需要审查结果并评估模型的准确性。

使用**属性**窗格可通过基于对象的推断（使用深度学习分类对象工具或使用深度学习检测对象工具）或通过探索性分析（交互式对象检测工具）[检查结果](https://pro.arcgis.com/zh-cn/pro-app/3.1/help/analysis/image-analyst/review-results-from-deep-learning.htm)。

可使用[计算对象检测的精度](https://pro.arcgis.com/zh-cn/pro-app/3.1/tool-reference/image-analyst/compute-accuracy-for-object-detection.htm)工具生成表和报表以在执行对象检测之后进行准确度评估。