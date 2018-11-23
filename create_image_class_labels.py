import os
import numpy as np 


'''
目标文件
生成image_class_labels.txt文件
image_classes.txt是create_image_classes.py生成

'''

fileiclc = open('image_class_labels.txt', 'w')
num = 1
j = 1
y = 1
image_array = np.loadtxt('image_classes.txt', str)
# print(image_array[6756])
for i in range(len(image_array)-1):
  y = num
  if image_array[i] != image_array[i+1]:
    # num = num + 1
    y = num
    num = num + 1
  # print(y)
  fileiclc.write(str(j)+' '+str(y)+'\n')
  j=j+1

print("保存文件成功")
fileiclc.close()