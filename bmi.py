h = float(input("身長は何㎝ですか？")) / 100.0
w = float(input("体重は何㎏ですか？"))
# bmi = w / (h * h)
bmi = w / h ** 2
print("あなたのBMI値は、",bmi,"です。")