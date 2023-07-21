# Excel函数公式
> 下载<a href="../media/函数查询表.xlsx" download='函数查询表.xlsx'>函数查询表</a>
## ABS
> 返回数字的绝对值。
 一个数字的绝对值是该数字不带其符号的形式。

```
ABS(number)
number必需。
 需要计算其绝对值的实数。

```
## ACCRINT
> 返回定期付息证券的应计利息。

```
ACCRINT(issue, first_interest, settlement, rate, par, frequency, [basis], [calc_method])
issue必需。
 有价证券的发行日。
first_interest必需。
 有价证券的首次计息日。
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
rate必需。
 有价证券的年息票利率。
par必需。
 证券的票面值。
 如果省略此参数，则 ACCRINT 使用 ￥10,000。
frequency必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
Basis  日计数基准0 或省略US (NASD)
 30/3601 实际/实际2 实际/3603 实际/3654 欧洲 30/360calc_method可选。
 一个逻辑值，指定当结算日期晚于首次计息日期时用于计算总应计利息的方法。
 如果值为 TRUE (1)
，则返回从发行日到结算日的总应计利息。
 如果值为 FALSE (0)
，则返回从首次计息日到结算日的应计利息。
 如果不输入此参数，则默认为 TRUE。

```
## ACCRINTM
> 返回在到期日支付利息的有价证券的应计利息。

```
ACCRINTM(issue, settlement, rate, par, [basis])
ACCRINTM 函数语法具有下列参数：Issue必需。
 有价证券的发行日。
Settlement必需。
 有价证券的到期日。
Rate必需。
 有价证券的年息票利率。
Par必需。
 证券的票面值。
 如果省略此参数，则 ACCRINTM 使用 ￥10,000。
Basis可选。
 要使用的日计数基准类型。
Basis   日计数基准0 或省略 US (NASD)
 30/3601  实际/实际2  实际/3603  实际/3654  欧洲 30/360
```
## ACOS
> 返回数字的反余弦值。
 反余弦值是指余弦值为 number 的角度。
 返回的角度以弧度表示，弧度值在 0（零）到 pi 之间。

```
ACOS(number)
number必需。
 所求角度的余弦值，必须介于 -1 到 1 之间。

```
## ACOSH
> 返回数字的反双曲余弦值。
 该数字必须大于或等于 1。
 反双曲余弦值是指双曲余弦值为 number 的值，因此 ACOSH(COSH(number)
)
 等于 number。

```
ACOSH(number)
number必需。
 大于或等于 1 的任意实数。

```
## ACOT 
> 返回数字的反余切值的主值。

```
ACOT(number)
number必需。
 Number 为所需的角度的余切值。
 它必须是一个实数。

```
## ACOTH 
> 返回数字的反双曲余切值。

```
ACOTH(number)
number必需。
Number 的绝对值必须大于 1。

```
## ADDRESS
> 你可以使用 ADDRESS 函数，根据指定行号和列号获得工作表中的某个单元格的地址。
例如，ADDRESS(2,3)
 返回 $C$2。
再例如，ADDRESS(77,300)
 返回 $KN$77。
可以使用其他函数（如 ROW 和 COLUMN 函数）为 ADDRESS 函数提供行号和列号参数。

```
ADDRESS(row_num, column_num, [abs_num], [a1], [sheet_text])
row_num  必需。
 一个数值，指定要在单元格引用中使用的行号。
column_num必需。
 一个数值，指定要在单元格引用中使用的列号。
abs_num   可选。
 一个数值，指定要返回的引用类型。
abs_num   返回的引用类型1 或省略绝对值2 绝对行号，相对列标3 相对行号，绝对列标4 相对值a1可选。
 一个逻辑值，指定 A1 或 R1C1 引用样式。
 在 A1 样式中，列和行将分别按字母和数字顺序添加标签。
 在 R1C1 引用样式中，列和行均按数字顺序添加标签。
 如果参数 A1 为 TRUE 或被省略，则 ADDRESS 函数返回 A1 样式引用；如果为 FALSE，则 ADDRESS 函数返回 R1C1 样式引用。
sheet_text可选。
 一个文本值，指定要用作外部引用的工作表的名称。
 例如，公式 =ADDRESS(1,1,,,Sheet2)
 返回 Sheet2!$A$1。
 如果忽略参数 sheet_text，则不使用任何工作表名称，并且该函数所返回的地址引用当前工作表上的单元格。

```
## AGGREGATE
> 返回列表或数据库中的合计。
 AGGREGATE 函数可将不同的聚合函数应用于列表或数据库，并提供忽略隐藏行和错误值的选项。

```
AGGREGATE(function_num, options, ref1, [ref2], …)
function_num必需。
 一个介于 1 到 19 之间的数字，指定要使用的函数。
function_num   函数1  AVERAGE2  COUNT3  COUNTA4  MAX5  MIN6  PRODUCT7  STDEV.S8  STDEV.P9  SUM10VAR.S11VAR.P12MEDIAN13MODE.SNGL14LARGE15SMALL16PERCENTILE.INC17QUARTILE.INC18PERCENTILE.EXC19QUARTILE.EXCoptions必需。
 一个数值，决定在函数的计算区域内要忽略哪些值。
options  行为0 或省略   忽略嵌套 SUBTOTAL 和 AGGREGATE 函数1忽略隐藏行、嵌套 SUBTOTAL 和 AGGREGATE 函数2忽略错误值、嵌套 SUBTOTAL 和 AGGREGATE 函数3忽略隐藏行、错误值、嵌套 SUBTOTAL 和 AGGREGATE 函数4忽略空值5忽略隐藏行6忽略错误值7忽略隐藏行和错误值ref1必需。
函数的第一个数值参数，这些函数具有要计算聚合值的多个数值参数。
ref2,...可选。
要计算聚合值的 2 至 253 个数值参数。

```
## AMORDEGRC
> 返回每个结算期间的折旧值。
 该函数主要为法国会计系统提供。
 如果某项资产是在该结算期的中期购入的，则按直线折旧法计算。
 该函数与函数 AMORLINC 相似，不同之处在于该函数中用于计算的折旧系数取决于资产的寿命。

```
AMORDEGRC(cost, date_purchased, first_period, salvage, period, rate, [basis])
cost必需。
 资产原值。
date_purchased必需。
 购入资产的日期。
first_period必需。
 第一个期间结束时的日期。
salvage必需。
 资产在使用寿命结束时的残值。
period必需。
 期间。
rate必需。
 折旧率。
basis可选。
 要使用的年基准。
basis  日期系统0 或省略 360 天（NASD 方法）1  实际3  一年 365 天4  一年 360 天（欧洲方法）
```
## AMORLINC
> 返回每个结算期间的折旧值。
 该函数主要为法国会计系统提供。
 如果某项资产是在该结算期的中期购入的，则按直线折旧法计算。

```
AMORLINC(cost, date_purchased, first_period, salvage, period, rate, [basis])
cost必需。
 资产原值。
date_purchased必需。
 购入资产的日期。
first_period必需。
 第一个期间结束时的日期。
salvage必需。
 资产在使用寿命结束时的残值。
period必需。
 期间。
rate必需。
 折旧率。
basis可选。
 要使用的年基准。
basis   日期系统0 或省略 360 天（NASD 方法）1  实际3  一年 365 天4  一年 360 天（欧洲方法）
```
## AND
> 是一个逻辑函数，用于确定测试中的所有条件是否均为 TRUE。

```

```
## ARABIC
> 将罗马数字转换为阿拉伯数字。

```
ARABIC(text)
text必需。
 用引号括起来的字符串、空字符串 ()
 或对包含文本的单元格的引用。

```
## AREAS
> 返回引用中的区域个数。
 区域是指连续的单元格区域或单个单元格。

```
AREAS(reference)
reference必需。
 对某个单元格或单元格区域的引用，可包含多个区域。
 如果需要将几个引用指定为一个参数，则必须用括号括起来，以免 Microsoft Excel 将逗号解释为字段分隔符。
 参见以下示例。

```
## ASC
> 将字符串中的全角（双字节）英文字母或片假名更改为半角（单字节）字符
```
ASC(text)
text必需。
文本或对包含要更改文本的单元格的引用。
如果文本不包含任何全角字母，则不会对文本进行转换。

```
## ASIN
> 返回数字的反正弦值。
 反正弦值是指正弦值为 number 的角度。
 返回的角度以弧度表示，弧度值在 -pi/2 到 pi/2 之间。

```
ASIN(number)
number必需。
 所求角度的正弦值，必须介于 -1 到 1 之间。

```
## ASINH
> 返回数字的反双曲正弦值。
 反双曲正弦值是指双曲正弦值为 number 的值，因此 ASINH(SINH(number)
)
 等于 number。

```
ASINH(number)
number必需。
 任意实数。

```
## ATAN
> 返回数字的反正切值。
 反正切值是指正切值为 number 的角度。
 返回的角度以弧度表示，弧度值在 -pi/2 到 pi/2 之间。

```
ATAN(number)
number必需。
 所求角度的正切值。

```
## ATAN2
> 返回给定的 X 轴及 Y 轴坐标值的反正切值。
 反正切值是指从 X 轴到通过原点 (0, 0)
 和坐标点 (x_num, y_num)
 的直线之间的夹角。
 该角度以弧度表示，弧度值在 -pi 到 pi 之间（不包括 -pi）。

```
ATAN2(x_num, y_num)
x_num必需。
 点的 x 坐标。
y_num必需。
 点的 y 坐标。

```
## ATANH
> 返回数字的反双曲正切值。
 Number 必须介于 -1 到 1 之间（不包括 -1 和 1）。
 反双曲正切值是指双曲正切值为 number 的值，因此 ATANH(TANH(number)
)
 等于 number。

```
ATANH(number)
number必需。
 -1 到 1 之间的任意实数。

```
## AVEDEV
> 返回一组数据点到其算术平均值的绝对偏差的平均值。
 AVEDEV 是对一组数据中变化性的度量。

```
AVEDEV(number1, [number2], ...)
number1, number2, ...number1 是必需的，后续数字是可选的。
 要计算其绝对偏差平均值的 1 到 255 个参数。
 也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## AVERAGE
> 返回参数的平均值（算术平均值）。
 例如，如果范围A1:A20 包含数字，则公式 =AVERAGE(A1:A20)
 将返回这些数字的平均值。

```
AVERAGE(number1, [number2], ...)
number1必需。
 要计算平均值的第一个数字、单元格引用或单元格区域。
number2, ...可选。
 要计算平均值的其他数字、单元格引用或单元格区域，最多可包含 255 个。

```
## AVERAGEA
> 计算参数列表中数值的平均值（算术平均值）。

```
AVERAGEA(value1, [value2], ...)
value1, value2, ...value1 是必需的，后续值是可选的。
 需要计算平均值的 1 到 255 个单元格、单元格区域或值。

```
## AVERAGEIF
> 返回某个区域内满足给定条件的所有单元格的平均值（算术平均值）。

```
AVERAGEIF(range, criteria, [average_range])
range必需。
要计算平均值的一个或多个单元格，其中包含数字或包含数字的名称、数组或引用。
criteria必需。
形式为数字、表达式、单元格引用或文本的条件，用来定义将计算平均值的单元格。
例如，条件可以表示为 32、32、>32、苹果 或 B4。
average_range可选。
计算平均值的实际单元格组。
如果省略，则使用 range。

```
## AVERAGEIFS
> 返回满足多个条件的所有单元格的平均值（算术平均值）。

```
AVERAGEIFS(average_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
average_range必需。
要计算平均值的一个或多个单元格，其中包含数字或包含数字的名称、数组或引用。
criteria_range1、criteria_range2 等criteria_range1 是必需的，后续 criteria_range 是可选的。
在其中计算关联条件的 1 至 127 个区域。
criteria1、criteria2 等criteria1 是必需的，后续 criteria 是可选的。
 形式为数字、表达式、单元格引用或文本的 1 至 127 个条件，用来定义将计算平均值的单元格。
 例如，条件可以表示为 32、32、>32、苹果 或 B4。

```
## BAHTTEXT
> 使用 ß（泰铢）货币格式将数字转换为文本
```
BAHTTEXT(number)
number必需。
 要转换成文本的数字、对包含数字的单元格的引用或结果为数字的公式。

```
## BASE 
> 将数字转换为具备给定基数的文本表示。

```
BASE(number, radix, [min_length])
number必需。
 要转换的数字。
 必须为大于或等于 0 并小于 2^53 的整数。
radix  必需。
 要将数字转换成的基本基数。
 必须为大于或等于 2 且小于或等于 36 的整数。
min_length可选。
 返回字符串的最小长度。
 必须为大于或等于 0 的整数。

```
## BESSELI
> 返回修正 Bessel 函数值，它与用纯虚数参数运算时的 Bessel 函数值相等。

```
BESSELI(x, n)
x必需。
 用来计算函数的值。
n必需。
 贝赛耳函数的阶数。
 如果 n 不是整数，将被截尾取整。

```
## BESSELJ
> 返回 Bessel 函数值。

```
BESSELJ(x, n)
x必需。
 用来计算函数的值。
n必需。
 贝赛耳函数的阶数。
 如果 n 不是整数，将被截尾取整。

```
## BESSELK
> 返回修正 Bessel 函数值，它与用纯虚数参数运算时的 Bessel 函数值相等。

```
BESSELK(x, n)
x必需。
 用来计算函数的值。
n必需。
 函数的阶数。
 如果 n 不是整数，将被截尾取整。

```
## BESSELY
> 返回 Bessel 函数值，也称为 Weber 函数或 Neumann 函数。

```
BESSELY(X, N)
BESSELY 函数语法具有以下参数：X必需。
 用来计算函数的值。
N必需。
 函数的阶数。
 如果 n 不是整数，将被截尾取整。

```
## BETA.DIST 
> 返回 Beta 分布。
Beta 分布通常用于研究样本中一定部分的变化情况，例如，人们一天中看电视的时间比率。

```
BETA.DIST(x,alpha,beta,cumulative,[A],[B])
x必需。
 用来计算其函数的值，介于值 A 和 B 之间alpha必需。
 分布参数。
beta必需。
 分布参数。
cumulative必需。
 决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 BETA.DIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。
A可选。
 x 所属区间的下界。
B可选。
 x 所属区间的上界。

```
## BETA.INV 
> 返回 Beta 累积概率密度函数 (BETA.DIST)
 的反函数。
如果 probability = BETA.DIST(x,...TRUE)
，则 BETA.INV(probability,...)
 = x。
 beta 分布函数可用于项目设计，在已知预期的完成时间和变化参数后，模拟可能的完成时间。

```
BETA.INV(probability,alpha,beta,[A],[B])
BETA.INV 函数语法具有以下参数：probability必需。
 与 beta 分布相关的概率。
alpha必需。
 分布参数。
beta必需。
 分布参数。
A可选。
 x 所属区间的下界。
B可选。
 x 所属区间的上界。

```
## BETADIST
> 返回累积 beta 概率密度函数。
 Beta 分布通常用于研究样本中一定部分的变化情况，例如，人们一天中看电视的时间比率。

```
BETADIST(x,alpha,beta,[A],[B])
x必需。
 用来计算其函数的值，介于值 A 和 B 之间。
alpha 必需。
 分布参数。
beta   必需。
 分布参数。
A 可选。
 x 所属区间的下界。
B  可选。
 x 所属区间的上界。

```
## BETAINV
> 返回指定 beta 分布的累积 beta 概率密度函数的反函数。
 也就是说，如果 probability = BETADIST(x,...)
，则 BETAINV(probability,...)
 = x。
 beta 分布函数可用于项目设计，在已知预期的完成时间和变化参数后，模拟可能的完成时间。

```
BETAINV(probability,alpha,beta,[A],[B])
probability必需。
 与 beta 分布相关的概率。
alpha   必需。
 分布参数。
beta 必需。
 分布参数。
A   可选。
 x 所属区间的下界。
B   可选。
 x 所属区间的上界。

```
## BIN2DEC
> 将二进制数转换为十进制数。

```
BIN2DEC(number)
number必需。
 要转换的二进制数。
 Number 包含的字符不能超过 10 个（10 位）。
 Number 的最高位为符号位。
 其余 9 位是数量位。
 负数用二进制补码记数法表示。

```
## BIN2HEX
> 将二进制数转换为十六进制数。

```
BIN2HEX(number, [places])
number必需。
 要转换的二进制数。
 Number 包含的字符不能超过 10 个（10 位）。
 Number 的最高位为符号位。
 其余 9 位是数量位。
 负数用二进制补码记数法表示。
places   可选。
 要使用的字符数。
 如果省略 Places，BIN2HEX 将使用必需的最小字符数。
 Places 可用于在返回的值前置 0（零）。

```
## BIN2OCT
> 将二进制数转换为八进制数。

```
BIN2OCT(number, [places])
number必需。
 要转换的二进制数。
 Number 包含的字符不能超过 10 个（10 位）。
 Number 的最高位为符号位。
 其余 9 位是数量位。
 负数用二进制补码记数法表示。
places   可选。
 要使用的字符数。
 如果省略 places，BIN2OCT 将使用必需的最小字符数。
 Places 可用于在返回的值前置 0（零）。

```
## BINOM.DIST 
> 返回一元二项式分布的概率。
 BINOM.DIST 用于处理固定次数的试验或实验问题，前提是任意试验的结果仅为成功或失败两种情况，实验是独立实验，且在整个试验过程中成功的概率固定不变。
 例如，BINOM.DIST 可以计算三个即将出生的婴儿中两个是男孩的概率。

```
BINOM.DIST(number_s,trials,probability_s,cumulative)
number_s必需。
 试验的成功次数。
trials必需。
 独立试验次数。
probability_s必需。
 每次试验成功的概率。
cumulative必需。
 决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 BINOM.DIST 返回累积分布函数，即最多存在 number_s 次成功的概率；如果为 FALSE，则返回概率密度函数，即存在 number_s 次成功的概率。

```
## BINOM.DIST.RANGE 
> 使用二项式分布返回试验结果的概率。

```
BINOM.DIST.RANGE(trials,probability_s,number_s,[number_s2])
BINOM.DIST.RANGE 函数语法具有下列参数。
trials必需。
 独立试验次数。
 必须大于或等于 0。
probability_s必需。
 每次试验成功的概率。
 必须大于或等于 0 并小于或等于 1。
number_s必需。
 试验成功次数。
 必须大于或等于 0 并小于或等于 Trials。
number_s2可选。
 如提供，则返回试验成功次数将介于 number_s 和 number_s2 之间的概率。
 必须大于或等于 number_s 并小于或等于 trials。

```
## BINOM.INV 
> 返回一个数值，它是使得累积二项式分布的函数值大于等于临界值的最小整数。

```
BINOM.INV(trials,probability_s,alpha)
trials必需。
 贝努利试验次数。
probability_s必需。
 一次试验中成功的概率。
alpha必需。
 临界值。

```
## BINOMDIST
> 返回一元二项式分布的概率。
 BINOMDIST 用于处理固定次数的试验或实验问题，前提是任意试验的结果仅为成功或失败两种情况，实验是独立实验，且在整个试验过程中成功的概率固定不变。
 例如，BINOMDIST 可以计算三个即将出生的婴儿中两个是男孩的概率。

```
BINOMDIST(number_s,trials,probability_s,cumulative)
number_s   必需。
 试验的成功次数。
trials 必需。
 独立试验次数。
probability_s  必需。
 每次试验成功的概率。
cumulative  必需。
 决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 BINOMDIST 返回累积分布函数，即最多存在 number_s 次成功的概率；如果为 FALSE，则返回概率密度函数，即存在 number_s 次成功的概率。

```
## BITAND 
> 返回两个数的按位“与”。

```
BITAND( number1, number2)
number1必需。
 必须为十进制格式并大于或等于 0。
number2必需。
 必须为十进制格式并大于或等于 0。

```
## BITLSHIFT 
> 返回向左移动指定位数后的数值。

```
BITLSHIFT(number, shift_amount)
number 必需。
 Number 必须为大于或等于 0 的整数。
shift_amount必需。
 Shift_amount 必须为整数。

```
## BITOR 
> 返回两个数的按位“或”。

```
BITOR(number1, number2)
number1必需。
 必须为十进制格式并大于或等于 0。
number2必需。
 必须为十进制格式并大于或等于 0。

```
## BITRSHIFT 
> 返回向右移动指定位数后的数值。

```
BITRSHIFT(number, shift_amount)
number必需。
 必须为大于或等于 0 的整数。
shift_amount必需。
 必须为整数。

```
## BITXOR 
> 返回两个数值的按位“异或”结果。

```
BITXOR(number1, number2)
number1必需。
 必须大于或等于 0。
number2必需。
 必须大于或等于 0。

```
## CALL
> 调用动态链接库或代码源中的过程
```
语法1：与 REGISTER 配合使用CALL(register_id,[argument1],...)
register_id它是以前执行的 REGISTER 或 REGISTER.ID 函数返回的值。
语法2：单独使用（在 Microsoft Excel for Windows 中）CALL(module_text,procedure,type_text,[argument1],...])
module_text必需。
带引号的文本，用于指定动态链接库 (DLL)
 的名称，该链接库包含 Microsoft Excel for Windows 中的过程。
procedure必需。
用于指定 Microsoft Excel for Windows 的 DLL 中的函数名称的文本。
还可以使用函数的序数值，该值来自模块定义文件 (.DEF)
 中的 EXPORTS 语句。
序数值不能为文本形式。
type_text   必需。
指定返回值的数据类型以及 DLL 或代码源的所有参数的数据类型的文本。
Type_text 的首字母指定返回值。
有关 type_text 所使用的代码的详细信息，请参阅使用 CALL 和 REGISTER 函数。
对于独立的 DLL 或代码源 (XLL)
，可以省略此参数。
argument1,...可选。
要传递到过程的参数。

```
## CEILING
> 返回将参数 number 向上舍入（沿绝对值增大的方向）为最接近的指定基数的倍数。
 例如，如果您不希望在价格使用所有“分”值，当产品价格为 $4.42 时，则可以使用公式 =CEILING(4.42,0.05)
 将价格向上舍入到最接近的 5 美分。

```
CEILING(number, significance)
number必需。
 要舍入的值。
significance必需。
 要舍入到的倍数。

```
## CEILING.MATH 
> 将数字向上舍入为最接近的整数或最接近的指定基数的倍数。

```
CEILING.MATH(number, [significance], [mode])
number   必需。
 数字必须小于 9.99E+307 并大于 -2.229E-308。
significance可选。
 要将 Number 舍入的倍数。
mode可选。
 对于负数，控制 Number 是按朝向 0 还是远离 0 的方向舍入。

```
## CEILING.PRECISE
> 返回一个数字，该数字向上舍入为最接近的整数或最接近的有效位的倍数。
 无论该数字的符号如何，该数字都向上舍入。
 但是，如果该数字或有效位为 0，则返回 0。

```
CEILING.PRECISE(number, [significance])
number   必需。
要进行舍入的值。
significance可选。
 要将数字舍入的倍数。

```
## CELL
> CELL 函数返回有关单元格的格式、位置或内容的信息。
 例如，如果要在对单元格执行计算之前，验证它包含的是数值而不是文本，则可以使用以下公式：= IF( CELL(type, A1)
 = v, A1 * 2, 0)
仅当单元格 A1 包含数值时，此公式才计算 A1*2 ；如果 A1 包含文本或为空，则此公式将返回 0。

```
CELL(info_type, [reference])
info_type必需。
 一个文本值，指定要返回的单元格信息的类型。
 下面的列表显示了 Info_type 参数的可能值及相应的结果。
info_type 返回结果address 引用中第一个单元格的引用，文本类型。
col 引用中单元格的列标。
color  如果单元格中的负值以不同颜色显示，则为值 1；否则，返回 0（零）。
contents引用中左上角单元格的值：不是公式。
filename包含引用的文件名（包括全部路径），文本类型。
“format”与单元格的数字格式相对应的文本值。
“parentheses”   如果单元格中为正值或所有单元格均加括号，则为值 1；否则返回 0。
“prefix”  与单元格中的“前置标签”相对应的文本值。
“protect”   如果单元格没有锁定，则为值 0；如果单元格锁定，则返回 1。
“row”引用中单元格的行号。
type   与单元格中的数据类型相对应的文本值。
width 取整后的单元格的列宽。
列宽以默认字号的一个字符的宽度为单位。
reference可选。
 需要其相关信息的单元格。
 如果省略，则将 Info_type 参数中指定的信息返回给最后更改的单元格。
 如果参数 reference 是某一单元格区域，则函数 CELL 只将该信息返回给该区域左上角的单元格。
