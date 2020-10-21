
# stderr 重定向到 file
command 2 > file

# 将 stdout 和 stderr 合并后重定向到 file
command > file 2>&1

wc -l << EOF
    欢迎来到
    菜鸟教程
    www.runoob.com
EOF

# /dev/null 文件
command > /dev/null