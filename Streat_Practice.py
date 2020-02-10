import numpy as np
import matplotlib.pyplot as plt

def standardize(x):
    x_maen = x.mean()
    std = x.std()
    return (x - x_maen) / std

def f(x_std, w_0, w_1):
    return w_0 + w_1 * x_std

def E(x_std, y, w_0, w_1):
    return 0.5*np.sum((y-f(x_std, w_0, w_1))**2)

def gradient_method(x_std, y):
    w_0 = np.random.rand()
    w_1 = np.random.rand()

    LNR = 0.001

    difference = 1
    differences = [1]
    count = 0
    err_before = E(x_std, y, w_0, w_1)
    
    log = '{}回目: w0 = {:.3f}, w1 = {:.3f}, 差分 = {:.4f}'

    while difference > 0.01:
        tmp_w_0 = w_0 - LNR * np.sum(f(x_std,w_0,w_1)-y)
        tmp_w_1 = w_1 - LNR * np.sum((f(x_std, w_0, w_1)-y)*x_std)
        w_0 = tmp_w_0
        w_1 = tmp_w_1

        err_after = E(x_std, y, w_0, w_1)

        difference = err_before - err_after
        differences.append(difference)
        # print("err_after = " + str(err_after))
        # print("err_before = " + str(err_before))
        err_before = err_after
        if (count == 1 or count %100 == 0):
            # print("w_0 = " + str(w_0))
            # print("w_1 = " + str(w_1))
            print(log.format(count, w_0, w_1,difference))
        count+=1
    print(log.format(count, w_0, w_1, difference))
    #print("difference = " + str(difference) )
    x_count = np.array(len(differences))
    yoko_sen = np.linspace(start=0,stop=1,num=x_count)
    #print("x_count = " + str(x_count))
    plt.plot(yoko_sen, differences)
    plt.show()

    return w_0, w_1


data = np.loadtxt(fname='sales.csv', dtype='int',delimiter=',',skiprows=1)
x = data[:,0]
y = data[:,1]
x_std = standardize(x)
#print("x_std = " + str(x_std))
w_0, w_1 = gradient_method(x_std,y)

x_axis = np.linspace(start=-3,stop=3,num=100)
#print("x_axis = " + str(x_axis))
plt.plot(x_std, y, '.')
plt.plot(x_axis, f(x_axis, w_0,w_1))
plt.show()

input_x = input('予測に使用するxの値を入力してください>')
x_mean=x.mean()
std = x.std()
pred=(int(input_x)-x_mean)/std
print(f(pred, w_0, w_1))

