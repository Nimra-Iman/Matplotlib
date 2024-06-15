# scatter plt is used to show relationship between two variables
import matplotlib.pyplot as plt
plt.xlabel("time")
plt.ylabel("speed")
plt.title("time vs sped")
col=["red","b","g","y","orange"]
time=[1,2,3,4,5]
speed=[20,40,5,90,100]
distance=[20,60,80,4,13]

sizess=[500,400,90,630,10]
a=[0.4,0.6,1,0.8,0.3]
# m=["*",".","^","^","*"]  # this is not allowed

# plt.scatter(time,speed,label="car",color=col, edgecolors="red",
#             linewidths=3,s=sizess, marker="*", alpha=a) #s=500 khali bhi likh skty agar
#                 # sab ka ek hi size rkhna h, marker s ap shape change kr skty ho
# plt.legend()
# plt.show()


# ANOTHER FEATURE IN SCATTER PLOT IS COLORMAP
# colormap m bhtttt saary colors hn, ek poori bht bri list h colors ki or hr name ka
# apna ke colorbar h yani hr color ka poora ek bar h jis k ander bhhtt colors hn

# color bar list contains e.g: Accent, blues, BrBG, BuGn, BuPu, Dark2, Greens, Greys etc etc 
colllors=[10,50,80,45,100]
plt.scatter(time,speed,c=colllors,cmap="Accent", edgecolors="black",linewidths=2)
# plt.colorbar() #is s colormap m "Accent" name ka poora color bar show ho ga, or is 
# scatterplot k marker k colors vhi hon gy jo numbers hm n colllors m likhyn hn or y
# colors us color baar ki sides pr jo numbers hn us k braber h asal m,,,,, hm colorbar
# k saath labels bhi lga skty hn, like below:
l=plt.colorbar()
l.set_label("colorbaar", fontsize=15)



# we can also show multiple scatter plotrs as well:
plt.scatter(time, distance, c="red",s=500)
plt.show()

