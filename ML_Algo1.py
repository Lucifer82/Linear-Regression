import matplotlib.pyplot as plt

def linear_regression(c1,c2,df,train_data):
    X_avg,y_avg=df[c1].mean(),df[c2].mean()
    num=0
    den=0
    theta1=0
    theta0=0
    for a,b in df[[c1,c2]].values:
        num+=(a-X_avg)*(b-y_avg)
        den+=(a-X_avg)**2
    theta1=num/den
    theta0=y_avg-theta1*X_avg
    plt.scatter(df[c1],df[c2],label='REAL_POINTS')
    plt.xlabel(c1)
    plt.ylabel(c2)
    plt.plot(df[c1],theta1*df[c1]+theta0,'r',label='PREDICTED_LINE')
    plt.legend()
    plt.show()
    print('The predicted result of ',c2,' for ',c1,train_data,'is')
    return theta0+theta1*train_data
