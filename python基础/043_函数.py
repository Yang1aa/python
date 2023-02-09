# _*_ coding : utf-8 _*_
# @Time : 2023/2/9 10:32
# @Author : yangliuan
# @File : 043_函数
# @Project : python基础

# 定义函数
def sum(a, b):
    c = a + b
    print(c)


sum(100, 200)
sum(b=200, a=100)


def sum(a, b):
    c = a + b
    return c
