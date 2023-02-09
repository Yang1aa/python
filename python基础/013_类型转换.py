# _*_ coding : utf-8 _*_
# @Time : 2023/2/6 12:36
# @Author : yangliuan
# @File : 013_类型转换
# @Project : python基础
#
# a = "123"
# print(type(a))
# print(type(int(a)))
#
# b = 1.23
# print(type(b))
# print(int(b))
#
# c = 1.56
# print(type(c))
# print(int(c))
#
# d = True
# print(type(d))
# print(int(d))
# print(type(int(d)))
#
# # 以下两种情况将会转换失败
# '''
# 123.456 和 12ab 字符串，都包含非法字符，不能被转换成为整数，会报错
# print(int("123.456"))
# print(int("12ab"))
# '''
#
# a = 80
# print(type(str(a)))
#
# a = True
# print(str(a))
# print(type(str(a)))
#
# a = 1
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))
#
# a = 2
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))
#
# a = -2
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = "hello"
# print(bool(a))
# print(type(bool(a)))
#
# a = "   "
# print(bool(a))
# print(type(bool(a)))
#
# a = ""
# print(bool(a))
# print(type(bool(a)))

# b = ['1', '2', '3', '4']
# print(bool(b))
# print(type(bool(b)))
# c = []
# print(bool(c))
# print(type(bool(c)))

# a = (1, 2, 3)
# print(bool(a))
# print(type(bool(a)))

# a = ()
# print(bool(a))
# print(type(bool(a)))

# a = {}
# print(bool(a))
# print(type(bool(a)))

a = {'name': 'zs'}
print(bool(a))
print(type(bool(a)))
