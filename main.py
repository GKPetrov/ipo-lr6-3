num=int(input("Введите кол-во строк"))
str_list=[]
new_list=[]
if(num<0):
    print("error")
else:
    for i in range(num):
        str_list.append(input("Введите строку"))
    for i in range(num):
            str_list[i]=str_list[i].split(" ")
    for i in range(num):
        new_list.extend(str_list[i])
    print(len(set(new_list)))
