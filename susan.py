# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'
# %%
import cv2


# %%
import matplotlib.pyplot as plt


# %%
img=cv2.imread('images/Cars0.png')


# %%
def displayImg(img,*args):
    plt.imshow(img,*args)
    plt.show()


# %%
displayImg(img)


# %%
# single channel
# convert to gray image
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# displayImg(grayImg,cmap='gray')

cv2.imshow('gray',grayImg)
cv2.waitKey(0)


# %%



