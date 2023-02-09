# _*_ coding : utf-8 _*_
# @Time : 2023/2/9 12:01
# @Author : yangliuan
# @File : 047_文件
# @Project : python基础

# fp = open("demo.txt", "w")
# fp.write("hello world!\n" * 5)
# # fp.close()
# fp = open("demo.txt", "r")
# content = fp.readline()
# print(content)
# content = fp.readlines()
# print(content)
# # fp.close()
# 序列化
# fp = open("demo.txt", "w")
# name_list = ['zhangsan', 'lisii']
# # dumps()
# # import json
# #
# # json_name_list = json.dumps(name_list)
# #
# # dump()
# import json
#
# json.dump(name_list, fp)
#
# fp.close()


# 反序列化
# # loads()
# fp = open("demo.txt","r")
# content = fp.read()
# import json
# content = json.loads(content)
# print(type(content))

# load()
fp = open("demo.txt", "r")
import json

result = json.load(fp)
print(result)
print(type(result))
fp.close()