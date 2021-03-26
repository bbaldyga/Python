import matplotlib.pyplot as plt
x_values =list(range(1,1001))
y_values =[x**2 for x in x_values]
plt.scatter(x_values,y_values,s=40)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=24)
plt.ylabel("Square of Value",fontsize=24)

#Set size of tick labels.
#plt.tick_params(axis='both',which='major',labelsize=14)
#plt.scatter(x_values, y_values,c='red', edgecolor='none', s=40)
#plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolors='none',s=40)
#using colormap
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)
plt.axis([0, 1100, 0, 1100000])
#saving plots
plt.savefig('squares_plot.png')
plt.show()



