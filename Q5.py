import pandas as pd
import matplotlib.pyplot as plt


def avg_price():
    data = pd.read_csv('Price vs selling unit.csv')
    avg = data['Price'].mean()
    print(avg)

def show_graph():
    data = pd.read_csv('Price vs selling unit.csv')
    data.plot.bar()
    plt.show()


if __name__ == '__main__':
    avg_price()
    show_graph()