n = 1234
result = 0

if n < 0:
    print("Số ko hợp lệ")
else:
    while n > 0:
        chuSoCuoi = n % 10
        result = result * 10 + chuSoCuoi
        n = n // 10
        print(result)
