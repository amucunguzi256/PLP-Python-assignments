
my_list = []
numbers= [10,20,30,40]
for i in numbers:
    my_list.append(i)
my_list.insert(2,15)
my_list.extend([50,60,70])
my_list.pop()
my_list.sort()
print(my_list.index(30))