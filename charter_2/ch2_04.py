"""

个人所得税：
    编写一个计算个人所得税的程序，要求输入收入金额后，能够输出应缴的个人所得税。个人所得税征收办法如下：
    起征点为2000元。
    ·不超过500元的部分，征收5%。
    ·超过500～2000元的部分，征收10%。
    ·超过2000～5000元的部分，征收15%。
    ·超过5000～20000元的部分，征收20%。
    ·超过20000～40000元的部分，征收25%。
    ·超过40000～60000元的部分，征收30%。
    ·超过60000～80000元的部分，征收35%。
    ·超过80000～100000元的部分，征收40%。
    ·超过100000元以上的，征收

"""

TAXBASE = 2000

"""
    分为9个阶段，每个阶段第一个值为个税起征点，第二个值为该阶段截止点，第三个值为税率
"""
TaxTable = [(0, 500, 0.05),
            (500, 2000, 0.10),
            (2000, 5000, 0.15),
            (5000, 20000, 0.20),
            (20000, 40000, 0.25),
            (40000, 60000, 0.30),
            (60000, 80000, 0.35),
            (80000, 100000, 0.40),
            (100000, 1e10, 0.45)]


# 计算税收
def CaculateTax(profit):
    tax = 0.0
    profit -= TAXBASE   # 超过个税起征点的收入。   TAXBASE：个税起征点。 profit：存放个人收入超过个税起征点的部分
    i = 0
    for i in range(len(TaxTable)):
        # 判断profit是否在当前的缴税范围内
        if (profit > TaxTable[i][0]):
            if (profit > TaxTable[i][2]):   # profit超过当前的缴税范围
                tax += (TaxTable[i][1] - TaxTable[i][0]) * TaxTable[i][2]
            else:   # profit未超过当前的缴税范围
                tax += (profit - TaxTable[i][0]) * TaxTable[i][2]
            profit -= TaxTable[i][1]
            if profit < 0:
                profit = 0
            print("征税范围：%6d～%6d 该范围内缴税金额：%6.2f 超出该范围的金额：%6d" % (TaxTable[i][0], TaxTable[i][1], tax, profit))
    return tax


if __name__=="__main__":
    print("请输入个人收入金额：", end='')
    profit = int(input())
    tax = CaculateTax(profit)
    print("您的个人所得税为 %12.2f" % tax)




