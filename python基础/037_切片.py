# _*_ coding : utf-8 _*_
# @Time : 2023/2/8 16:16
# @Author : yangliuan
# @File : 037_切片
# @Project : python基础


# 切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。
# 切片的语法：[起始:结束:步长]，也可以简化使用 [起始:结束]
# 注意：选取的区间从"起始"位开始，到"结束"位的前一位结束（不包含结束位本身)，步长表示选取间隔。

s = "hello world"

print(s[0:4])

print(s[1:])

print(s[:4])

print(s[0::3])
