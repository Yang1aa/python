# _*_ coding : utf-8 _*_
# @Time : 2023/2/8 16:22
# @Author : yangliuan
# @File : 038_字典
# @Project : python基础

info = {'name': '班长', 'age': 18}
print(info['age'])  # 获取年龄
# print(info['sex']) # 获取不存在的key，会发生异常
print(info.get('sex'))  # 获取不存在的key，获取到空的内容，不会出现异常

info = {'name': '班长'}
print('添加之前的字典为:%s' % info)
info['id'] = 100  # 为不存在的键赋值就是添加元素
print('添加之后的字典为:%s' % info)

info = {'name': '班长', 'id': 100}
print('删除前,%s' % info)
del info['name']  # del 可以通过键删除字典里的指定元素
print('删除后,%s' % info)
{'name': '班长', 'id': 100}
{'id': 100}

info = {'name': 'monitor', 'id': 100}
print('删除前,%s' % info)
del info  # del 也可以直接删除变量
# print('删除后,%s' % info)

info = {'name': 'monitor', 'id': 100}
print('清空前,%s' % info)
info.clear()
print('清空后,%s' % info)


info = {'name': '班长', 'age': 18}

for key in info.keys():
    print(key)
for value in info.values():
    print(value)
for key, value in info.items():
    print(key, value)
for item in info.items():
    print(item)
