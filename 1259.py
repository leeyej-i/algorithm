import sys
while True:
    str_data=sys.stdin.readline().strip()
    if str_data == '0':
        break
    
    def solve(str_data):
        num = len(str_data)//2
        for i in range(num):
            if str_data[i] != str_data[len(str_data)-1-i]:
                return 'no'
        
        return 'yes'
    
    print(solve(str_data))