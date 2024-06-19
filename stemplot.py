# they are used in signal systems
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,2,4,1,5]
plt.stem(x,y,linefmt="-.", markerfmt="r+", bottom=2, basefmt="green", label="python",
           orientation="horizontal"     )  
# --- linefmt="--" (dashed line)  or ":" (ditted) or "-."(dashed_dot) or "-" (solid) 
            # it can also be linefmt="r--" and so on
# --- markerfmt="r+" yani red color ka marker ho or us ka symbol + ho, or "r*" or 
#               "ro" fot dotted marker, it can also be markerfmt="+"
# --- bottom=1 krny s ab jo horizontal line lgi thi vo 1 pr ho gi show, 
#               bottom=9 kr k dekhna 
# --- basefmt="green" krny s baseline ka color change ho gya
# --- use_line_collection=False
plt.legend()
plt.show()

