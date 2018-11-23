import os
import numpy as np 

'''
目录重命名
格式：
001.Acadian_Flycatcher
002.American_Crow
...

'''

# rootdir = 'test/'
# i=0
# j=1
# listdir = os.listdir(rootdir)
# # print(listdir)
# # src = os.path.join(rootdir, listdir[0])
# # dst = os.path.join(rootdir, str(j)+'.'+listdir[0])
# # os.rename(src, dst)
# # print(dst)

# for line in listdir:
#     src = os.path.join(rootdir, listdir[i])
#     if i<10:
#         dst = os.path.join(rootdir, str(0)+str(0)+str(j)+'.'+listdir[i])
#     else:
#         dst = os.path.join(rootdir, str(0)+str(j)+'.'+listdir[i])
#     i=i+1
#     j=j+1
#     os.rename(src, dst)

# print("成功")


'''
图片文件重命名
格式：
Acadian_Flycatcher/Acadian_Flycatcher_1.jpg
Acadian_Flycatcher/Acadian_Flycatcher_2.jpg
...

'''

def reName(dirname):
    '''
    实现将所有类别中的所有文件重新命名
    '''
    # 该文件夹下所有的文件（包括文件夹）
    for category in os.listdir(dirname):
        # print(category)
        catdir = os.path.join(dirname, category)
        # 如果不是文件夹则跳过
        if not os.path.isdir(catdir):
            continue
        files = os.listdir(catdir)
        # print(files)
        # files.remove('.DS_Store')
        count = 0
        for cur_file in files:
            print("正在处理" + category + "分类下的" + cur_file)
            filename = os.path.join(catdir,cur_file)
            count = count + 1
            # 原来的文件路径
            oldDir = os.path.join(catdir,cur_file)
            # 如果是文件夹则跳过
            if os.path.isdir(oldDir):
                continue
            # 文件名
            filename=os.path.splitext(cur_file)[0]
            # 文件扩展
            filetype=os.path.splitext(cur_file)[1]
            # 新的文件路径
            newDir=os.path.join(catdir,catdir.split('.')[1]+'_'+str(count)+filetype)
            # 重命名
            os.rename(oldDir, newDir)

if __name__ == '__main__':
    dirname = 'images/'
    # reName(dirname)


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
        # file.write(str(j)+' '+s[7:])   # 创建images.txt时
        file.write(str(j)+' '+s)  # 创建classes.txt时
        j=j+1
    file.close()
    print("保存文件成功") 

# text_save('images.txt', _fs)


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
# text_save('classes.txt', class_file)


'''
中间文件
生成image_classes.txt文件

'''

# filei = open('images.txt', 'r')
# fileic = open('image_classes.txt', 'w')
# for line in filei.readlines():
#   # print(line)
#   x = line.split('/')[0].split(' ')[1]
#   # print(x)
#   fileic.write(x+'\n')
# print("保存文件成功")
# filei.close()
# fileic.close()


'''
目标文件
生成image_class_labels.txt文件

'''

# fileiclc = open('image_class_labels.txt', 'w')
# num = 1
# j = 1
# y = 1
# image_array = np.loadtxt('image_classes.txt', str)
# # print(image_array[6756])
# for i in range(len(image_array)-1):
#   y = num
#   if image_array[i] != image_array[i+1]:
#     # num = num + 1
#     y = num
#     num = num + 1
#   # print(y)
#   fileiclc.write(str(j)+' '+str(y)+'\n')
#   j=j+1

# print("保存文件成功")
# fileiclc.close()
