"""
1.4 百钱百鸡
1．问题描述
中国古代数学家张丘建在他的《算经》中提出了一个著名的“百钱百鸡问题”：一只公鸡值五钱，一只母鸡值三钱，三只小鸡值一钱，现在要用百钱买百鸡，请问公鸡、母鸡、小鸡各多少只？

用百钱如果只买公鸡，最多可以买20只，但题目要求买100只，由此可知，所买公鸡的数量肯定在0～20之间。同理，母鸡的数量在0～33之间。在此不妨把公鸡、母鸡和小鸡的数量分别设为cock、hen、
chicken，则cock+hen+chicken=100，因此百钱买百鸡问题就转化成解不定方程组
x + y + z = 100
5x + 3y + z/3 = 100


3．算法设计
对于不定方程组，我们可以利用穷举循环的方法来解决，也就是通过对未知数可变范围的穷举，验证方程在什么情况下成立，从而得到相应的解。因公鸡的取值范围是0～20，可用循环语句“for cock in
range(0,21);”实现。钱的数量是固定的，要买的鸡的数量也是固定的，所以母鸡数量是受到公鸡数量限制的。同理，小鸡数量受到公鸡和母鸡数量的限制，因此我们可以利用三层循环的嵌套来解决，第一层循环控
制公鸡的数量，第二层控制母鸡的数量，最内层控制小鸡的数量。


4．知识点补充
结构化程序设计包括三种基本结构：顺序结构、选择结构（分支结构）和循环结构（重复结构），利用这三种基本结构可以解决很多复杂问题。
·顺序结构：一种简单的程序设计，按照程序中语句的顺序依次执行，每条语句都能被执行且只执行一次。
·选择结构：包括简单选择和多分支选择结构，可根据条件，判断应该选择哪一条分支来执行相应的语句序列。简单选择结构采用简单或一般的if语句即可解决，对于复杂的选择结构可以使用嵌套的if…elif…
else语句实现。
·循环结构：可根据给定条件，判断是否需要重复执行某一相同程序段。


下面介绍Python语言的循环结构。
（1）while循环
while循环语法格式如下：
while 判断条件:
执行语句
其中，判断条件可以是任何表达式，所有非空、非零的值都为True，当判断条件为False时，循环结束；执行语句可以是单条语句，也可以是一个语句块。

（2）for循环
for循环语法格式如下：
for iterating_var in sequence:
statements(s)，其中，sequence是任意序列，如列表（数组）、字典或元组等，也可以通过range()函数产生一个整数列表，以完成计数循环；iterating_var
是序列中需要遍历的元素；statements是待执行的语句块。
range()函数使用格式如下：
range([start , ] stop[ , step])
其中，start为可选参数，表示起始数；stop为终止数，如果range()函数只有一个参数n，则将产生一个0～(n-1)的整数列表，也就是循环n-1次；step为可选参数，表示循环步长，不写时，默认步长为1。
需要注意的是，while循环结构首先对while条件进行判断，当条件为True时，执行条件语句块；当执行完语句块时，再次判断while条件是否为True，若仍然为True，则继续执行语句块，直到条件为False时结束
循环。
while循环结构的流程图如图1.6所示。

（3）for循环结构
for循环结构首先对for语句的条件判断，游标（序列都会有一个游标，游标一般从第0个位置开始）指向序列的第0个位置，也就是序列的第一个元素，判断序列sequence中是否有元素。如果有，就将这个元素
赋值给iterating_var，然后执行循环体语句块，执行完成后，游标下移一位，再次判断该位置是否有元素；如果有，继续将该元素赋值给iterating_var，继续执行循环语句块；游标再往下移一位，一直循环下
去，直到下一个位置没有元素时结束循环

for循环结构的流程图如图1.7所示。
在循环语句中，循环体可以是由一个或多个语句构成的，当其中某个语句是循环语句时，即一个循环体中完整地包含了另外一个循环，就形成了循环嵌套结构，我们称之为多重循环，并且把这个循环语句称为外层循环语句，而把循环体中的循环语句称为内层循环语句。在理解多
重循环语句时，只要把内层循环语句看作是外层循环语句的循环体的一部分就可以了。在程序执行时，外层循环语句与内层循环语句的关系，有点像钟表的时针与分针的关系，分针走了60格，时针才走1格。对于

多重循环来说，只有内层循环语句执行到判断条件为假时，才返回到其上层循环语句继续执行。


5．确定程序框架
在设计循环时首先要考虑循环的三要素，即循环变量的初值、循环的控制条件和使循环趋于结束的循环变量值的改变。针对本题来说，每层循环的初值是0（即买的100只鸡中，可能没有
公鸡，也可能没有母鸡或小鸡）；循环的控制条件是公鸡、母鸡和小鸡用百钱最多能够买到的数量［根据上面分析可知：公鸡最多20只，母鸡最多33只，小鸡最多100只（虽然百钱最多可以买到300只小鸡，但题目
要求只买100只）］；穷举循环的特点就是把所有情况都考虑到，因此

每层循环执行一次，对应循环变量的值就要加1。程序流程图如图1.8所示


6．确定公鸡、母鸡和小鸡数量
根据这三层循环我们可以得到很多种方案，在这些方案中有些是不符合cock+hen+chicken=100并且5×cock+3×hen+chicken/3=100这两个条件
的。因此结果输出之前我们要把合理的方案筛选出来，即如果结果满足cock+hen+chicken=100和5×cock+3×hen+chicken/3=100，则输出。很明
显，控制条件即为语句if(5×cock+3×hen+chicken/3.0==100)and(cock+hen+chicken==100)。
注意：在Python语言中，使用and关键字表示“逻辑与”；使用or关键字表示“逻辑或”；使用not关键字表示“逻辑非”。
另外，运算符“/”表示除，x除以y，结果为带小数点的浮点数；而运算符“//”表示取整除，返回商的整数部分。


7．完整的程序
根据上面的分析，编写程序如下：
"""


