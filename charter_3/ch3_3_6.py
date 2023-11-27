"""

自守数
1．问题描述
  自守数是指一个数的平方的尾数等于该数自身的自然数。
  例如，5**2=25，25**2=625，76**2=5776，9376**2=87909376。求100 000以内的自守数。

2．问题分析
  根据自守数的定义，求解本题的关键是知道当前所求自然数的位数，以及该数平方的尾数与被乘数、乘数之间的关系。

3．算法设计
    从低位到高位将某个整数拆分。对于一个整数（设变量名为a），无论其位数多少，若欲将最低位拆分则只需对10进行求模运算，即a%10；
    拆分次低位首先要想办法将原来的次低位作为最低位来处理，用原数对10求商可得到由除最低位之外的数形成的新数，且新数的最低
    位是原数的次低位，根据拆分最低位的方法将次低位求出，即先进行a//10运算，后进行a%10运算；对于其他位上的数算法相同。
    利用这个方法要解决的一个问题是，什么情况下才算把所有数都拆分完了呢？当拆分到只剩原数最高位时（即新数为个位数时），再对10求商的话，
    得到的结果肯定为0，可通过这个条件判断是否拆分完毕。根据题意，应将每次拆分出来的数据存储到数组中，原数的最低位存到下标为0的位置，
    次低位存到下标为1的位置，以此类推。程序段如下：

    将数组中元素重新组合成一个新数。拆分时变量a的最高位仍然存储在数组中下标最大的位置，根据“回文数”定义，新数中数据的顺序与a中数据的顺序相反，
    所以我们按照下标从大到小的顺序分别取出数组中的元素组成新数k。由几个数字组成一个新数时只需用每一个数字乘以所在位置对应的权值，然后相加即可，
    在编程过程中应该有一个变量 t来存储每一位对应的权值，个位权值为1，十位权值为10，百位权值为100，以此类推，所以可以利用循环，每循环一次，
    t的值就扩大10倍。对应的程序段如下：

"""


if __name__=="__main__":
    m = [1] * 17
    count = 0
    print("No. number it's square(palindrome)")
    for n in range(1,256):      # 穷举n的取值范围
        k,i,t,a = 0,0,1,n*n     # 计算 n 的平方
        squ = a
        while a != 0:           # 从低到高分解 a 的每一位存于数组 m[1]~m[16]
            m[i] = a % 10
            a //= 10
            i += 1

        while i > 0:
            k += m[i-1] * t     # t 记录某一位置对应的权值
            t *= 10
            i -= 1

        if k == squ:
            count += 1
            print("%2d%10d%10d" % (count, n, n*n))


