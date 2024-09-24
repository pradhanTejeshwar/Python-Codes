import pandas as pd
import matplotlib.pyplot as plt

def show_graph():
    data = pd.read_csv('Price vs selling unit.csv')
    data.plot.bar()
    plt.show()

def data_len():
    data = pd.read_csv('Price vs selling unit.csv')
    total = len(data['Price'])
    print(total)


if __name__ == '__main__':
    data_len()
    show_graph()