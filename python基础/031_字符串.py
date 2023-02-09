# _*_ coding : utf-8 _*_
# @Time : 2023/2/7 16:53
# @Author : yangliuan
# @File : 031_字符串
# @Project : python基础


# 获取长度:len len函数可以获取字符串的长度。
s = "china"
print(len(s))
# 查找内容:find 查找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中第一次
# 出现的开始位置索引值，如果不存在，则返回-1.
print(s.find('c'))
# 判断:startswith,endswith 判断字符串是不是以谁谁谁开头/结尾
print(s.startswith('c'))
print(s.endswith('a'))
# 计算出现次数:count 返回 str在start和end之间 在 mystr里面出现的次数
print(s.count('a'))
# 替换内容:replace 替换字符串中指定的内容，如果指定次数count，则替换不会超过count次。
print(s.replace('c', 'd'))
# 切割字符串:split 通过参数的内容切割字符串
print(s.split('i'))
# 修改大小写:upper,lower 将字符串中的大小写互换
print(s.upper())
print(s.lower())
# 空格处理:strip 去空格
# 字符串拼接:join 字符串拼接
print(s.join())
