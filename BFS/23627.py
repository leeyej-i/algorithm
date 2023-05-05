import sys
str_data=sys.stdin.readline().strip()
if str_data.find('driip',len(str_data)-5, len(str_data)) > -1 :
    print("cute")
else :
    print("not cute")