#!/bin/bash
# echo "Hello World !"

# for file in `ls /etc`; do
#     echo ${file}
# done

# # 只读变量
# myUrl="https://www.google.com"
# readonly myUrl
# echo $myUrl

# # 删除变量
# unset $myUrl

# # 双引号
# your_name='runoob'
# str="Hello, I know you are \"$your_name\"! \n"
# echo -e $str

# your_name="runoob"
# # 使用双引号拼接
# greeting="hello, "$your_name" !"
# greeting_1="hello, ${your_name} !"
# echo $greeting  $greeting_1
# # 使用单引号拼接
# greeting_2='hello, '$your_name' !'
# greeting_3='hello, ${your_name} !'
# echo $greeting_2  $greeting_3

# # 获取字符串长度
# string="abcd"
# echo ${#string} #输出 4

# 提取子字符串
string="runoob is a great site"
echo ${string:1:4} # 输出 unoo

# 查找子字符串
echo $((index "$string" io))  # 输出 4

# Shell 数组
# array_name=(value0 value1 value2 value3)
array_name[0]=value0
array_name[1]=value1
echo ${array_name[1]}
echo ${array_name[@]}

# 取得数组元素的个数
length=${#array_name[@]}

多行注释
:<<EOF
注释内容...
注释内容...
注释内容...
EOF