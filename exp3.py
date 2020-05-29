import matplotlib.pyplot as plt
x = [2,4,6,8]
y = [10,12,8,14]
plt.plot(x,y,label="line",color="RED")
plt.legend()
plt.bar(x, y)
plt.show()