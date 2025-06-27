# kisi bhi graph k ander k area ka color fill krny k liye fill_between ka use krty hn,
# yani graph k kisi region ko alag s show kr skyn.
import matplotlib.pyplot as plt
import numpy as np
time=np.array([2,3,4,5,6])
speed=np.array([3,6,9,12,15])
plt.scatter(time,speed,marker="*",label="scatterplot")
plt.title("this is relationship")
plt.xlabel("x_axis")
plt.ylabel("y_axis")

# plt.fill_between(time,speed) #esa krny s line k neechy poory area ko color kry ga


# plt.fill_between(x=(2,3),y1=3,y2=12, color="r")  #yani x_axis ka 2 s 3 tak color show ho or y axis ka
# # 3 s 12 tak show ho


plt.fill_between(time, speed, where=(time>=2) & (time<=4))  #agar hm "where" ko use nhi krty
# to hmy "x" k saath "y" parameter dena zruri tha but where k saath hm bs ek parameter ko
# bhi de skty hn. lekin is m abhi bhi ek error ay ga k " '>=' not supported between 
# instances of 'list' and 'int' " to is s bachny k liye hm data hi numpy ki array m dety hn

plt.show()                        