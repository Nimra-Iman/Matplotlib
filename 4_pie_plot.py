# pie chart or pie plot is used to show proportiona and percentages
import matplotlib.pyplot as plt
x=[10,20,30,40]  #yani meri 100% salary m s 10% saving hoti h, 20% food m kharcha hota h etc
y=["saving","food","bills","rent"]
col=["r","b","g","y"]
plt.title("pie graph showing expenditures")
plt.pie(x, labels=y, colors=col)
plt.legend(loc=3) #loc means location, where you wanna place label
# plt.show()


# explode parameter: (yani m chahti hu k is pie graph m koi part baher ki trah dikhai de)
ex=[0.2,0.0,0.0,0.0]  # baki sab 0.0 hn but saving ka 0.2 h, yani saving vala part thora sa
# baher ko show ho ga, yani ap kisi ko bhi baher nikal skty ho
# plt.pie(x,labels=y,explode=ex) 
# plt.show() 



# "autopct"(if you want k hr part k uper us ki percentage bhi show ho), "shadow" 
# and radius(to increase the size of circle of pie graph)
# plt.pie(x, labels=y, autopct="%0.1f%%", shadow=True, radius=1.5) # %0.1f%%  "0.1f" yani point k baad 1 
# #                       digit show ho, %%0.2f% krny s point k baad 2 digits show hon gy
#                     #   and % ka sign bhi show ho ga q k hm n ek % ka symbol izafi lgaya
#                     # h , yani two "%%" lgay hn, as you can see.
# plt.show()


# labeldistance(yar labels ko graph s thora door ya paas show krna ho to)
# plt.pie(x, labels=y, autopct="%0.1f%%", labeldistance=1.5) 
# plt.show()


# startangle() deafult is 0 degree, yani phly number pr saving hn to graph ofcourse
# saving s start ho ga and by default saving vala hissa 0 degree s start ho ga, 
# hm start ko chnage kr skty hn 0 degree s, koi bhi angle rkh skty hn
# plt.pie(x, labels=y, autopct="%0.1f%%", labeldistance=1.5, startangle=90) 
# plt.show()


# textprops(yani text properties, is k ander jo bhi cheez jay ga vo dictionery ki
# form m jay ga , hm is k fontsize ka parameter daalyn gy to increase the fontsize)
# plt.pie(x, labels=y, autopct="%0.1f%%", labeldistance=1.5, textprops={"fontsize": 19}) 
# plt.show()

# counterclock ( to rotate circle from counterclockwise to clock wise) default is counterclockwise
# plt.pie(x, labels=y, autopct="%0.1f%%", counterclock=False) 
# plt.show()


# wedgeprops ( is k ander bhi jo kuch jay ga vo dictionery ki form m jay ga or m 
# is m linewidth daalu gi to increase the shadow. agar m n shadow=True kiye bagher
# line width daali to koi affect nhi ho ga  )
# plt.pie(x, labels=y,shadow=True, autopct="%0.1f%%",textprops={"fontsize": 15}, 
#         wedgeprops={"linewidth":5,  "edgecolor":"black", "linestyle":":"})  #"width": 2 krny s hr ek ek part ki 
#         # width brhy gi, is s readability khraab ho gi 
# plt.show()


# center() Imagine the plot area as a grid where the origin (0.0, 0.0) is at the
#  bottom-left corner. Moving the center to (0.5, 0.5) places the pie chart in the middle 
# of the plot area. Moving it to (1.0, 1.0) shifts it further towards the top-right corner.

# plt.pie(x, labels=y,shadow=True, autopct="%0.1f%%",textprops={"fontsize": 15}, 
#         center=(1.0,2.0)  )   #yani graph ka center 1.0 x-axis and 2.0 y-axis pr ho
# plt.show()


# rotatelabel (to rotate the label)
# plt.pie(x, labels=y,shadow=True, autopct="%0.1f%%",textprops={"fontsize": 15}, 
#          rotatelabels=True )

# plt.show()


# --------------------------  DOT pie chart
# plt.pie([1])
# plt.show()


# ---------------------  DONUT pie chart/ multiple pie chart (yani ek pie chart k ander doosra
#                   pie chart, us k ander teesra pie chart)
# plt.pie(x, labels=y, colors=col,radius=1.5)
# data=[20,30,40,10]
# plt.pie(data,radius=0.5)
# plt.legend()
# plt.show()


# ------------------ DONUT CHART
# plt.pie(x, labels=y, colors=col,radius=1)
# plt.pie([1],colors="white",radius=0.7)
# plt.show()


# ANOTHER WAY TO CREATE DONUT CHART:
# plt.pie(x, labels=y, colors=col,radius=1)
# cr=plt.Circle(xy=(0,0),radius=0.5,facecolor="white") 
# plt.gca().add_artist(cr)
plt.show()

