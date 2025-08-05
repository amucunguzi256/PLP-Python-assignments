print("---------------\nWelcome to my Calculator.\n--------------")
x,y,z=input("Please input 2 numbers and an operation Separated by one space: ").split(" ")
if z =="+":
    ans= int(x) + int(y)
elif z =="-":
    ans= int(x)- int(y)
elif z =="*":
    ans= int(x) * int(y)
elif z =="/":
    ans= int(x) / int(y)

print(f"{x} {z} {y} = {ans}")