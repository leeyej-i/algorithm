# 백준 17413
# 실버 3 / 단어 뒤집기 2
import sys
S = sys.stdin.readline().strip()
word = []
check = 0
for item in S :
    if item == ' ':
        word.reverse()
        print("".join(word), end=' ')
        word.clear()
    elif item == '<':
        word.reverse()
        print("".join(word), end='')
        word.clear()
        print(item, end='')
        check = 1
        continue
    elif item == '>':
        print(item, end='')
        check = 0
        continue
    elif check == 1 :
        print(item, end='')
        continue
    else :
        word.append(item)

if len(word) != 0:
   word.reverse()
   print("".join(word), end=' ')