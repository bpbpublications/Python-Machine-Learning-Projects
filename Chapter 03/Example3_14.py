x = [5, 10,7]
y = [12, 6, 15]
x1 = [3, 8, 12]
y1 = [5, 9, 15]
plt.scatter(x,y,color='r', label="Red", marker='o', s=200, alpha=0.2)
plt.scatter(x1,y1,color='g', label="Green")
plt.legend()
plt.show()
