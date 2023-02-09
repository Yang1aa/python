# _*_ coding : utf-8 _*_
# @Time : 2023/2/8 11:13
# @Author : yangliuan
# @File : 032_列表
# @Project : python基础


# append 在末尾添加元素
# insert 在指定位置插入元素
# extend 合并两个列表
# 定义变量A，默认有3个元素
A = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
#
# print("‐‐‐‐‐添加之前，列表A的数据‐‐‐‐‐A=%s" % A)
# # 提示、并添加元素
# temp = input('请输入要添加的学生姓名:')
# A.append(temp)
# print("‐‐‐‐‐添加之后，列表A的数据‐‐‐‐‐A=%s" % A)
# temp = input('请输入要添加的学生姓名:')
# A.insert(len(A), temp)
# print("‐‐‐‐‐添加之后，列表A的数据‐‐‐‐‐A=%s" % A)
# A.extend(A)
# print("‐‐‐‐‐添加之后，列表A的数据‐‐‐‐‐A=%s" % A)


# 查询元素
# name = input("请输入查询名字：")
# if name in A:
#     print("true")
# else:
#     print("false")
#
# if name not in A:
#     print("请输入添加")


# 删除元素
# del：根据下标进行删除
# pop：删除最后一个元素
# remove：根据元素的值进行删除
movieName = ['加勒比海盗', '骇客帝国', '第一滴血', '指环王', '霍比特人', '速度与激情']
print('‐‐‐‐‐‐删除之前‐‐‐‐‐‐movieName=%s' % movieName)
del movieName[2]
print('‐‐‐‐‐‐删除之后‐‐‐‐‐‐movieName=%s' % movieName)
movieName = ['加勒比海盗', '骇客帝国', '第一滴血', '指环王', '霍比特人', '速度与激情']
print('‐‐‐‐‐‐删除之前‐‐‐‐‐‐movieName=%s' % movieName)
movieName.pop()
print('‐‐‐‐‐‐删除之后‐‐‐‐‐‐movieName=%s' % movieName)
movieName = ['加勒比海盗', '骇客帝国', '第一滴血', '指环王', '霍比特人', '速度与激情']
print('‐‐‐‐‐‐删除之前‐‐‐‐‐‐movieName=%s' % movieName)
movieName.remove('指环王')
print('‐‐‐‐‐‐删除之后‐‐‐‐‐‐movieName=%s' % movieName)
