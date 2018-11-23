import os
import numpy as np 

'''
目录重命名
格式：
001.Acadian_Flycatcher
002.American_Crow
...

'''

rootdir = 'test/'
i=0
j=1
listdir = os.listdir(rootdir)
# print(listdir)
# src = os.path.join(rootdir, listdir[0])
# dst = os.path.join(rootdir, str(j)+'.'+listdir[0])
# os.rename(src, dst)
# print(dst)

for line in listdir:
    src = os.path.join(rootdir, listdir[i])
    if i<10:
        dst = os.path.join(rootdir, str(0)+str(0)+str(j)+'.'+listdir[i])
    else:
        dst = os.path.join(rootdir, str(0)+str(j)+'.'+listdir[i])
    i=i+1
    j=j+1
    os.rename(src, dst)

print("成功")