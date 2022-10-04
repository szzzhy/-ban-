#输入自变量值x；对应点的函数值y；
#m为一个int，是想要预测的点的自变量值。
#返回值为m对应的拉格朗日插值函数值
def Lagrange_interpolation(x,y,m):
    sum=0   #最终计算结果
    for i in range(len(x)):
        temp=1.0    #暂存l[i]的结果
        for j in range(len(x)):#求l[i]的累乘过程
            if(i!=j):
                temp=temp*(m-x[j])/(x[i]-x[j])
        sum=sum+temp*y[i]
    return sum


def Newtown_interpolation(x,y,m):
    sum=y[0]   #最终计算结果
    for i in range(1,len(x)):
        temp=0.0   #暂存0,i的差商的结果
        for j in range(i+1):#求0,i的差商,此处的j相当于f(xk)中的k
            temp2=y[j]  #暂存一部分0,i的差商的结果
            for k in range(i+1):
                if(k!=j):
                    temp2=temp2/(x[j]-x[k])
            temp=temp+temp2#此时求出了0,i的差商
        for j in range(i):
            temp=temp*(m-x[j])
        sum=sum+temp
    return sum

#同ppt例2的插值验证无误
x=[-1,1,3,4]
y=[-2,0,-6,3]
print(Lagrange_interpolation(x,y,2))
print(Newtown_interpolation(x,y,2))
x=[2,2.5,4]
y=[0.5,0.4,0.25]
print(Lagrange_interpolation(x,y,3))
print(Newtown_interpolation(x,y,3))