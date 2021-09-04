from __future__ import print_function
import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread(cv2.samples.findFile("326GlareCrop.JPG"), 3)


#img = cv2.blur(img,(21,21))
width, height, channel = img.shape

#B, G, R = img[:, :, 0]/255, img[:, :, 1]/255, img[:, :, 2]/255

#hsv_img = np.zeros((width, height, channel), dtype=np.uint8)
hsv_img = np.zeros((width, height, channel), dtype=np.uint8)

s_img = np.zeros((width, height), dtype=np.uint8)
v_img = np.zeros((width, height), dtype=np.uint8)
for i in range(width):
    for j in range(height):

    # Defining Hue
        h, s, v = 0.0, 0.0, 0.0
        r, g, b = img.item(i, j, 2)/255, img.item(i, j, 1)/255, img.item(i, j, 0)/255

        max_rgb, min_rgb = max(r, g, b), min(r, g, b)
        dif_rgb = max_rgb-min_rgb

        if r == g == b:
            h = 0
        elif max_rgb == r:
            h = ((60.0*(g-b))/dif_rgb)
        elif max_rgb == g:
            h = (((60.0*(b-r))/dif_rgb)+120.0)
        elif max_rgb == b:
            h = (((60.0*(r-g))/dif_rgb)+240.0)
        if h < 0:
            h = h+360
        #elif max_rgb == r and g < b:
            #h = (((60(g-b))/(max_rgb-min_rgb))+360)
        #elif max_rgb == r and g >= b:
            #h = (((60*(g-b))/(max_rgb-min_rgb))+0)

    # Defining Satuation
        if max_rgb == 0:
            s = 0
        else:
            s = ((max_rgb-min_rgb)/max_rgb)
    # Defining Value

        v = max_rgb
        #print(h, s, v)
        hsv_img[i][j][0], hsv_img[i][j][1], hsv_img[i][j][2] = h/2, 255, 255
        v_img[i][j] = v*255
        s_img[i][j] = s*255
hsv_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
#cv2.imwrite('../Cod326_HUE.jpg', hsv_img)
#cv2.imwrite('../Cod0310_P9200130_Saturation.jpg', s_img)
#cv2.imwrite('../Cod0310_P9200130_Value.jpg', v_img)
#hsv_img = cv2.cvtColor(hsv_img, cv2.COLOR_BGR2RGB)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.imshow(hsv_img)
ax2.imshow(v_img, cmap="gray")
ax3.imshow(s_img, cmap="gray")
#plt.imshow(hsv_img)
#cv2.imshow(img)
#plt.imshow(s_img, cmap="gray")
plt.show()
