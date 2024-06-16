# to create multiple graphs under single figure
import matplotlib.pyplot as plt

# x=["a","b","c","d"]
# y=[1,2,3,4]
# plt.bar(x,y)


# x=[23,34,45,56]
# y=[12,23,34,55]
# plt.scatter(x,y)


# x=[10,20,40,30]
# plt.pie(x)


# x=[1,2,3,4]
# y=[5,6,7,8]
# plt.stem(x,y)
# plt.show()

# ab jo m n uper code likha us s saary graphs ek doosry k uper show hon gy, but hm chahty
# hn k saary ek hi figue m alag alag show hon

x=["a","b","c","d"]
y=[1,2,3,4]
plt.subplot(2,2,1)    #below 4 figures has 2 rows horizontal and 2 vertical columns
# which accommodated 4 figures and 1 2 3 4 are respective position in that figure
plt.bar(x,y)


x=[23,34,45,56]
y=[12,23,34,55]
plt.subplot(2,2,2)  #or y graph declare krny vali line of code s phly likhna h
plt.scatter(x,y)


x=[10,20,40,30]
plt.subplot(2,2,3)
plt.pie(x)

x=[1,2,3,4]
y=[5,6,7,8]
plt.subplot(2,2,4)
plt.stem(x,y)
plt.show()