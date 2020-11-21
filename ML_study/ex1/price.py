import numpy as np
import matplotlib.pyplot as plot
data = np.loadtxt('./ex1/ex1data1.txt', delimiter=',')
x = data[:, 0]
y = data[:, 1]
def abline(slope, intercept):
    x_vals = x
    y_vals = intercept + slope * x_vals
    plot.plot(x_vals, y_vals, color='red', linewidth=5,zorder=10)
def J_func (x,y,k,b):
    l=len(x)
    func=k*x+b
    SqrErr=np.power((func-y),2)
    J=1/(2*l)*np.sum(SqrErr)
    return J
def func1 (x,y,k,b):
    l=len(x)
    func=k*x+b
    SqrErr=np.power((func-y),2)
    J=1/l*np.sum(SqrErr)
    return J
def func2 (x,y,k,b):
    l=len(x)
    func=k*x+b
    SqrErr=x*np.power((func-y),2)
    J=1/l*np.sum(SqrErr)
    return J

def recursion (k,b,alpha):
    k_new=k-alpha*func1(x,y,k,b)
    b_new=b-alpha*func2(x,y,k,b)
    temp=np.array([k_new,b_new])
    if (np.abs(J_func(x,y,k_new,b_new)-J_func(x,y,k,b))<0.0001):
        # print("vic")
        return temp
    else:
        # print(temp) 
        # print("yes")
        return recursion (k_new,b_new,alpha)
ans=recursion(1,1,0.00000001) ## In this step, how to let alpha automatically fit in the object data?
print(ans[0],ans[1])
abline(ans[0],ans[1])
plot.scatter(x,y,s=100,zorder=0)
plot.title('title',fontsize=24)
plot.xlabel('x',fontsize=12)
plot.ylabel('y',fontsize=12)
plot.tick_params(axis='both',labelsize=12)
plot.show()