print("type num 1")
a = int(input())
print("type num 2")
b = int(input())
print("sum is ", a+b)

print("type a string")
s = input()
if (len(s)<2):
    print("")
else:
    print(s[0:2]+s[len(s)-2:len(s)])