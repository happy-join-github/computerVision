import cv2
img = cv2.imread('../dataset/shiyan/img/train/015-91_90-248&454_464&524-464&524_248&520_248&454_462&460-0_0_3_24_33_29_27_27-141-187.jpg')
img = cv2.resize(img,(400,400))
cv2.imshow('img',img)
cv2.waitKey(0)