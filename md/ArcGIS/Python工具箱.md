# Python工具箱

## 概念

Python 工具箱 (**.pyt**) 是一个简单的文本文件，可以在任何文本编辑器（如记事本或 VI 等）中或者任何 Python IDE（如 PythonWin 等）中创建、查看和编辑。

Python 工具箱 (**.pyt**) 是一个可在任何文本编辑器或 Python IDE 中编辑的 ASCII 文件。

## 模板

~~~python
import arcpy


class Toolbox(object):
    def __init__(self):
        """定义工具箱（工具箱的名称是 .pyt 文件的名称）。"""
        self.label = "Toolbox"
        self.alias = ""

        # 与此工具箱关联的工具类列表
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """定义工具（工具名称是类的名称）。"""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """定义参数定义"""
        params = None
        return params

    def isLicensed(self):
        """设置工具是否获得执行许可。"""
        return True

    def updateParameters(self, parameters):
        """在执行内部验证之前修改参数的值和属性。 每当更改参数时，都会调用此方法。"""
        return

    def updateMessages(self, parameters):
        """修改通过内部验证为每个工具参数创建的消息。 此方法在内部验证后调用。"""
        return

    def execute(self, parameters, messages):
        """工具的源代码。"""
        return
~~~

## Toolbox类

~~~python
class Toolbox(object):
    def __init__(self):
        self.label = "Toolbox"
        self.alias = ""
        self.tools = [Tool]
~~~

**Toolbox**类是**Python工具箱**的必须具有的类，且名称不能更改。

工具箱被创建为名为 **Toolbox** 的类。在 **Toolbox** 类的 **`__init__`** 方法中，定义工具箱的属性，这些属性包括 **alias**、**label** 和 **description**。工具箱的名称由 .pyt 的名称定义。必须将 **tools** 属性设置为包含工具箱中定义的所有工具类的列表。

**提示:**

要确保 ArcGIS 正确识别 Python 工具箱，该工具箱类的名称必须仍为 **Toolbox**。

## Tool类

该类定义了工具箱中一个个具体的工具，例如裁剪工具对应裁剪类。

~~~python
class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False
~~~

| 工具方法         | 必选/可选 | 描述                                                         |
| ---------------- | --------- | ------------------------------------------------------------ |
| `__init__`       | 必填信息  | 初始化工具类。                                               |
| getParameterInfo | 可选      | 定义工具的参数                                               |
| isLicensed       | 可选      | 返回该工具是否获得执行许可。                                 |
| updateParameters | 可选      | 在用户每次在工具对话框中更改参数时调用。从 updateParameters 返回后，地理处理将调用它的内部验证例程。 |
| updateMessages   | 可选      | 在从内部验证例程返回后调用。您可以检查在内部验证过程中创建的消息并根据需要进行更改。 |
| execute          | 必填信息  | 工具的源代码。                                               |

### 设置工具类的 `__init__`方法

工具类中的 **__init__** 方法是标准 Python 类初始化方法。对于 Python 工具箱中的工具，**__init__** 方法用于设置该工具的属性，这些属性包括工具的**标注**和**描述**。工具的名称由类的名称确立（在下例中，工具的名称为 **CalculateSinuosity**）。

```python
class CalculateSinuosity(object):
    def __init__(self):
        self.label = "Calculate Sinuosity"
        self.description = "Sinuosity measures the amount that a river meanders within its valley, " + \
                           "calculated by dividing total stream length by valley length."
```

可在工具的**`__init__`** 方法中设置以下属性。

| 属性               | 描述                                                         |
| ------------------ | ------------------------------------------------------------ |
| canRunInBackground | 如果 **canRunInBackground** 取消设置或设置为 **True**，此工具将遵循**地理处理选项** 对话框中的当前**后台处理** 设置。如果设置为 **False**，工具将始终在前台运行，从而覆盖**地理处理选项** 对话框中的**后台处理**设置。 |
| category           | 工具所在工具集的名称。工具集是在工具箱内组织工具的一种方式。 |
| 描述               | 工具的描述。                                                 |
| 标注               | 标注是工具的显示名称，如**“目录”窗口** 中所示。              |
| 样式表             | 更改用于工具的默认样式表。如果取消设置，则使用默认样式表。   |

### 定义 Python 工具箱中的参数

