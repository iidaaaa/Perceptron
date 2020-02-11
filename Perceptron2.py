import numpy as np
import matplotlib.pyplot as plt

#ステップ関数
def step_function(x1,x2,w1,w2):
    step_x1 = x1 * w1
    step_x2 = x2 * w2
    step_x = step_x1 + step_x2

    if step_x >= 0:
        return 1
    else:
        return -1


#重み更新
def weight_update(x1,x2,t):
    w1 = np.random.rand()
    w2 = np.random.rand()
    
    loop = 5
    count = 1
    for i in range(loop):
        for update_x1, update_x2, update_t in zip(x1,x2,t):
            if step_function(update_x1, update_x2, w1, w2) != update_t:
                w1 = w1 + update_x1 * update_t
                w2 = w2 + update_x2 * update_t

                print(str(count) + "回目の重みを更新" + " w = " + str(w1) + ", " + str(w2))
                count += 1

    return w1,w2


def main():
    #データ入力
    data = np.loadtxt(
        'trainingData.csv',
        delimiter = ','
    )
    x1 = data[:,0]
    x2 = data[:,1]
    t = data[:,2]

    w1 ,w2 = weight_update(x1,x2,t)

    #表の作成
    for x1, x2, t in zip(x1, x2, t):
        if t ==1:
            plt.plot(x1, x2,  "*", markersize=15, color="g")
        else:
            plt.plot(x1, x2,  ".", markersize=15, color="r")

    xx = np.arange(0,170)
    plt.plot(xx, -w1 / w2 * xx, linestyle='solid',color="k")

    plt.show()

    #数値入力・識別
    input_x1 = float(input("縦の長さ = "))
    input_x2 = float(input("横の長さ = "))
    print("\n")

    print("識別結果↓")
    if step_function(input_x1,input_x2,w1,w2) == 1:
        print('"縦長"')
    else:
        print('"横長"')

if __name__ == '__main__':
    main()