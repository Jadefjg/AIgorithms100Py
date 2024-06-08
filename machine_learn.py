# 使用鸢尾花数据集进行分类任务的入门

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

predictions = classifier.predict(X_test)
print("准确率:", accuracy_score(y_test, predictions))