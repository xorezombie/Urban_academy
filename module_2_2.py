fist= int(input())
second=int(input())
third=int(input())
if fist==second==third:
    print(3)
elif fist==second or fist==third or second==third:
    print(2)
else:
    print(0)