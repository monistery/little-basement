#!/usr/bin/python 
# -*- coding: UTF-8 -*-

# 第一行代码似乎不是注释必须的代码去了也不会报错
numbers = list(range(1,6))

print(numbers)
print('\n')

even_numbers = list(range(2,11,2)) # 2,11 表示range的范围为2-11， 最后一个2表示每次递进不是加一而是加二
print(even_numbers)
print('\n')


squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)
print('\n')

squares = [value**2 for value in range(1,11)]
print(squares)
