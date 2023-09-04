from leaf import Daon
import pandas as dafa
from IPython.display import display
from species import Species

# 1. Jika ada data baru, dengan kolom yang ada, bisa atau tidak menebak species data baru tersebut
# 2. Jika ada data baru dan salah satu kolom dihilangkan, bisa atau tidak menebak species data baru tersebut
# 3. Jika ada data baru dan ditambahkan lagi satu kolom untuk semua data yang ada, bisa atau tidak menebak species data baru tersebut
# 4. Jika ada data baru dan juga golongan species baru, bisa atau tidak untuk menebak species data baru tersebut

def labelling(data):
    temp = []
    for daun in data:
        if len(daun) == 2:
            temp.append(Daon(daun[0], daun[1]))
            continue
        elif len(daun) == 1:
            temp.append(Daon(daun[0]))
            continue
        temp.append(Daon(daun[0], daun[1], daun[2], daun[3]))
    return temp

def process_data(data, header):
    for head in header:
        if head == 'leaf width':
            data[head] = data[head].astype(float)
        elif head == 'leaf length':
            data[head] = data[head].astype(float)
        elif head == 'species':
            data[head] = data[head].astype(str)
        else:
            data[head] = data[head].astype(str)
   
    return data

def menu():
    print("Studi Kasus: ")
    print("1. Jika ada data baru, dengan kolom yang ada, bisa atau tidak menebak species data baru tersebut")
    print("2. Jika ada data baru dan salah satu kolom dihilangkan, bisa atau tidak menebak species data baru tersebut")
    print("3. Jika ada data baru dan ditambahkan lagi satu kolom untuk semua data yang ada, bisa atau tidak menebak species data baru tersebut")
    print("4. Jika ada data baru dan juga golongan species baru, bisa atau tidak untuk menebak species data baru tersebut")
    pilih = int(input("Pilih menu: "))
    return pilih


def main():
    data = dafa.read_csv('dataset/data.csv')
    # data.columns = ['width', 'length', 'species']
    header = data.columns.tolist()
    res = process_data(data, header)
    # print(daon)
    # print(res)
    pilih = menu()
    if pilih == 1:
        print("1.  Jika ada data baru, dengan kolom yang ada, bisa atau tidak menebak species data baru tersebut")

        data1 = dafa.read_csv(r'dataset/soal1.csv')
        header1 = data1.columns.tolist()

        res1 = process_data(data1, header1)
        daun1 = labelling(res1.values.tolist())

        for daun in daun1:
            daun.define_species()
            daun = daun.tolist()
            res.loc[len(res)] = daun

        print(res)
    elif pilih == 2:
        print("2. Jika ada data baru dan salah satu kolom dihilangkan, bisa atau tidak menebak species data baru tersebut")
        
        data2 = dafa.read_csv(r'dataset/soal2.csv')
        header2 = data2.columns.tolist()

        res2 = process_data(data2, header2)
        daun2 = labelling(res2.values.tolist())
        for daun in daun2:
            daun.define_species()
            daun = daun.tolist()
            res.loc[len(res)] = daun

        print(res)
    elif pilih == 3:
        print("3. Jika ada data baru dan ditambahkan lagi satu kolom untuk semua data yang ada, bisa atau tidak menebak species data baru tersebut")

        data3 = dafa.read_csv(r'dataset/soal3.csv')
        header3 = data3.columns.tolist()

        temp3 = process_data(data3, header3)
        # print(temp3)
        daun3 = labelling(temp3.values.tolist())
        # print(daun3)
        res3 = dafa.DataFrame(columns=header3)
        for daun in daun3:
            # print(daun.addition)
            daun.define_species()
            daun = daun.tolist()
            res3.loc[len(res3)] = daun
            # print(daun)
        print(res3)
    elif pilih == 4:
        print("4. Jika ada data baru dan juga golongan species baru, bisa atau tidak untuk menebak species data baru tersebut")

        species_list = [
            Species('small-leaf', )
        ]

        data4 = dafa.read_csv(r'dataset/soal4.csv')
        header4 = data4.columns.tolist()

        temp4 = process_data(data4, header4)
        daun4 = labelling(temp4.values.tolist())
        res4 = dafa.DataFrame(columns=header4)
        for daun in daun4:
            daun.define_species()
            daun = daun.tolist()
            res4.loc[len(res4)] = daun
        print(res4)
main()