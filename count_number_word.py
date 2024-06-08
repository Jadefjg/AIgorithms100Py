from collections import Counter


text = "这是一个简单的示例文本，用于演示如何统计单词出现次数"

words = text.split()

word_counts = Counter(words)

for word,count in word_counts.items():
    print(f"'{word}': {count}次")