num=int(input("Введите кол-во строк"))
a=list()
b=list()
if(num<0):
    print("error")
else:
    for i in range(num):
        a.append(str(input("Введите строку")))
    for i in range(num):
            a[i]=a[i].split(" ")
    for i in range(num):
        b.extend(a[i])
    print(len(set(b)))