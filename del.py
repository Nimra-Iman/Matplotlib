import matplotlib.pyplot as plt
from numpy import random
random.seed(0)
data=random.randint(50,size=(50))
l=[0,10,20,30,40,50]
print(data)
plt.hist(data, bins=l ,color="green",edgecolor="black",alpha=0.8,label="distribution of data",
             )
plt.axvline(49)
plt.legend()
plt.show()





