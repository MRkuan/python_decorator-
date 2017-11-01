#!/usr/bin/env python3
# -*- coding: utf-8 -*-## 
# ref:https://zhuanlan.zhihu.com/p/21696291?utm_source=com.youdao.note&utm_medium=social

## 一. 预备知识
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(a(), '---', a)
print(b(), '---', b)


'''
理解下 *args, **kwargs
'''
#ref: http://blog.csdn.net/callinglove/article/details/45483097
#理解 *号
def fun(a,b,c):
    print(a,b,c)
l = [1,2,3] #list。list是一种有序的集合
fun(*l)

# * 在函数定义作用 
def fun(a, *args):
    print ( "a is ", a)
    print ( "args is ", args)

fun(11,12,34,43)

# **在函数定义作用
def fun(a, b, c):
    print(a,b,c)

d={'b':5, 'c':7}
fun(1, **d)
    
    
'''
二.装饰器的定义是：装饰器实质上是一个函数。它把一个函数作为输入并且返回另外一个函数。
其实其是闭包概念的深化。依然是本书例子：
'''
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('document_it Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)

#高大上用法

@document_it
def add_ints(a, b):
    return a + b
add_ints(3, 5)

##应用多个装饰器
def square_it(func):
    def another_new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return another_new_function

#正过来调用
@document_it
@square_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

#翻过来调用
@square_it
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)