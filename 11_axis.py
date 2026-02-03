# if we want k x-axis and y-axis pr kon s digits show hon, to hm x-ticks and y-ticks ko use
# kryn gy
import matplotlib.pyplot as plt
x=[1,3,2,4,1]
y=[3,1,5,4,1]
plt.plot(x,y)
plt.xticks(x,labels=["python","c","c++","java","html"]) #hm yhan labels bhi show krva
# skty hn, x-axis m jhan "1" show hona tha ab vhan python show ho ga, yhan 3 show
# hona tha ab vhan pr "c" show ho ga, jhan "2" show hona tha ab vhan "c++" show
# ho ga and jhan "4" show hona tha vhan "java" and then again jhan pr "1" show hona
# tha to hm n bola k vhan "python" show ho ga but again hm n keh dia k jhan "1" show
# hona tha vhan "html" show kro to "HTML" overwrite kr de gi "python" ko , x list m data
# sorted nhi h, 
# plt.yticks(x)

# plt.xlim(0,10) #yani x-axis pr 0 s le kr 10 tak digits any chhaye
# plt.ylim(0,10) #same fot y -axis,,,,  same isi cheez ko hm plt.axis k zrye bhi kr skty hn

# plt.axis([0,10,0,7])  #yani x-axis m 0 s 10 tak digits show hn, and y axis m 0 s 7 tak 
            # show ho 
plt.show()






