import random


secret_number = random.randint(1,100)
guess = None
attempts = 0


while guess != secret_number:
    guess = int(input("请输入你猜的数字(1-100之间)："))
    attempts += 1
    if guess < secret_number:
        print("太小了！")
    elif guess > secret_number:
        print("太大了！")


print(f"恭喜你！你在第{attempts}次尝试中猜对了数字{secret_number}")