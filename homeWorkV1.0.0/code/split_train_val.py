# 数据集划分
# 训练图片150验证图片50
import os

train_img = os.listdir('../dataset/images/train/')
val_img = os.listdir('../dataset/images/val/')

for i in range(len(train_img)):
    old_path = '../dataset/shiyan/labels/'+train_img[i][:-4]+'.txt'
    new_path = '../dataset/labels/train/'+train_img[i][:-4]+'.txt'
    os.rename(old_path,new_path)
    print(i+1)

for j in range(len(val_img)):
    old_path = '../dataset/shiyan/labels/'+val_img[j][:-4]+'.txt'
    new_path = '../dataset/labels/val/' + val_img[j][:-4] + '.txt'
    os.rename(old_path,new_path)
    print(j+1)
