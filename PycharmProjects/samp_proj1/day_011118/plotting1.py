
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256)
Y1 = np.sin(X)
Y2 = np.cos(X)
Y3 = np.tan(X)
Y4 = np.sqrt(1 - X*X)

plt.figure(figsize=(6,4), dpi=80) # 6 for x axis and 4 for y axis, dpi decides how large the plot will be,
# figsize is proportional x and y values

plt.plot(X,Y1, color='blue',linewidth=2.5, linestyle=':', label='sin')
#plt.show()

plt.plot(X,Y2,color='red', linewidth=2.5, label='cos')
plt.xlim(X.min()*1.2)
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$\pi/2$',r'$\pi$'],rotation=30) # to view the actual values
plt.yticks([+1,0,-1],rotation=30)

ax = plt.gca()
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.xaxis.set_ticks_position('bottom') # top means the x-axis values will be floating at the top
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
plt.legend(loc='best')

for labels in ax.get_xticklabels() + ax.get_yticklabels():
    labels.set_fontsize(16)
    labels.set_bbox(dict(facecolor='grey', # to create a box around the values ( color of box -> facecolor,
                         edgecolor='red',                  # outline of box -> edgecolor, alpha-> transparency of box
                         alpha=0.35))
plt.savefig('myplot.png') #savefig before show

plt.show()

plt.plot(X,Y3)
plt.ylim(Y3.min()*1.5)
plt.show()

plt.plot(X,Y4)
plt.show()