# if __name__=="__main__":
#     # cock表示公鸡数量，hen表示母鸡数量，chicken表示小鸡数量，总共100只
#     # 外层循环控制公鸡数量取值范围为0～20
#     cock = 0
#     while cock <= 20:
#         # 内层循环控制母鸡数量取值范围为0～33
#         hen = 0
#         while hen <= 33:
#             # 内层循环控制小鸡数量取值范围为0～100
#             chicken = 0
#             while chicken <= 100:
#                 # 条件控制
#                 if (5*cock + 3*hen + chicken / 3.0 == 100) and (cock + hen + chicken == 100):
#                     print("cock=%2d,hen=%2d,chicken=%2d\n" % (cock, hen, chicken))
#                 chicken += 1
#             hen += 1
#         cock += 1



"""
9．问题拓展
以上算法需要穷举尝试21×34×101=72 114次，算法的效率显然太低
了。对于这类求解不定方程的问题，各层循环的控制变量直接与方程的
未知数相关，并且采用对未知数的取值范围穷举和组合的方法得到全部
的解。对于本题来说，公鸡的数量确定后，小鸡的数量就固定为100-
cock-hen，无须再进行穷举了，此时约束条件只有一个，即
5×cock+3×hen+chicken/3=100，这样我们利用两重循环即可求解本题，
代码如下：

"""

if __name__=="__main__":
    # 外层循环控制公鸡数量取整范围为0～20
    cock = 0
    while cock <= 20:
        # 内层循环控制母鸡数量取值范围为0～30
        hen = 0
        while hen <= 33:
            # 小鸡的数量
            chicken = 100 - cock - hen
            if 5 * cock + 3 * hen + chicken / 3.0 == 100:
                print("cock=%2d,hen=%2d,chicken=%2d\n" %(cock, hen, chicken))
            hen+=1
        cock+=1



