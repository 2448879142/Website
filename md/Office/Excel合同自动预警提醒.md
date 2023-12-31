# 合同自动预警提醒

## 函数公式

> 日期函数EDATE

- 函数定义：计算从开始日期算起的数个月之前或之后的日期
- 使用格式：EDATE(Start_date,Months)
- 参数解释：
  - start_date：一个日期值，代表开始日期，指定表示日期的数值（序列号值）或单元格引用。
  - months：指定月份数，小数部分的值被向下舍入，若指定数值为正数则返回"start_date"之后的日期(指定月份数之后)，若指定数值为负数则返回"start_date"之前的日期(指定月份数之前)

> 日期函数DAY

- 函数定义：返回以序列数表示的某日期的天数。 天数是介于 1 到 31 之间的整数
- 使用格式：DAY(serial_number)
- 参数解释：
  - serial_number：要查找的日期。

> 日期函数TODAY

- 函数定义：返回当前系统的日期。
- 使用格式：TODAY()，该函数没有参数，只用一对括号就可以。

## 思路

- 基于合同开始日期和期限，通过函数计算得到合同截止日期
- 基于合同截止日期，通过函数计算合同截止日期与当前日期的差值，获得合同到期日剩余天数
- 利用条件格式中数据条功能，将差值转换为指定条形图
- 将表格转化为超级表，添加切片器对公司名称、期限进行筛选

> 点击附件下载<a href="../media/合同自动预警提醒.xlsx" download='合同自动预警提醒.xlsx'>合同自动预警提醒.xlsx</a>