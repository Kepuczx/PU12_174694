import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def zad1():
    x = np.arange(1, 20, 0.1)
    y = 1/x


    plt.plot(x , y, ':>', label='liniowa')

    plt.legend(labels=['f(x) = 1/x'])

    plt.xlabel('x')
    plt.ylabel('f(x)')

    plt.title('Wykres funkcji f(x) dla x[1,20]')
    plt.show()

def zad2():
    x = np.arange(1, 21)
    y = 1 / x

    fig, ax = plt.subplots()
    ax.plot(x, y, marker=(3, 0, -90), color='green', linestyle='dotted', label='f(x)=1/x')
    ax.set_title('Wykres funkcji f(x) dla x[1,20]')

    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')


    ax.set_xlim([0, 21])
    ax.set_ylabel([0, 1])
    ax.legend()

    plt.show()


def zad3():
    x = np.arange(0.0, 30.0, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)


    plt.plot(x, y1, label='sin(x)')
    plt.plot(x, y2, label='cos(x)')

    plt.xlabel('X')
    plt.ylabel('Y')

    plt.title('Wykres fukcji sin(x) oraz cos(x)')

    plt.legend()
    plt.show()



def zad4():
    df1 = pd.read_csv('iris.csv')
    df = pd.DataFrame(df1)
    x1 = df.iloc[:, 0]
    x2 = df.iloc[:, 1]

    data = {'a': df.iloc[:, 0], 'b': df.iloc[:, 1], 'c': np.random.randint(0, 149, 149)}

    plt.scatter('a', 'b', c='c', s=x1-x2, data=data)
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    plt.show()






def main():
    #zad1()
    #zad2()
    #zad3()
    zad4()

if __name__ == '__main__':
    main()