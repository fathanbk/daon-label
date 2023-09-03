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

def menu():
    print("Studi Kasus: ")
    print("1.  Jika ada data baru, dengan kolom yang ada, bisa atau tidak menebak species data baru tersebut")
    print("2. Jika ada data baru dan salah satu kolom dihilangkan, bisa atau tidak menebak species data baru tersebut")
    print("3. Jika ada data baru dan ditambahkan lagi satu kolom untuk semua data yang ada, bisa atau tidak menebak species data baru tersebut")
    print("4. Jika ada data baru dan juga golongan species baru, bisa atau tidak untuk menebak species data baru tersebut")
    pilih = int(input("Pilih menu: "))
    return pilih


def main():
    data = dafa.read_csv('data.csv')
    # data.columns = ['width', 'length', 'species']
    header = data.columns.tolist()
    res = process_data(data, header)
    print(res)
    pilih = menu()
    if pilih == 1:
        print("1.  Jika ada data baru, dengan kolom yang ada, bisa atau tidak menebak species data baru tersebut")
        data1 = dafa.read_csv('soal1.csv')
        header1 = data1.columns.tolist()
        res1 = process_data(data1, header1)
        print(res1)
        # res = res.append(res1, ignore_index=True)
        # print(res)
main()