import os
import numpy as np 

'''
中间文件
生成image_classes.txt文件
images.txt是create_images.py生成

'''

filei = open('images.txt', 'r')
fileic = open('image_classes.txt', 'w')
for line in filei.readlines():
  # print(line)
  x = line.split('/')[0].split(' ')[1]
  # print(x)
  fileic.write(x+'\n')
print("保存文件成功")
filei.close()
fileic.close()