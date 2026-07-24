#簡易密碼生成器，用於生成隨機密碼，並轉換成大寫以供使用
import random
import string

def generate_random_code(length=10):
    # 定義字元庫
    characters = string.ascii_letters + string.digits
    
    # 隨機選取指定長度的字元組成密碼
    random_code = ''.join(random.choice(characters) for _ in range(length))
    return random_code

# 隨機產生五組長度為10的密碼
codes = []
for i in range(5):
    code = generate_random_code(10)
    codes.append(code)

#檢查用
print("未轉換密碼：")
print(codes)

#把小寫字母轉成大寫並檢查長度
transformed_codes = [c.upper() for c in codes if len(c) == 10]

#大寫密碼
for index, item in enumerate(transformed_codes):
    print(f"密碼 {index}: {item}")