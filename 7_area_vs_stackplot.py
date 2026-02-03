# stakeplot is useful when the individual data values and additionally their cumulative 
# value are of interest.


# Area plots are best used to visualize trends over time, focusing on volume, 
# magnitude, and cumulative totals rather than just precise data points. They are ideal 
# for showing part-to-whole relationships, such as how individual categories contribute 
# to a total over a continuous interval (e.g., monthly sales, website traffic


# FOR TIME SERIES DATA, LINE PLOT IS MOST IMPORTANT AND IS CONSIDERED AS STANDARD BUT
# AREA PLOT ALSO BE USED BUT ESPECIALLY WHEN WE HAVE TO SHOW CUMULATIVE EFFECT

# You can see not only the growth in traffic but also how each source adds up to the total.
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
