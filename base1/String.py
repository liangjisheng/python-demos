
# Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符
# 字符串的截取的语法格式如下 变量[头下标:尾下标]
# 索引值以 0 为开始值，-1 为从末尾的开始位置
# 加号(+)是字符串的连接符,星号(*)表示复制当前字符串，紧跟的数字为复制的次数

str = "runoob";
print(str);
print(str[0 : -1]);		# 负数表示从末尾开始，输出第一个到倒数第二个所有字符
print(str[0]);			# 第一个字符
print(str[2 : 5]);		# 第三个到第5个字符.包括开始，不包括结束，与C++中的区间是一致的
print(str[2:]);			# 第三个开始的所有字符
print(str * 2);			# 输出两次str
print(str + " test");	# 字符串连接
print();

# Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串
print("ru\noob");
print(r"ru\noob");

# 反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行
# Python 没有单独的字符类型，一个字符就是长度为1的字符串
word = "python";
print(word[0], word[5]);
# -1表示倒数第一个字符，-0(假设有)表示字符串最后一个元素的下一个位置
print(word[-1], word[-6]);
# 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误

input();