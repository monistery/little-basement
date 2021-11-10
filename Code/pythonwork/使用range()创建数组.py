
# -*- coding: UTF-8 -*-

# ��һ�д����ƺ�����ע�ͱ���Ĵ���ȥ��Ҳ���ᱨ��
numbers = list(range(1,6))

print(numbers)
print('\n')

even_numbers = list(range(2,11,2)) # 2,11 ��ʾrange�ķ�ΧΪ2-11�� ���һ��2��ʾÿ�εݽ����Ǽ�һ���ǼӶ�
print(even_numbers)
print('\n')


squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)
print('\n')

squares = [value**2 for value in range(1,11)]
print(squares)
