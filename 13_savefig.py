# in order to save matplotlib graphs in .png format
import matplotlib.pyplot as plt
x=[30,40,10,20]
plt.hist(x)
plt.title("graph of monthy expenditures")
plt.savefig("histogram", dpi=2000, facecolor="g", transparent=True, bbox_inches="tight")

# dpi=2000 - (dots per inch) is s graph ki quality bhhtt achi ay gi, jitna bhi zoom kr lo 
              # pixels nhi phaty gy 

# by default picture png m save ho gi, agar format chnage krna chahty hn, e.g m pdf 
        # m save krna chahti hu file ko to name k agy.pdf likh den gy , like below:
        # plt.savefig("histogram.pdf")

# facecolor="g" deny s graph k sides pr border a jay ga.

# transparent=True krny s border k sath saath graph ka  background color bhi change ho jay ga

# Without bbox_inches="tight", the saved image might include extra white space around the
#  figure, which is often not desirable, especially for publications or presentations 
# where you want the plot to be as compact as possible.



plt.show()
