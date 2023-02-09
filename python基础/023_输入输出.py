# _*_ coding : utf-8 _*_
# @Time : 2023/2/7 11:26
# @Author : yangliuan
# @File : 023_输入输出
# @Project : python基础

print("故事里的小黄花")

# 格式化输出 %s代表字符串 %d代表数值
name = "zs"

age = 18

print('我的名字是%s我的年龄是%d' % (name, age))

password = input("请输入密码：")
print(password)
print(type(password))