~~~python
    def getParameterInfo(self):
        """Define parameter definitions"""
        # First parameter
        param0 = arcpy.Parameter(
            displayName="Input Features",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        # Second parameter
        param1 = arcpy.Parameter(
            displayName="Sinuosity Field",
            name="sinuosity_field",
            datatype="Field",
            parameterType="Optional",
            direction="Input")

    	param1.value = "sinuosity"

        # Third parameter
        param2 = arcpy.Parameter(
            displayName="Output Features",
            name="out_features",
            datatype="GPFeatureLayer",
            parameterType="Derived",
            direction="Output")

        param2.parameterDependencies = [param0.name]
        param2.schema.clone = True

        params = [param0, param1, param2]

        return params
~~~

几乎所有工具都具有参数，您可在工具对话框或脚本中设置参数值。执行工具时，会将参数值发送到该工具的源代码。工具将读取这些值，然后继续执行操作。

在 Python 工具箱 (**.pyt**) 中，通过创建 **[Parameter](https://desktop.arcgis.com/zh-cn/arcmap/10.3/analyze/arcpy-classes/parameter.htm)** 对象并设置其属性在工具类 **getParameterInfo** 方法中定义工具参数。

### 访问 Python 工具箱中的参数

在 Python 工具箱中，工具的主要部分位于 **execute** 方法中。该部分负责各种分析、转换和数据创建。在 **execute** 方法中，可调用其他工具并访问 [ArcPy](https://desktop.arcgis.com/zh-cn/arcmap/10.3/analyze/arcpy/what-is-arcpy-.htm)、其他自定义功能或第三方 Python 功能。

**execute** 方法本身具有的参数可用于处理参数和[消息](https://desktop.arcgis.com/zh-cn/arcmap/10.3/analyze/creating-tools/writing-messages-in-a-python-toolbox.htm)，包括 **parameter** 对象列表和 **messages** 对象。

在 **execute** 方法中，可使用 **valueAsText** 方法从列表中访问每个参数的值。可根据需要访问其他 **[Parameter](https://desktop.arcgis.com/zh-cn/arcmap/10.3/analyze/arcpy-classes/parameter.htm)** 对象属性。

使用参数对象的 **valueAsText** 方法访问参数值：

```python
def execute(self, parameters, messages):
    inFeatures      = parameters[0].valueAsText
    outFeatureClass = parameters[1].valueAsText
```

### 在 Python 工具箱中写入消息

运行工具时，ArcPy 完全知晓调用它的应用程序。其中一个主要作用是您可以在 Python 中写入消息，并且您的消息会自动出现在工具对话框、[地理处理历史](http://pro.arcgis.com/zh-cn/pro-app/help/analysis/geoprocessing/the-basics/geoprocessing-history.htm)和 **Python** 窗口中。而且调用您工具的任何模型或脚本工具均有权访问您所写入的消息。

~~~python
def execute(self, parameters, messages):
    input = parameters[0].valueAsText
    output = parameters[1].valueAsText
        
    # If the input has no features, add an error message, and raise
    #  an arcpy.ExecuteError
    if int(arcpy.GetCount_management(input)[0]) == 0:
        messages.addErrorMessage("{0} has no features.".format(input))
        raise arcpy.ExecuteError
            
    return
~~~

在 Python 工具箱中，**messages** 对象用于向工具中添加附加消息。

| 消息方法                                                     | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **addMessage(message)**                                      | 向工具消息添加信息性消息                                     |
| **addErrorMessage(message)**                                 | 向工具消息添加错误消息注:**addErrorMessage** 不会抛出异常。  |
| **addWarningMessage(message)**                               | 向工具消息添加警告消息                                       |
| **addIDMessage(message_type, message_ID, add_argument1=None, add_argument2=None)** | 使用地理处理[消息代码](http://pro.arcgis.com/zh-cn/pro-app/tool-reference/tool-errors-and-warnings/understanding-geoprocessing-tool-errors-and-warnings.htm)添加任意类型的消息 |
| **addGPMessages()**                                          | 向工具消息添加来自上次运行的地理处理工具的消息               |

## 对 Python 工具箱中的工具编写文档

Python 工具箱和其中的工具可像任何其他地理处理工具一样编写文档说明。

可通过不同方式对 Python 工具箱或其工具的帮助文档进行编辑。

- 在目录窗口或 ArcCatalog 中：

  - 右键单击所创建的工具或工具箱，然后单击**项目描述**。将打开**项目描述** 窗口，其中显示了**描述**页面。
  - 单击**编辑**按钮 ![编辑元数据](https://desktop.arcgis.com/zh-cn/arcmap/10.3/analyze/creating-tools/GUID-FC09795D-7E12-4CB6-881D-8BADD634E5A0-web.png)。

- 在搜索窗口中：

  如果工具或工具箱是**搜索** 窗口中列出的搜索结果（如[查找工具快速浏览](https://desktop.arcgis.com/zh-cn/arcmap/10.3/analyze/finding-tools/a-quick-tour-of-finding-tools.htm#ESRI_SECTION2_0A9CB1D243E146F48837F5EAA168777B)中所述），则可执行以下操作来访问其**描述**页面：

  - 将指针悬停在工具或工具箱名称上；将弹出一个窗口，其底部包含一个指向**项目描述**的链接。单击该链接打开**项目描述** 窗口，然后单击**编辑**按钮 ![编辑元数据](https://desktop.arcgis.com/zh-cn/arcmap/10.3/analyze/creating-tools/GUID-FC09795D-7E12-4CB6-881D-8BADD634E5A0-web.png)。
  - 单击工具或工具箱名称下面的摘要行以打开**项目描述** 窗口，然后单击**编辑**按钮 ![编辑元数据](https://desktop.arcgis.com/zh-cn/arcmap/10.3/analyze/creating-tools/GUID-FC09795D-7E12-4CB6-881D-8BADD634E5A0-web.png)。

对于 Python 工具箱，工具箱和工具文档说明存储在与工具箱和工具名称相关联的 **.xml** 文件中。各个工具的帮助文档都存储于单独的 **.xml** 文件中。