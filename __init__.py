from leaf import Daon
import pandas as dafa
from IPython.display import display

# def labelling():

def process_data(width, length, species):
    data = []
    for i in range(len(width)):
        data.append(Daon(width = width[i], length = length[i]))
    
    return data

def add_row(data):
    return data

def remove_row(data):
    return data

def add_column(data):
    return data

def remove_column(data):
    return data

def main():
    data = dafa.read_csv('data.csv')
    # data.columns = ['width', 'length', 'species']
    print(data.columns.tolist())
    
    # res = process_data()
    # for i in res:
    #     print(i.define_species())
    #     print(i.width, i.length, i.species, i.addition)

main()