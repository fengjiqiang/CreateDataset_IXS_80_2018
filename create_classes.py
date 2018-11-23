import os
import numpy as np 

'''
非必须目标文件
生成classes.txt文件
公用text_save函数，只需修改少许

'''

def create_classes_file(filename):
    with open(filename, 'r') as f:
      xlist = []
      for line in f.readlines():
        x = line.split('/')[0]
        y = x.split(' ')[1]
      # print(y)
        if y not in xlist:
          xlist.append(y)
      # print(xlist)
    return xlist

class_file = create_classes_file('images.txt')


def text_save(filename, data):#filename为写入txt文件的路径，data为要写入数据列表.
    file = open(filename, 'w')
    j=1
    for i in range(len(data)):
        s = str(data[i])
        # s = s..replace('[','').replace(']','')  #去除[],这两行按数据不同，可以选择
        # s = s.replace("'", '').replace(',', '').replace(' ', '') + '\n'
        s = s + '\n'
        # print(s)   # images/American_Crow/97.0534.jpeg
        # file.write(str(j)+' '+s[7:])   # 创建images.txt时
        file.write(str(j)+' '+s)  # 创建classes.txt时
        j=j+1
    file.close()
    print("保存文件成功")

text_save('classes.txt', class_file)