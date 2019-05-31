# name = input("please input your name!")
# print("hello",name)

# a = -1
# if a >= 0:
#     print(a)
# else:
#     print(-a)

# a = ['a','b','c']
# s = a 
# s.append(a)
# def h(l):
#     for i in l:
#         if isinstance(i,list) :
#             h(i)
#         else:
#             print(i)    

# if __name__ == "__main__":
#     h(s)

# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d.get('Bob'))
# print('Bob' in d)
# t = (1,2,3)
# s = set(t)
# print(s)
# map = {(1,[2,3])}
# print(map)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#出入参数为tuple，*arg作为一个tuple
# def hello(greeting, *args):
#     if (len(args)==0):
#         print('%s!' % greeting)
#     else:
#         print('%s, %s!' % (greeting, ', '.join(args)))
# hello('Hi') # => greeting='Hi', args=()
# hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
# hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')
# names = ('Bart', 'Lisa')
# hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')


#**kw作为一个dict
# def print_scores(**kw):
#     for name, score in kw.items():
#         print('%10s  %d' % (name, score))
#     print()
# print_scores(Adam=99, Lisa=88, Bart=77)
# data = {
#     'Adam Lee': 99,
#     'Lisa S': 88,
#     'F.Bart': 77
# }
# print_scores(**data)
# def print_info(name, *, gender, city='Beijing', age):
#     print('Personal Info')
#     print('---------------')
#     print('   Name: %s' % name)
#     print(' Gender: %s' % gender)
#     print('   City: %s' % city)
#     print('    Age: %s' % age)
#     print()
# print_info('Bob', gender='male', age=20)
# print_info('Lisa', gender='female', city='Shanghai', age=18)

#列表生成式
# list = [x * x for x in range(1, 11) if x % 2 == 0]
# print(list)
# print([m + n for m in 'ABC' for n in 'XYZ'])

# import os
# print([d for d in os.listdir('.')])

# d = {'x':1,'y':2,'z':3}
# for k,v in d.items():
#     print(k,"=",v)
# for k in d:
#     print(k)
# for v in d.values():
#     print(v)

# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# f = fib(10)
# for index in f:
#     print(index)

#杨辉三角
# def triangel(n):
#      ArrList, index = [1], 0
#      while index < n:
#          yield ArrList
#          ArrList = [1] + [ArrList[i] + ArrList[i + 1] for i in range(len(ArrList) - 1)] + [1]
#          index += 1
#      return 'done'

# f = triangel(3)
# for index in f:
#     print(index)



# from functools import reduce
# def fun1(x,y):
#     return x *10 + y
# def fun2(n):
#     digits = {'0':0,'1':1,'2':2,'3':3,'4':4}
#     return digits[n]
# print(reduce(fun1, map(fun2, '13')))

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def char2num(s):
#     return DIGITS[s]
# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))
# print(str2int('1234'))

import re
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(1))
print(re.split(r'\s+','a b    c'))
print(re.split(r'[\s\,]+','a,b    c'))
