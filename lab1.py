import cv2
import numpy as np
import matplotlib.pyplot as plt
original=cv2.imread("image/cat.jpg")
if original is None:
    raise FileNotFoundError("file not fine") 
rgb=cv2.cvtColor(original,cv2.COLOR_BGR2RGB)
h,w=rgb.shape[:2]
y,x=np.ogrid[:h,:w]
print(y,x)

circle_x=0.23
circle_y=0.5
circle_radius=0.3
rect_left=0.35
rect_right=0.88
A=((x-circle_x)**2+(y-circle_y)**2<=(min(h,w)*circle_radius)**2)
B=((x>=w*rect_left)& (y<w*rect_right)&(y>=h*0.45) & (y<h*0.85))

mask={
    'NOT A':~A,
    'A OR B':A|B,
    'A AND B':A&B,
    'A XOR B':A^B
}
# fig,axes=plt.subplots(2,4,figsize=(16,8))
# for col,(name,mask) in enumerate(mask.items()){

# }