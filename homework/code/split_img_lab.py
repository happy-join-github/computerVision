# 数据分割，挑选200张图片进行训练模型
import os
import random
img_path = 'images/train/'
lab_path ='labels/train/'

img_lst = []
for i in range(0,200):
    img_dir = os.listdir(img_path)
    num = random.randint(0,len(img_dir)-1)
    while num in img_lst:
        num = random.randint(0,len(img_dir)-1)
    
    new_img_path = 'shiyan/images/'+img_dir[num]
    # 移动图片
    os.rename(img_path+img_dir[num],new_img_path)
    img_lst.append(img_dir[num][:-4])
    print(i+1)

lab_dir = os.listdir(lab_path)
for i in range(200):
    old_lab_s = lab_path+img_lst[i]+'.txt'
    new_lab_path = 'shiyan/labels/'+img_lst[i]+'.txt'
    os.rename(old_lab_s,new_lab_path)
    print(i+1)
