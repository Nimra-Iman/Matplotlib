# stakeplot is useful when the individual data values and additionally their cumulative 
# value are of interest.
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
area1=[2,4,7,1,3]
area2=[6,3,1,9,4]
l=["area1","area2"]
# plt.stackplot(x,area1,area2,labels=l, colors=["r","b"])  #are2 ki values asal m jo
#  show hon gi vo area1 ki values m
# add ho kr show hon gi, e.g: area2 ki value 6 thi jab x ki value 1 thi but graph m area2
# # 8 pr show ho ga for x=1 because 6+2=8
# plt.legend(loc=2) 
# plt.show() 

# baseline="zero" or baseline="sym" or baseline="wiggle"
plt.stackplot(x,area1,area2,labels=l, baseline="sym")
plt.title("stakeplot", fontsize=15) 
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.grid()
plt.legend(loc=2) 
plt.show() 
