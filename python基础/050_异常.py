# _*_ coding : utf-8 _*_
# @Time : 2023/2/9 19:20
# @Author : yangliuan
# @File : 050_异常
# @Project : python基础

# 异常的格式
# try:
#      可能出现的异常代码
# except  异常类型
#     友好提示
try:
    fp = open("text.txt", "r")
    fp.read()
except FileNotFoundError:
    print("没有创建文件")
