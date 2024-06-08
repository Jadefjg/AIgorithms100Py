import pandas as pd


data = pd.read_csv('data.csv')
print(data.head())  # 打印前五行数据
mean = data['column_name'].mean()  # 计算某列的平均值
print(f"{data.columns[0]}的平均值为: {mean}")