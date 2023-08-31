from leaf import Daon
import pandas as dafa
from IPython.display import display


# def labelling():

def process_data(data, header):
    for head in header:
        if head == 'width':
            data[head] = data[head].astype(float)
        elif head == 'length':
            data[head] = data[head].astype(float)
        elif head == 'species':
            data[head] = data[head].astype(str)
        else:
            data[head] = data[head].astype(str)
   
    return data



def main():
    data = dafa.read_csv('data.csv')
    # data.columns = ['width', 'length', 'species']
    header = data.columns.tolist()
    res = process_data(data, header)
    print(res)
main()