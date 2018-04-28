'''print("type num 1")
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
'''
tasks = []

while True:
    print("type action 1/2/3/4=insert/remove/showAll/close")
    in1 = input()
    if(in1 == "1"):
        print("type a task")
        tasks.append(input())
    elif(in1=="2"):
        print("type which task you want to remove")
        tasks.remove(input())
    elif(in1=='3'):
        for el in tasks:
            print(el)
    elif(in1=='4'):
        break


