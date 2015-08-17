#!/usr/bin/env python2

import sys

hello_str="Hello World"
hello_int = 21
hello_bool = True
hello_tuple = (21,32)

print(hello_tuple[0])

hello_list=["hello","this","is","a","list"]

hello_list=list()
hello_list.append("hello",)
hello_list.append("this",)
hello_list.append("is",)
hello_list.append("a",)
hello_list.append("list",)

hello_dict={"first_name":"matt",
    "last_name":"fraser",
    "eye_colour":"blue"}

print(hello_dict["first_name"])
print(hello_dict["first_name"]+" "+hello_dict["last_name"]+" "+hello_dict["eye_colour"])

print(hello_list[4])
hello_list[4]+="!"
print(hello_list[4])

target_int = raw_input("how many integers?")

try:
    target_int=int(target_int)
except ValueError:
    sys.exit("enter an integer")

ints=list()
count=0

while count < target_int:
    new_int=raw_input("please enter integer {0}:".format(count+1))
    isint=False
    try:
        new_int=int(new_int)
        isint=True
    except:
        print("not an integer")

    if isint==True:
        ints.append(new_int)
        count+=1

print("using a for loop...")
for value in ints:
    print(str(value))

print("using a while loop")

total=len(ints)
count=0
while count < total:
    print(str(ints[count]))
    count+=1
