# 백준 10820
# 브론즈 2 / 문자열 분석
while True:
    try:
        result = [0 for _ in range(4)]
        data = input()
        result[3] = len(data)
        data = data.replace(" ", "")
        result[3] -= len(data)
        for i in data:
            check = ord(i)
            if 48 <= check <= 57:
                result[2] += 1
            elif 65 <= check <= 90:
                result[1] += 1
            elif 97 <= check <= 122:
                result[0] += 1
        print(*result)

    except EOFError:
        break
