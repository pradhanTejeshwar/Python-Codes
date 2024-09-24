import pandas as pd
def data_len():
    data = pd.read_csv('Price vs selling unit.csv')
    total = len(data['Price'])
    print(total)


if __name__ == '__main__':
    data_len()