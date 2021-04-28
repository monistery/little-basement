# -*- coding: UTF-8 -*-
# 文件名：name[].py

name = ['Bai', 'wang', 'li', 'tong']
message = "my name is " + name[-2].title() + "."
print(name)

name.append('cai')
message = "my name is " + name[-1].title() + "."
print(name)
print("\n") 

name.insert(1,'ma')
message = "my name is " + name[1].title() + "."
print(name) 
print("\n") 

del name[-1]
print(name) 
print("\n") 

poped_name = name.pop()
print(name)
print(poped_name) 
print("\n") 

name.reverse()
print(name)
print("\n") 

print(name)
print(sorted(name))# 从小到大排序同时没有对原数组改动
print(sorted(name, reverse = True))# 从大到小排序同时没有对原数组改动
print("\n") 

name.sort()# 从小到大排序同时对原数组改动
print(name)
name.sort(reverse = True)#从大到小排序同时对原数组改动
print(name)