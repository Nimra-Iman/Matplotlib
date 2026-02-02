# histogram visualizes the distribution of data
import matplotlib.pyplot as plt
# x=[2,2,2,4,6,8]  # "2" three times h baqi sab 1 time hn
# plt.hist(x)
# plt.show()

from numpy import random
random.seed(0)
data=random.randint(15,size=50)
plt.title("histogram via matplotlib")
plt.xlabel("data",fontsize=15)
plt.ylabel("frequency or distribution of data")

# histogram m ek dataset pr ek hi color show ho ga, esa nhi ho skta k ek dataset k
# hr element ka color different show ho

# plt.hist(data,color="purple",alpha=0.4,edgecolor="black",linestyle=":",linewidth=3,label="data")
# plt.legend()
#  plt.show()



# ----------------------------------------  bins 
# print(data)
l=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] 
li=[0,5,10,15]
# plt.hist(data,bins=li,edgecolor="black") #agar ap y bins parameter nhi lgaty to smjh hi nhi
# # ati shi s k kon ca element kitni dfa aya, ab m n yha bins=li likha yani li m btaya hua h k
# # 0 s 5 valy elemnts kitni baar ay, 6 s 10 valy kitni baar ay or 11 s 15 valy kitni bar ay
# plt.show()



# ----------------------------------------  range  
# isi trah range parameter bhi de skty hn, histogram m range parameter 3rd parameter hota h
# and bins 2nd parametr hota h, m yhan bins ko auto kr rhi, agar bins m "auto" ya koi
# single integer pass na kia jay to range parameter ignore ho jata h

# plt.hist(data,"auto",(0,100),edgecolor="black") 
# plt.show()



# ----------------------------------------  cumulative parameter
# A cumulative histogram is a type of histogram in which each bin contains the sum of the
# counts for that bin and all previous bins. This type of histogram can help visualize the
#  cumulative distribution of the data.

# plt.hist(data, bins=l,edgecolor="black",cumulative=True) 
# plt.hist(data, bins=li,edgecolor="black",cumulative=-1)  #Reverse Cumulative Histogram:
# plt.show()




# ----------------------------------------  bottom parameter
# plt.hist(data,edgecolor="black",bottom=10)  #yani y axis ka bottom 10 s start ho ga
# plt.show() ab e.g phly 0 - 10 ki range k elemnts ki occurance 9 thi, to ab bottom=10
# krny s vo occurance 19 show ho gi, yani ab 10 add hon gy beech m 


# ---------------------------------------  align =left,right, mid(default)
datas=random.randint(10,60, (50))
b=[10,20,30,40,50,60]
# plt.hist(datas,bins=b, align="left",edgecolor="black")
# plt.show()


# -----------------------------  histtype (can be "step", "stepfilled", "barstacked","bar")
# plt.hist(datas,bins=b, histtype="stepfilled",edgecolor="black")
# plt.show()


# -----------------------  orientation
# plt.hist(datas,bins=b, orientation="horizontal",edgecolor="black")
# plt.show()


# ----------------- rwidth (yani width ko km krna)
# plt.hist(datas,bins=b, rwidth=0.8,edgecolor="black")
# plt.show()


# ----------------- log table
# plt.hist(datas,bins=b, log=True,edgecolor="black")
# plt.show()


# --------------  divide graph via line
plt.hist(datas,bins=b,edgecolor="black")
plt.axvline(45,color="green",label="parted data") #ab dataset m jhan pr 45 number ay ga vhan ek green line 
# # show ho gi
# plt.legend()
# plt.grid()  #to show grid
plt.show()