import os
import numpy as np 

'''
目标文件
生成images.txt文件
公用text_save函数，只需修改少许

'''
rootdir = 'images/'
def list_all_files(rootdir):
    _files = []
    listd = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0, len(listd)):
           path = os.path.join(rootdir, listd[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path+'/'))
           if os.path.isfile(path):
              _files.append(path)
    return _files


_fs = list_all_files(rootdir)
# print(_fs)

def text_save(filename, data):#filename为写入txt文件的路径，data为要写入数据列表.
    file = open(filename, 'w')
    j=1
    for i in range(len(data)):
        s = str(data[i])
        # s = s..replace('[','').replace(']','')  #去除[],这两行按数据不同，可以选择
        # s = s.replace("'", '').replace(',', '').replace(' ', '') + '\n'
        s = s + '\n'
        # print(s)   # images/American_Crow/97.0534.jpeg
        file.write(str(j)+' '+s[7:])   # 创建images.txt时
        # file.write(str(j)+' '+s)  # 创建classes.txt时
        j=j+1
    file.close()
    print("保存文件成功") 

text_save('images.txt', _fs)