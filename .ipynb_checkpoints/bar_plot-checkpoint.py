import matplotlib.pyplot as plt #yani matplotlib ki pyplot class ko import kro
# pyplot class graphs ko plot krny m use hoti h
import numpy as np  

x=["python","c","c++","java"]
y=[85,70,60,83] #polularity
z=[20,30,40,50]
plt.xlabel("languages", fontsize="15") #we can also show labels across x and y axis and cen even change the 
# fontsize of labels
plt.ylabel("popularity of languages",fontsize="20")
plt.title("Relationship between languages and their popularity")
col=["r","pink","y","g"]

# plt.bar(x,y,width=0.4,color=col) #hr bar bhhhttt chora tha, is liye width km kr di thori
# width range from 0 to 1

# plt.bar(x,y, align="edge") #is s x_parameters k name ek side pr show hon gy

# plt.bar(x,y,edgecolor="red", linewidth=5, linestyle=":")  #edgecolor s bar k edges pr color show krty hn, or us color ko
# thora ziada show krny k liye, yani edgevolor ki width ko thick krny k liye linewidth ko 
# increase krty hn,  linestyle ko use krty hn agar bar k edges solid ki bijay dotted krny
# hon to

# plt.bar(x,y,alpha=0.4) #graph ki opacity ko km krna h to alpha ko use krty hn,
# alpha ki value 0-1 hoti h

# plt.bar(x,y,label="popularity") #agar ap ko koi label bhi show krna ho
# plt.legend() #label tab tak show nhi ho ga jab tak ap plt.legend() ko call nhi kro gy
# plt.legend("popularity") y 2nd method h label lgany ka


#!!!!!!!!!!! how to create multiple bar graphs:  !!!!!!!!!!!!!!!!!!!!!!
# w=0.2
# plt.bar(x,y,color="r",alpha=0.5,width=w)
# plt.bar(x,z,color="g",width=w) #lekin esy krny s y dono graphs ek doosry k uper overlap huy huy hn


# ------------ if we want k graphs overlap na hon bal k ek doosry k paas m show hon:
x=["python","c","c++","java"]
y=[85,70,60,83] #polularity
z=[20,30,40,50]
w=0.2
p=np.arange(len(x)) # p=[0,1,2,3] yani "x" k elements k indexes
p1=[j+w for j in p]
plt.xlabel("languages", fontsize="15") #we can also show labels across x and y axis and cen even change the 
# fontsize of labels
plt.ylabel("popularity of languages",fontsize="20")
plt.title("Relationship between languages and their popularity")


plt.bar(p,y,width=w,label="popularity") 
plt.bar(p1,z,width=w,label="popularity1")
plt.xticks(p+w/2, x , rotation=20) #p+w means position yani ticks khan pr show hon, 
# x is liye likha ta k un digits ki jga pr names show ho jo hm x list m daaly huy hn,
#  location s hm un x_axis k parameters ko rotated show kr skty hn
# ,,, is liye kr rhyn hn k hm chahty hn k x_axis pr numbers ki bijay
# vhi c,c++ etc shoe ho p+w ko 2 s divide is liye kia ta k y names dono bars k drmian m show hon

# xticks(  is used to get and set the current tick locations and labels of the x-axis.)

# Syntax:
# matplotlib.pyplot.xticks(ticks=None, labels=None, **kwargs)

plt.legend()
plt.show()


#  !!!!!!!!!!!!!!  horizontal bar graph  !!!!!!!!!!!!!!!!!!!!
plt.barh(x,y)
plt.show()


# barh error show kry ga agr hm n width=___ dia ho to, hmy height=___ dena h in case of barh
# like below:::
# plt.barh(p,y,height=w,color="green",edgecolor="black",linestyle=":",linewidth=3,label="wikipedia")
# plt.barh(p1,z,color="red",height=w)
# plt.legend()
# plt.show()
