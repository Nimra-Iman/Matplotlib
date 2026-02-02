# min, Q1, median, Q3, max
# Q1 s Q3 IQR h or vhi box plot h, baki ka hissa whisker plot kehlata h

import matplotlib.pyplot as plt
data=[20,10,30,60,70,40,50]
# plt.boxplot(data)
# plt.show()


# (notch = True) to chnage the shape of box, yani box ki bijay V shape kuch show ho
# (vert = False) to show orizontal box plot.
plt.boxplot(data, notch=True, vert=False)
plt.show()


# (widths) to increase width of box. default width is 0.2
# (labels) jo bhi lables add krny hn vio list ki form m krny hn q k hm mostly ek s ziada
                # boxplot bna rhy hoty hn,to he ek ka apna apna label
# (patch_artist=True) to fill color inside box
# plt.boxplot(data , widths=0.5, labels=["market"], patch_artist=True)
# plt.show()



# (showmeans=True) mean ko highlight kr de ga
# to show outlier
datas=[10,20,30,40,50,60,70,170]
# plt.boxplot(datas )
# plt.show()



# whis=__  to join whisk to outlier
# plt.boxplot(datas , whis=5)
# plt.show()  



# to change the color and shape of outlier whole:
# sym=" " esy kryn gy if you want to hide outlier
# boxprops:  to change the color of boxline or is k ander jo bhi jay ga vo dictionery ki 
            # form m jay ga
# capprops: to chnage the color of min and max line and same is k ander bhi 
            #  dictionery ki form m hi likhyn gy::  capprops = dict(color="r") esy bhi likh 
            #  skty dict ko
# whiskerprops: 
# plt.boxplot(datas , sym="g+", boxprops={"color":"r"}, capprops={"color":"g"},
#              whiskerprops=dict(color= "green"),
#              flierprops= dict(markeredgecolor="b"))
# plt.show()



# to show multiple boxplots:
# plt.boxplot(datas , sym="g+", boxprops={"color":"r"}, capprops={"color":"g"},
#              whiskerprops=dict(color= "green"),
#              flierprops= dict(markeredgecolor="b"))
# plt.boxplot(data)
# plt.show()   #esa krny s dono ekdoosry k uper show hon gy, hmy esa nhi krna, is liye
# following is true

# y=[data, datas]
# plt.boxplot(y)
# plt.show()