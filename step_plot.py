# For data that doesn't change at a continuous rate, a Step Line Chart is an effective way
# to display the durations of values and the magnitudes of changes between them.
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[4,5,3,2,1]
z=[4,1,2,8,5]
plt.step(x,y, color="g", marker="*", ms=9, mfc="r", label="1st graph")
plt.step(x,z, color="r", marker=".", ms=10, mfc="m", label="2nd graph")
# mfc=marker face color
# ms= marker size
plt.grid()
plt.xlabel("x_exis")
plt.ylabel("y_asix")
plt.title("step plot")
plt.legend(loc=1)
plt.show()