CELL 格式代码下面的列表描述了当参数 Info_type 为“format”，以及参数 reference 为用内置数字格式设置的单元格时，函数 CELL 返回的文本值。
如果 Excel 的格式为 CELL 函数返回值常规G0  F0#,##0 ,00.00 F2#,##0.00 ,2$#,##0_)
;($#,##0)
 C0$#,##0_)
;[Red]($#,##0)
C0-$#,##0.00_)
;($#,##0.00)
   C2$#,##0.00_)
;[Red]($#,##0.00)
  C2-0% P00.00%P20.00E+00 S2# ?/? 或 # ??/??  Gyy-m-d 或 yy-m-d h:mm 或 dd-mm-yy  D4d-mmm-yy 或 dd-mmm-yy  D1d-mmm 或 dd-mmm  D2mmm-yy   D3dd-mm  D5h:mm AM/PM   D7h:mm:ss AM/PM   D6h:mm  D9h:mm:ss  D8
```
## CHAR
> 返回由代码数字指定的字符
```
CHAR(number)
number必需。
 介于 1 到 255 之间的数字，指定所需的字符。
 使用的是当前计算机字符集中的字符。

```
## CHIDIST
> 返回 χ2 分布的右尾概率。
 χ2 分布与 χ2 测试相关联。
 使用 χ2 测试可比较观察值和预期值。
 例如，某项遗传学实验可能假设下一代植物将呈现出某一组颜色。
 通过使用该函数比较观察结果和理论值，可以确定初始假设是否有效。

```
CHIDIST(x,deg_freedom)
x 必需。
 用来计算分布的数值。
deg_freedom   必需。
 自由度数。

```
## CHIINV
> 返回 χ2 分布的右尾概率的反函数。
 如果 probability = CHIDIST(x,...)
，则 CHIINV(probability,...)
 = x。
 使用此函数可比较观察结果与理论值，以确定初始假设是否有效。

```
CHIINV(probability,deg_freedom)
probability  必需。
 与 χ2 分布相关联的概率。
deg_freedom  必需。
 自由度数。

```
## CHISQ.DIST 
> 返回 χ2 分布。
χ2 分布通常用于研究样本中某些事物变化的百分比，例如人们一天中用来看电视的时间所占的比例。

```
CHISQ.DIST(x,deg_freedom,cumulative)
x必需。
 用来计算分布的数值。
deg_freedom必需。
 自由度数。
cumulative必需。
 决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 CHISQ.DIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。

```
## CHISQ.DIST.RT 
> 返回 χ2 分布的右尾概率。
χ2 分布与 χ2 测试相关联。
 使用 χ2 测试可比较观察值和预期值。
 例如，某项遗传学实验可能假设下一代植物将呈现出某一组颜色。
 通过使用该函数比较观察结果和理论值，可以确定初始假设是否有效。

```
CHISQ.DIST.RT(x,deg_freedom)
x必需。
 用来计算分布的数值。
deg_freedom必需。
 自由度数。

```
## CHISQ.INV 
> 返回 χ2 分布的左尾概率的反函数。
χ2 分布通常用于研究样本中某些事物变化的百分比，例如人们一天中用来看电视的时间所占的比例。

```
CHISQ.INV(probability,deg_freedom)
probability必需。
 与 χ2 分布相关联的概率。
deg_freedom必需。
 自由度数。

```
## CHISQ.INV.RT 
> 返回 χ2 分布的右尾概率的反函数。
如果 probability = CHISQ.DIST.RT(x,...)
，则 CHISQ.INV(probability,...)
 = x。
 使用此函数可比较观察结果与理论值，以确定初始假设是否有效。

```
CHISQ.INV.RT(probability,deg_freedom)
probability必需。
 与 χ2 分布相关联的概率。
deg_freedom必需。
 自由度数。

```
## CHISQ.TEST 
> 返回独立性检验值。
CHISQ.TEST 返回卡方 (χ2)
 分布的统计值和相应的自由度数。
 您可以使用 χ2 检验值确定假设结果是否经过实验验证。

```
CHISQ.TEST(actual_range,expected_range)
actual_range必需。
 包含观察值的数据区域，用于检验预期值。
expected_range必需。
 包含行列汇总的乘积与总计值之比率的数据区域。

```
## CHITEST
> 返回独立性检验值。
 CHITEST 返回卡方 (χ2)
 分布的统计值和相应的自由度数。
 您可以使用 χ2 检验值确定假设结果是否经过实验验证。

```
CHITEST(actual_range,expected_range)
actual_range  必需。
 包含观察值的数据区域，用于检验预期值。
xpected_range  必需。
 包含行列汇总的乘积与总计值之比率的数据区域。

```
## CHOOSE
> 使用 index_num 返回数值参数列表中的数值。
 使用 CHOOSE 可以根据索引号从最多 254 个数值中选择一个。
 例如，如果 value1 到 value7 表示一周的 7 天，那么将 1 到 7 之间的数字用作 index_num 时，CHOOSE 将返回其中的某一天。

```
CHOOSE(index_num, value1, [value2], ...)
index_num必需。
 用于指定所选定的数值参数。
 index_num 必须是介于 1 到 254 之间的数字，或是包含 1 到 254 之间的数字的公式或单元格引用。
如果 index_num 为 1，则 CHOOSE 返回 value1；如果为 2，则 CHOOSE 返回 value2，以此类推。
如果 index_num 小于 1 或大于列表中最后一个值的索引号，则 CHOOSE 返回 #VALUE! 错误值。
如果 index_num 为小数，则在使用前将被截尾取整。
value1, value2, ...value1 是必需的，后续值是可选的。
 1 到 254 个数值参数，CHOOSE 将根据 index_num 从中选择一个数值或一项要执行的操作。
 参数可以是数字、单元格引用、定义的名称、公式、函数或文本。

```
## CLEAN
> 删除文本中所有不能打印的字符。
 对从其他应用程序导入的文本使用 CLEAN，将删除其中含有的当前操作系统无法打印的字符。
 例如，可以使用 CLEAN 删除某些通常出现在数据文件开头和结尾处且无法打印的低级计算机代码。

```
CLEAN(text)
text必需。
 要从中删除非打印字符的任何工作表信息。

```
## CODE
> 返回文本字符串中第一个字符的数字代码
```
CODE(text)
text必需。
 要为其获取第一个字符的代码的文本。

```
## COLUMN
> 返回指定单元格引用的列号。
 例如，公式 =COLUMN(D10)
 返回 4，因为列 D 为第四列。

```
COLUMN([reference])
reference可选。
 要返回其列号的单元格或单元格范围。
如果省略参数 reference 或该参数为一个单元格区域，并且 COLUMN 函数是以水平数组公式的形式输入的，则 COLUMN 函数将以水平数组的形式返回参数 reference 的列号。
将公式作为数组公式输入从公式单元格开始，选择要包含数组公式的区域。
 按 F2，再按 Ctrl+Shift+Enter。

```
## COLUMNS
> 返回数组或引用的列数。

```
COLUMNS(array)
array必需。
 要计算列数的数组、数组公式或是对单元格区域的引用。

```
## COMBIN
> 返回给定数目项目的组合数 使用函数 COMBIN 确定给定数目项目可能的总组数。

```
COMBIN(number, number_chosen)
number   必需。
 项目的数量。
number_chosen必需。
 每一组合中项目的数量。

```
## COMBINA 
> 返回给定数目的项的组合数（包含重复）。

```
COMBINA(number, number_chosen)
number  必需。
 必须大于或等于 0 并大于或等于 Number_chosen。
 非整数值将被截尾取整。
number_chosen必需。
 必须大于或等于 0。
 非整数值将被截尾取整。

```
## COMPLEX
> 将实系数及虚系数转换为 x+yi 或 x+yj 形式的复数。

```
COMPLEX(real_num, i_num, [suffix])
real_num必需。
 复数的实系数。
i_num  必需。
 复数的虚系数。
suffix  可选。
 复数中虚系数的后缀。
 如果省略，则认为它是“i”。

```
## CONCAT 
> 将多个区域和/或字符串的文本组合起来，但不提供分隔符或 IgnoreEmpty 参数。

```
CONCAT(text1, [text2],…)
text1必需。
要联接的文本项。
字符串或字符串数组，如单元格区域。
text2, ... 可选。
要联接的其他文本项。
文本项最多可以有 253 个文本参数。
每个参数可以是一个字符串或字符串数组，如单元格区域。

```
## CONCATENATE
> 将几个文本项合并为一个文本项
```
CONCATENATE(text1, [text2], ...)
text1 必需。
要联接的第一个项目。
项目可以是文本值、数字或单元格引用。
text2, ...  可选。
要联接的其他文本项目。
最多可以有 255 个项目，总共最多支持 8,192 个字符。

```
## CONFIDENCE
> 使用正态分布返回总体平均值的置信区间。

```
CONFIDENCE(alpha,standard_dev,size)
alpha  必需。
 用来计算置信水平的显著性水平。
 standard_dev必需。
 数据区域的总体标准偏差，假定为已知。
size  必需。
 样本大小。

```
## CONFIDENCE.NORM 
> 使用正态分布返回总体平均值的置信区间。
置信区间为某一范围的值。
 样本平均值 x 位于此范围的中心，此范围为 x ± CONFIDENCE.NORM。
 例如，如果 x 是通过邮件订购的产品交付时间的样本平均值，x ± CONFIDENCE.NORM 为总体平均值范围。
 对于在此范围中的任意总体平均值 μ0，从 μ0 而非 x 中获取样本平均值的概率大于 alpha；对于不在此范围内的任意总体平均值 μ0，从 μ0 而非 x 中获取样本平均值的概率小于 alpha。
 换言之，假设我们使用 x、standard_dev 和字号在显著性水平 alpha 上构建一个双尾测试，其中假设总体平均值为 μ0。
 则如果 μ0 处于置信区间，我们将不会拒绝该假设；如果 μ0 未处于置信区间，则将拒绝该假设。
 置信区间无法使我们推断出概率 1 - alpha，即我们的下一个包的发送时间处于置信区间内。

```
CONFIDENCE.NORM(alpha,standard_dev,size)
alpha必需。
 用来计算置信水平的显著性水平。
 置信水平等于 100*(1 - alpha)
%，亦即，如果 alpha 为 0.05，则置信水平为 95%。
standard_dev必需。
 数据区域的总体标准偏差，假定为已知。
size必需。
 样本大小。

```
## CONFIDENCE.T 
> 使用学生的 t 分布返回总体平均值的置信区间。

```
CONFIDENCE.T(alpha,standard_dev,size)
alpha必需。
 用来计算置信水平的显著性水平。
 置信水平等于 100*(1 - alpha)
%，亦即，如果 alpha 为 0.05，则置信水平为 95%。
standard_dev必需。
 数据区域的总体标准偏差，假定为已知。
size必需。
 样本大小。

```
## CONVERT
> 将数字从一种度量系统转换为另一种度量系统。
 例如，CONVERT 可将以英里为单位的距离表转换为以千米为单位的距离表。

```
CONVERT(number,from_unit,to_unit)
number是以 from_unit 为单位的需要进行转换的数值。
from_unit是数值的单位。
to_unit 是结果的单位。
 CONVERT 接受 from_unit 和 to_unit 的以下文本值（引号中）：重量和质量 From_unit 或 to_unit克 g斯勒格 sg磅（常衡制） lbmU（原子质量单位）  u盎司（常衡制） ozm颗粒 grain美担cwt 或 shweight英担uk_cwt 或 lcwt (hweight)
英石stone吨ton英吨uk_ton 或 LTON (brton)
距离From_unit 或 to_unit米m法定英里mi海里Nmi英寸in英尺ft码yd埃ang厄尔ell光年ly秒差距parsec 或 pc皮卡（1/72 英寸）   Picapt 或 Pica派卡（1/6 英寸） pica美制调查英里（法定英里） survey_mi时间From_unit 或 to_unit年yr日day 或 d小时hr分钟mn 或 min秒sec 或 s压强From_unit 或 to_unit帕斯卡   Pa（或 p）大气压   atm（或 at）毫米汞柱   mmHg磅平方英寸   psi托   Torr力From_unit 或 to_unit牛顿N达因dyn（或 dy）磅力lbf朋特pond能量 From_unit 或 to_unit焦耳 J尔格 e热力学卡 cIT 卡 cal电子伏 eV（或 ev）马力-小时HPh（或 hh）瓦特-小时Wh（或 wh）英尺磅  flb英热单位   BTU（或 btu）功率   From_unit 或 to_unit英制马力   HP（或 h）公制马力   PS瓦特W（或 w）磁From_unit 或 to_unit特斯拉T高斯ga温度From_unit 或 to_unit摄氏度C（或 cel）华氏度F（或 fah）开氏温标K（或 kel）兰氏度Rank列氏度Reau容积（或 液体度量 ）   From_unit 或 to_unit茶匙 tsp现代茶匙 tspm汤匙 tbs液量盎司 oz杯  cup美制 品脱 pt（或 us_pt）英制 品脱 uk_pt夸脱   qt英制夸脱（英国）   uk_qt加仑   gal英制加仑（英国）   uk_gal升   l 或 L (lt)
立方埃   ang3 或 ang^3美制 油桶  barrel美制 蒲式耳  bushel立方英尺   ft3 或 ft^3立方英寸   in3 或 in^3立方光年   ly3 或 ly^3立方米   m3 或 m^3立方英里   mi3 或 mi^3立方码   yd3 或 yd^3立方海里   Nmi3 或 Nmi^3立方皮卡Picapt3、Picapt^3、Pica3 或 Pica^3总注册吨GRT (regton)
尺码吨（运费吨）MTON面积 From_unit 或 to_unit国际英亩 uk_acre美制 调查/法定英亩  us_acre平方埃 ang2 或 “ang^2公亩 ar平方英尺 ft2 或 ft^2公顷 ha平方英寸 in2 或 in^2平方光年 ly2 或 ly^2平方米 m2 或 m^2摩根  Morgen平方英里  mi2 或 mi^2平方海里  Nmi2 或 Nmi^2平方皮卡  Picapt2、Pica2、Pica^2 或 Picapt^2平方码  yd2 或 yd^2信息  From_unit 或 to_unit比特  bit字节  byte速度  From_unit 或 to_unit海里  admkn节  kn米每小时  m/h 或 m/hr米每秒  m/s 或 m/sec英里每小时  mph下列缩写的单位前缀可以加在任何的公制单位 from_unit 或 to_unit 之前。
前缀乘子 缩写尧它   1E+24Y泽它   1E+21Z千兆兆   1E+18E千万亿   1E+15P万亿   1E+12T十亿   1E+09G百万   1E+06M千   1E+03k百   1E+02h十   1E+01da 或 e十分之一   1E-01 d百分之一   1E-02 c千分之一   1E-03 m微   1E-06 u毫微   1E-09 n兆分之一   1E-12 p千万亿分之一  1E-15  f阿托   1E-18 a普托   1E-21 z科托   1E-24 y二进制前缀 前缀值   缩写   派生自yobi   2^80 = 1 208 925 819 614 629 174 706 176  Yi 尧它zebi   2^70 = 1 180 591 620 717 411 303 424  Zi 泽它exbi   2^60 = 1 152 921 504 606 846 976 Ei 千兆兆pebi  2^50 = 1 125 899 906 842 624 Pi 千万亿tebi   2^40 = 1 099 511 627 776Ti 万亿gibi   2^30 = 1 073 741 824   Gi十亿mebi 2^20 = 1 048 576  Mi   百万kibi   2^10 = 1024  ki 千
```
## CORREL
> 返回返回 Array1 和 Array2 单元格区域的相关系数。
使用相关系数确定两个属性之间的关系。
例如，您可以检查一个位置的平均温度和空调使用情况之间的关系。

```
CORREL(array1,array2)
array1必需。
值的单元格区域。
array2必需。
值的第二个单元格区域。

```
## COS
> 返回已知角度的余弦值。

```
COS(number)
number  必需。
 想要求余弦的角度，以弧度表示。

```
## COSH
> 返回数字的双曲余弦值。

```
COSH(number)
number必需。
 想要求双曲余弦的任意实数。

```
## COT 
> 返回以弧度表示的角度的余切值。

```
COT(number)
number必需。
 要获得其余切值的角度，以弧度表示。

```
## COTH 
> 返回一个双曲角度的双曲余切值。

```
COTH(number)
number必需。

```
## COUNT
> 计算包含数字的单元格个数以及参数列表中数字的个数。

```
COUNT(value1, [value2], ...)
COUNT 函数语法具有下列参数：value1必需。
 要计算其中数字的个数的第一项、单元格引用或区域。
value2, ...可选。
 要计算其中数字的个数的其他项、单元格引用或区域，最多可包含 255 个。

```
## COUNTA
> 计算范围中不为空的单元格的个数。

```
COUNTA(value1, [value2], ...)
value1必需。
 表示要计数的值的第一个参数。
value2, ...可选。
 表示要计数的值的其他参数，最多可包含 255 个参数。

```
## COUNTBLANK
> 用于计算单元格区域中的空单元格的个数。

```
COUNTBLANK（rang）rang必需。
 需要计算其中空白单元格个数的区域。

```
## COUNTIF
> 用于统计满足某个条件的单元格的数量。
例如，统计特定城市在客户列表中出现的次数。

```
COUNTIF(range, criteria)
range   必需。
要进行计数的单元格组。
区域可以包括数字、数组、命名区域或包含数字的引用。
空白和文本值将被忽略。
criteria   必需。
用于决定要统计哪些单元格的数量的数字、表达式、单元格引用或文本字符串。
例如，可以使用 32 之类数字，“>32”之类比较，B4 之类单元格，或“苹果”之类单词。
COUNTIF 仅使用一个条件。
 如果要使用多个条件，请使用 COUNTIFS。

```
## COUNTIFS
> 计算区域内符合多个条件的单元格的数量
```
COUNTIFS(criteria_range1, criteria1, [criteria_range2, criteria2],…)
criteria_range1必需。
 在其中计算关联条件的第一个区域。
criteria1必需。
 条件的形式为数字、表达式、单元格引用或文本，它定义了要计数的单元格范围。
 例如，条件可以表示为 32、>32、B4、apples或 32。
criteria_range2, criteria2, ...可选。
 附加的区域及其关联条件。
 最多允许 127 个区域/条件对。

```
## COUPDAYBS
> COUPDAYBS 函数返回从付息期开始到结算日的天数。

```
COUPDAYBS(settlement, maturity, frequency, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
frequency必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis日计数基准0 或省略  US (NASD)
 30/3601   实际/实际2   实际/3603   实际/3654   欧洲 30/360
```
## COUPDAYS
> 返回结算日所在的付息期的天数。

```
COUPDAYS(settlement, maturity, frequency, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
frequency必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis  日计数基准0 或省略US (NASD)
 30/3601 实际/实际2 实际/3603 实际/3654 欧洲 30/360
```
## COUPDAYSNC
> 返回从结算日到下一票息支付日之间的天数。

```
COUPDAYSNC(settlement, maturity, frequency, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
frequency必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis   日计数基准0 或省略 US (NASD)
 30/3601  实际/实际2  实际/3603  实际/3654  欧洲 30/360
```
## COUPNCD
> 返回一个表示在结算日之后下一个付息日的数字。

```
COUPNCD(settlement, maturity, frequency, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
frequency必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis  日计数基准0 或省略US (NASD)
 30/3601实际/实际2实际/3603实际/3654欧洲 30/360
```
## COUPNUM
> 返回在结算日和到期日之间的付息次数，向上舍入到最近的整数。

```
COUPNUM(settlement, maturity, frequency, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
frequency必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis   日计数基准0 或省略 US (NASD)
 30/3601  实际/实际2  实际/3603  实际/3654  欧洲 30/360
```
## COUPPCD
> 返回表示结算日之前的上一个付息日的数字。

```
COUPPCD(settlement, maturity, frequency, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
frequency必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis 日计数基准0或省略US (NASD)
 30/3601实际/实际2实际/3603实际/3654欧洲 30/360
```
## COVAR
> 返回协方差，即两个数据集中每对数据点的偏差乘积的平均数。
利用协方差确定两个数据集之间的关系。
例如，您可检查教育程度与收入是否成正比。

```
COVAR(array1,array2)
array1必需。
整数的第一个单元格区域。
array2必需。
整数的第二个单元格区域。

```
## COVARIANCE.P 
> 返回总体协方差，即两个数据集中每对数据点的偏差乘积的平均数。
利用协方差确定两个数据集之间的关系。

```
COVARIANCE.P(array1,array2)
array1必需。
整数的第一个单元格区域。
array2必需。
整数的第二个单元格区域。

```
## COVARIANCE.S 
> 返回样本协方差，即两个数据集中每对数据点的偏差乘积的平均值。

```
COVARIANCE.S(array1,array2)
array1必需。
整数的第一个单元格区域。
array2必需。
整数的第二个单元格区域。

```
## CRITBINOM
> 返回一个数值，它是使得累积二项式分布的函数值大于等于临界值的最小整数。
 此函数可用于质量检验。
 例如，使用 CRITBINOM 来决定装配线上整批产品达到检验合格所允许的最多残次品个数。

```
CRITBINOM(trials,probability_s,alpha)
trials 必需。
 贝努利试验次数。
probability_s   必需。
 一次试验中成功的概率。
alpha 必需。
 临界值。

```
## CSC 
> 返回角度的余割值，以弧度表示。

```
CSC(number)
number必需。

```
## CSCH 
> 返回角度的双曲余割值，以弧度表示。

```
CSCH(number)
number必需。

```
## CUBEKPIMEMBER
> 返回重要性能指示器 (KPI)
 属性，并在单元格中显示 KPI 名称。
 KPI 是一种用于监控单位绩效的可计量度量值，如每月总利润或季度员工调整。

```
CUBEKPIMEMBER(connection, kpi_name, kpi_property, [caption])
connection必需。
 一个表示多维数据集的连接名称的文本字符串。
kpi_name必需。
 一个表示多维数据集的 KPI 名称的文本字符串。
kpi_property  必需。
 返回的 KPI 组件，可以是以下值之一：整型 枚举常量说明1   KPIValue 实际值2   KPIGoal   目标值3   KPIStatus KPI 在特定时刻的状态4   KPITrend  走向值的度量5   KPIWeight   分配给 KPI 的相对权重6   KPICurrentTimeMember   KPI 的临时根据内容如果您为 kpi_property 指定 KPIValue，则只在单元格中显示 kpi_name。
caption 可选。
 是显示在单元格中的可选文本字符串，而不是 kpi_name 和 kpi_property。

```
## CUBEMEMBER
> 返回多维数据集中的成员或元组。
用于验证多维数据集内是否存在成员或元组。

```
CUBEMEMBER(connection, member_expression, [caption])
connection必需。
 一个表示多维数据集的连接名称的文本字符串。
member_expression必需。
 多维表达式 (MDX)
 的文本字符串，用来计算出多维数据集中的唯一成员。
 此外，也可以将 member_expression 指定为单元格区域或数组常量的元组。
caption可选。
 显示在多维数据集的单元格（而不是标题）中的文本字符串（如果定义了一个文本字符串）。
 当返回元组时，所用的标题为元组中最后一个成员的文本字符串。

```
## CUBEMEMBERPROPERTY
> 返回多维数据集中成员属性的值。
 用于验证多维数据集内是否存在某个成员名并返回此成员的指定属性。

```
CUBEMEMBERPROPERTY(connection, member_expression, property)
CUBEMEMBERPROPERTY 函数语法具有以下参数：Connection必需。
一个表示多维数据集的连接名称的文本字符串。
Member_expression必需。
一个文本字符串，表示多维数据集中的一个成员的多维表达式 (MDX)
。
Property必需。
一个文本字符串，表示返回的属性的名称或对包含该属性的名称的单元格的引用。

```
## CUBERANKEDMEMBER
> 返回集合中的第 n 个或排在一定名次的成员。
 用来返回集合中的一个或多个元素，如业绩最好的销售人员或前 10 名的学生。

```
CUBERANKEDMEMBER(connection, set_expression, rank, [caption])
connection  必需。
 一个表示多维数据集的连接名称的文本字符串。
set_expression必需。
 集表达式的文本字符串，例如 {[Item1].children}。
 Set_expression 也可以是 CUBESET 函数，或者是对包含 CUBESET 函数的单元格的引用。
rank   必需。
 用于指定要返回的最高值的整型值。
 如果排名值为 1，它将返回最高值；如果排名值为 2，它将返回第二高的值，依此类推。
 要返回最高的前 5 个值，请使用 5 次 CUBERANKEDMEMBER ，每一次指定从 1 到 5 的不同排名。
caption  可选。
 显示在多维数据集的单元格（而不是标题）中的文本字符串（如果定义了一个文本字符串）。

```
## CUBESET
> 定义成员或元组的计算集。
方法是向服务器上的多维数据集发送一个集合表达式，此表达式创建集合，并随后将该集合返回到 Microsoft Excel。

```
CUBESET(connection, set_expression, [caption], [sort_order], [sort_by])
connection  必需。
 一个表示多维数据集的连接名称的文本字符串。
set_expression必需。
 产生一组成员或元组的集合表达式的文本字符串。
 Set_expression 也可以是对 Excel 区域的单元格引用，该区域包含一个或多个成员、元组或包含在集合中的集合。
caption  可选。
 显示在多维数据集的单元格（而不是标题）中的文本字符串（如果定义了一个文本字符串）。
sort_order 可选。
 要执行的排序类型（如果有），可以为下列类型之一：整型  枚举常量  说明 Sort_by参数0SortNone 按当前顺序保留集合 忽略1SortAscending使用 sort_by 按升序对集合进行排序。
   必选2SortDescending  使用 sort_by 按降序对集合进行排序。
   必选3SortAlphaAscending  按字母升序对集合进行排序。
 忽略4Sort_Alpha_Descending 按字母降序对集合进行排序。
 忽略5Sort_Natural_Ascending 按自然升序对集合进行排序。
 忽略6Sort_Natural_Descending   按自然降序对集合进行排序。
 忽略默认值为 0。
 对一组元组进行字母排序是以每个元组中最后一个元素为排序依据的。
 有关这些不同的排序顺序的详细信息，请参阅 Microsoft Office SQL Analysis Services 帮助系统。
sort_by   可选。
 排序所依据的值的文本字符串。
 例如，要获得销售量最高的城市，则 set_expression 为一组城市，sort_by 为销售量。
 或者，要获得人口最多的城市，则 set_expression 为一组城市，sort_by 为人口量。
 如果 sort_order 需要 sort_by，而 sort_by 被忽略，则 CUBESET 函数返回 #VALUE! 错误消息。

```
## CUBESETCOUNT
> 返回集合中的项目数。

```
CUBESETCOUNT(set)
set必需。
 Microsoft Office Excel 表达式的文本字符串，该表达式计算出由 CUBESET 函数定义的集合。
 Set 也可以是 CUBESET 函数，或者是对包含 CUBESET 函数的单元格的引用。

```
## CUBEVALUE
> 从多维数据集中返回汇总值。

```
CUBEVALUE(connection, [member_expression1], [member_expression2], …)
connection必需。
 一个表示多维数据集的连接名称的文本字符串。
member_expression可选。
多维表达式 (MDX)
 的文本字符串，用来计算出多维数据集内的成员或元组。
另外，member_expression 可以是由 CUBESET 函数定义的集合。
使用 member_expression 作为切片器来定义要返回其汇总值的多维数据集部分。
如果 member_expression 中未指定度量值，则使用该多维数据集的默认度量值。

```
## CUMIPMT
> 返回一笔贷款在给定的 start_period 到 end_period 期间累计偿还的利息数额。

```
CUMIPMT(rate, nper, pv, start_period, end_period, type)
rate必需。
 利率。
nper必需。
 总付款期数。
pv必需。
 现值。
start_period必需。
 计算中的首期。
 付款期数从 1 开始计数。
end_period必需。
 计算中的末期。
type必需。
 付款时间类型。
type  时间类型0（零）期末付款1期初付款
```
## CUMPRINC
> 返回一笔贷款在给定的 start_period 到 end_period 期间累计偿还的本金数额。

```
CUMPRINC(rate, nper, pv, start_period, end_period, type)
rate必需。
 利率。
nper必需。
 总付款期数。
pv必需。
 现值。
start_period必需。
 计算中的首期。
 付款期数从 1 开始计数。
end_period必需。
 计算中的末期。
type必需。
 付款时间类型。
type 时间类型0（零）期末付款1期初付款
```
## DATE
> 是一个日期函数主要帮助在excel中输入日期值，将三个单独的值并将它们合并为一个日期，避免在其他函数中使用日期进行计算是出现意外的错误。

```
DATE(year,month,day)
year  必需。
year 参数的值可以包含一到四位数字。
Excel 将根据计算机正在使用的日期系统来解释 year 参数。
默认情况下，Microsoft Excel for Windows 使用的是 1900 日期系统，这表示第一个日期为 1900 年 1 月 1 日。
month   必需。
一个正整数或负整数，表示一年中从 1 月至 12 月（一月到十二月）的各个月。
day 必需。
一个正整数或负整数，表示一月中从 1 日到 31 日的各天。

```
## DATEDIF
> 计算两个日期之间的天数、月数或年数。
在需要计算年龄的公式中, 此函数非常有用。

```
DATEDIF(start_date,end_date,unit)
start_date 必需。
用于表示时间段的第一个（即起始）日期的日期。
 日期值有多种输入方式：带引号的文本字符串（例如 2001/1/30）、序列号（例如 36921，在商用 1900 日期系统时表示 2001 年 1 月 30 日）或其他公式或函数的结果（例如 DATEVALUE(2001/1/30)
）。
end_date  必需。
用于表示时间段的最后一个（即结束）日期的日期。
unit 要返回的信息类型：Unit  返回结果Y一段时期内的整年数。
M   一段时期内的整月数。
D一段时期内的天数。
MD start_date 与 end_date 之间天数之差。
 忽略日期中的月份和年份。
 “YM”  start_date 与 end_date 之间月份之差。
 忽略日期中的天和年份YD   start_date 与 end_date 的日期部分之差。
 忽略日期中的年份。

```
## DATEVALUE
> DATEVALUE 函数将存储为文本的日期转换为 Excel 识别为日期的序列号。
 例如，公式=DATEVALUE(1/1/2008)
 返回 39448，即日期 2008-1-1 的序列号。
 即使如此，请注意，计算机的系统日期设置可能会导致 DATEVALUE 函数的结果会与此示例不同。
如果工作表包含采用文本格式的日期并且要对这些日期进行筛选、排序、设置日期格式或执行日期计算，则 DATEVALUE 函数将十分有用。
要将序列号显示为日期，您必须对单元格应用日期格式。
 请在“另请参阅”部分中查找指向有关将数字显示为日期的详细信息的链接。

```
DATEVALUE(date_text)
date_text必需。
代表采用 Excel 日期格式的日期的文本，或是对包含这种文本的单元格的引用。
例如，用于表示日期的引号内的文本字符串 2008-1-30 或 30-Jan-2008。

```
## DAVERAGE
> 对列表或数据库中满足指定条件的记录字段（列）中的数值求平均值。

```
DAVERAGE(database, field, criteria)
database必需。
构成列表或数据库的单元格区域。
 数据库是包含一组相关数据的列表，其中包含相关信息的行为记录，而包含数据的列为字段。
 列表的第一行包含每一列的标签。
field 必需。
指定函数所使用的列。
 输入两端带双引号的列标签，如 使用年数 或 产量；或是代表列表中列位置的数字（不带引号）：1 表示第一列，2 表示第二列，依此类推。
criteria 必需。
为包含指定条件的单元格区域。
 可以为参数指定 criteria 任意区域，只要此区域包含至少一个列标签，并且列标签下至少有一个在其中为列指定条件的单元格。

```
## DAY
> 返回以序列数表示的某日期的天数。
 天数是介于 1 到 31 之间的整数。

```
DAY(serial_number)
serial_number必需。
要查找的日期。
应使用 DATE 函数输入日期，或将日期作为其他公式或函数的结果输入。
例如，使用函数 DATE(2008,5,23)
 输入 2008 年 5 月 23 日。
如果日期以文本形式输入，则会出现问题。

```
## DAYS
> 返回两个日期之间的天数
```
DAYS(end_date, start_date)
end_date必需。
 Start_date 和 End_date 是用于计算期间天数的起止日期。
start_date   必需。
Start_date 和 End_date 是用于计算期间天数的起止日期。

```
## DAYS360
> 按照一年 360 天的算法（每个月以 30 天计，一年共计 12 个月），DAYS360 函数返回两个日期间相差的天数，这在一些会计计算中将会用到。
 如果财会系统是基于一年 12 个月，每月 30 天，可使用此函数帮助计算支付款项。

```
DAYS360(start_date,end_date,[method])
start_date、end_date必需。
 用于计算期间天数的起止日期。
 如果 start_date 在 end_date 之后，则 DAYS360 函数将返回一个负数。
 应使用 DATE 函数输入日期，或者将从其他公式或函数派生日期。
 例如，使用函数 DATE(2008,5,23)
 以返回 2008 年 5 月 23 日。
 如果日期以文本形式输入，则会出现问题。
method可选。
 逻辑值，用于指定在计算中是采用美国方法 还是欧洲方法。
method   定义FALSE 或省略美国 (NASD)
 方法。
 如果起始日期是一个月的最后一天，则等于同月的 30 号。
如果终止日期是一个月的最后一天，并且起始日期早于 30 号，则终止日期等于下一个月的 1 号，否则，终止日期等于本月的 30 号。
TRUE   欧洲方法。
 如果起始日期和终止日期为某月的 31 号，则等于当月的 30 号。

```
## DB
> 使用固定余额递减法，计算一笔资产在给定期间内的折旧值。

```
DB(cost, salvage, life, period, [month])
cost必需。
 资产原值。
salvage必需。
 折旧末尾时的值（有时也称为资产残值）。
life必需。
 资产的折旧期数（有时也称作资产的使用寿命）。
period必需。
 您要计算折旧的时期。
 Period 必须使用与 life 相同的单位。
month可选。
 第一年的月份数。
 如果省略月份，则假定其值为 12。

```
## DBCS 
> 将字符串中的半角（单字节）英文字母或片假名更改为全角（双字节）字符
```
DBCS(text)
text必需。
文本或包含要转换的文本的单元格的引用。
如果文本中不包含任何半角英文字母或片假名，则不会对文本进行转换。

```
## DCOUNT
> 返回列表或数据库中满足指定条件的记录字段（列）中包含数字的单元格的个数。
字段参数为可选项。
 如果省略字段，DCOUNT 计算数据库中符合条件的所有记录数。

```
DCOUNT(database, field, criteria)
database必需。
 构成列表或数据库的单元格区域。
 数据库是包含一组相关数据的列表，其中包含相关信息的行为记录，而包含数据的列为字段。
 列表的第一行包含每一列的标签。
field 必需。
 指定函数所使用的列。
 输入两端带双引号的列标签，如 使用年数 或 产量；或是代表列表中列位置的数字（不带引号）：1 表示第一列，2 表示第二列，依此类推。
criteria必需。
 包含所指定条件的单元格区域。
 可以为参数 criteria 指定任意区域，只要此参数包含至少一个列标签，并且列标签下至少有一个在其中为列指定条件的单元格。

```
## DCOUNTA
> 返回列表或数据库中满足指定条件的记录字段（列）中的非空单元格的个数。
字段参数为可选项。
 如果省略字段，DCOUNTA 计算数据库中符合条件的所有记录数。

```
DCOUNTA(database, field, criteria)
database必需。
 构成列表或数据库的单元格区域。
 数据库是包含一组相关数据的列表，其中包含相关信息的行为记录，而包含数据的列为字段。
 列表的第一行包含每一列的标签。
field可选。
 指定函数所使用的列。
 输入两端带双引号的列标签，如 使用年数 或 产量；或是代表列表中列位置的数字（不带引号）：1 表示第一列，2 表示第二列，依此类推。
criteria必需。
 包含所指定条件的单元格区域。
 可以为参数 criteria 指定任意区域，只要此区域包含至少一个列标签，并且列标签下至少有一个在其中为列指定条件的单元格。

```
## DDB
> 用双倍余额递减法或其他指定方法，返回指定期间内某项固定资产的折旧值。

```
DDB(cost, salvage, life, period, [factor])
cost必需。
 资产原值。
salvage必需。
 折旧末尾时的值（有时也称为资产残值）。
 该值可以是 0。
life必需。
 资产的折旧期数（有时也称作资产的使用寿命）。
period必需。
 您要计算折旧的时期。
 Period 必须使用与 life 相同的单位。
factor可选。
 余额递减速率 如果省略 factor，则假定其值为 2（双倍余额递减法）。

```
## DEC2BIN
> 将十进制数转换为二进制数。

```
DEC2BIN(number, [places])
number必需。
 要转换的十进制整数。
 如果数字为负数，则忽略有效的 place 值，且 DEC2BIN 返回 10 个字符的（10 位）二进制数，其中最高位为符号位。
 其余 9 位是数量位。
 负数由二进制补码记数法表示。
places可选。
 要使用的字符数。
 如果省略 places，则 DEC2BIN 使用必要的最小字符数。
 Places 可用于在返回的值前置 0（零）。

```
## DEC2HEX
> 将十进制数转换为十六进制数。

```
DEC2HEX(number, [places])
number必需。
 要转换的十进制整数。
 如果数字为负数，则忽略 places，且 DEC2HEX 返回 10 个字符的（40 位）十六进制数，其中最高位为符号位。
 其余 39 位是数量位。
 负数由二进制补码记数法表示。
places可选。
 要使用的字符数。
 如果省略 places，则 DEC2HEX 使用必要的最小字符数。
 Places 可用于在返回的值前置 0（零）。

```
## DEC2OCT
> 将十进制数转换为八进制数。

```
DEC2OCT(number, [places])
number必需。
 要转换的十进制整数。
 如果数字为负数，则忽略 places，且 DEC2OCT 返回 10 个字符的（30 位）八进制数，其中最高位为符号位。
 其余 29 位是数量位。
 负数由二进制补码记数法表示。
places可选。
 要使用的字符数。
 如果省略 places，则 DEC2OCT 使用必要的最小字符数。
 Places 可用于在返回的值前置 0（零）。

```
## DECIMAL 
> 按给定基数将数字的文本表示形式转换成十进制数。

```
DECIMAL(text, radix)
text必需。
radix必需。
radix 必须是整数。

```
## DEGREES
> 将弧度转换为度。

```
DEGREES(angle)
angle必需。
 要转换的角度，以弧度表示。

```
## DELTA
> 检验两个值是否相等。
 如果 number1=number2，则返回 1；否则返回 0。
 可以使用此函数来筛选一组值。
 例如，通过对几个 DELTA 函数进行求和，可计算相等对的数量。
 此函数也称为 Kronecker Delta 函数。

```
DELTA(number1, [number2])
number1必需。
 第一个数字。
number2可选。
 第二个数字。
 如果省略，则假设 Number2 值为零。

```
## DEVSQ
> 返回各数据点与数据均值点之差（数据偏差）的平方和。

```
DEVSQ(number1, [number2], ...)
number1, number2, ...number1 是必需的，后续数字是可选的。
 用于计算偏差平方和的 1 到 255 个参数。
 也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## DGET
> 从列表或数据库的列中提取符合指定条件的单个值。

```
DGET(database, field, criteria)
database必需。
 构成列表或数据库的单元格区域。
 数据库是包含一组相关数据的列表，其中包含相关信息的行为记录，而包含数据的列为字段。
 列表的第一行包含每一列的标签。
field 必需。
 指定函数所使用的列。
 输入两端带双引号的列标签，如 使用年数 或 产量；或是代表列表中列位置的数字（不带引号）：1 表示第一列，2 表示第二列，依此类推。
criteria 必需。
 包含所指定条件的单元格区域。
 可以为参数 criteria 指定任意区域，只要此区域包含至少一个列标签，并且列标签下至少有一个在其中为列指定条件的单元格。

```
## DISC
> 返回有价证券的贴现率。

```
DISC(settlement, maturity, pr, redemption, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
pr必需。
 有价证券的价格（按面值为 ￥100 计算）。
redemption必需。
 面值 ￥100 的有价证券的清偿价值。
basis可选。
 要使用的日计数基准类型。
basis 日计数基准0 或省略   US (NASD)
 30/3601实际/实际2实际/3603实际/3654欧洲 30/360
```
## DMAX
> 返回列表或数据库中满足指定条件的记录字段（列）中的最大数字。

```
DMAX(database, field, criteria)
database必需。
 构成列表或数据库的单元格区域。
 数据库是包含一组相关数据的列表，其中包含相关信息的行为记录，而包含数据的列为字段。
 列表的第一行包含每一列的标签。
field必需。
 指定函数所使用的列。
 输入两端带双引号的列标签，如 使用年数 或 产量；或是代表列表中列位置的数字（不带引号）：1 表示第一列，2 表示第二列，依此类推。
criteria必需。
 包含所指定条件的单元格区域。
 可以为参数 criteria 指定任意区域，只要此区域包含至少一个列标签，并且列标签下至少有一个在其中为列指定条件的单元格。

```
## DMIN
> 返回列表或数据库中满足指定条件的记录字段（列）中的最小数字。

```
DMIN(database, field, criteria)
database必需。
 构成列表或数据库的单元格区域。
 数据库是包含一组相关数据的列表，其中包含相关信息的行为记录，而包含数据的列为字段。
 列表的第一行包含每一列的标签。
field必需。
 指定函数所使用的列。
 输入两端带双引号的列标签，如 使用年数 或 产量；或是代表列表中列位置的数字（不带引号）：1 表示第一列，2 表示第二列，依此类推。
criteria必需。
 包含所指定条件的单元格区域。
 可以为参数 criteria 指定任意区域，只要此区域包含至少一个列标签，并且列标签下至少有一个在其中为列指定条件的单元格。

```
## DOLLAR
> 使用 ￥（人民币）货币格式将数字转换为文本
```
DOLLAR(number, [decimals])
number必需。
数字、对包含数字的单元格的引用或是计算结果为数字的公式。
decimals   可选。
数值小数点右边的位数。
如果这是负数，则将数字四舍五入到小数点左侧。
如果省略 decimals，则假设为 2。

```
## DOLLARDE
> 将以整数部分和分数部分表示的价格（例如 1.02）转换为以小数部分表示的价格。
 分数表示的金额数字有时可用于表示证券价格。
该值的分数部分除以一个指定的整数。
 例如，如果要以十六进制形式来表示价格，则将分数部分除以 16。
 在这种情况下，1.02 表示 $1.125 ($1 + 2/16 = $1.125)
。

```
DOLLARDE(fractional_dollar, fraction)
fractional_dollar必需。
 以整数部份和分数部分表示的数字，用小数点隔开。
fraction必需。
 用作分数中的分母的整数。

```
## DOLLARFR
> 使用 DOLLARFR 将小数转换为分数表示的金额数字，如证券价格。

```
DOLLARFR(decimal_dollar, fraction)
decimal_dollar必需。
 小数。
fraction必需。
 用作分数中的分母的整数。

```
## DPRODUCT
> 返回列表或数据库中满足指定条件的记录字段（列）中的数值的乘积。

```
DPRODUCT(database, field, criteria)
database必需。
 构成列表或数据库的单元格区域。
 数据库是包含一组相关数据的列表，其中包含相关信息的行为记录，而包含数据的列为字段。
 列表的第一行包含每一列的标签。
field 必需。
 指定函数所使用的列。
 输入两端带双引号的列标签，如 使用年数 或 产量；或是代表列表中列位置的数字（不带引号）：1 表示第一列，2 表示第二列，依此类推。
criteria必需。
 包含所指定条件的单元格区域。
 可以为参数 criteria 指定任意区域，只要此区域包含至少一个列标签，并且列标签下至少有一个在其中为列指定条件的单元格。

```
## DSTDEV
> 返回利用列表或数据库中满足指定条件的记录字段（列）中的数字作为一个样本估算出的总体标准偏差。

```
DSTDEV(database, field, criteria)
database必需。
 构成列表或数据库的单元格区域。
 数据库是包含一组相关数据的列表，其中包含相关信息的行为记录，而包含数据的列为字段。
 列表的第一行包含每一列的标签。
field 必需。
 指定函数所使用的列。
 输入两端带双引号的列标签，如 使用年数 或 产量；或是代表列表中列位置的数字（不带引号）：1 表示第一列，2 表示第二列，依此类推。
criteria 必需。
 包含所指定条件的单元格区域。
 可以为参数 criteria 指定任意区域，只要此区域包含至少一个列标签，并且列标签下至少有一个在其中为列指定条件的单元格。

```
## DSTDEVP
> 返回利用列表或数据库中满足指定条件的记录字段（列）中的数字作为样本总体计算出的总体标准偏差。

```
DSTDEVP(database, field, criteria)
database必需。
 构成列表或数据库的单元格区域。
 数据库是包含一组相关数据的列表，其中包含相关信息的行为记录，而包含数据的列为字段。
 列表的第一行包含每一列的标签。
field必需。
 指定函数所使用的列。
 输入两端带双引号的列标签，如 使用年数 或 产量；或是代表列表中列位置的数字（不带引号）：1 表示第一列，2 表示第二列，依此类推。
criteria必需。
 包含所指定条件的单元格区域。
 可以为参数 criteria 指定任意区域，只要此区域包含至少一个列标签，并且列标签下至少有一个在其中为列指定条件的单元格。

```
## DSUM
> 对列表或数据库中符合条件的记录的字段列中的数字求和
```
DSUM(database, field, criteria)
database必需。
 构成列表或数据库的单元格区域。
 数据库是包含一组相关数据的列表，其中包含相关信息的行为记录，而包含数据的列为字段。
 列表的第一行包含每一列的标签。
field必需。
 指定函数所使用的列。
 输入两端带双引号的列标签，如 使用年数 或 产量；或是代表列表中列位置的数字（不带引号）：1 表示第一列，2 表示第二列，依此类推。
criteria   必需。
 为包含指定条件的单元格区域。
 可以为参数指定 criteria 任意区域，只要此区域包含至少一个列标签，并且列标签下至少有一个在其中为列指定条件的单元格。

```
## DURATION
> 用于计量债券价格对于收益率变化的敏感程度。

```
DURATION(settlement, maturity, coupon, yld, frequency, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
coupon必需。
 有价证券的年息票利率。
yld必需。
 有价证券的年收益率。
frequency必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis   日计数基准0 或省略 US (NASD)
 30/3601  实际/实际2  实际/3603  实际/3654  欧洲 30/360
```
## DVAR
> 利用列表或数据库中满足指定条件的记录字段（列）中的数字作为一个样本估算出的总体方差。

```
DVAR(database, field, criteria)
database必需。
 构成列表或数据库的单元格区域。
 数据库是包含一组相关数据的列表，其中包含相关信息的行为记录，而包含数据的列为字段。
 列表的第一行包含每一列的标签。
field 必需。
 指定函数所使用的列。
 输入两端带双引号的列标签，如 使用年数 或 产量；或是代表列表中列位置的数字（不带引号）：1 表示第一列，2 表示第二列，依此类推。
criteria 必需。
 包含所指定条件的单元格区域。
 可以为参数 criteria 指定任意区域，只要此区域包含至少一个列标签，并且列标签下至少有一个在其中为列指定条件的单元格。

```
## DVARP
> 通过使用列表或数据库中满足指定条件的记录字段（列）中的数字计算样本总体的样本总体方差。

```
DVARP(database, field, criteria)
database必需。
 构成列表或数据库的单元格区域。
 数据库是包含一组相关数据的列表，其中包含相关信息的行为记录，而包含数据的列为字段。
 列表的第一行包含每一列的标签。
field 必需。
 指定函数所使用的列。
 输入两端带双引号的列标签，如 使用年数 或 产量；或是代表列表中列位置的数字（不带引号）：1 表示第一列，2 表示第二列，依此类推。
criteria必需。
 包含所指定条件的单元格区域。
 可以为参数 criteria 指定任意区域，只要此区域包含至少一个列标签，并且列标签下至少有一个在其中为列指定条件的单元格。

```
## EDATE
> 返回表示某个日期的序列号，该日期与指定日期 (start_date)
 相隔（之前或之后）指示的月份数。
 使用函数 EDATE 可以计算与发行日处于一月中同一天的到期日的日期。

```
EDATE(start_date, months)
start_date必需。
一个代表开始日期的日期。
应使用 DATE 函数输入日期，或将日期作为其他公式或函数的结果输入。
例如，使用函数 DATE(2008,5,23)
 输入 2008 年 5 月 23 日。
如果日期以文本形式输入，则会出现问题。
months 必需。
 start_date 之前或之后的月份数。
 months 为正值将生成未来日期；为负值将生成过去日期。

```
## EFFECT
> 利用给定的名义年利率和每年的复利期数，计算有效的年利率。

```
EFFECT(nominal_rate, npery)
nominal_rate必需。
 名义利率。
npery必需。
 每年的复利期数。

```
## ENCODEURL 
> 返回 URL 编码的字符串
```
ENCODEURL(text)
text要进行 URL 编码的字符串。

```
## EOMONTH
> 返回某个月份最后一天的序列号，该月份与 start_date 相隔（之后或之后）指示的月份数。
 使用函数 EOMONTH 可以计算正好在特定月份中最后一天到期的到期日。

```
EOMONTH(start_date, months)
start_date必需。
一个代表开始日期的日期。
应使用 DATE 函数输入日期，或将日期作为其他公式或函数的结果输入。
例如，使用函数 DATE(2008,5,23)
 输入 2008 年 5 月 23 日。
如果日期以文本形式输入，则会出现问题。
months必需。
 start_date 之前或之后的月份数。
 months 为正值将生成未来日期；为负值将生成过去日期。

```
## ERF
> 返回误差函数在上下限之间的积分。

```
ERF(lower_limit,[upper_limit])
lower_limit必需。
 ERF 函数的积分下限。
upper_limit可选。
 ERF 函数的积分上限。
 如果省略，ERF 积分将在零到 lower_limit 之间。

```
## ERF.PRECISE 
> 返回误差函数。

```
ERF.PRECISE(x)
x必需。
 ERF.PRECISE 函数的积分下限。

```
## ERFC
> 返回从 x 到无穷大积分的互补 ERF 函数。

```
ERFC(x)
x必需。
 ERFC 函数的积分下限。

```
## ERFC.PRECISE 
> 返回从 x 到无穷大积分的互补 ERF 函数。

```
ERFC.PRECISE(x)
x必需。
ERFC.PRECISE 函数的积分下限。

```
## ERROR.TYPE
> 返回对应于 Microsoft Excel 中的错误值之一的数字或返回“#N/A”错误（如果不存在错误）。
 您可以使用 IF 函数中的 ERROR.TYPE 测试错误值并返回一个文本字符串（例如消息）而非错误值。

```
ERROR.TYPE(error_val)
error_val必需。
 要查找其标识号的错误值。
 尽管 error_val 可作为实际的错误值，但它通常是对包含要测试的公式的单元格的引用。
error_val   函数 ERROR.TYPE 返回#NULL! 1#DIV/0! 2#VALUE!   3#REF!4#NAME?   5#NUM! 6#N/A 7#GETTING_DATA 8其他值   #N/A
```
## EUROCONVERT
> 用于将数字转换为欧元形式，将数字由欧元形式转换为欧元成员国货币形式，或利用欧元作为中间货币将数字由某一欧元成员国货币转化为另一欧元成员国货币形式（三角转换关系）
```
EUROCONVERT(number,source,target,full_precision,triangulation_precision)
number必需。
 要转换的货币值，或对包含该值的单元格的引用。
source  必需。
 由三个字母组成的字符串，或对包含该字符串的单元格的引用，对应于源货币的 ISO 代码。
 
```
## EVEN
> 返回数字向上舍入到的最接近的偶数。
 您可以使用此函数来处理成对出现的项目。
 例如，一个包装箱一行可以装一宗或两宗货物。
 将这些货物的数目向上舍入到最接近的偶数，只有当该值与包装箱的容量一致时，包装箱才会装满。

```
EVEN(number)
number必需。
 要舍入的值。

```
## EXACT
> 检查两个文本值是否相同
```
EXACT(text1, text2)
text1必需。
 第一个文本字符串。
text2必需。
 第二个文本字符串。

```
## EXP
> 返回 e 的 n 次幂。
 常数 e 等于 2.71828182845904，是自然对数的底数。

```
Exp( number )
number必需。
 底数 e 的指数。

```
## EXPON.DIST 
> 返回指数分布。
 使用 EXPON.DIST 可以建立事件之间的时间间隔模型，如银行自动提款机支付一次现金所花费的时间。
 例如，可通过 EXPON.DIST 来确定这一过程最长持续一分钟的发生概率。

```
EXPON.DIST(x,lambda,cumulative)
x必需。
 函数值。
lambda必需。
 参数值。
cumulative必需。
 逻辑值，用于指定指数函数的形式。
 如果 cumulative 为 TRUE，则 EXPON.DIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。

```
## EXPONDIST
> 返回指数分布。
 使用 EXPONDIST 可以建立事件之间的时间间隔模型，如银行自动提款机支付一次现金所花费的时间。
 例如，可通过 EXPONDIST 来确定这一过程最长持续一分钟的发生概率。

```
EXPONDIST(x,lambda,cumulative)
x必需。
 函数值。
lambda必需。
 参数值。
cumulative必需。
 逻辑值，用于指定指数函数的形式。
 如果 cumulative 为 TRUE，则 EXPONDIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。

```
## F.DIST 
> 返回 F 概率分布。
此函数用于确定两个数据集是否具有不同程度。
例如，您可以检查测试分数的男士和女士输入高中，并确定是否不同于男生女性的变化。

```
F.DIST(x,deg_freedom1,deg_freedom2,cumulative)
x必需。
 用来计算函数的值。
deg_freedom1必需。
 分子自由度。
deg_freedom2必需。
 分母自由度。
cumulative必需。
 决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 F.DIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。

```
## F.DIST.RT 
> 返回两个数据集的（右尾）F 概率分布（变化程度）。
 使用此函数可以确定两组数据是否存在变化程度上的不同。
 例如，分析进入中学的男生、女生的考试分数，来确定女生分数的变化程度是否与男生不同。

```
F.DIST.RT(x,deg_freedom1,deg_freedom2)
x必需。
 用来计算函数的值。
deg_freedom1必需。
 分子自由度。
deg_freedom2必需。
 分母自由度。

```
## F.INV 
> 返回 F 概率分布函数的反函数值。
如果 p = F.DIST(x,...)
，则 F.INV(p,...)
 = x。
 在 F 检验中，可以使用 F 分布比较两组数据中的变化程度。
 例如，可以分析美国和加拿大的收入分布，判断两个国家/地区是否有相似的收入变化程度。

```
F.INV(probability,deg_freedom1,deg_freedom2)
probability必需。
 F 累积分布的概率值。
deg_freedom1必需。
 分子自由度。
deg_freedom2必需。
 分母自由度。

```
## F.INV.RT 
> 返回（右尾）F 概率分布函数的反函数值。
如果 p = F.DIST.RT(x,...)
，则 F.INV.RT(p,...)
 = x。
 在 F 检验中，可以使用 F 分布比较两组数据中的变化程度。
 例如，可以分析美国和加拿大的收入分布，判断两个国家/地区是否有相似的收入变化程度。

```
F.INV.RT(probability,deg_freedom1,deg_freedom2)
probability必需。
 F 累积分布的概率值。
deg_freedom1必需。
 分子自由度。
deg_freedom2必需。
 分母自由度。

```
## F.TEST 
> 返回 F 检验的结果，即当 array1 和 array2 的方差无明显差异时的双尾概率。
使用此函数可确定两个示例是否有不同的方差。
 例如，给定公立和私立学校的测验分数，可以检验各学校间测验分数的差别程度。

```
F.TEST(array1,array2)
array1必需。
 第一个数组或数据区域。
array2必需。
 第二个数组或数据区域。

```
## FACT
> 返回数的阶乘。
 一个数的阶乘等于 1*2*3*...* 该数。

```
FACT(number)
number必需。
 要计算其阶乘的非负数。
 如果 number 不是整数，将被截尾取整。

```
## FACTDOUBLE
> 返回数字的双倍阶乘。

```
FACTDOUBLE(number)
number必需。
 为其返回双倍阶乘的值。
 如果 number 不是整数，将被截尾取整。

```
## FDIST
> 返回两个数据集的（右尾）F 概率分布（变化程度）。
 使用此函数可以确定两组数据是否存在变化程度上的不同。
 例如，分析进入中学的男生、女生的考试分数，来确定女生分数的变化程度是否与男生不同。

```
FDIST(x,deg_freedom1,deg_freedom2)
x必需。
 用来计算函数的值。
deg_freedom1必需。
 分子自由度。
deg_freedom2必需。
 分母自由度。

```
## FILTER
> FILTER函数允许您筛选出根据您定义的条件的数据区域。

```

```
## FILTERXML 
> 通过使用指定的 XPath，返回 XML 内容中的特定数据
```
FILTERXML(xml, xpath)
xml必需。
有效 XML 格式中的字符串。
xpath   必填。
标准 XPath 格式字符串。

```
## FIND
> 在一个文本值中查找另一个文本值（区分大小写）
```
FIND(find_text, within_text, [start_num])
find_text必需。
 要查找的文本。
within_text必需。
 包含要查找文本的文本。
start_num可选。
 指定开始进行查找的字符。
 within_text 中的首字符是编号为 1 的字符。
 如果省略 start_num，则假定其值为 1。

```
## FINDB
> 在一个文本值中查找另一个文本值（区分大小写）
```
FINDB(find_text, within_text, [start_num])
find_text必需。
 要查找的文本。
within_text必需。
 包含要查找文本的文本。
start_num可选。
 指定开始进行查找的字符。
 within_text 中的首字符是编号为 1 的字符。
 如果省略 start_num，则假定其值为 1。

```
## FINV
> 返回（右尾）F 概率分布函数的反函数值。
 如果 p = FDIST(x,...)
，则 FINV(p,...)
 = x。
在 F 检验中，可以使用 F 分布比较两组数据中的变化程度。
 例如，可以分析美国和加拿大的收入分布，判断两个国家/地区是否有相似的收入变化程度。

```
FINV(probability,deg_freedom1,deg_freedom2)
probability  必需。
 F 累积分布的概率值。
deg_freedom1   必需。
 分子自由度。
deg_freedom2必需。
 分母自由度。

```
## FISHER
> 返回 x 的 Fisher 变换值。
 该变换生成一个正态分布而非偏斜的函数。
 使用此函数可以完成相关系数的假设检验。

```
FISHER(x)
x必需。
 要对其进行变换的数值。

```
## FISHERINV
> 返回 Fisher 逆变换值。
 使用该变换可以分析数据区域或数组之间的相关性。
 如果 y = FISHER(x)
，则 FISHERINV(y)
 = x。

```
FISHERINV(y)
y必需。
 要对其进行逆变换的数值。

```
## FIXED
> 将数字格式设置为具有固定小数位数的文本
```
FIXED(number, [decimals], [no_commas])
number必需。
 要进行舍入并转换为文本的数字。
decimals可选。
 小数点右边的位数。
no_commas可选。
 一个逻辑值，如果为 TRUE，则会禁止 FIXED 在返回的文本中包含逗号。

```
## FLOOR
> 将参数 number 向下舍入（沿绝对值减小的方向）为最接近的 significance 的倍数。

```
FLOOR(number, significance)
number必需。
 要舍入的数值。
significance必需。
 要舍入到的倍数。

```
## FLOOR.MATH 
> 将数字向下舍入为最接近的整数或最接近的指定基数的倍数。

```
FLOOR.MATH(number, significance, mode)
number必需。
 要向下舍入的数字。
significance可选。
 要舍入到的倍数。
mode可选。
 舍入负数的方向（接近或远离 0）。

```
## FLOOR.PRECISE
> 返回一个数字，该数字向下舍入为最接近的整数或最接近的 significance 的倍数。
 无论该数字的符号如何，该数字都向下舍入。
 但是，如果该数字或有效位为 0，则返回 0。

```
FLOOR.PRECISE(number, [significance])
number必需。
要进行舍入的值。
significance可选。
 要将数字舍入的倍数。
如果省略 significance，则其默认值为 1。

```
## FORECAST
> 根据现有值计算或预测未来值。
 预测值为给定 x 值后求得的 y 值。
 已知值为现有的 x 值和 y 值，并通过线性回归来预测新值。
 可以使用该函数来预测未来销售、库存需求或消费趋势等。

```
FORECAST(x, known_y's, known_x's)
x必需。
 需要进行值预测的数据点。
known_y's必需。
 相关数组或数据区域。
known_x's必需。
 独立数组或数据区域。

```
## FORECAST.ETS 
> 通过使用指数平滑 (ETS)
 算法的 AAA 版本，返回基于现有（历史）值的未来值
```
FORECAST.ets ( target_date ,value,timeline,[seasonality ],[data_completion],[summary])
target_date必需。
要为其预测值的数据点。
目标日期可以是日期/时间或数值。
 如果目标日期按时间前后排列处于历史时间线结束之前，则 FORECAST.ETS 将返回 #NUM! 错误。
value必需。
 值是历史值，您要为其预测下一点。
timeline必需。
独立数组或数值数据区域。
时间线中的日期之间必须有一致步长且不能为零。
 无需对时间线进行排序，因为 FORECAST.ETS 会对其进行隐式排序，以进行计算。
 如果无法在提供的时间线中识别一致步长，则 Forecast.ETS 将返回 #NUM! 错误。
 如果时间线包含重复值，则 Forecast.ETS 将返回 #VALUE! 错误。
 如果时间线和值的范围大小不同，则 Forecast.ETS 将返回 #N/A 错误。
seasonlity可选。
一个数值。
 默认值为 1，意味着 Excel 自动检测季节性进行预测，并使用正整数作为季节性模式的长度。
 0 表示无季节性，意味着预测为线性预测。
 正整数指示算法使用此长度模式作为季节性。
 对于其他任何值，FORECAST.ETS 将返回 #NUM! 错误。
最大支持 seasonality 是8,760（一年中的小时数）。
 该数字上方的任何 seasonality 将导致# NUM ! 错误。
date_completion可选。
虽然时间线需要数据点之间的一致步长，但 FORECAST.ETS 支持最多 30% 的丢失数据，并会自动对其进行调整。
 0 表示算法将缺少的点视为零。
 通过将缺少的点算为邻接点的平均值，默认值 1 将计算缺少的点。
summary可选。
虽然时间线需要数据点之间的一致步长，但 FORECAST.ETS 会聚合具有相同时间戳的多个点。
聚合参数是一个数值，指明要用于聚合具有相同时间戳的多个值的方法。
默认值 0 将使用 AVERAGE，而其他选项为 SUM、COUNT、COUNTA、MIN、MAX、MEDIAN。

```
## FORECAST.ETS.CONFINT 
> 返回指定目标日期预测值的置信区间
```
FORECAST.ETS.CONFINT ( target_date ,value,timeline,[ confidence_level ][ seasonality ],[ data_completion ],[summary])
FORECAST.ETS.CONFINT 函数语法具有以下参数：target_date必需。
要为其预测值的数据点。
目标日期可以是日期/时间或数字。
 如果目标日期在历史时间线结束前按时间顺序排序，则 FORECAST.ETS.CONFINT 将返回 #NUM! 错误。
value必需。
 值是历史值，您要为其预测下一点。
timeline必需。
独立数组或数值数据区域。
时间线中的日期之间必须有一致步长且不能为零。
 无需对时间线进行排序，因为 FORECAST.ETS.CONFINT 会对其进行隐式排序，以进行计算。
 如果无法在提供的时间线中识别一致步长，则 FORECAST.ETS.CONFINT 将返回 #NUM! 错误。
 如果时间线包含重复值，则 FORECAST.ETS.CONFINT 将返回 #VALUE! 错误。
 如果时间线和值的范围大小不同，则 FORECAST.ETS.CONFINT 将返回 #N/A 错误。
confidence_level   可选。
0 和 1 之间的一个数值（独占），指示计算置信区间的置信度。
 例如，对于 90% 的置信区间，将计算 90% 置信度（90% 的未来点将处于此预测范围内）。
 默认值为 95%。
 对于 (0,1)
 范围外的数值，FORECAST.ETS.CONFINT 将返回 #NUM! 错误。
seasonality可选。
一个数值。
 默认值为 1，意味着 Excel 自动检测季节性进行预测，并使用正整数作为季节性模式的长度。
 0 表示无季节性，意味着预测为线性预测。
 正整数指示算法使用此长度模式作为季节性。
 对于其他任何值，FORECAST.ETS.CONFINT 将返回 #NUM! 错误。
最大支持 seasonality 是8,760（一年中的小时数）。
 该数字上方的任何 seasonality 将导致# NUM ! 错误。
data_completion可选。
虽然时间线需要数据点之间的一致步长，但 FORECAST.ETS.CONFINT 支持最多 30% 的丢失数据，并会自动对其进行调整。
 0 表示算法将缺少的点视为零。
 通过将缺少的点算为邻接点的平均值，默认值 1 将计算缺少的点。
summary可选。
虽然时间线需要数据点之间的一致步长，但 FORECAST.ETS.CONFINT 会聚合具有相同时间戳的多个点。
聚合参数是一个数值，指明要用于聚合具有相同时间戳的多个值的方法。
默认值 0 将使用 AVERAGE，而其他选项为 SUM、COUNT、COUNTA、MIN、MAX、MEDIAN。

```
## FORECAST.ETS.SEASONALITY 
> 返回 Excel 针对指定时间系列检测到的重复模式的长度
```
FORECAST.ETS.SEASONALITY(value, timeline,[data_completion], [summary])
value必需。
 值是历史值，您要为其预测下一点。
timeline必需。
独立数组或数值数据区域。
时间线中的日期之间必须有一致步长且不能为零。
 无需对时间线进行排序，因为 FORECAST.ETS.SEASONALITY 会对其进行隐式排序，以进行计算。
 如果无法在提供的时间线中识别一致步长，则 FORECAST.ETS.SEASONALITY 将返回 #NUM! 错误。
 如果时间线包含重复值，则 FORECAST.ETS.SEASONALITY 将返回 #VALUE! 错误。
 如果时间线和值的范围大小不同，则 FORECAST.ETS.SEASONALITY 将返回 #N/A 错误。
data_completion可选。
虽然时间线需要数据点之间的一致步长，但 FORECAST.ETS.SEASONALITY 支持最多 30% 的丢失数据，并会自动对其进行调整。
 0 表示算法将缺少的点视为零。
 通过将缺少的点算为邻接点的平均值，默认值 1 将计算缺少的点。
summary可选。
虽然时间线需要数据点之间的一致步长，但 FORECAST.ETS.SEASONALITY 会聚合具有相同时间戳的多个点。
聚合参数是一个数值，指明要用于聚合具有相同时间戳的多个值的方法。
默认值 0 将使用 AVERAGE，而其他选项为 SUM、COUNT、COUNTA、MIN、MAX、MEDIAN。

```
## FORECAST.ETS.STAT 
> 返回作为时间序列预测的结果的统计值。

```
FORECAST.ETS.STAT(value, timeline, statistic_type, [seasonality], [data_completion], [summary])
value必需。
 值是历史值，您要为其预测下一点。
timeline必需。
独立数组或数值数据区域。
时间线中的日期之间必须有一致步长且不能为零。
 无需对时间线进行排序，因为 FORECAST.ETS.STAT 会对其进行隐式排序，以进行计算。
 如果无法在提供的时间线中识别一致步长，则 FORECAST.ETS.STAT 将返回 #NUM! 错误。
 如果时间线包含重复值，则 FORECAST.ETS.STAT 将返回 #VALUE! 错误。
 如果时间线和值的范围大小不同，则 FORECAST.ETS.STAT 将返回 #N/A 错误。
statistic_type必需。
 数字值介于1和8之间，指示哪些统计值将不会为计算预测返回。
seasonality 可选。
一个数值。
 默认值为 1，意味着 Excel 自动检测季节性进行预测，并使用正整数作为季节性模式的长度。
 0 表示无季节性，意味着预测为线性预测。
 正整数指示算法使用此长度模式作为季节性。
 对于其他任何值，FORECAST.ETS.STAT 将返回 #NUM! 错误。
最大支持 seasonality 是8,760（一年中的小时数）。
 该数字上方的任何 seasonality 将导致# NUM ! 错误。
data_completion可选。
虽然时间线需要数据点之间的一致步长，但 FORECAST.ETS.STAT 支持最多 30% 的丢失数据，并会自动对其进行调整。
 0 表示算法将缺少的点视为零。
 通过将缺少的点算为邻接点的平均值，默认值 1 将计算缺少的点。
summary可选。
虽然时间线需要数据点之间的一致步长，但 FORECAST.ETS.STAT 会聚合具有相同时间戳的多个点。
聚合参数是一个数值，指明要用于聚合具有相同时间戳的多个值的方法。
默认值 0 将使用 AVERAGE，而其他选项为 SUM、COUNT、COUNTA、MIN、MAX、MEDIAN。

```
## FORECAST.LINEAR 
> 返回基于现有值的未来值
```
FORECAST.LINEAR( x , known _ y ' s , known _ x ' s )
x   必需。
 需要进行值预测的数据点。
known_y's必需。
 相关数组或数据区域。
known_x's必需。
 独立数组或数据区域。

```
## FORMULATEXT 
> 以字符串的形式返回公式。

```
FORMULATEXT(reference)
reference必需。
对单元格或单元格区域的引用。

```
## FREQUENCY
> 以垂直数组的形式返回频率分布
```
FREQUENCY(data_array, bins_array)
FREQUENCY 函数语法具有下列参数：Data_array必需。
 要对其频率进行计数的一组数值或对这组数值的引用。
 如果 data_array 中不包含任何数值，则 FREQUENCY 返回一个零数组。
Bins_array必需。
 要将 data_array 中的值插入到的间隔数组或对间隔的引用。
 如果 bins_array 中不包含任何数值，则 FREQUENCY 返回 data_array 中的元素个数。

```
## FTEST
> 返回 F 检验的结果 F 检验返回当 array1 和 array2 的方差无明显差异时的双尾概率。
 使用此函数可确定两个示例是否有不同的方差。
 例如，给定公立和私立学校的测验分数，可以检验各学校间测验分数的差别程度。

```
FTEST(array1,array2)
array1必需。
 第一个数组或数据区域。
array2必需。
 第二个数组或数据区域。

```
## FV
> FV 是一个财务函数，用于根据固定利率计算投资的未来值。
 可以将 FV 与定期付款、固定付款或一次付清总额付款结合使用。

```
FV(rate,nper,pmt,[pv],[type])
rate必需。
 各期利率。
nper必需。
年金的付款总期数。
pmt必需。
 各期所应支付的金额，在整个年金期间保持不变。
 通常 pmt 包括本金和利息，但不包括其他费用或税款。
 如果省略 pmt，则必须包括 pv 参数。
pv可选。
 现值，或一系列未来付款的当前值的累积和。
 如果省略 pv，则假定其值为 0（零），并且必须包括 pmt 参数。
type可选。
 数字 0 或 1，用以指定各期的付款时间是在期初还是期末。
 如果省略 type，则假定其值为 0。
type  支付时间0期末1期初
```
## FVSCHEDULE
> 返回应用一系列复利率计算的初始本金的未来值。
 使用 FVSCHEDULE 通过变量或可调节利率计算某项投资未来的价值。

```
FVSCHEDULE(principal, schedule)
principal必需。
 现值。
schedule必需。
 要应用的利率数组。

```
## GAMMA 
> 返回 γ 函数值
```
GAMMA(number)
number必需。
 返回一个数字。

```
## GAMMA.DIST 
> 返回 γ 分布
```
GAMMA.DIST(x,alpha,beta,cumulative)
x   必需。
 用来计算分布的数值。
alpha必需。
 分布参数。
beta 必需。
 分布参数。
 如果 beta = 1，则 GAMMA.DIST 返回标准伽玛分布。
cumulative必需。
 决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 GAMMA.DIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。

```
## GAMMA.INV 
> 返回 γ 累积分布函数的反函数
```
GAMMA.INV(probability,alpha,beta)
probability必需。
 伽玛分布相关的概率。
alpha   必需。
 分布参数。
beta 必需。
分布参数。
如果 beta = 1，则 GAMMA.INV 返回标准伽玛分布。

```
## GAMMADIST
> 返回伽玛分布函数的函数值。
 可以使用此函数来研究呈斜分布的变量。
 伽玛分布通常用于排队分析。

```
GAMMADIST(x,alpha,beta,cumulative)
x必需。
 用来计算分布的数值。
alpha必需。
 分布参数。
beta  必需。
 分布参数。
 如果 beta = 1，则 GAMMADIST 返回标准伽玛分布。
cumulative   必需。
 决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 GAMMADIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。

```
## GAMMAINV
> 返回伽玛累积分布函数的反函数值。
 如果 p = GAMMADIST(x,...)
，则 GAMMAINV(p,...)
 = x。
 使用此函数可以研究有可能呈斜分布的变量。

```
GAMMAINV(probability,alpha,beta)
probability必需。
 伽玛分布相关的概率。
alpha   必需。
 分布参数。
beta必需。
 分布参数。
 如果 beta = 1，则 GAMMAINV 返回标准伽玛分布。

```
## GAMMALN
> 返回 γ 函数的自然对数，Γ(x)

```
GAMMALN(x)
x必需。
 要计算其 GAMMALN 的数值。

```
## GAMMALN.PRECISE 
> 返回 γ 函数的自然对数，Γ(x)

```
GAMMALN.PRECISE(x)
x必需。
 要计算其 GAMMALN.PRECISE 的数值。

```
## GAUSS 
> 返回小于标准正态累积分布 0.5 的值
```
GAUSS(z)
z必需。
返回一个数字。

```
## GCD
> 返回两个或多个整数的最大公约数。
 最大公约数是能够同时整除 number1 和 number2 而没有余数的最大整数。

```
GCD(number1, [number2], ...)
number1, number2, ...number1 是必需的，后续数字是可选的。
 介于 1 和 255 之间的值。
 如果任意值不是整数，将被截尾取整。

```
## GEOMEAN
> 返回几何平均值
```
GEOMEAN(number1, [number2], ...)
number1, number2, ...number1 是必需的，后续数字是可选的。
 用于计算平均值的 1 到 255 个参数。
 也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## GESTEP
> 如果 number>=step，则返回 1；否则返回 0（零）。
 可以使用此函数来筛选一组值。
 例如，通过对几个 GESTEP 函数进行求和，可计算超过阈值的值的计数。

```
GESTEP(number, [step])
number必需。
 要针对步骤进行测试的值。
Step  可选。
 阈值。
 如果省略 step 值，则 GESTEP 使用零。

```
## GETPIVOTDATA
> 返回存储在数据透视表中的数据。
您可以使用 GETPIVOTDATA 检索汇总数据从数据透视表，前提是在报表中可见的汇总数据。

```
GETPIVOTDATA(data_field, pivot_table, [field1, item1, field2, item2], ...)
data_field必需。
 包含要检索的数据的数据字段的名称，用引号引起来。
pivot_table   必填。
对任何单元格、 单元格区域或命名的区域的数据透视表中的单元格的引用。
此信息用于确定哪些数据透视表包含您要检索的数据。
field1、 item1、 field2、 item2   可选。
1 到 126 对的字段名称和描述您要检索的数据的项名称。
对可按任何顺序排列。
字段名称和日期和数字以外的项目名称用引号。
OLAP 数据透视表项目可以包含维度的源名称以及该项目的源名称。

```
## GROWTH
> 返回指数趋势值
```
GROWTH(known_y's, [known_x's], [new_x's], [const])
known_y's必需。
 关系表达式 y = b*m^x 中已知的 y 值集合。
   如果数组 known_y's 在单独一列中，则 known_x's 的每一列被视为一个独立的变量。
   如果数组 known_y's 在单独一行中，则 known_x's 的每一行被视为一个独立的变量。
   如果 known_y's 中的任何数为零或为负数，则 GROWTH 返回。
 错误值 #NUM!。
known_x's可选。
 关系表达式 y=b*m^x 中已知的 x 值集合，为可选参数。
   数组 known_x's 可以包含一组或多组变量。
 如果仅使用一个变量，那么只要 known_x's 和 known_y's 具有相同的维数，则它们可以是任何形状的区域。
 如果用到多个变量，则 known_y's 必须为向量（即必须为一行或一列）。
如果省略 known_x's，则假设该数组为 {1,2,3,...}，其大小与 known_y's 相同。
new_x's可选。
 需要 GROWTH 返回对应 y 值的新 x 值。
new_x's 与 known_x's 一样，对每个自变量必须包括单独的一列（或一行）。
 因此，如果 known_y's 是单列的，known_x's 和 new_x's 应该有同样的列数。
 如果 known_y's 是单行的，known_x's 和 new_x's 应该有同样的行数。
如果省略 new_x's，则假设它和 known_x's 相同。
如果 known_x's 与 new_x's 都被省略，则假设它们为数组 {1,2,3,...}，其大小与 known_y's 相同。
const可选。
 一个逻辑值，用于指定是否将常量 b 强制设为 1。
  如果 const 为 TRUE 或省略，b 将按正常计算。
  如果 const 为 FALSE，b 将设为 1，m 值将被调整以满足 y = m^x。

```
## HARMEAN
> 返回调和平均值
```
HARMEAN(number1, [number2], ...)
number1, number2, ...Number1 是必需的，后续数字是可选的。
 用于计算平均值的 1 到 255 个参数。
 也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## HEX2BIN
> 将十六进制数转换为二进制数。

```
HEX2BIN(number, [places])
number必需。
 要转换的十六进制数。
 Number 不能包含超过 10 个字符。
 number 的最高位为符号位（从右侧起第 40 位）。
 其余 9 位是数量位。
 负数由二进制补码记数法表示。
places可选。
 要使用的字符数。
 如果省略 places，则 HEX2BIN 使用必要的最小字符数。
 Places 可用于在返回的值前置 0（零）。

```
## HEX2DEC
> 将十六进制数转换为十进制数。

```
HEX2DEC(number)
number必需。
 要转换的十六进制数。
 Number 不能包含超过 10 个字符（40 位）。
 Number 的最高位为符号位。
 其余 39 位是数量位。
 负数由二进制补码记数法表示。

```
## HEX2OCT
> 将十六进制数转换为八进制数。

```
HEX2OCT(number, [places])
number必需。
 要转换的十六进制数。
 Number 不能包含超过 10 个字符。
 Number 的最高位为符号位。
 其余 39 位是数量位。
 负数由二进制补码记数法表示。
places可选。
 要使用的字符数。
 如果省略 places，则 HEX2OCT 使用必要的最小字符数。
 Places 可用于在返回的值前置 0（零）。

```
## HLOOKUP
> 在表格的首行或数值数组中搜索值，然后返回表格或数组中指定行的所在列中的值。
 当比较值位于数据表格的首行时，如果要向下查看指定的行数，则可使用 HLOOKUP。
 当比较值位于所需查找的数据的左边一列时，则可使用 VLOOKUP。
HLOOKUP 中的 H 代表“行”。

```
HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])
lookup_value必需。
 要在表格的第一行中查找的值。
 Lookup_value 可以是数值、引用或文本字符串。
table_array必需。
 在其中查找数据的信息表。
 使用对区域或区域名称的引用。
table_array 的第一行的数值可以为文本、数字或逻辑值。
如果 range_lookup 为 TRUE，则 table_array 的第一行的数值必须按升序排列：...-2、-1、0、1、2、...、A-Z、FALSE、TRUE；否则，HLOOKUP 将不能给出正确的数值。
 如果 range_lookup 为 FALSE，则 table_array 不必进行排序。
   文本不区分大小写。
row_index_num必需。
 table_array 中将返回的匹配值的行号。
 row_index_num 为 1 时，返回 table_array 的第一行的值；row_index_num 为 2 时，返回 table_array 第二行中的值，依此类推。
 如果 row_index_num 小于 1，则 HLOOKUP 返回 错误值 #VALUE!；如果 row_index_num 大于 table_array 的行数，则 HLOOKUP 返回 错误值 #REF!。
range_lookup可选。
 一个逻辑值，指定希望 HLOOKUP 查找精确匹配值还是近似匹配值。
 如果为 TRUE 或省略，则返回近似匹配值。
 换言之，如果找不到精确匹配值，则返回小于 lookup_value 的最大值。
 如果为 False，则 HLOOKUP 将查找精确匹配值。
 如果找不到精确匹配值，则返回错误值 #N/A。

```
## HOUR
> 将序列号转换为小时
```
HOUR(serial_number)
serial_number必需。
 时间值，其中包含要查找的小时数。
 时间值有多种输入方式：带引号的文本字符串（例如 6:45 PM）、十进制数（例如 0.78125 表示 6:45 PM）或其他公式或函数的结果（例如 TIMEVALUE(6:45 PM)
）。

```
## HYPERLINK
> HYPERLINK函数创建跳转到当前工作簿中的其他位置或以打开存储在网络服务器、 intranet或 Internet 上的文档的快捷方式。
单击包含超链接函数的单元格时，Excel 将跳转到的位置列出，或打开您指定的文档。

```
HYPERLINK(link_location，[friendly_name])
link_location必需。
可以作为文本打开的文档的路径和文件名。
Link_location 可以指向文档中的某个更为具体的位置，如 Excel 工作表或工作簿中特定的单元格或命名区域，或是指向 Microsoft Word 文档中的书签。
路径可以表示存储在硬盘驱动器上的文件，或是服务器上的通用命名约定 (UNC)
 路径（在 Excel 中），或是在 Internet 或 Intranet 上的统一资源定位器 (URL)
 路径。
friendly_name可选。
单元格中显示的跳转文本或数字值。
Friendly_name 显示为蓝色并带有下划线。
如果省略 friendly_name，单元格会将 link_location 显示为跳转文本。
Friendly_name 可以为数值、文本字符串、名称或包含跳转文本或数值的单元格。
如果 friendly_name 返回错误值（例如，#VALUE!），单元格将显示错误值以替代跳转文本。

```
## HYPGEOM.DIST
> 返回超几何分布
```
HYPGEOM.DIST(sample_s,number_sample,population_s,number_pop,cumulative)
sample_s必需。
 样本中成功的次数。
number_sample必需。
 样本量。
population_s  必需。
 总体中成功的次数。
number_pop  必需。
 总体大小。
cumulative  必需。
 决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 HYPGEOM.DIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。

```
## HYPGEOMDIST
> 返回超几何分布。
 如果已知样本量、总体成功次数和总体大小，则 HYPGEOMDIST 返回样本取得已知成功次数的概率。
 HYPGEOMDIST 用于处理以下的有限总体问题，在该有限总体中，每次观察结果或为成功或为失败，并且已知样本量的每个子集的选取是等可能的。

```
HYPGEOMDIST(sample_s,number_sample,population_s,number_pop)
sample_s   必需。
 样本中成功的次数。
number_sample   必需。
 样本量。
population_s 必需。
 总体中成功的次数。
number_pop  必需。
 总体大小。

```
## IF
> IF 函数是 Excel 中最常用的函数之一, 它允许你在值和预期结果之间进行逻辑比较。
因此 IF 语句可能有两个结果。
第一个结果是比较结果为 True，第二个结果是比较结果为 False。
例如，=IF(C2=”Yes”,1,2)
 表示 IF(C2 = Yes, 则返回 1, 否则返回 2)
。

```

```
## IFERROR
> 如果公式的计算结果错误，则返回您指定的值；否则返回公式的结果。
 使用 IFERROR 函数可捕获和处理公式中的错误。

```
IFERROR(value, value_if_error)
value必需。
 检查是否存在错误的参数。
value_if_error必需。
 公式的计算结果错误时返回的值。
 计算以下错误类型：#N/A、#VALUE!、#REF!、#DIV/0!、#NUM!、 #NAME? 或 #NULL!。

```
## IFNA 
> 如果公式返回错误值 #N/A，则结果返回您指定的值；否则返回公式的结果。

```
IFNA(value, value_if_na)
value必需。
 用于检查错误值 #N/A 的参数。
value_if_na必需。
 公式计算结果为错误值 #N/A 时要返回的值。

```
## IFS 
> IFS 函数检查是否满足一个或多个条件, 并返回与第一个 TRUE 条件对应的值。
IFS 可以替换多个嵌套的 IF 语句, 并且更易于在多个条件下读取。

```
IFS(logical_test1, value_if_true1, [logical_test2, value_if_true2], [logical_test3, value_if_true3],…)
logical_test1  必需。
计算结果为 TRUE 或 FALSE 的条件。
value_if_true1必需。
 当 logical_test1 的计算结果为 TRUE 时要返回结果。
可以为空。
logical_test2…logical_test127 可选。
计算结果为 TRUE 或 FALSE 的条件。
value_if_true2…value_if_true127 可选。
 当 logical_testN 的计算结果为 TRUE 时要返回结果。
每个 value_if_trueN 对应于一个条件 logical_testN。
可以为空。

```
## IMABS
> 返回以 x+yi 或 x+yj 文本格式表示的复数的绝对值（模）。

```
IMABS(inumber)
inumber必需。
 需要计算其绝对值的复数。

```
## IMAGINARY
> 返回以 x+yi 或 x+yj 文本格式表示的复数的虚系数。

```
IMAGINARY(inumber)
inumber必需。
 需要计算其虚系数的复数。

```
## IMARGUMENT
> 返回参数  Theta (theta)
，即以弧度表示的角。

```
IMARGUMENT(inumber)
inumber必需。
需要计算其参数  Theta 的复数。

```
## IMCONJUGATE
> 返回以 x+yi 或 x+yj 文本格式表示的复数的共轭复数。

```
IMCONJUGATE(inumber)
inumber必需。
 需要计算其共轭数的复数。

```
## IMCOS
> 返回以 x+yi 或 x+yj 文本格式表示的复数的余弦。

```
IMCOS(inumber)
inumber必需。
 需要计算其余弦的复数。

```
## IMCOSH 
> 返回以 x+yi 或 x+yj 文本格式表示的复数的双曲余弦值。

```
IMCOSH(inumber)
inumber必需。
 需要计算其双曲余弦值的复数。

```
## IMCOT 
> 返回以 x+yi 或 x+yj 文本格式表示的复数的余切值。

```
IMCOT(inumber)
inumber必需。
 需要计算其余切值的复数。

```
## IMCSC 
> 返回以 x+yi 或 x+yj 文本格式表示的复数的余割值。

```
IMCSC(inumber)
inumber必需。
 需要计算其余割值的复数。

```
## IMCSCH 
> 返回以 x+yi 或 x+yj 文本格式表示的复数的双曲余割值。

```
IMCSCH(inumber)
inumber必需。
 需要计算其双曲余割值的复数。

```
## IMDIV
> 返回以 x+yi 或 x+yj 文本格式表示的两个复数的商。

```
IMDIV(inumber1, inumber2)
inumber1必需。
 复数分子或被除数。
inumber2必需。
 复数分母或除数。

```
## IMEXP
> 返回以 x+yi 或 x+yj 文本格式表示的复数的指数。

```
IMEXP(inumber)
inumber必需。
 需要计算其指数的复数。

```
## IMLN
> 返回以 x+yi 或 x+yj 文本格式表示的复数的自然对数。

```
IMLN(inumber)
inumber必需。
 需要计算其自然对数的复数。

```
## IMLOG10
> 返回以 x + yi 或 x + yj 文本格式表示的复数的常用对数（以 10 为底数）。

```
IMLOG10(inumber)
inumber必需。
 需要计算其常用对数的复数。

```
## IMLOG2
> 返回以 x+yi 或 x+yj 文本格式表示的复数的以 2 为底数的对数。

```
IMLOG2(inumber)
inumber必需。
 需要计算以 2 为底数的对数的复数。

```
## IMPOWER
> 返回以 x+yi 或 x+yj 文本格式表示的复数的 n 次幂。

```
IMPOWER(inumber, number)
inumber必需。
需要计算其幂值的复数。
number必需。
需要对复数应用的幂次。

```
## IMPRODUCT
> 返回以 x+yi 或 x+yj 文本格式表示的 1 至 255 个复数的乘积。

```
IMPRODUCT(inumber1, [inumber2], ...)
inumber1, [inumber2], …inumber1 是必需的，后续 inumber 不是必需的。
 1 到 255 个要相乘的复数。

```
## IMREAL
> 返回以 x+yi 或 x+yj 文本格式表示的复数的实系数。

```
IMREAL(inumber)
inumber必需。
 需要计算其实系数的复数。

```
## IMSEC 
> 返回以 x+yi 或 x+yj 文本格式表示的复数的正割值。

```
IMSEC(inumber)
inumber必需。
 需要计算其正割值的复数。

```
## IMSECH 
> 返回以 x+yi 或 x+yj 文本格式表示的复数的双曲正割值。

```
IMSECH(inumber)
inumber必需。
 需要计算其双曲正割值的复数。

```
## IMSIN
> 返回以 x+yi 或 x+yj 文本格式表示的复数的正弦值。

```
IMSIN(inumber)
inumber必需。
 需要计算其正弦的复数。

```
## IMSINH 
> 返回以 x+yi 或 x+yj 文本格式表示的复数的双曲正弦值。

```
IMSINH(inumber)
inumber必需。
 需要计算其双曲正弦值的复数。

```
## IMSQRT
> 返回以 x+yi 或 x+yj 文本格式表示的复数的平方根。

```
IMSQRT(inumber)
inumber必需。
 需要计算其平方根的复数。

```
## IMSUB
> 返回以 x+yi 或 x+yj 文本格式表示的两个复数的差。

```
IMSUB(inumber1, inumber2)
inumber1必需。
 从（复）数中减去 inumber2。
inumber2必需。
 从 inumber1 中减（复）数。

```
## IMSUM
> 返回以 x+yi 或 x+yj 文本格式表示的两个或多个复数的和。

```
IMSUM(inumber1, [inumber2], ...)
inumber1, [inumber2], ...inumber1 是必需的，后续数值不是必须的。
 1 到 255 个要相加的复数。

```
## IMTAN 
> 返回以 x+yi 或 x+yj 文本格式表示的复数的正切值。

```
IMTAN(inumber)
inumber必需。
 需要计算其正切值的复数。

```
## INDEX
> INDEX 函数返回表格或区域中的值或值的引用。

```
INDEX(array, row_num, [column_num])
array必需。
单元格区域或数组常量。
 如果数组只包含一行或一列，则相对应的参数 Row_num 或 Column_num 为可选参数。
 如果数组有多行和多列，但只使用 Row_num 或 Column_num，函数 INDEX 返回数组中的整行或整列，且返回值也为数组。
row_num   必需。
选择数组中的某行，函数从该行返回数值。
如果省略 Row_num，则必须有 Column_num。
column_num可选。
选择数组中的某列，函数从该列返回数值。
如果省略 Column_num，则必须有 Row_num。

```
## INDIRECT
> 返回由文本字符串指定的引用。
此函数立即对引用进行计算，并显示其内容。
如果需要更改公式中对单元格的引用，而不更改公式本身，请使用函数 INDIRECT。

```
INDIRECT(ref_text, [a1])
ref_text必需。
对单元格的引用，此单元格包含 A1 样式的引用、R1C1 样式的引用、定义为引用的名称或对作为文本字符串的单元格的引用。
如果 ref_text 不是合法的单元格引用，则 INDIRECT 返回 错误值。
如果 ref_text 是对另一个工作簿的引用（外部引用），则被引用的工作簿必须已打开。
如果源工作簿没有打开，则 INDIRECT 返回错误值 #REF!。
a1可选。
一个逻辑值，用于指定包含在单元格 ref_text 中的引用的类型。
如果 a1 为 TRUE 或省略，ref_text 被解释为 A1-样式的引用。
如果 a1 为 FALSE，则将 ref_text 解释为 R1C1 样式的引用。

```
## INFO
> 返回有关当前操作环境的信息。

```
INFO(type_text)
type_text必需。
 用于指定要返回的信息类型的文本。
type_text  返回结果directory当前目录或文件夹的路径。
numfile  打开的工作簿中活动工作表的数目。
origin 以当前滚动位置为基准，返回窗口中可见的左上角单元格的绝对单元格引用osversion  当前操作系统的版本号，文本值。
recalc 当前的重新计算模式，返回“自动”或“手动”。
release   Microsoft Excel 的版本号，文本值。
system   操作系统名称：Macintosh =“mac”,Windows =“pcdos”
```
## INT
> 将数字向下舍入到最接近的整数。

```
Int( number )
number必需。
 需要进行向下舍入取整的实数。

```
## INTERCEPT
> 返回线性回归线的截距
```
INTERCEPT(known_y's, known_x's)
known_y's必需。
 因变的观察值或数据的集合。
known_x's必需。
 自变的观察值或数据的集合。

```
## INTRATE
> 返回完全投资型证券的利率。

```
INTRATE(settlement, maturity, investment, redemption, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
investment必需。
 有价证券的投资额。
redemption必需。
 有价证券到期时的兑换值。
basis可选。
 要使用的日计数基准类型。
basis日计数基准0 或省略  US (NASD)
 30/3601   实际/实际2   实际/3603   实际/3654   欧洲 30/360
```
## IPMT
> 基于固定利率及等额分期付款方式，返回给定期数内对投资的利息偿还额。

```
IPMT(rate, per, nper, pv, [fv], [type])
rate必需。
 各期利率。
per必需。
 用于计算其利息数额的期数，必须在 1 到 nper 之间。
nper必需。
年金的付款总期数。
pv必需。
 现值，或一系列未来付款的当前值的累积和。
fv可选。
 未来值，或在最后一次付款后希望得到的现金余额。
 如果省略 fv，则假定其值为 0（例如，贷款的未来值是 0）。
type可选。
 数字 0 或 1，用以指定各期的付款时间是在期初还是期末。
 如果省略 type，则假定其值为 0。
type   支付时间0 期末1 期初
```
## IRR
> 返回由值中的数字表示的一系列现金流的内部收益率。
 这些现金流不必等同，因为它们可能作为年金。
 但是，现金流必须定期（如每月或每年）出现。
 内部收益率是针对包含付款（负值）和收入（正值）的定期投资收到的利率。

```
IRR(values, [guess])
values必需。
 数组或单元格的引用，这些单元格包含用来计算内部收益率的数字。
   values 必须包含至少一个正值和一个负值，以计算返回的内部收益率。
guess可选。
 对函数 IRR 计算结果的估计值。

```
## ISBLANK
> 这些函数统称为 IS 函数，此类函数可检验指定值并根据结果返回 TRUE 或 FALSE。
 例如，如果参数 value 引用的是空单元格，则 ISBLANK 函数返回逻辑值 TRUE；否则，返回 FALSE。
在对某一值执行计算或执行其他操作之前，可以使用 IS 函数获取该值的相关信息。
 例如，通过将 ISERROR 函数与 IF 函数结合使用，可以在出现错误时执行其他操作：=IF(ISERROR(A1)
, 出现错误。
, A1 * 2)
此公式检验单元格 A1 中是否存在错误情形。
 如果存在，则 IF 函数返回消息“出现错误”。
如果不存在，则 IF 函数执行计算 A1*2。

```
ISBLANK(value)
value必需。
 指的是要测试的值。
 参数 value 可以是空白（空单元格）、错误值、逻辑值、文本、数字、引用值，或者引用要测试的以上任意值的名称。
如果值为空白单元格，则返回 TRUE。

```
## ISERR
> 这些函数统称为 IS 函数，此类函数可检验指定值并根据结果返回 TRUE 或 FALSE。
 例如，如果参数 value 引用的是空单元格，则 ISBLANK 函数返回逻辑值 TRUE；否则，返回 FALSE。
在对某一值执行计算或执行其他操作之前，可以使用 IS 函数获取该值的相关信息。
 例如，通过将 ISERROR 函数与 IF 函数结合使用，可以在出现错误时执行其他操作：=IF(ISERROR(A1)
, 出现错误。
, A1 * 2)
此公式检验单元格 A2 中是否存在错误情形。
 如果存在，
```
ISERR(value)
value必需。
 指的是要测试的值。
 参数 value 可以是空白（空单元格）、错误值、逻辑值、文本、数字、引用值，或者引用要测试的以上任意值的名称。
如果值为任意错误值（除去 #N/A），则返回 TRUE
```
## ISERROR
> 这些函数统称为 IS 函数，此类函数可检验指定值并根据结果返回 TRUE 或 FALSE。
 例如，如果参数 value 引用的是空单元格，则 ISBLANK 函数返回逻辑值 TRUE；否则，返回 FALSE。
在对某一值执行计算或执行其他操作之前，可以使用 IS 函数获取该值的相关信息。
 例如，通过将 ISERROR 函数与 IF 函数结合使用，可以在出现错误时执行其他操作：=IF(ISERROR(A1)
, 出现错误。
, A1 * 2)
此公式检验单元格 A2 中是否存在错误情形。
 如果存在，
```
ISERROR(value)
value必需。
 指的是要测试的值。
 参数 value 可以是空白（空单元格）、错误值、逻辑值、文本、数字、引用值，或者引用要测试的以上任意值的名称。
如果值为任意错误值（#N/A、#VALUE!、#REF!、#DIV/0!、#NUM!、#NAME? 或#NULL!），则返回 TRUE。

```
## ISEVEN
> 如果参数 number 为偶数，返回 TRUE，否则返回 FALSE。

```
ISEVEN(number)
number必需。
 要测试的值。
 如果 number 不是整数，将被截尾取整。

```
## ISFORMULA 
> 检查是否存在包含公式的单元格引用，然后返回 TRUE 或 FALSE。

```
ISFORMULA(reference)
reference必需。
 引用是对要测试单元格的引用。
 引用可以是单元格引用或引用单元格的公式或名称。

```
## ISLOGICAL
> 这些函数统称为 IS 函数，此类函数可检验指定值并根据结果返回 TRUE 或 FALSE。
 例如，如果参数 value 引用的是空单元格，则 ISBLANK 函数返回逻辑值 TRUE；否则，返回 FALSE。
在对某一值执行计算或执行其他操作之前，可以使用 IS 函数获取该值的相关信息。
 例如，通过将 ISERROR 函数与 IF 函数结合使用，可以在出现错误时执行其他操作：=IF(ISERROR(A1)
, 出现错误。
, A1 * 2)
此公式检验单元格 A1 中是否存在错误情形。
 如果存在，则 IF 函数返回消息“出现错误”。
如果不存在，则 IF 函数执行计算 A1*2。

```
ISLOGICAL(value)
value必需。
 指的是要测试的值。
 参数 value 可以是空白（空单元格）、错误值、逻辑值、文本、数字、引用值，或者引用要测试的以上任意值的名称。
如果值为逻辑值，则返回 TRUE。

```
## ISNA
> 这些函数统称为 IS 函数，此类函数可检验指定值并根据结果返回 TRUE 或 FALSE。
 例如，如果参数 value 引用的是空单元格，则 ISBLANK 函数返回逻辑值 TRUE；否则，返回 FALSE。
在对某一值执行计算或执行其他操作之前，可以使用 IS 函数获取该值的相关信息。
 例如，通过将 ISERROR 函数与 IF 函数结合使用，可以在出现错误时执行其他操作：=IF(ISERROR(A1)
, 出现错误。
, A1 * 2)
此公式检验单元格 A1 中是否存在错误情形。
 如果存在，则 IF 函数返回消息“出现错误”。
如果不存在，则 IF 函数执行计算 A1*2。

```
ISNA(value)
value必需。
 指的是要测试的值。
 参数 value 可以是空白（空单元格）、错误值、逻辑值、文本、数字、引用值，或者引用要测试的以上任意值的名称。
如果值为错误值 #N/A（值不存在），则返回 TRUE。

```
## ISNONTEXT
> 这些函数统称为 IS 函数，此类函数可检验指定值并根据结果返回 TRUE 或 FALSE。
 例如，如果参数 value 引用的是空单元格，则 ISBLANK 函数返回逻辑值 TRUE；否则，返回 FALSE。
在对某一值执行计算或执行其他操作之前，可以使用 IS 函数获取该值的相关信息。
 例如，通过将 ISERROR 函数与 IF 函数结合使用，可以在出现错误时执行其他操作：=IF(ISERROR(A1)
, 出现错误。
, A1 * 2)
此公式检验单元格 A1 中是否存在错误情形。
 如果存在，则 IF 函数返回消息“出现错误”。
如果不存在，则 IF 函数执行计算 A1*2。

```
ISNONTEXT(value)
value必需。
 指的是要测试的值。
 参数 value 可以是空白（空单元格）、错误值、逻辑值、文本、数字、引用值，或者引用要测试的以上任意值的名称。
如果值为不是文本的任意项，则返回 TRUE。

```
## ISNUMBER
> 这些函数统称为 IS 函数，此类函数可检验指定值并根据结果返回 TRUE 或 FALSE。
 例如，如果参数 value 引用的是空单元格，则 ISBLANK 函数返回逻辑值 TRUE；否则，返回 FALSE。
在对某一值执行计算或执行其他操作之前，可以使用 IS 函数获取该值的相关信息。
 例如，通过将 ISERROR 函数与 IF 函数结合使用，可以在出现错误时执行其他操作：=IF(ISERROR(A1)
, 出现错误。
, A1 * 2)
此公式检验单元格 A1 中是否存在错误情形。
 如果存在，则 IF 函数返回消息“出现错误”。
如果不存在，则 IF 函数执行计算 A1*2。

```
ISNUMBER(value)
value必需。
 指的是要测试的值。
 参数 value 可以是空白（空单元格）、错误值、逻辑值、文本、数字、引用值，或者引用要测试的以上任意值的名称。
如果值为数字，则返回 TRUE。

```
## ISO.CEILING 
> 返回一个数字，该数字向上舍入为最接近的整数或最接近的有效位的倍数。
 无论该数字的符号如何，该数字都向上舍入。
 但是，如果该数字或有效位为 0，则返回 0。

```
ISO.CEILING(number, [significance])
number   必需。
要进行舍入的值。
significance可选。
 要将数字舍入的可选倍数。
如果省略 significance，则其默认值为 1。

```
## ISODD
> ISODD函数用于判断数字是否为奇数，如果是，则返回TRUE；否则返回FALSE。

```

```
## ISOWEEKNUM 
> 返回给定日期在全年中的 ISO 周数
```
ISOWEEKNUM(date)
date必需。
 日期是 Excel 用于日期和时间计算的日期-时间代码。

```
## ISPMT
> 计算利率支付 （或接收） 给定期间内的贷款 （或投资） 甚至本金付款。

```
ISPMT(rate, per, nper, pv)
rate必需。
投资利率。
per 必需。
为其您想要查找感兴趣，并且必须介于 1 到 Nper 之间时间段。
nper   必需。
投资的付款期总数。
pv必需。
投资的现值。
对于贷款，Pv 是贷款金额。

```
## ISREF
> 这些函数统称为 IS 函数，此类函数可检验指定值并根据结果返回 TRUE 或 FALSE。
 例如，如果参数 value 引用的是空单元格，则 ISBLANK 函数返回逻辑值 TRUE；否则，返回 FALSE。
在对某一值执行计算或执行其他操作之前，可以使用 IS 函数获取该值的相关信息。
 例如，通过将 ISERROR 函数与 IF 函数结合使用，可以在出现错误时执行其他操作：=IF(ISERROR(A1)
, 出现错误。
, A1 * 2)
此公式检验单元格 A1 中是否存在错误情形。
 如果存在，则 IF 函数返回消息“出现错误”。
如果不存在，则 IF 函数执行计算 A1*2。

```
ISREF(value)
value必需。
 指的是要测试的值。
 参数 value 可以是空白（空单元格）、错误值、逻辑值、文本、数字、引用值，或者引用要测试的以上任意值的名称。
如查值为引用，则返回 TRUE。

```
## ISTEXT
> 这些函数统称为 IS 函数，此类函数可检验指定值并根据结果返回 TRUE 或 FALSE。
 例如，如果参数 value 引用的是空单元格，则 ISBLANK 函数返回逻辑值 TRUE；否则，返回 FALSE。
在对某一值执行计算或执行其他操作之前，可以使用 IS 函数获取该值的相关信息。
 例如，通过将 ISERROR 函数与 IF 函数结合使用，可以在出现错误时执行其他操作：=IF(ISERROR(A1)
, 出现错误。
, A1 * 2)
此公式检验单元格 A1 中是否存在错误情形。
 如果存在，则 IF 函数返回消息“出现错误”。
如果不存在，则 IF 函数执行计算 A1*2。

```
ISTEXT(value)
value必需。
 指的是要测试的值。
 参数 value 可以是空白（空单元格）、错误值、逻辑值、文本、数字、引用值，或者引用要测试的以上任意值的名称。
如果值为文本，则返回 TRUE。

```
## KURT
> 返回数据集的峰值
```
KURT(number1, [number2], ...)
number1, number2, ...Number1 是必需的，后续数字是可选的。
 用于计算峰值的 1 到 255 个参数。
 也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## LARGE
> 返回数据集中第 k 个最大值
```
LARGE(array,k)
array必需。
 需要确定第 k 个最大值的数组或数据区域。
k必需。
 返回值在数组或数据单元格区域中的位置（从大到小排）。

```
## LCM
> 返回整数的最小公倍数。
 最小公倍数是所有整数参数 number1、number2 等的倍数中的最小正整数。
 使用 LCM 添加具有不同分母的分数。
倍数
```
LCM(number1, [number2], ...)
number1, number2, ...number1 是必需的，后续数字是可选的。
 要计算其最小公倍数的 1 到 255 个值。
 如果值不是整数，将被截尾取整。

```
## LEFT
> 从文本字符串的第一个字符开始返回指定个数的字符。

```
LEFT(text, [num_chars])
text必需。
 包含要提取的字符的文本字符串。
num_chars可选。
 指定要由 LEFT 提取的字符的数量。
num_chars 必须。
大于或等于零。
如果 num_chars 大于文本长度，则 LEFT 返回全部文本。
如果省略 num_chars，则假定其值为 1。

```
## LEFTB
> 基于所指定的字节数返回文本字符串中的第一个或前几个字符。

```
LEFTB(text, [num_bytes])
text必需。
 包含要提取的字符的文本字符串。
num_bytes可选。
按字节指定要由 LEFTB 提取的字符的数量
```
## LEN
> 返回文本字符串中的字符个数
```
LEN(text)
text必需。
 要查找其长度的文本。
 空格将作为字符进行计数。

```
## LENB
>  返回文本字符串中用于代表字符的字节数。

```
LENB(text)
text必需。
 要查找其长度的文本。
 空格将作为字符进行计数。

```
## LINEST
> 返回线性趋势的参数
```
LINEST(known_y's, [known_x's], [const], [stats])
known_y's必需。
 关系表达式 y = mx + b 中已知的 y 值集合。
   如果 known_y's 对应的单元格区域在单独一列中，则 known_x's 的每一列被视为一个独立的变量。
   如果 known_y's 对应的单元格区域在单独一行中，则 known_x's 的每一行被视为一个独立的变量。
known_x's可选。
 关系表达式 y = mx + b 中已知的 x 值集合。
   known_x's 对应的单元格区域可以包含一组或多组变量。
 如果仅使用一个变量，那么只要 known_x's 和 known_y's 具有相同的维数，则它们可以是任何形状的区域。
 如果用到多个变量，则 known_y's 必须为向量（即必须为一行或一列）。
   如果省略 known_x's，则假设该数组为 {1,2,3,...}，其大小与 known_y's 相同。
const可选。
 一个逻辑值，用于指定是否将常量 b 强制设为 0。
  如果 const 为 TRUE 或省略，b 将按正常计算。
  如果 const 为 FALSE，b 将被设为 0，并同时调整 m 值使 y = mx。
stats可选。
 一个逻辑值，用于指定是否返回附加回归统计值。
如果 stats 为 TRUE，则 LINEST 函数返回附加回归统计值，这时返回的数组为 {mn,mn-1,...,m1,b;sen,sen-1,...,se1,seb;r2,sey;F,df;ssreg,ssresid}。
 如果 stats 为 FALSE 或省略，则函数 LINEST 只返回系数 m 和常量 b。

```
## LN
> 返回数字的自然对数。
 自然对数以常数 e (2.71828182845904)
 为底。

```
LN(number)
number必需。
 想要计算其自然对数的正实数。

```
## LOG
> 根据指定底数返回数字的对数。

```
LOG(number, [base])
number必需。
 想要计算其对数的正实数。
base可选。
 对数的底数。
 如果省略 base，则假定其值为 10。

```
## LOG10
> 返回数字以 10 为底的对数。

```
LOG10(number)
number必需。
 想要计算其以 10 为底的对数的正实数。

```
## LOGEST
> 返回指数趋势的参数
```
LOGEST(known_y's, [known_x's], [const], [stats])
known_y's必需。
 关系表达式 y = b*m^x 中已知的 y 值集合。
   如果数组 known_y's 在单独一列中，则 known_x's 的每一列被视为一个独立的变量。
   如果数组 known_y's 在单独一行中，则 known_x's 的每一行被视为一个独立的变量。
known_x's可选。
 关系表达式 y=b*m^x 中已知的 x 值集合，为可选参数。
   数组 known_x's 可以包含一组或多组变量。
 如果仅使用一个变量，那么只要 known_x's 和 known_y's 具有相同的维数，则它们可以是任何形状的区域。
 如果使用多个变量，则 known_y's 必须是向量（即具有一列高度或一行宽度的单元格区域）。
如果省略 known_x's，则假设该数组为 {1,2,3,...}，其大小与 known_y's 相同。
const可选。
 一个逻辑值，用于指定是否将常量 b 强制设为 1。
  如果 const 为 TRUE 或省略，b 将按正常计算。
  如果 const 为 FALSE，则常量 b 将设为 1，而 m 的值满足公式 y=m＾x。
stats可选。
 一个逻辑值，用于指定是否返回附加回归统计值。
 如果 stats 为 TRUE，函数 LOGEST 将返回附加的回归统计值，因此返回的数组为 {mn,mn-1,...,m1,b;sen,sen-1,...,se1,seb;r 2,sey; F,df;ssreg,ssresid}。
  如果 stats 为 FALSE 或省略，则函数 LOGEST 只返回系数 m 和常量 b。

```
## LOGINV
> 返回 x 的对数累积分布函数的反函数值，此处的 ln(x)
 是服从参数 mean 和 standard_dev 的正态分布。
 如果 p = LOGNORMDIST(x,...)
，则 LOGINV(p,...)
 = x。
使用对数分布可分析经过对数变换的数据。

```
LOGINV(probability,mean, standard_dev)
probability必需。
 与对数分布相关的概率。
mean  必需。
 ln(x)
 的平均值。
standard_dev必需。
 ln(x)
 的标准偏差。

```
## LOGNORM.DIST 
> 返回对数累积分布函数
```
LOGNORM.DIST(x,mean,standard_dev,cumulative)
x  必需。
 用来计算函数的值。
mean  必需。
 ln(x)
 的平均值。
standard_dev必需。
 ln(x)
 的标准偏差。
cumulative 必需。
 决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 LOGNORM.DIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。

```
## LOGNORM.INV 
> 返回对数累积分布的反函数
```
LOGNORM.INV(probability, mean, standard_dev)
LOGNORM.INV 函数语法具有下列参数：Probability必需。
 与对数分布相关的概率。
Mean必需。
 ln(x)
 的平均值。
standard_dev必需。
 ln(x)
 的标准偏差。

```
## LOGNORMDIST
> 返回 x 的对数累积分布函数的函数值，此处的 ln(x)
 是服从参数 mean 和 standard_dev 的正态分布。
 使用此函数可以分析经过对数变换的数据。

```
LOGNORMDIST(x,mean,standard_dev)
x必需。
 用来计算函数的值。
mean必需。
 ln(x)
 的平均值。
standard_dev必需。
 ln(x)
 的标准偏差。

```
## LOOKUP
> 当您需要查询一行或一列并查找另一行或列中的相同位置的值时，会使用其中一个查找和引用函数 LOOKUP。

```
LOOKUP(lookup_value, lookup_vector, [result_vector])
lookup_value必需。
 LOOKUP 在第一个向量中搜索的值。
 Lookup_value 可以是数字、文本、逻辑值、名称或对值的引用。
lookup_vector必需。
 只包含一行或一列的区域。
 lookup_vector 中的值可以是文本、数字或逻辑值。
  重要: lookup_vector 中的值必须按升序排列：..., -2, -1, 0, 1, 2, ..., A-Z, FALSE, TRUE；否则，LOOKUP 可能无法返回正确的值。
 文本不区分大小写。
result_vector可选。
只包含一行或一列的区域。
result_vector 参数必须与 lookup_vector 参数大小相同。
其大小必须相同。

```
## LOWER
> 将一个文本字符串中的所有大写字母转换为小写字母。

```
LOWER(text)
text必需。
 要转换为小写字母的文本。
 LOWER 不改变文本中的非字母字符。

```
## MATCH
> 使用 MATCH 函数在 范围 单元格中搜索特定的项，然后返回该项在此区域中的相对位置。

```
MATCH(lookup_value, lookup_array, [match_type])
lookup_value必需。
要在 lookup_array 中匹配的值。
例如，如果要在电话簿中查找某人的电话号码，则应该将姓名作为查找值，但实际上需要的是电话号码。
lookup_value 参数可以为值（数字、文本或逻辑值）或对数字、文本或逻辑值的单元格引用。
lookup_array必需。
要搜索的单元格区域。
match_type可选。
数字 -1、0 或 1。
match_type 参数指定 Excel 如何将 lookup_value 与 lookup_array 中的值匹配。
此参数的默认值为 1。
下表介绍该函数如何根据 match_type 参数的设置查找值。
match_type   行为1 或省略查找小于或等于 lookup_value 的最大值。
0 查找完全等于 lookup_value 的第一个值。
-1   查找大于或等于 lookup_value 的最小值。
MATCH 返回匹配值在 lookup_array 中的位置，而非其值本身。
例如，MATCH(b,{a,b,c},0)
返回 2，即“b”在数组 {a,b,c} 中的相对位置。
匹配文本值时，MATCH 函数不区分大小写字母。
如果 MATCH 函数查找匹配项不成功，它会返回错误值 #N/A。
如果 match_type 为 0 且 lookup_value 为文本字符串，您可在 lookup_value 参数中使用通配符 - 问号 (?)
 和星号 (*)
 。
问号匹配任意单个字符；星号匹配任意一串字符。
如果要查找实际的问号或星号，请在字符前键入波形符 (~)
。

```
## MAX
> 返回参数列表中的最大值
```
MAX(number1, [number2], ...)
number1, number2, ...Number1 是必需的，后续数字是可选的。
 要从中查找最大值的 1 到 255 个数字。

```
## MAXA
> 返回参数列表中的最大值，包括数字、文本和逻辑值
```
MAXA(value1,[value2],...)
value1必需。
 要从中找出最大值的第一个数值参数。
value2,...可选。
 要从中找出最大值的 2 到 255 个数值参数。

```
## MAXIFS 
> 返回一组给定条件或标准指定的单元格之间的最大值
```
MAXIFS(max_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
max_range必需。
确定最大值的实际单元格区域。
criteria_range1   必需。
是一组用于条件计算的单元格。
criteria1必需。
用于确定哪些单元格是最大值的条件，格式为数字、表达式或文本。
一组相同的条件适用于 MINIFS、SUMIFS 和 AVERAGEIFS 函数。
criteria_range2,criteria2, ...可选。
附加区域及其关联条件。
最多可以输入 126 个区域/条件对。

```
## MDETERM
> 返回一个数组的矩阵行列式的值。

```
MDETERM(array)
array必需。
 行数和列数相等的数值数组。

```
## MDURATION
> 返回假设面值 ￥100 的有价证券的 Macauley 修正期限。

```
MDURATION(settlement, maturity, coupon, yld, frequency, [basis])
settlement  必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity   必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
coupon 必需。
 有价证券的年息票利率。
yld  必需。
 有价证券的年收益率。
frequency 必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis   日计数基准0 或省略 US (NASD)
 30/3601  实际/实际2  实际/3603  实际/3654  欧洲 30/360
```
## MEDIAN
> 返回给定数值集合的中值
```
MEDIAN(number1, [number2], ...)
number1, number2, ...number1 是必需的，后续数字是可选的。
 要计算中值的 1 到 255 个数字。

```
## MID
> 从文本字符串中的指定位置起返回特定个数的字符
```
MID(text, start_num, num_chars)
text必需。
 包含要提取字符的文本字符串。
start_num必需。
 文本中要提取的第一个字符的位置。
 文本中第一个字符的 start_num 为 1，以此类推。
num_chars必需。
 指定希望 MID 从文本中返回字符的个数。

```
## MIDB
> 从文本字符串中的指定位置起返回特定个数的字节
```
MIDB(text, start_num, num_bytes)
text必需。
 包含要提取字符的文本字符串。
num_bytes必需。
 指定希望 MIDB 从文本中返回字符的个数（字节数）。

```
## MIN
> 返回参数列表中的最小值
```
MIN(number1, [number2], ...)
number1, number2, ...number1 是可选的，后续数字是可选的。
 要从中查找最小值的 1 到 255 个数字。

```
## MINA
> 返回参数列表中的最小值，包括数字、文本和逻辑值
```
MINA(value1, [value2], ...)
value1, value2, ...value1 是必需的，后续值是可选的。
 要从中查找最小值的 1 到 255 个数值。

```
## MINIFS 
> 返回一组给定条件或标准指定的单元格之间的最小值。

```
MINIFS(min_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
min_range   必需。
确定最小值的实际单元格区域。
criteria_range1   必需。
是一组用于条件计算的单元格。
criteria1 必需。
用于确定哪些单元格是最小值的条件，格式为数字、表达式或文本。
一组相同的条件适用于 MAXIFS、SUMIFS 和 AVERAGEIFS 函数。
criteria_range2,criteria2, ...可选。

```
## MINUTE
> 返回时间值中的分钟。
 分钟是一个介于 0 到 59 之间的整数。

```
MINUTE(serial_number)
serial_number必需。
 一个时间值，其中包含要查找的分钟。
 时间值有多种输入方式：带引号的文本字符串（例如 6:45 PM）、十进制数（例如 0.78125 表示 6:45 PM）或其他公式或函数的结果（例如 TIMEVALUE(6:45 PM)
）。

```
## MINVERSE
> 返回数组中存储的矩阵的逆矩阵。

```
MINVERSE(array)
array必需。
 行数和列数相等的数值数组。

```
## MIRR
> 返回一系列定期现金流的修改后内部收益率 MIRR 同时考虑投资的成本和现金再投资的收益率。

```
MIRR(values, finance_rate, reinvest_rate)
values   必需。
 数组或对包含数字的单元格的引用。
 这些数值代表一系列定期支出（负值）和收益（正值）。
finance_rate必需。
 现金流中使用的资金支付的利率。
reinvest_rate必需。
 将现金流再投资的收益率。

```
## MMULT
> 返回两个数组的矩阵乘积。
结果矩阵的行数与 array1 的行数相同，矩阵的列数与 array2 的列数相同。

```
MMULT(array1, array2)
array1、array2必需。
要进行矩阵乘法运算的两个数组。

```
## MOD
> 返回两数相除的余数。
 结果的符号与除数相同。

```
MOD(number, divisor)
number必需。
 要计算余数的被除数。
divisor必需。
 除数。

```
## MODE
> 日常工作中，有时候我们需要在庞大的一组数据中统计出出现频率最高的数据（即众数），为我们的数据统计和数据管理提供决策。
这种情况下，就需要用到mode函数了。
mode函数是一个非常有用的函数。
mode函数，返回某一区域中出现频率最高的数值，是一个位置测量函数。

```
MODE(number1,[number2],...)
number1, number2, ... 是用于统计频率出现次数来计算的 1 到 30 个参数。
参数可以是数字，也可以是包含数字的名称、数组或引用。
如果参数中包含文本、逻辑值或空白单元格等非数值的值，这些非数值的值将被忽略；但零值的单元格将计算在内。

```
## MODE.MULT 
> 返回一组数据或数据区域中出现频率最高或重复出现的数值的垂直数组
```
MODE.MULT((number1,[number2],...)
number1必需。
要计算其众数的第一个数字参数。
number2, ...可选。
要计算其众数的 2 到 254 个数字参数。
也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## MODE.SNGL 
> 返回在数据集内出现次数最多的值
```
MODE.SNGL(number1,[number2],...)
number1必需。
要计算其众数的第一个参数。
number2, ...可选。
要计算其众数的 2 到 254 个参数。
也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## MONTH
> 返回日期（以序列数表示）中的月份。
 月份是介于 1（一月）到 12（十二月）之间的整数。

```
MONTH(serial_number)
serial_number必需。
要查找的月份日期。
应使用 DATE 函数输入日期，或将日期作为其他公式或函数的结果输入。
例如，使用函数 DATE(2008,5,23)
 输入 2008 年 5 月 23 日。
如果日期以文本形式输入，则会出现问题。

```
## MROUND
> MROUND 返回舍入到所需倍数的数字。

```
MROUND(number, multiple)
number必需。
 要舍入的值。
nultiple必需。
 要舍入到的倍数。

```
## MULTINOMIAL
> 返回参数和的阶乘与各参数阶乘乘积的比值。

```
MULTINOMIAL(number1, [number2], ...)
number1, number2, ...number1 是必需的，后续数字是可选的。
 要计算多项式的 1 到 255 个值。

```
## MUNIT 
> 返回指定维度的单位矩阵。

```
MUNIT(dimension)
dimension必需。
 维度是一个整数，指定要返回的单位矩阵的维度。
 返回一个数组。
 维度必须大于零。

```
## N
> 返回转化为数值后的值。

```
N(value)
value必需。
 要转换的值。
 N 转换下表中列出的值。
value N 返回值数字该数字日期（Microsoft Excel 的一种内部日期格式） 该日期的序列号TRUE   1FALSE  0错误值，例如 #DIV/0!  错误值其他值 0
```
## NA
> 返回错误值 #N/A。
错误值 #N/A 表示“无值可用”。
使用 NA 标记空单元格。
通过在缺少信息的单元格中输入 #N/A，您可以避免无意中将空单元格包括在计算中。
（当公式引用的单元格包含 #N/A 时，公式返回错误值 #N/A。
）
```
NA( )
NA 函数语法没有参数。

```
## NEGBINOM.DIST 
> 返回负二项式分布
```
NEGBINOM.DIST(number_f,number_s,probability_s,cumulative)
NEGBINOM.DIST 函数语法具有下列参数：Number_f必需。
 失败的次数。
Number_s必需。
 成功次数的阈值。
Probability_s必需。
 成功的概率。
cumulative必需。
 决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 NEGBINOM.DIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。

```
## NEGBINOMDIST
> 返回负二项式分布。
 当成功概率为常量 probability_s 时，NEGBINOMDIST 返回在达到 number_s 次成功之前，出现 number_f 次失败的概率。
 此函数与二项式分布相似，只是它的成功次数固定，试验次数为变量。
 与二项式分布相同的是，二者均假定试验是独立的。
例如，如果要找 10 个反应敏捷的人，且已知候选人符合相关条件的概率为 0.3。
 NEGBINOMDIST 将计算出在找到 10 个合格候选人之前，需面试特定数目的不合格候选人的概率。

```
NEGBINOMDIST(number_f,number_s,probability_s)
number_f  必需。
 失败的次数。
number_s   必需。
 成功次数的阈值。
probability_s  必需。
 成功的概率。

```
## NETWORKDAYS
> 返回参数 start_date 和 end_date 之间完整的工作日数值。
 工作日不包括周末和专门指定的假期。
 可以使用函数 NETWORKDAYS，根据某一特定时期内雇员的工作天数，计算其应计的报酬。

```
NETWORKDAYS(start_date, end_date, [holidays])
start_date必需。
 一个代表开始日期的日期。
end_date 必需。
 一个代表终止日期的日期。
holidays   可选。
不在工作日历中的一个或多个日期所构成的可选区域，例如：省/市/自治区和国家/地区的法定假日以及其他非法定假日。
该列表可以是包含日期的单元格区域，或是表示日期的序列号的数组常量。

```
## NETWORKDAYS.INTL 
> 返回两个日期之间的所有工作日数，使用参数指示哪些天是周末，以及有多少天是周末。
 周末和任何指定为假期的日期不被视为工作日。

```
NETWORKDAYS.INTL(start_date, end_date, [weekend], [holidays])
start_date、end_date必需。
 要计算其差值的日期。
 start_date 可以早于或晚于 end_date，也可以与它相同。
weekend可选。
 表示介于 start_date 和 end_date 之间但又不包括在所有工作日数中的周末日。
 Weekend 是一个用于指定周末日的周末数字或字符串。
weekend 数值表示以下周末日：weekend周末日1 或省略 星期六、星期日2  星期日、星期一3  星期一、星期二4  星期二、星期三5  星期三、星期四6  星期四、星期五7  星期五、星期六11仅星期日12仅星期一13仅星期二14仅星期三15仅星期四16仅星期五17仅星期六周末字符串值的长度为七个字符，并且字符串中的每个字符表示一周中的一天（从星期一开始）。
 1 表示非工作日，0 表示工作日。
 在字符串中仅允许使用字符 1 和 0。
 使用 1111111 将始终返回 0。
例如，0000011 结果为星期六和星期日是周末。
holidays可选。
 一组可选的日期，表示要从工作日日历中排除的一个或多个日期。
 holidays 应是一个包含相关日期的单元格区域，或者是一个由表示这些日期的序列值构成的数组常量。
 holidays 中的日期或序列值的顺序可以是任意的。

```
## NOMINAL
> 基于给定的实际利率和年复利期数，返回名义年利率。

```
NOMINAL(effect_rate, npery)
effect_rate必需。
 实际利率。
npery必需。
 每年的复利期数。

```
## NORM.DIST 
> 返回正态累积分布
```
NORM.DIST(x,mean,standard_dev,cumulative)
x必需。
 需要计算其分布的数值。
mean必需。
 分布的算术平均值。
standard_dev必需。
 分布的标准偏差。
cumulative必备.确定函数形式的逻辑值。
如果累积性为 TRUE, 则为 标准。
DIST 返回累积分布函数;如果为 FALSE, 则返回概率密度函数。

```
## NORM.INV 
> 返回正态累积分布的反函数
```
NORM.INV(probability,mean,standard_dev)
probability必需。
 对应于正态分布的概率。
mean必需。
 分布的算术平均值。
standard_dev必需。
 分布的标准偏差。

```
## NORM.S.DIST 
> 返回标准正态累积分布
```
NORM.S.DIST(z,cumulative)
z必需。
 需要计算其分布的数值。
cumulative必需。
 cumulative 是决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 NORMS.DIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。

```
## NORM.S.INV 
> 返回标准正态累积分布函数的反函数
```
NORM.S.INV(probability)
probability必需。
 对应于正态分布的概率。

```
## NORMDIST
> 返回指定平均值和标准偏差的正态分布函数。
 此函数在统计方面应用范围广泛（包括假设检验）。

```
NORMDIST(x,mean,standard_dev,cumulative)
x 必需。
 需要计算其分布的数值。
mean 必需。
 分布的算术平均值。
standard_dev   必需。
 分布的标准偏差。
cumulative必需。
 决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 NORMDIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。

```
## NORMINV
> 返回指定平均值和标准偏差的正态累积分布函数的反函数值。

```
NORMINV(probability,mean,standard_dev)
probability必需。
 对应于正态分布的概率。
mean  必需。
 分布的算术平均值。
standard_dev必需。
 分布的标准偏差。

```
## NORMSDIST
> 返回标准正态累积分布函数的函数值。
 该分布的平均值为 0（零），标准偏差为 1。
 可以使用此函数代替标准正态曲线面积表。

```
NORMSDIST(z)
z必需。
 需要计算其分布的数值。

```
## NORMSINV
> 返回标准正态累积分布函数的反函数值。
 该分布的平均值为 0，标准偏差为 1。

```
NORMSINV(probability)
probability必需。
 对应于正态分布的概率。

```
## NOT
> 对其参数的逻辑求反
```

```
## NOW
> 返回当前日期和时间的序列号。
 如果在输入该函数前，单元格格式为“常规”，Excel 会更改单元格格式，使其与区域设置的日期和时间格式匹配。
 可以在功能区“开始”选项卡上的“数字”组中使用命令来更改日期和时间格式。
当需要在工作表上显示当前日期和时间或者需要根据当前日期和时间计算一个值并在每次打开工作表时更新该值时，使用 NOW 函数很有用。

```
Now()
NOW 函数语法没有参数。

```
## NPER
> 基于固定利率及等额分期付款方式，返回某项投资的总期数。

```
NPER(rate,pmt,pv,[fv],[type])
rate必需。
 各期利率。
pmt必需。
 各期所应支付的金额，在整个年金期间保持不变。
 通常 pmt 包括本金和利息，但不包括其他费用或税款。
pv   必需。
 现值，或一系列未来付款的当前值的累积和。
fv可选。
 未来值，或在最后一次付款后希望得到的现金余额。
 如果省略 fv，则假定其值为 0（例如，贷款的未来值是 0）。
type可选。
 数字 0 或 1，用以指定各期的付款时间是在期初还是期末。
type支付时间0 或省略 期末1  期初
```
## NPV
> 使用贴现率和一系列未来支出（负值）和收益（正值）来计算一项投资的净现值。

```
NPV(rate,value1,[value2],...)
rate必需。
某一期间的贴现率。
value1, value2, ...value1 是必需的，后续值是可选的。
这些是代表支出及收入的 1 到 254 个参数。

```
## NUMBERVALUE 
> 以与区域设置无关的方式将文本转换为数字
```
NUMBERVALUE(text, [decimal_separator], [group_separator ])
text必需。
 要转换为数字的文本。
decimal_separator可选。
 用于分隔结果的整数和小数部分的字符。
group_separator可选。
 用于分隔数字分组的字符，例如，千位与百位之间以及百万位与千位之间。

```
## OCT2BIN
> 将八进制数转换为二进制数。

```
OCT2BIN(number, [places])
number必需。
要转换的八进制数。
Number 不能包含超过10个字符。
Number 的最高位为符号位。
其余 29 位是数量位。
负数由二进制补码记数法表示。
places可选。
要使用的字符数。
如果省略 places，则 OCT2BIN 使用必要的最小字符数。
Places 可用于在返回的值前置 0（零）。

```
## OCT2DEC
> 将八进制数转换为十进制数。

```
OCT2DEC(number)
number必需。
 要转换的八进制数。
 Number 不能包含超过 10 个八进制字符（30位）。
 Number 的最高位为符号位。
 其余 29 位是数量位。
 负数由二进制补码记数法表示。

```
## OCT2HEX
> 将八进制数转换为十六进制数。

```
OCT2HEX(number, [places])
number必需。
 要转换的八进制数。
 Number 不能包含超过 10 个八进制字符（30位）。
 Number 的最高位为符号位。
 其余 29 位是数量位。
 负数由二进制补码记数法表示。
places可选。
 要使用的字符数。
 如果省略 places，则 OCT2HEX 使用必要的最小字符数。
 Places 可用于在返回的值前置 0（零）。

```
## ODD
> 返回数字向上舍入到的最接近的奇数。

```
ODD(number)
number必需。
 要舍入的值。

```
## ODDFPRICE
> 返回首期付息日不固定（长期或短期）的面值 ￥100 的有价证券价格。

```
ODDFPRICE(settlement, maturity, issue, first_coupon, rate, yld, redemption, frequency, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
issue必需。
 有价证券的发行日。
first_coupon必需。
 有价证券的首期付息日。
rate必需。
 有价证券的利率。
yld必需。
 有价证券的年收益率。
redemption必需。
 面值 ￥100 的有价证券的清偿价值。
frequency必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis   日计数基准0 或省略 US (NASD)
 30/3601  实际/实际2  实际/3603  实际/3654  欧洲 30/360
```
## ODDFYIELD
> 返回首期付息日不固定的有价证券（长期或短期）的收益率。

```
ODDFYIELD(settlement, maturity, issue, first_coupon, rate, pr, redemption, frequency, [basis])
settlement  必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity   必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
issue 必需。
 有价证券的发行日。
first_coupon必需。
 有价证券的首期付息日。
rate必需。
 有价证券的利率。
pr必需。
 有价证券的价格。
redemption 必需。
 面值 ￥100 的有价证券的清偿价值。
frequency必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis日计数基准0 或省略  US (NASD)
 30/3601   实际/实际2   实际/3603   实际/3654   欧洲 30/360
```
## ODDLPRICE
> 返回末期付息日不固定的面值 ￥100 的有价证券（长期或短期）的价格。

```
ODDLPRICE(settlement, maturity, last_interest, rate, yld, redemption, frequency, [basis])
settlement  必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity  必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
last_interest必需。
 有价证券的末期付息日。
rate   必需。
 有价证券的利率。
yld 必需。
 有价证券的年收益率。
redemption必需。
 面值 ￥100 的有价证券的清偿价值。
frequency必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis  日计数基准0 或省略US (NASD)
 30/3601 实际/实际2 实际/3603 实际/3654 欧洲 30/360
```
## ODDLYIELD
> 返回末期付息日不固定的有价证券（长期或短期）的收益率。

```
ODDLYIELD(settlement, maturity, last_interest, rate, pr, redemption, frequency, [basis])
settlement 必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity  必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
last_interest必需。
 有价证券的末期付息日。
rate   必需。
有价证券的利率pr   必需。
 有价证券的价格。
redemption必需。
 面值 ￥100 的有价证券的清偿价值。
frequency   必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis日计数基准0 或省略  US (NASD)
 30/3601   实际/实际2   实际/3603   实际/3654   欧洲 30/360
```
## OFFSET
> 返回对单元格或单元格区域中指定行数和列数的区域的引用。
 返回的引用可以是单个单元格或单元格区域。
 可以指定要返回的行数和列数。

```
OFFSET(reference, rows, cols, [height], [width])
OFFSET 函数语法具有下列参数：引用必需。
 要以其为偏移量的底数的引用。
 引用必须是对单元格或相邻的单元格区域的引用；否则OFFSET 返回 错误值 #VALUE!。
Rows必需。
 需要左上角单元格引用的向上或向下行数。
 使用 5 作为 rows 参数，可指定引用中的左上角单元格为引用下方的 5 行。
 Rows 可为正数（这意味着在起始引用的下方）或负数（这意味着在起始引用的上方）。
Cols必需。
 需要结果的左上角单元格引用的从左到右的列数。
 使用 5 作为 cols 参数，可指定引用中的左上角单元格为引用右方的 5 列。
 Cols 可为正数（这意味着在起始引用的右侧）或负数（这意味着在起始引用的左侧）。
高度可选。
 需要返回的引用的行高。
 Height 必须为正数。
宽度可选。
 需要返回的引用的列宽。
 Width 必须为正数。

```
## OR
> 它是一个逻辑函数，用于确定测试中的所有条件是否均为 TRUE。

```

```
## PDURATION 
> 返回投资到达指定值所需的期数。

```
PDURATION(rate, pv, fv)
rate必需。
 rate 为每期利率。
pv   必需。
 pv 为投资的现值。
fv必需。
 fv 为所需的投资未来值。

```
## PEARSON
> 返回 Pearson 乘积矩相关系数
```
PEARSON(array1, array2)
array1必需。
 自变量集合。
array2必需。
 因变量集合。

```
## PERCENTILE
> 返回区域中数值的第 k 个百分点的值。
 可以使用此函数来确定接受的阈值。
 例如，可以决定检查得分高于第 90 个百分点的候选人。

```
PERCENTILE(array,k)
array必需。
定义相对位置的数组或数据区域。
k必需。
 0 到 1 之间的百分点值，包含 0 和 1。

```
## PERCENTILE.EXC 
> 返回某个区域中的数值的第 k 个百分点值，此处的 k 的范围为 0 到 1（不含 0 和 1）
```
PERCENTILE.EXC(array,k)
array必需。
定义相对位置的数组或数据区域。
k必需。
 0 到 1 之间的百分点值，不包含 0 和 1。

```
## PERCENTILE.INC 
> 返回区域中数值的第 k 个百分点的值
```
PERCENTILE.INC(array,k)
array必需。
定义相对位置的数组或数据区域。
k必需。
 0 到 1 之间的百分点值，包含 0 和 1。

```
## PERCENTRANK
> 将某个数值在数据集中的排位作为数据集的百分比值返回，此处的百分比值的范围为 0 到 1。
 此函数可用于计算值在数据集内的相对位置。
 例如，可以使用 PERCENTRANK 计算能力测试得分在所有测试得分中的位置。

```
PERCENTRANK(array,x,[significance])
array必需。
 定义相对位置的数值数组或数值数据区域。
x   必需。
 需要得到其排位的值。
significance可选。
 用于标识返回的百分比值的有效位数的值。
 如果省略，则 PERCENTRANK 使用 3 位小数 (0.xxx)
。

```
## PERCENTRANK.EXC 
> 将某个数值在数据集中的排位作为数据集的百分点值返回，此处的百分点值的范围为 0 到 1（不含 0 和 1）
```
PERCENTRANK.EXC(array,x,[significance])
array必需。
 定义相对位置的数值数组或数值数据区域。
x必需。
 需要得到其排位的值。
significance可选。
 用于标识返回的百分比值的有效位数的值。
 如果省略，则 PERCENTRANK.EXC 使用 3 位小数 (0.xxx)
。

```
## PERCENTRANK.INC 
> 返回数据集中值的百分比排位
```
PERCENTRANK.INC(array,x,[significance])
array必需。
 定义相对位置的数值数组或数值数据区域。
x   必需。
 需要得到其排位的值。
significance   可选。
 用于标识返回的百分比值的有效位数的值。
 如果省略，则 PERCENTRANK.INC 使用 3 位小数 (0.xxx)
。

```
## PERMUT
> 返回给定数目对象的排列数
```
PERMUT(number, number_chosen)
number必需。
 表示对象个数的整数。
number_chosen必需。
 表示每个排列中对象个数的整数。

```
## PERMUTATIONA 
> 返回可从总计对象中选择的给定数目对象（含重复）的排列数
```
PERMUTATIONA(number, number-chosen)
number  必需。
表示对象总数的整数。
number_chosen   必需。
 表示每个排列中对象数目的整数。

```
## PHI 
> 返回标准正态分布的密度函数值
```
PHI(x)
x   必需。
 X 是所需的标准正态分布密度值。

```
## PHONETIC
> 提取文本字符串中的拼音（汉字注音）字符。
该函数只适用于日文版。

```
PHONETIC(reference)
reference必需。
文本字符串或对单个单元格或包含 furigana 文本字符串的单元格区域的引用。

```
## PI
> 返回数字 3.14159265358979（数学常量 pi），精确到 15 个数字。

```
PI 函数语法没有参数
```
## PMT
> PMT 是一个财务函数，用于根据固定付款额和固定利率计算贷款的付款额。

```
PMT(rate, nper, pv, [fv], [type])
rate  必需。
 贷款利率。
nper 必需。
 该项贷款的付款总数。
pv  必需。
 现值，或一系列未来付款额现在所值的总额，也叫本金。
fv   可选。
 未来值，或在最后一次付款后希望得到的现金余额。
 如果省略 fv，则假定其值为 0（零），即贷款的未来值是 0。
type可选。
 数字 0（零）或 1 指示支付时间。
type 支付时间0 或省略  期末1   期初
```
## POISSON
> 返回泊松分布。
 泊松分布的一个常见应用是预测特定时间内的事件数，例如 1 分钟内到达收费停车场的汽车数。

```
POISSON(x,mean,cumulative)
x  必需。
 事件数。
mean   必需。
 期望值。
cumulative必需。
 一逻辑值，确定所返回的概率分布的形式。
 如果 cumulative 为 TRUE，则 POISSON 返回发生的随机事件数在零（含零）和 x（含 x）之间的累积泊松概率；如果为 FALSE，则 POISSON 返回发生的事件数正好是 x 的泊松概率密度函数。

```
## POISSON.DIST 
> 返回泊松分布
```
POISSON.DIST(x,mean,cumulative)
x必需。
 事件数。
mean必需。
 期望值。
cumulative必需。
 一逻辑值，确定所返回的概率分布的形式。
 如果 cumulative 为 TRUE，则 POISSON.DIST 返回发生的随机事件数在零（含零）和 x（含 x）之间的累积泊松概率；如果为 FALSE，则 POISSON 返回发生的事件数正好是 x 的泊松概率密度函数。

```
## POWER
> 返回数字乘幂的结果。

```
POWER(number, power)
number必需。
 基数。
 可为任意实数。
power必需。
 基数乘幂运算的指数。

```
## PPMT
> 返回根据定期固定付款和固定利率而定的投资在已知期间内的本金偿付额。

```
PPMT(rate, per, nper, pv, [fv], [type])
rate  必需。
 各期利率。
per   必需。
 指定期数，该值必须在 1 到 nper 范围内。
nper 必需。
年金的付款总期数。
pv 必需。
现值即一系列未来付款当前值的总和。
fv   可选。
 未来值，或在最后一次付款后希望得到的现金余额。
 如果省略 fv，则假定其值为 0（零），即贷款的未来值是 0。
type可选。
 数字 0 或 1，用以指定各期的付款时间是在期初还是期末。
type  支付时间0 或省略   期末1期初
```
## PRICE
> 返回定期付息的面值 ￥100 的有价证券的价格。

```
PRICE(settlement, maturity, rate, yld, redemption, frequency, [basis])
PRICE 函数语法具有下列参数：Settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
Maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
Rate必需。
 有价证券的年息票利率。
Yld必需。
 有价证券的年收益率。
Redemption必需。
 面值 ￥100 的有价证券的清偿价值。
Frequency必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
Basis可选。
 要使用的日计数基准类型。
Basis日计数基准0 或省略  US (NASD)
 30/3601   实际/实际2   实际/3603   实际/3654   欧洲 30/360
```
## PRICEDISC
> 返回折价发行的面值 ￥100 的有价证券的价格。

```
PRICEDISC(settlement, maturity, discount, redemption, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity 必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
discount 必需。
 有价证券的贴现率。
redemption必需。
 面值 ￥100 的有价证券的清偿价值。
basis可选。
 要使用的日计数基准类型。
basis   日计数基准0 或省略 US (NASD)
 30/3601  实际/实际2  实际/3603  实际/3654  欧洲 30/360
```
## PRICEMAT
> 返回到期付息的面值 ￥100 的有价证券的价格。

```
PRICEMAT(settlement, maturity, issue, rate, yld, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity 必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
issue必需。
 有价证券的发行日，以时间序列号表示。
rate  必需。
 有价证券在发行日的利率。
yld必需。
 有价证券的年收益率。
basis可选。
 要使用的日计数基准类型。
basis 日计数基准0 或省略   US (NASD)
 30/3601实际/实际2实际/3603实际/3654欧洲 30/360
```
## PROB
> 返回区域中的数值落在指定区间内的概率
```
PROB(x_range, prob_range, [lower_limit], [upper_limit])
x_range必需。
 具有各自相应概率值的 x 数值区域。
prob_range必需。
 与 x_range 中的值相关联的一组概率值。
lower_limit可选。
 要计算其概率的数值下界。
upper_limit可选。
 要计算其概率的可选数值上界。

```
## PRODUCT
> PRODUCT 函数使所有以参数形式给出的数字相乘并返回乘积。
 例如，如果单元格 A1 和 A2 中包含数字，则可以使用公式 =PRODUCT(A1,A2)
 将这两个数字相乘。
 您也可以通过使用乘 (*)
 数学运算符（例如 =A1*A2）执行相同的操作。

```
PRODUCT(number1, [number2], ...)
number1必需。
 要相乘的第一个数字或范围。
number2, ...可选。
 要相乘的其他数字或单元格区域，最多可以使用 255 个参数。

```
## PROPER
> 将文本字符串的首字母以及文字中任何非字母字符之后的任何其他字母转换成大写。
 将其余字母转换为小写。

```
PROPER(text)
text必需。
 用引号括起来的文本、返回文本值的公式，或者对包含要进行部分大写转换文本的单元格的引用。

```
## PV
> PV 是一个财务函数，用于根据固定利率计算贷款或投资的现值。
 可以将 PV 与定期付款、固定付款（如按揭或其他贷款）或投资目标的未来值结合使用。

```
PV(rate, nper, pmt, [fv], [type])
rate必需。
 各期利率。
 例如，如果您获得年利率为 10% 的汽车贷款，并且每月还款一次，则每月的利率为 10%/12（即 0.83%）。
 您需要在公式中输入 10%/12（即 0.83%）或 0.0083 作为利率。
nper必需。
 年金的付款总期数。
 例如，如果您获得为期四年的汽车贷款，每月还款一次，则贷款期数为 4*12（即 48）期。
 您需要在公式中输入 48 作为 nper。
pmt必需。
 每期的付款金额，在年金周期内不能更改。
 通常，pmt 包括本金和利息，但不含其他费用或税金。
 例如，对于金额为 ￥100,000、利率为 12% 的四年期汽车贷款，每月付款为 ￥2633.30。
 您需要在公式中输入 -2633.30 作为 pmt。
 如果省略 pmt，则必须包括 fv 参数。
fv可选。
 未来值，或在最后一次付款后希望得到的现金余额。
 如果省略 fv，则假定其值为 0（例如，贷款的未来值是 0）。
 例如，如果要在 18 年中为支付某个特殊项目而储蓄 ￥500,000，则 ￥500,000 就是未来值。
 然后，您可以对利率进行保守的猜测，并确定每月必须储蓄的金额。
 如果省略 fv，则必须包括 pmt 参数。
type可选。
 数字 0 或 1，用以指定各期的付款时间是在期初还是期末。
type支付时间0 或省略 期末1  期初
```
## QUARTILE
> 返回一组数据的四分位点。
 四分位点通常用于销售和调查数据，以对总体进行分组。
 例如，您可以使用 QUARTILE 查找总体中前 25% 的收入值。

```
QUARTILE(array,quart)
array必需。
 要求得四分位数值的数组或数字型单元格区域。
quart必需。
 指定返回哪一个值。

```
## QUARTILE.EXC 
> 基于百分点值返回数据集的四分位，此处的百分点值的范围为 0 到 1（不含 0 和 1）
```
QUARTILE.EXC(array,quart)
array必需。
 要求得四分位数值的数组或数字型单元格区域。
quart必需。
 指定返回哪一个值。

```
## QUARTILE.INC 
> 返回一组数据的四分位点
```
QUARTILE.INC(array,quart)
array必需。
 要求得四分位数值的数组或数字型单元格区域。
quart必需。
 指定返回哪一个值。
如果 quart 等于 函数 QUARTILE.INC 返回0  最小值1  第一个四分位数（第 25 个百分点值）2  中分位数（第 50 个百分点值）3  第三个四分位数（第 75 个百分点值）4  最大值
```
## QUOTIENT
> 返回除法的整数部分。
 要放弃除法的余数时，可使用此函数。

```
QUOTIENT(numerator, denominator)
numerator必需。
 被除数。
denominator必需。
 除数。

```
## RADIANS
> 将度数转换为弧度。

```
RADIANS(angle)
angle必需。
 要转换的以度数表示的角度。

```
## RAND
> RAND 返回了一个大于等于 0 且小于 1 的平均分布的随机实数。
每次计算工作表时都会返回一个新的随机实数。

```
RAND 函数语法没有参数。

```
## RANDARRAY
> 返回随机数字的数组。
你可以指定要填充的行数和列数、最小值和最大值, 以及是返回整数还是十进制值。

```
 RANDARRAY ([rows], [columns], [min], [max], [whole_number])
rows  要返回的行数columns  要返回的列数min   你希望返回的最小数量max   你希望返回的最大数量whole_number   返回整数或十进制值。
对于整数, 为 TRUE，如果为 FALSE, 则返回十进制数。

```
## RANDBETWEEN
> 返回位于两个指定数之间的一个随机整数。
 每次计算工作表时都将返回一个新的随机整数。

```
RANDBETWEEN(bottom, top)
bottom必需。
 RANDBETWEEN 将返回的最小整数。
top必需。
 RANDBETWEEN 将返回的最大整数。

```
## RANK
> 返回一列数字的数字排位。
 数字的排位是其相对于列表中其他值的大小。
 （如果要对列表进行排序，则数字排位可作为其位置。
）
```
RANK(number,ref,[order])
number必需。
 要找到其排位的数字。
ref 必需。
 数字列表的数组，对数字列表的引用。
 Ref 中的非数字值会被忽略。
order可选。
 一个指定数字排位方式的数字。
  如果 order 为 0（零）或省略，Microsoft Excel 对数字的排位是基于 ref 为按照降序排列的列表。
   如果 order 不为零，Microsoft Excel 对数字的排位是基于 ref 为按照升序排列的列表。

```
## RANK.AVG 
> 返回一列数字的数字排位
```
RANK.AVG(number,ref,[order])
number必需。
 要找到其排位的数字。
ref必需。
 数字列表的数组，对数字列表的引用。
 Ref 中的非数字值会被忽略。
order可选。
 一个指定数字排位方式的数字。

```
## RANK.EQ 
> 返回一列数字的数字排位。
 其大小与列表中其他值相关；如果多个值具有相同的排位，则返回该组值的最高排位。

```
RANK.EQ(number,ref,[order])
number必需。
 要找到其排位的数字。
ref必需。
 数字列表的数组，对数字列表的引用。
 Ref 中的非数字值会被忽略。
order可选。
 一个指定数字排位方式的数字。

```
## RATE
> 返回年金每期的利率。
 RATE 是通过迭代计算的，可以有零或多个解法。
 如果在 20 次迭代之后，RATE 的连续结果不能收敛于 0.0000001 之内，则 RATE 返回 错误值 #NUM!。

```
RATE(nper, pmt, pv, [fv], [type], [guess])
nper必需。
年金的付款总期数。
pmt必需。
 每期的付款金额，在年金周期内不能更改。
 通常，pmt 包括本金和利息，但不含其他费用或税金。
 如果省略 pmt，则必须包括 fv 参数。
pv必需。
现值即一系列未来付款当前值的总和。
Fv可选。
未来值，或在最后一次付款后希望得到的现金余额。
如果省略 fv，则假定其值为 0（例如，贷款的未来值是 0）。
如果省略 fv，则必须包括 pmt 参数。
type可选。
 数字 0 或 1，用以指定各期的付款时间是在期初还是期末。
type 支付时间0 或省略  期末1   期初guess可选。
 预期利率。
如果省略 guess，则假定其值为 10%。
如果 RATE 不能收敛，请尝试不同的 guess 值。
 如果 guess 在 0 和 1 之间，RATE 通常会收敛。

```
## RECEIVED
> 返回一次性付息的有价证券到期收回的金额。

```
RECEIVED(settlement, maturity, investment, discount, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
investment必需。
 有价证券的投资额。
discount 必需。
 有价证券的贴现率。
basis   可选。
 要使用的日计数基准类型。
basis   日计数基准0 或省略 US (NASD)
 30/3601  实际/实际2  实际/3603  实际/3654  欧洲 30/360
```
## REGISTER.ID
> 返回已注册过的指定动态链接库 (DLL)
 或代码源的注册号
```
REGISTER.ID(module_text,procedure,[type_text])
module_text必需。
文本，用于指定 Microsoft Excel for Windows 中包含函数的 DLL 的名称。
procedure必需。
用于指定 Microsoft Excel for Windows 的 DLL 中的函数名称的文本。
还可以使用函数的序数值，该值来自模块定义文件 (.DEF)
 中的 EXPORTS 语句。
序数值或源 ID 号不能为文本形式。
type_text可选。
指定返回值的数据类型以及 DLL 的所有参数的数据类型的文本。
Type_text 的首字母指定返回值。
如果函数或代码源已经注册过，则可以省略此参数。

```
## REPLACE
> 替换文本中的字符
```
REPLACE(old_text, start_num, num_chars, new_text)
old_text必需。
 要替换其部分字符的文本。
start_num必需。
 old_text 中要替换为 new_text 的字符位置。
num_chars必需。
 old_text 中希望 REPLACE 使用 new_text 来进行替换的字符数。
new_text必需。
 将替换 old_text 中字符的文本。

```
## REPLACEB
> 替换文本中的字节
```
REPLACEB(old_text, start_num, num_bytes, new_text)
old_text必需。
 要替换其部分字符的文本。
start_num  必需。
 old_text 中要替换为 new_text 的字符位置。
num_bytes必需。
old_text 中希望 REPLACEB 使用 new_text 来进行替换的字节数。
new_text必需。
 将替换 old_text 中字符的文本。

```
## REPT
> 按给定次数重复文本
```
REPT(text, number_times)
text必需。
 需要重复显示的文本。
number_times必需。
 用于指定文本重复次数的正数。

```
## RIGHT
> 根据所指定的字符数返回文本字符串中最后一个或多个字符。

```
RIGHT(text,[num_chars])
text必需。
 包含要提取字符的文本字符串。
num_chars可选。
 指定希望 RIGHT 提取的字符数。

```
## RIGHTB
> 根据所指定的字节数返回文本字符串中最后一个或多个字符。

```
RIGHTB(text,[num_bytes])
text必需。
 包含要提取字符的文本字符串。
num_bytes可选。
 按字节指定要由 RIGHTB 提取的字符的数量。

```
## ROMAN
> 将阿拉伯数字转换为文字形式的罗马数字
```
ROMAN(number, [form])
number必需。
 需要转换的阿拉伯数字。
form可选。
指定所需罗马数字类型的数字。
罗马数字样式的范围从古典到简化，形式值越大，样式越简明。
请参阅以下示例 ROMAN(499,0)
。
form Type0 或省略  古典。
1   更简明。
 请参阅下面的示例。
2   更简明。
 请参阅下面的示例。
3   更简明。
 请参阅下面的示例。
4   简化。
TRUE古典。
FALSE   简化。

```
## ROUND
> ROUND 函数将数字四舍五入到指定的位数。

```
ROUND(number, num_digits)
number必需。
 要四舍五入的数字。
num_digits必需。
 要进行四舍五入运算的位数。

```
## ROUNDDOWN
> 朝着零的方向将数字进行向下舍入。

```
ROUNDDOWN(number, num_digits)
number必需。
需要向下舍入的任意实数。
num_digits必需。
要将数字舍入到的位数。

```
## ROUNDUP
> 朝着远离 0（零）的方向将数字进行向上舍入。

```
ROUNDUP(number, num_digits)
number必需。
需要向上舍入的任意实数。
num_digits必需。
要将数字舍入到的位数。

```
## ROW
> 返回引用的行号。

```
ROW([reference])
reference可选。
 需要得到其行号的单元格或单元格区域。
  如果省略 reference，则假定是对函数 ROW 所在单元格的引用。
  如果 reference 为一个单元格区域，并且 ROW 作为垂直数组输入，则 ROW 将以垂直数组的形式返回 reference 的行号。
   reference 不能引用多个区域。

```
## ROWS
> 返回引用或数组的行数。

```
ROWS(array)
array必需。
 需要得到其行数的数组、数组公式或对单元格区域的引用。

```
## RRI 
> 返回投资增长的等效利率。

```
RRI(nper, pv, fv)
nper必需。
 Nper 为投资的期数。
pv必需。
 Pv 为投资的现值。
fv 必需。
 Fv 为投资的未来值。

```
## RSQ
> 返回 Pearson 乘积矩相关系数的平方
```
RSQ(known_y's,known_x's)
known_y's必需。
 数组或数据点区域。
known_x's必需。
 数组或数据点区域。

```
## RTD
> 从支持 COM 自动化的程序中检索实时数据
```
RTD(ProgID, server, topic1, [topic2], ...)
ProgID必需。
 已安装在本地计算机上的已注册 COM 自动化加载项 ProgID 的名称。
 将该名称用引号括起来。
server必需。
应运行加载项的服务器的名称。
如果没有服务器，则在本地运行程序，将此参数保留为空。
否则，输入引号 ()
 将服务器名称括起来。
在 Visual Basic for Applications (VBA)
 中使用 RTD 时，服务器需要双引号或 VBA Nullstring 属性，即使在本地运行服务器也不例外。
topic1, topic2, ...topic1 是必需的，后续主题是可选的。
 1 到 253 个参数，这些参数放在一起代表一个唯一的实时数据。

```
## SEARCH
> 在一个文本值中查找另一个文本值（不区分大小写）
```
SEARCH(find_text,within_text,[start_num])
find_text必需。
要查找的文本。
within_text必需。
要在其中搜索 find_text 参数的值的文本。
start_num可选。
within_text 参数中从之开始搜索的字符编号。

```
## SEARCHB
> 在一个文本值中查找另一个文本值（不区分大小写）
```
SEARCH(find_text,within_text,[start_num])
find_text必需。
要查找的文本。
within_text必需。
要在其中搜索 find_text 参数的值的文本。
start_num可选。
within_text 参数中从之开始搜索的字符编号。

```
## SEC 
> 返回角度的正割值。

```
SEC(number)
number必需。
 Number 为要获得其正割值的角度，以弧度表示。

```
## SECH 
> 返回角度的双曲正割值。

```
SECH(number)
number必需。
 Number 为对应所需双曲正割值的角度，以弧度表示。

```
## SECOND
> 返回时间值的秒数。
 秒数是 0（零）到 59 范围内的整数。

```
SECOND(serial_number)
serial_number必需。
 一个时间值，其中包含要查找的秒数。
 时间值有多种输入方式：带引号的文本字符串（例如 6:45 PM）、十进制数（例如 0.78125 表示 6:45 PM）或其他公式或函数的结果（例如 TIMEVALUE(6:45 PM)
）。

```
## SEQUENCE
> 在数组中生成一系列连续数字
```
SEQUENCE(rows,[columns],[start],[step])
rows必需。
要返回的行数columns  可选。
要返回的列数start 可选。
序列中第一个数字step 可选。
数组中每个连续值递增的值
```
## SERIESSUM
> 返回幂级数的和。

```
SERIESSUM(x, n, m, coefficients)
x必需。
 幂级数的输入值。
n必需。
 x 的首项乘幂。
m必需。
 级数中每一项的乘幂 n 的步长增加值。
coefficients必需。
 与 x 的每个连续乘幂相乘的一组系数。
 coefficients 中的值的数量决定了幂级数中的项数。
 例如，如果 coefficients 中有三个值，则幂级数中将有三项。

```
## SHEET 
> 返回引用工作表的工作表编号。

```
SHEET(value)
value可选。
 Value 为所需工作表编号的工作表或引用的名称。
 如果 Value 被省略，则 SHEET 返回含有该函数的工作表编号。

```
## SHEETS 
> 返回引用中的工作表数。

```
SHEETS(reference)
reference可选。
 Reference 指一项引用，此函数要获得引用中所包含的工作表数。
 如果 Reference 被省略，SHEETS 返回工作簿中含有该函数的工作表数。

```
## SIGN
> 确定数字的符号。
 如果数字为正数，则返回 1；如果数字为 0，则返回零 (0)
；如果数字为负数，则返回 -1。

```
SIGN(number)
number必需。
 任意实数。

```
## SIN
> 返回已知角度的正弦。

```
Sin( number )
number必需。
 需要求正弦的角度，以弧度表示。

```
## SINGLE
> SINGLE 函数将使用称为绝对交集的逻辑返回单个值。
SINGLE 可能返回一个值、一个单元格区域或一个错误。

```
SINGLE(value)
value必需。
要使用绝对交集求值的值。

```
## SINH
> 返回数字的双曲正弦。

```
SINH(number)
number必需。
 任意实数。

```
## SKEW
> 返回分布的不对称度
```
SKEW(number1, [number2], ...)
number1, number2, ...Number1 是必需的，后续数字是可选的。
 用于计算偏斜度的 1 到 255 个参数。
 也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## SKEW.P 
> 返回一个分布的不对称度：用来体现某一分布相对其平均值的不对称程度
```
SKEW.P(number1, [number2],…)
number1, number2,…number1 是必选项，后续数字是可选项。
number1、number2、… 等是 1 至 254 个数字，或包含数字的名称、数组或引用，您要以此函数获得其样本总体的分布不对称度。

```
## SLN
> 返回一个期间内的资产的直线折旧。

```
SLN(cost, salvage, life)
cost 必需。
 资产原值。
salvage必需。
 折旧末尾时的值（有时也称为资产残值）。
life必需。
 资产的折旧期数（有时也称作资产的使用寿命）。

```
## SLOPE
> 返回线性回归线的斜率
```
SLOPE(known_y's, known_x's)
known_y's必需。
 数字型因变量数据点数组或单元格区域。
known_x's必需。
 自变量数据点集合。

```
## SMALL
> 返回数据集中的第 k 个最小值
```
SMALL(array,k)
array必需。
 需要找到第 k 个最小值的数组或数值数据区域。
k必需。
 要返回的数据在数组或数据区域里的位置（从小到大）。

```
## SORT
> SORT 函数可对某个区域或数组的内容进行排序。

```
SORT(array,[sort_index],[sort_order],[by_col])
array   必需。
要排序的区域或数组sort_index可选。
一个数字，表示要按其排序的行或列sort_order可选。
一个数字，表示所需的排序顺序；1 表示升序（默认值），-1 表示降序by_col可选
```
## SORTBY
> SORTBY 函数基于相应范围或数组中的值对范围或数组的内容进行排序。

```
SORTBY (array, by_array1, [sort_order1], [by_array2], [sort_order2],...)
array 必需。
要进行排序的数组或区域by_array1 必需。
要对其进行排序的数组或区域sort_order1可选。
要用于排序的顺序。
1 表示升序，-1 表示降序by_array2   可选。
要对其进行排序的数组或区域sort_order2可选。
要用于排序的顺序。

```
## SQRT
> 返回正的平方根。

```
SQRT(number)
number必需。
 要计算其平方根的数字。

```
## SQRTPI
> 返回某数与 pi 的乘积的平方根。

```
SQRTPI(number)
number必需。
 与 pi 相乘的数。

```
## STANDARDIZE
> 返回正态化数值
```
STANDARDIZE(x, mean, standard_dev)
x必需。
 需要进行正态化的数值。
mean必需。
分布的算术平均值。
standard_dev必需。
分布的标准偏差。

```
## STDEV
> 根据样本估计标准偏差。
标准偏差可以测量值在平均值（中值）附近分布的范围大小。

```
STDEV(number1,[number2],...)
number1必需。
对应于总体样本的第一个数值参数。
number2, ...可选。
对应于总体样本的 2 到 255 个数值参数。
  也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## STDEV.P 
> 基于整个样本总体计算标准偏差
```
STDEV.P(number1,[number2],...)
number1必需。
对应于总体的第一个数值参数。
number2, ...可选。
对应于总体的 2 到 254 个数值参数。
也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## STDEV.S 
> 基于样本估算标准偏差
```
STDEV.S(number1,[number2],...)
number1必需。
对应于总体样本的第一个数值参数。
也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。
number2, ...可选。
对应于总体样本的 2 到 254 个数值参数。
也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## STDEVA
> 基于样本（包括数字、文本和逻辑值）估算标准偏差
```
STDEVA(value1, [value2], ...)
value1, value2, ...value1 是必需的，后续值是可选的。
 对应于总体样本的 1 到 255 个值。
 也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## STDEVP
> 根据作为参数给定的整个总体计算标准偏差。
标准偏差可以测量值在平均值（中值）附近分布的范围大小。

```
STDEVP(number1,[number2],...)
number1必需。
对应于总体的第一个数值参数。
number2, ...   可选。
对应于总体的 2 到 255 个数值参数。
 也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## STDEVPA
> 基于样本总体（包括数字、文本和逻辑值）计算标准偏差
```
STDEVPA(value1, [value2], ...)
value1, value2, ...value1 是必需的，后续值是可选的。
 对应于总体的 1 到 255 个值。
 也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## STEYX
> 返回通过线性回归法预测每个 x 的 y 值时所产生的标准误差
```
STEYX(known_y's, known_x's)
known_y's必需。
 因变量数据点数组或区域。
known_x's必需。
 自变量数据点数组或区域。

```
## SUBSTITUTE
> 在文本字符串中用新文本替换旧文本
```
SUBSTITUTE(text, old_text, new_text, [instance_num])
text必需。
 需要替换其中字符的文本，或对含有文本（需要替换其中字符）的单元格的引用。
old_text必需。
 需要替换的文本。
new_text必需。
 用于替换 old_text 的文本。
Instance_num可选。
 指定要用 new_text 替换 old_text 的事件。
 如果指定了 instance_num，则只有满足要求的 old_text 被替换。
 否则，文本中出现的所有 old_text 都会更改为 new_text。

```
## SUBTOTAL
> 返回列表或数据库中的分类汇总。
通常，使用 Excel 桌面应用程序中“数据”选项卡上“大纲”组中的“分类汇总”命令更便于创建带有分类汇总的列表。
一旦创建了分类汇总列表，就可以通过编辑 SUBTOTAL 函数对该列表进行修改。

```
SUBTOTAL(function_num,ref1,[ref2],...)
function_num 必需。
 数字 1-11 或 101-111，用于指定要为分类汇总使用的函数。
 如果使用 1-11，将包括手动隐藏的行，如果使用 101-111，则排除手动隐藏的行；始终排除已筛选掉的单元格。
function_num（包含隐藏值） function_num（忽略隐藏值） 函数1101AVERAGE2102COUNT3103COUNTA4104MAX5105MIN6106PRODUCT7107STDEV8108STDEVP9109SUM10  110VAR11  111VARPref1必需。
要对其进行分类汇总计算的第一个命名区域或引用。
ref2,...可选。
要对其进行分类汇总计算的第 2 个至第 254 个命名区域或引用。

```
## SUM
> 求和函数，将单个值、单元格引用或是区域相加，或者将三者的组合相加。

```
SUM(number1,[number2],...)
number1   必需。
要相加的第一个数字。
该数字可以是 4 之类的数字，B6 之类的单元格引用或 B2:B8 之类的单元格范围。
number2-255   可选。
这是要相加的第二个数字。
可以按照这种方式最多指定 255 个数字。

```
## SUMIF
> 对 范围 中符合指定条件的值求和。
例如，如果某列中含有数字，你只需对大于 5 的数值求和。
可使用以下公式：=SUMIF(B2:B25,>5)

```
SUMIF(range, criteria, [sum_range])
SUMIF 函数语法具有以下参数：range   必需。
根据条件进行计算的单元格的区域。
每个区域中的单元格必须是数字或名称、数组或包含数字的引用。
空值和文本值将被忽略。
所选区域可以包含标准 Excel 格式的日期（示例如下）。
criteria   必需。
用于确定对哪些单元格求和的条件，其形式可以为数字、表达式、单元格引用、文本或函数。
例如，条件可以表示为 32、>32、B5、32、苹果 或 TODAY()
。
sum_range   可选。
要求和的实际单元格（如果要对未在 range 参数中指定的单元格求和）。
如果省略 sum_range 参数，Excel 会对在 range 参数中指定的单元格（即应用条件的单元格）求和。
可以在 criteria 参数中使用通配符 （包括问号 (?)
 和星号 (*)
）。
问号匹配任意单个字符；星号匹配任意一串字符。
如果要查找实际的问号或星号，请在该字符前键入波形符 (~)
。

```
## SUMIFS
> 计算其满足多个条件的全部参数的总量。

```
SUMIFS(sum_range, criteria_range1, criteria1, [criteria_range2, criteria2], ...)
sum_range   必需。
要求和的单元格区域。
criteria_range1   必需。
使用 Criteria1 测试的区域。
criteria_range1 和 criteria1 设置用于搜索某个区域是否符合特定条件的搜索对。
 一旦在该区域中找到了项，将计算 Sum_range 中的相应值的和。
criteria1   必需。
定义将计算 Criteria_range1 中的哪些单元格的和的条件。
 例如，可以将条件输入为 32、>32、B4、苹果 或 32。
criteria_range2, criteria2, …  可选。
附加的区域及其关联条件。
 最多可以输入 127 个区域/条件对。

```
## SUMPRODUCT
> 在给定的几组数组中，将数组间对应的元素相乘，并返回乘积之和。

```
SUMPRODUCT(array1, [array2], [array3], ...)
array1必需。
 其相应元素需要进行相乘并求和的第一个数组参数。
array2, array3,...可选。
 2 到 255 个数组参数，其相应元素需要进行相乘并求和。

```
## SUMSQ
> 返回参数的平方和。

```
SUMSQ(number1, [number2], ...)
number1, number2, ...number1 是必需的，后续数字是可选的。
 要对其求平方和的 1 到 255 个参数。
 也可以用单一数组或对某个数组的引用来代替用逗号分隔的参数。

```
## SUMX2MY2
> 返回两数组中对应数值的平方差之和。

```
SUMX2MY2(array_x, array_y)
array_x必需。
 第一个数组或数值区域。
array_y必需。
 第二个数组或数值区域。

```
## SUMX2PY2
> 返回两数组中对应值的平方和之和。

```
SUMX2PY2(array_x, array_y)
array_x必需。
 第一个数组或数值区域。
array_y必需。
 第二个数组或数值区域。

```
## SUMXMY2
> 返回两数组中对应数值之差的平方和。

```
SUMXMY2(array_x, array_y)
array_x必需。
 第一个数组或数值区域。
array_y必需。
 第二个数组或数值区域。

```
## SWITCH 
> SWITCH 函数根据值列表计算一个值（称为表达式），并返回与第一个匹配值对应的结果。
如果不匹配，则可能返回可选默认值。

```
SWITCH 函数最简单的形式表示：=SWITCH(要转换的值, 要匹配的值1...[2-126], 如存在匹配项1...[2-126]需返回的值, 如不存在匹配需返回的值)
可计算多达 126 个匹配的值和结果。

```
## SYD
> 返回在指定期间内资产按年限总和折旧法计算的折旧。

```
SYD(cost, salvage, life, per)
cost 必需。
 资产原值。
salvage   必需。
 折旧末尾时的值（有时也称为资产残值）。
life   必需。
 资产的折旧期数（有时也称作资产的使用寿命）。
per   必需。
 期间，必须与 life 使用相同的单位。

```
## T
> 返回值引用的文字。

```
T(value)
value必需。
 要测试的值。

```
## T.DIST 
> 返回学生 t-分布的百分点（概率）
```
T.DIST(x,deg_freedom, cumulative)
x必需。
 需要计算分布的数值。
deg_freedom必需。
 一个表示自由度数的整数。
cumulative必需。
 决定函数形式的逻辑值。
 如果 cumulative 为 TRUE，则 T.DIST 返回累积分布函数；如果为 FALSE，则返回概率密度函数。

```
## T.DIST.2T 
> 返回学生 t-分布的百分点（概率）
```
T.DIST.2T(x,deg_freedom)
x必需。
 需要计算分布的数值。
deg_freedom必需。
 一个表示自由度数的整数。

```
## T.DIST.RT 
> 返回学生 t-分布
```
T.DIST.RT(x,deg_freedom)
x必需。
 需要计算分布的数值。
deg_freedom必需。
 一个表示自由度数的整数。

```
## T.INV 
> 返回作为概率和自由度函数的学生 t 分布的 t 值
```
T.INV(probability,deg_freedom)
probability必需。
 与学生的 t 分布相关的概率。
deg_freedom必需。
 代表分布的自由度数。

```
## T.INV.2T 
> 返回学生 t-分布的反函数
```
T.INV.2T(probability,deg_freedom)
T.INV.2T 函数语法具有下列参数：Probability必需。
 与学生的 t 分布相关的概率。
Deg_freedom必需。
 代表分布的自由度数。

```
## T.TEST 
> 返回与学生 t-检验相关的概率
```
T.TEST(array1,array2,tails,type)
array1必需。
 第一个数据集。
array2必需。
 第二个数据集。
tails必需。
 指定分布尾数。
 如果 tails = 1，则 T.TEST 使用单尾分布。
 如果 tails = 2，则 T.TEST 使用双尾分布。
type必需。
 要执行的 t 检验的类型。
如果 type 等于   检验方法1  成对2  双样本等方差假设3  双样本异方差假设
```
## TAN
> 返回已知角度的正切。

```
TAN(number)
number必需。
 要求正切的角度，以弧度表示。

```
## TANH
> 返回数字的双曲正切。

```
TANH(number)
number必需。
 任意实数。

```
## TBILLEQ
> 返回国库券的等效收益率。

```
TBILLEQ(settlement, maturity, discount)
settlement必需。
 国库券的结算日。
 即在发行日之后，国库券卖给购买者的日期。
maturity 必需。
 国库券的到期日。
 到期日是国库券有效期截止时的日期。
discount 必需。
 国库券的贴现率。

```
## TBILLPRICE
> 返回面值 ￥100 的国库券的价格。

```
TBILLPRICE(settlement, maturity, discount)
settlement必需。
 国库券的结算日。
 即在发行日之后，国库券卖给购买者的日期。
maturity 必需。
 国库券的到期日。
 到期日是国库券有效期截止时的日期。
discount 必需。
 国库券的贴现率。

```
## TBILLYIELD
> 返回国库券的收益率。

```
TBILLYIELD(settlement, maturity, pr)
settlement必需。
 国库券的结算日。
 即在发行日之后，国库券卖给购买者的日期。
maturity 必需。
 国库券的到期日。
 到期日是国库券有效期截止时的日期。
pr 必需。
 面值 ￥100 的国库券的价格。

```
## TDIST
> 返回学生 t 分布的百分点（概率），其中，数字值 (x)
 是用来计算百分点的 t 的计算值。
 t 分布用于小型样本数据集的假设检验。
 可以使用该函数代替 t 分布的临界值表。

```
TDIST(x,deg_freedom,tails)
x必需。
 需要计算分布的数值。
deg_freedom  必需。
 一个表示自由度数的整数。
tails必需。
 指定返回的分布函数是单尾分布还是双尾分布。
 如果 Tails = 1，则 TDIST 返回单尾分布。
 如果Tails = 2，则 TDIST 返回双尾分布。

```
## TEXT
> 设置数字格式并将其转换为文本
```
TEXT(value,format_text）value 必须。
为数字值。
format_text   必须。
为设置单元格格式中自己所要选用的文本格式。
format_text说明000.0 小数点前面不够三位以0补齐，保留1位小数，不足一位以0补齐###   没用的0一律不显示00.## 小数点前不足两位以0补齐，保留两位，不足两位不补位正数；负数；零大于0，显示为“正数”；等于0，显示为“零”；小于0，显示为“负数”0000-00-00   按所示形式表示日期0000年00月00日   按所示形式表示日期aaaa   显示为中文星期几全称aaa   显示为中文星期几简称dddd   显示为英文星期几全称[>=90]优秀；[>=60]及格；不及格；   大于等于90，显示为“优秀”；大于等于60，小于90，显示为“及格”；小于60，显示为“不及格”[DBNum1][$-804]G/通用格式中文小写数字[DBNum2][$-804]G/通用格式元整中文大写数字，并加入“元整”字尾[DBNum3][$-804]G/通用格式中文小写数字[DBNum1][$-804]G/通用格式中文小写数字，11-19无设置[>20][DBNum1];[DBNum1]d11-显示为十一而不是一十一0.00,K以千为单位#!.0000万元以万元为单位，保留4位小数#!.0,万元以万元为单位，保留1位小数
```
## TEXTJOIN 
> 将多个区域和/或字符串的文本组合起来，并包括你在要组合的各文本值之间指定的分隔符。
如果分隔符是空的文本字符串，则此函数将有效连接这些区域。

```
TEXTJOIN(separator, ignore_empty, text1, [text2], …)
separator   必须。
文本字符串 (空)
 或一个或多个用双引号括起来的字符, 或对有效文本字符串的引用。
如果提供了一个数字, 它将被视为文本。
ignore_empty   必备。
如果为 TRUE，则忽略空白单元格。
text1必需。
要加入的文本项。
文本字符串或字符串数组, 例如单元格区域。
text2, ...  可选。
要加入的其他文本项。
文本项目最多可以包含252个文本参数, 包括text1。
每个都可以是文本字符串或字符串数组, 例如单元格区域。

```
## TIME
> 它能够在给定时、分、秒三个值的情况下，将三个值合并为一个Excel内部表示时间的小数
```
TIME(hour, minute, second)
hour必需。
 0（零）到 32767 之间的数字，代表小时。
 任何大于 23 的值都会除以 24，余数将作为小时值。
 例如，TIME(27,0,0)
 = TIME(3,0,0)
 = .125 或 3:00 AM。
minute必需。
 0 到 32767 之间的数字，代表分钟。
 任何大于 59 的值将转换为小时和分钟。
 例如，TIME(0,750,0)
 = TIME(12,30,0)
 = .520833 或 12:30 PM。
second必需。
 0 到 32767 之间的数字，代表秒。
 任何大于 59 的值将转换为小时、分钟和秒。
 例如，TIME(0,0,2000)
 = TIME(0,33,22)
 = .023148 或 12:33:20 AM
```
## TIMEVALUE
> 返回由文本字符串表示的时间的十进制数字。
 十进制数字是一个范围在 0（零）到 0.99988426 之间的值，表示 0:00:00 (12:00:00 AM)
 到 23:59:59 (11:59:59 P.M.)
 之间的时间。

```
TIMEVALUE(time_text)
time_text必需。
 一个文本字符串，代表以任一 Microsoft Excel 时间格式表示的时间（例如，代表时间的具有引号的文本字符串 6:45 PM 和 18:45）。

```
## TINV
> 返回学生 t 分布的双尾反函数。

```
TINV(probability,deg_freedom)
probability   必需。
 与双尾学生 t 分布相关的概率。
deg_freedom   必需。
 代表分布的自由度数。

```
## TODAY
> 返回当前日期的序列号。
 序列号是 Excel 用于日期和时间计算的日期-时间代码。

```
TODAY()
TODAY 函数语法没有参数。

```
## TRANSPOSE
> 转置数组或工作表上单元格区域的垂直和水平方向。

```
TRANSPOSE(array)
array 必需。
 需要进行转置的数组或工作表上的单元格区域。
 所谓数组的转置就是，将数组的第一行作为新数组的第一列，数组的第二行作为新数组的第二列，以此类推。
务必在键入公式后按 Ctrl+Shift+Enter。

```
## TREND
> 返回线性趋势值
```
TREND(known_y's, [known_x's], [new_x's], [const])
known_y's必需。
Y 值集您已经知道在关系 y = mx + b。
如果数组 known_y's 在单独一列中，则 known_x's 的每一列被视为一个独立的变量。
如果数组 known_y's 在单独一行中，则 known_x's 的每一行被视为一个独立的变量。
known_x's   必需。
一组可选的 x 值，您可能已经知道关系 y = mx + b。
数组 known_x's 可以包含一组或多组变量。
 如果仅使用一个变量，那么只要 known_x's 和 known_y's 具有相同的维数，则它们可以是任何形状的区域。
 如果用到多个变量，则 known_y's 必须为向量（即必须为一行或一列）。
如果省略 known_x's，则假设该数组为 {1,2,3,...}，其大小与 known_y's 相同。
new_x's 必需。
您要为其返回对应的 y 值的趋势的新 x 的值。
New_x's 与 known_x's 一样，对每个自变量必须包括单独的一列（或一行）。
 因此，如果 known_y's 是单列的，known_x's 和 new_x's 应该有同样的列数。
 如果 known_y's 是单行的，known_x's 和 new_x's 应该有同样的行数。
如果省略 new_x's，将假设它和 known_x's 一样。
如果 known_x's 和 new_x's 都省略，将假设它们为数组 {1,2,3,...}，大小与 known_y's 相同。
const 可选。
一个逻辑值，指定是否强制常量 b 为等于 0。
如果 const 为 TRUE 或省略，b 将按正常计算。
如果 const 为 FALSE，b 将被设为 0（零），m 将被调整以使 y = mx。

```
## TRIM
> 除了单词之间的单个空格之外，移除文本中的所有空格。
 对于从另一个可能含有不规则间距的应用程序收到的文本，可以使用 TRIM。

```
TRIM(text)
text必需。
 要从中移除空格的文本。

```
## TRIMMEAN
> 返回数据集的内部平均值
```
TRIMMEAN(array, percent)
array必需。
 需要进行整理并求平均值的数组或数值区域。
percent必需。
 从计算中排除数据点的分数。
 例如，如果 percent=0.2，从 20 点 (20 x 0.2)
 的数据集中剪裁 4 点：数据集顶部的 2 点和底部的 2 点。

```
## TRUNC
> 将数字的小数部分截去，返回整数。

```
TRUNC(number, [num_digits])
number必需。
 需要截尾取整的数字。
num_digits可选。
 用于指定取整精度的数字。
 num_digits 的默认值为 0（零）。

```
## TTEST
> 返回与学生 t 检验相关的概率。
 使用函数 TTEST 确定两个样本是否可能来自两个具有相同平均值的基础总体。

```
TTEST(array1,array2,tails,type)
array1必需。
 第一个数据集。
array2必需。
 第二个数据集。
tails 必需。
 指定分布尾数。
 如果 tails = 1，则 TTEST 使用单尾分布。
 如果 tails = 2，则 TTEST 使用双尾分布。
type必需。
 要执行的 t 检验的类型。

```
## TYPE
> 返回数值的类型。
 当某一个函数的计算结果取决于特定单元格中数值的类型时，可使用函数 TYPE。

```
TYPE(value)
value必需。
 可以为任意 Microsoft Excel 数值，如数字、文本以及逻辑值等等。
value函数 TYPE 返回数字 1文本 2逻辑值 4误差值 16数组 64
```
## UNICHAR 
> 返回给定数值引用的 Unicode 字符
```
UNICHAR(number)
number必需。
 Number 为代表字符的 Unicode 数字。

```
## UNICODE 
> 返回对应于文本的第一个字符的数字（代码点）
```
Unicode(text)
text必需。
 text 是要获得其 Unicode 值的字符。

```
## UNIQUE
> 返回列表或区域中的唯一值的列表
```

```
## UPPER
> 将文本转换为大写形式
```
UPPER(text)
text必需。
 要转换为大写字母的文本。
 文本可以是引用或文本字符串。

```
## VALUE
> 将文本参数转换为数字
```
VALUE(text)
text必需。
 用引号括起来的文本或包含要转换文本的单元格的引用。

```
## VAR
> 计算基于给定样本的方差。

```
VAR(number1,[number2],...)
number1 必需。
对应于总体样本的第一个数值参数。
number2, ...可选。
对应于总体样本的 2 到 255 个数值参数。

```
## VAR.P 
> 计算基于样本总体的方差
```
VAR.P(number1,[number2],...)
number1必需。
对应于总体的第一个数值参数。
number2, ...可选。
对应于总体的 2 到 254 个数值参数。

```
## VAR.S 
> 基于样本估算方差
```
VAR.S(number1,[number2],...)
number1必需。
对应于总体样本的第一个数值参数。
number2, ...可选。
对应于总体样本的 2 到 254 个数值参数。

```
## VARA
> 基于样本（包括数字、文本和逻辑值）估算方差
```
VARA(value1, [value2], ...)
value1, value2, ...Value1 是必需的，后续值是可选的。
 这些是对应于总体样本的 1 到 255 个数值参数。

```
## VARP
> 根据整个总体计算方差。

```
VARP(number1,[number2],...)
number1必需。
对应于总体的第一个数值参数。
number2,...可选。
对应于总体的 2 到 255 个数值参数。

```
## VARPA
> 基于样本总体（包括数字、文本和逻辑值）计算标准偏差
```
VARPA(value1, [value2], ...)
value1, value2, ...value1 是必需的，后续值是可选的。
 对应于总体的 1 到 255 个值参数。

```
## VDB
> 使用双倍余额递减法或其他指定方法，返回一笔资产在给定期间（包括部分期间）内的折旧值。
 函数 VDB 代表可变余额递减法。

```
VDB(cost, salvage, life, start_period, end_period, [factor], [no_switch])
cost  必需。
 资产原值。
salvage必需。
 折旧末尾时的值（有时也称为资产残值）。
 该值可以是 0。
life必需。
 资产的折旧期数（有时也称作资产的使用寿命）。
start_period必需。
 您要计算折旧的起始时期。
 Start_period 必须与 life 使用相同的单位。
end_period 必需。
 您要计算折旧的终止时期。
 End_period 必须与 life 使用相同的单位。
factor   可选。
 余额递减速率 如果省略 factor，则假定其值为 2（双倍余额递减法）。
 如果不想使用双倍余额递减法，请更改余额递减速率。
 有关双倍余额递减法的说明，请参阅函数 DDB。
no_switch可选。
 逻辑值，指定当折旧值大于余额递减计算值时，是否转用直线折旧法。
  如果 no_switch 为 TRUE，即使折旧值大于余额递减计算值，Microsoft Excel 也不转用直线折旧法。
  如果 no_switch 为 FALSE 或被忽略，且折旧值大于余额递减计算值时，Excel 将转用线性折旧法。

```
## VLOOKUP
> 在数组或表格第一列中查找，将一个数组或表格中一列数据引用到另外一个表中
```
Vlookup（lookup|_value,table_array,col_index_num,range_lookup）lookup|_value 在表格或区域的第一列中要搜索的值。
table_array   包含数据的单元格区域，即要查找的范围。
col_index_num参数中返回的搜寻值的列号。
range_lookup  逻辑值，指定希望Vlookup查找精确匹配值（0）还是近似值（1）。

```
## WEBSERVICE 
> 返回 Web 服务中的数据。

```
WEBSERVICE(url)
url必需。
 Web 服务的 URL。

```
## WEEKDAY
> 返回对应于某个日期的一周中的第几天。
 默认情况下，天数是 1（星期日）到 7（星期六）范围内的整数。

```
WEEKDAY(serial_number,[return_type])
serial_number必需。
 一个序列号，代表尝试查找的那一天的日期。
 应使用 DATE 函数输入日期，或者将日期作为其他公式或函数的结果输入。
 例如，使用函数 DATE(2008,5,23)
 输入 2008 年 5 月 23 日。
 如果日期以文本形式输入，则会出现问题。
return_type可选。
 用于确定返回值类型的数字。
return_type   返回的数字1 或省略   数字 1（星期日）到 7（星期六）。
 同 Microsoft Excel 早期版本。
2数字 1（星期一）到 7（星期日）。
3数字 0（星期一）到 6（星期日）。
11  数字 1（星期一）到 7（星期日）。
12  数字 1（星期二）到数字 7（星期一）。
13  数字 1（星期三）到数字 7（星期二）。
14  数字 1（星期四）到数字 7（星期三）。
15  数字 1（星期五）到数字 7（星期四）。
16  数字 1（星期六）到数字 7（星期五）。
17  数字 1（星期日）到 7（星期六）。

```
## WEEKNUM
> 返回特定日期的周数。
 例如，包含 1 月 1 日的周为该年的第 1 周，其编号为第 1 周。
此函数可采用两种机制：机制 1包含 1 月 1 日的周为该年的第 1 周，其编号为第 1 周。
机制 2包含该年的第一个星期四的周为该年的第 1 周，其编号为第 1 周。
 此机制是 ISO 8601 指定的方法，通常称作欧洲周编号机制。

```
WEEKNUM(serial_number,[return_type])
serial_number必需。
 代表一周中的日期。
 应使用 DATE 函数输入日期，或者将日期作为其他公式或函数的结果输入。
 例如，使用函数 DATE(2008,5,23)
 输入 2008 年 5 月 23 日。
 如果日期以文本形式输入，则会出现问题。
return_type可选。
 一数字，确定星期从哪一天开始。
 默认值为 1。
Return_type  一周的第一天为  机制1 或省略   星期日 12星期一 111  星期一 112  星期二 113  星期三 114  星期四 115  星期五 116  星期六 117  星期日 121  星期一 2
```
## WEIBULL
> 返回 Weibull 分布。
 可以将该分布用于可靠性分析，例如计算设备出现故障的平均时间。

```
WEIBULL(x,alpha,beta,cumulative)
x 必需。
 用来计算函数的值。
alpha  必需。
 分布参数。
beta必需。
 分布参数。
cumulative必需。
 确定函数的形式。

```
## WEIBULL.DIST 
> 返回 Weibull 分布
```
WEIBULL.DIST(x,alpha,beta,cumulative)
x必需。
 用来计算函数的值。
alpha必需。
 分布参数。
beta必需。
 分布参数。
cumulative必需。
 确定函数的形式。

```
## WORKDAY
> 返回在某日期（起始日期）之前或之后、与该日期相隔指定工作日的某一日期的日期值。
 工作日不包括周末和专门指定的假日。
 在计算发票到期日、预期交货时间或工作天数时，可以使用函数 WORKDAY 来扣除周末或假日。

```
WORKDAY(start_date, days, [holidays])
start_date必需。
 一个代表开始日期的日期。
days  必需。
 start_date 之前或之后不含周末及节假日的天数。
 Days 为正值将生成未来日期；为负值生成过去日期。
holidays可选。
一个可选列表，其中包含需要从工作日历中排除的一个或多个日期，例如各种省/市/自治区和国家/地区的法定假日及非法定假日。
该列表可以是包含日期的单元格区域，也可以是由代表日期的序列号所构成的数组常量。

```
## WORKDAY.INTL 
> 返回指定的若干个工作日之前或之后的日期的序列号（使用自定义周末参数）。
 周末参数指明周末有几天以及是哪几天。
 周末和任何指定为假期的日期不被视为工作日。

```
WORKDAY.INTL(start_date, days, [weekend], [holidays])
start_date必需。
 开始日期（将被截尾取整）。
days  必需。
 Start_date 之前或之后的工作日的天数。
 正值表示未来日期；负值表示过去日期；零值表示开始日期。
 Day-offset 将被截尾取整。
weekend可选。
 指示一周中属于周末的日子和不作为工作日的日子。
 Weekend 是一个用于指定周末日的周末数字或字符串。
weekend 数值表示以下周末日：weekend  周末日1 或省略   星期六、星期日2星期日、星期一3星期一、星期二4星期二、星期三5星期三、星期四6星期四、星期五7星期五、星期六11  仅星期日12  仅星期一13  仅星期二14  仅星期三15  仅星期四16  仅星期五17  仅星期六
```
## XIRR
> 返回一组不一定定期发生的现金流的内部收益率。
 若要计算一组定期现金流的内部收益率，请使用函数 IRR。

```
XIRR(values, dates, [guess])
value必需。
 与 dates 中的支付时间相对应的一系列现金流。
 首期支付是可选的，并与投资开始时的成本或支付有关。
 如果第一个值是成本或支付，则它必须是负值。
 所有后续支付都基于 365 天/年贴现。
 值系列中必须至少包含一个正值和一个负值。
date必需。
 与现金流支付相对应的支付日期表。
 日期可按任何顺序排列。
 应使用 DATE 函数输入日期，或者将日期作为其他公式或函数的结果输入。
 例如，使用函数 DATE(2008,5,23)
 输入 2008 年 5 月 23 日。
 如果日期以文本形式输入，则会出现问题 。
guess可选。
 对函数 XIRR 计算结果的估计值。

```
## XNPV
> 返回一组现金流的净现值，这些现金流不一定定期发生。
 若要计算一组定期现金流的净现值，请使用函数 NPV。

```
XNPV(rate, values, dates)
rate必需。
 应用于现金流的贴现率。
values必需。
 与 dates 中的支付时间相对应的一系列现金流。
 首期支付是可选的，并与投资开始时的成本或支付有关。
 如果第一个值是成本或支付，则它必须是负值。
 所有后续支付都基于 365 天/年贴现。
 数值系列必须至少要包含一个正数和一个负数。
dates必需。
 与现金流支付相对应的支付日期表。
 第一个支付日期代表支付表的开始日期。
 其他所有日期应晚于该日期，但可按任何顺序排列。

```
## XOR 
> 返回所有参数的逻辑异或。

```
XOR(logical1, [logical2],…)
logical1、logical2 等logical 1 是必需的，后续逻辑值是可选的。
您要检验的 1 至 254 个条件，可为 TRUE 或 FALSE，且可为逻辑值、数组或引用。

```
## YEAR
> 返回对应于某个日期的年份。
 Year 作为 1900 - 9999 之间的整数返回。

```
YEAR(serial_number)
serial_number必需。
 要查找的年份的日期。
 应使用 DATE 函数输入日期，或者将日期作为其他公式或函数的结果输入。
 例如，使用函数 DATE(2008,5,23)
 输入 2008 年 5 月 23 日。
 如果日期以文本形式输入，则会出现问题。

```
## YEARFRAC
> YEARFRAC计算代表整个 （ start_date和end_date） 的两个日期之间的天数的年分数。
例如，您可以使用YEARFRAC识别整个年的好处或义务要分配给特定术语的比例。

```
YEARFRAC(start_date, end_date, [basis])
start_date必需。
 一个代表开始日期的日期。
end_date必需。
 一个代表终止日期的日期。
basis可选。
 要使用的日计数基准类型。
basis 日计数基准0 或省略   US (NASD)
 30/3601实际/实际2实际/3603实际/3654欧洲 30/360
```
## YIELD
> 返回定期支付利息的债券的收益。
 函数 YIELD 用于计算债券收益率。

```
YIELD(settlement, maturity, rate, pr, redemption, frequency, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
rate必需。
 有价证券的年息票利率。
pr必需。
 有价证券的价格（按面值为 ￥100 计算）。
redemption必需。
 面值 ￥100 的有价证券的清偿价值。
frequency   必需。
 年付息次数。
 如果按年支付，frequency = 1；按半年期支付，frequency = 2；按季支付，frequency = 4。
basis可选。
 要使用的日计数基准类型。
basis日计数基准0 或省略  US (NASD)
 30/3601   实际/实际2   实际/3603   实际/3654   欧洲 30/360
```
## YIELDDISC
> 返回折价发行的有价证券的年收益率。

```
YIELDDISC(settlement, maturity, pr, redemption, [basis])
YIELDDISC 函数语法具有下列参数：Settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
Maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
Pr必需。
 有价证券的价格（按面值为 ￥100 计算）。
Redemption必需。
 面值 ￥100 的有价证券的清偿价值。
Basis可选。
 要使用的日计数基准类型。
Basis日计数基准0 或省略  US (NASD)
 30/3601   实际/实际2   实际/3603   实际/3654   欧洲 30/360
```
## YIELDMAT
> 返回到期付息的有价证券的年收益率。

```
YIELDMAT(settlement, maturity, issue, rate, pr, [basis])
settlement必需。
 有价证券的结算日。
 有价证券结算日是在发行日之后，有价证券卖给购买者的日期。
maturity必需。
 有价证券的到期日。
 到期日是有价证券有效期截止时的日期。
issue必需。
 有价证券的发行日，以时间序列号表示。
rate必需。
 有价证券在发行日的利率。
pr必需。
 有价证券的价格（按面值为 ￥100 计算）。
basis可选。
 要使用的日计数基准类型。
basis 日计数基准0 或省略   US (NASD)
 30/3601实际/实际2实际/3603实际/3654欧洲 30/360
```
## Z.TEST 
> 返回 z 检验的单尾概率值
```
Z.TEST(array,x,[sigma])
array必需。
 用来检验 x 的数组或数据区域。
x必需。
 要测试的值。
sigma可选。
 总体（已知）标准偏差。
 如果省略，则使用样本标准偏差。

```
## ZTEST
> 返回 z 检验的单尾概率值。
 对于给定的假设总体平均值 μ0，ZTEST 返回样本平均值大于数据集（数组）中观察平均值的概率，即观察样本平均值。

```
ZTEST(array,x,[sigma])
array必需。
 用来检验 x 的数组或数据区域。
x   必需。
 要测试的值。
sigma   可选。
 总体（已知）标准偏差。
 如果省略，则使用样本标准偏差。

```
## FALSE
> 返回逻辑值 FALSE。

```

```
## TRUE
> 返回逻辑值 TRUE。
希望基于条件返回值 TRUE 时，可使用此函数。
例如：=IF(A1=1,TRUE())
还可直接在单元格和公式中输入值 TRUE，而不使用此函数。
例如：=IF(A1=1,TRUE)
如果满足条件，Excel 在两个示例中均返回 TRUE。
如果不满足条件，Excel 在两个示例中均返回 FALSE。

```
TRUE()
TRUE 函数语法没有参数。

```
