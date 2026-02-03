import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,5,1,3,2]
plt.plot(x,y)
# plt.text(3,3,"python", bbox={"facecolor":"red"}, style="italic")  
# plt.text() -> yani mujy graph m beech m khi text show krvana h, 2,5 ka matlab k mujy vo
            # text x-axis m "3" and y-axis m "3" pr show ho, then us k baad vo text likhna
            # h jo ap ko show kvana h and then bbox={"facecolor":"red"} s ek box a jay or
            # us box ka color red show ho


# if you want k ap ko graph k kisi point ko show krna h arrow k saath yani arrow k head pr
# graph ka vo point ho and tail pr text ho:
# plt.annotate("python",xy=(4,3),xytext=(4.5,5), arrowprops={"facecolor":"green", "shrink":100})
        # "python" yani arrow ki tail pr text kia ho ga
        # "xy=(4,3)" yani arrow ki peak x-axis k 4 pr and y-axis k 3 pr ay gi
        # "xytext=(5,5))" yani vo text h yani python x-axis k 5 and y-axis k 5pr show ho

plt.legend(["label"],loc=7, facecolor="red", edgecolor="black",framealpha=0.5, 
shadow=True) #loc value range from 0 to 10
plt.show()
