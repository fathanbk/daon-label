from leaf import Daon
import pandas as dafa
from IPython.display import display
from species import Species
from math2 import make_range

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
        elif len(daun) == 3:
            temp.append(Daon(daun[0], daun[1], daun[2]))
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

def print_list(list, sep, property = None):
    for i in list:
        if i != list[-1]:
            if property != None:
                print(i.property, end=sep)
            else:
                print(i, end=sep)

def menu():
    print("\nStudi Kasus: ")
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
    print("\nData Awal:")
    print(res)
    pilih = menu()
    if pilih == 1:
        print("\n1.  Jika ada data baru, dengan kolom yang ada, bisa atau tidak menebak species data baru tersebut\n")

        species_list = [
            Species('small-leaf'),
            Species('big-leaf'),
        ]

        print('List Spesies : ')
        for i in species_list:
            if i != species_list[-1]:
                print(i.name, end=', ')
            else:
                print(i.name)

        print()

        data1 = dafa.read_csv(r'dataset/soal1.csv')

        width = make_range(data1['leaf width'].tolist(), species_list)
        length = make_range(data1['leaf length'].tolist(), species_list)
        print(f"Pembagian range lebar daun : {width}\n")
        print(f"Pembagian range panjang daun : {length}\n")
        # print(type(data1['leaf width'].tolist()[0]))

        for i in range(len(species_list)):
            species_list[i].max_length = length[i][1]
            species_list[i].min_length = length[i][0]
            species_list[i].max_width = width[i][1]
            species_list[i].min_width = width[i][0]
            species_list[i].max_area = species_list[i].max_length * species_list[i].max_width
            species_list[i].min_area = species_list[i].min_length *  species_list[i].min_width
            # print(species_list[i].max_length)

        species_df = dafa.DataFrame(columns=['name', 'min_length', 'max_length', 'min_width', 'max_width', 'min_area', 'max_area'])
        for species in species_list:
            species_df.loc[len(species_df)] = [species.name, species.min_length, species.max_length, species.min_width, species.max_width, species.min_area, species.max_area]
        print(species_df)
        print()

        header1 = data1.columns.tolist()

        res1 = process_data(data1, header1)
        daun1 = labelling(res1.values.tolist())

        for daun in daun1:
            daun.define_species(species_list)
            daun = daun.tolist()
            res.loc[len(res)] = daun

        print(res)
    elif pilih == 2:
        print("\n2. Jika ada data baru dan salah satu kolom dihilangkan, bisa atau tidak menebak species data baru tersebut\n")
        
        species_list = [
            Species('small-leaf'),
            Species('big-leaf'),
        ]

        data2 = dafa.read_csv(r'dataset/soal2.csv')
        header2 = data2.columns.tolist()

        width = []
        length = []
        for header in header2:
            if header == 'leaf width':
                width = make_range(data2[header].tolist(), species_list)
            elif header == 'leaf length':
                length = make_range(data2[header].tolist(), species_list)

        # if data2['leaf width'].empty == False : 
        #     width = make_range(data2['leaf width'].tolist(), species_list)
        # if data2['leaf length'].any() == False :
        #     length = make_range(data2['leaf length'].tolist(), species_list)

        print('List Spesies : ')
        for i in species_list:
            if i != species_list[-1]:
                print(i.name, end=', ')
            else:
                print(i.name)

        print()

        print(f"Pembagian range lebar daun : {width}\n")
        print(f"Pembagian range panjang daun : {length}")
        print()
        for i in range(len(species_list)):
            if length != []:
                species_list[i].max_length = length[i][1]
                species_list[i].min_length = length[i][0]
            if width != []:
                species_list[i].max_width = width[i][1]
                species_list[i].min_width = width[i][0]
            species_list[i].max_area = species_list[i].max_length * species_list[i].max_width
            species_list[i].min_area = species_list[i].min_length *  species_list[i].min_width
            # print(species_list[i].max_length)

        species_df = dafa.DataFrame(columns=['name', 'min_length', 'max_length', 'min_width', 'max_width', 'min_area', 'max_area'])
        for species in species_list:
            species_df.loc[len(species_df)] = [species.name, species.min_length, species.max_length, species.min_width, species.max_width, species.min_area, species.max_area]
        print(species_df)
        print()

        header2 = data2.columns.tolist()

        res2 = process_data(data2, header2)
        daun2 = labelling(res2.values.tolist())
        # print(type(daun2[0].length))
        for daun in daun2:
            daun.define_species(species_list)
            daun = daun.tolist()
            res.loc[len(res)] = daun

        print(res)
    elif pilih == 3:
        print("\n3. Jika ada data baru dan ditambahkan lagi satu kolom untuk semua data yang ada, bisa atau tidak menebak species data baru tersebut\n")

        species_list = [
            Species('small-leaf'),
            Species('big-leaf'),
        ]

        print('List Spesies : ')
        for i in species_list:
            if i != species_list[-1]:
                print(i.name, end=', ')
            else:
                print(i.name)

        print()

        data3 = dafa.read_csv(r'dataset/soal3.csv')

        width = make_range(data3['leaf width'].tolist(), species_list)
        length = make_range(data3['leaf length'].tolist(), species_list)
        print(f"Pembagian range lebar daun : {width}\n")
        print(f"Pembagian range panjang daun : {length}\n")
        # print(type(data3['leaf width'].tolist()[0]))

        for i in range(len(species_list)):
            species_list[i].max_length = length[i][1]
            species_list[i].min_length = length[i][0]
            species_list[i].max_width = width[i][1]
            species_list[i].min_width = width[i][0]
            species_list[i].max_area = species_list[i].max_length * species_list[i].max_width
            species_list[i].min_area = species_list[i].min_length *  species_list[i].min_width
            # print(species_list[i].max_length)

        species_df = dafa.DataFrame(columns=['name', 'min_length', 'max_length', 'min_width', 'max_width', 'min_area', 'max_area'])
        for species in species_list:
            species_df.loc[len(species_df)] = [species.name, species.min_length, species.max_length, species.min_width, species.max_width, species.min_area, species.max_area]
        print(species_df)
        print()

        header3 = data3.columns.tolist()

        temp3 = process_data(data3, header3)
        # print(temp3)
        daun3 = labelling(temp3.values.tolist())
        # print(daun3)
        res3 = dafa.DataFrame(columns=header3)
        for daun in daun3:
            # print(daun.addition)
            daun.define_species(species_list)
            daun = daun.tolist()
            res3.loc[len(res3)] = daun
            # print(daun)
        print(res3)
    elif pilih == 4:
        print("\n4. Jika ada data baru dan juga golongan species baru, bisa atau tidak untuk menebak species data baru tersebut\n")

        species_list = [
            Species('smaller-leaf'),
            Species('small-leaf'),
            # Species('medium-leaf'),
            Species('big-leaf'),
            Species('bigger-leaf'),
        ]

        print('List Spesies : ')
        for i in species_list:
            if i != species_list[-1]:
                print(i.name, end=', ')
            else:
                print(i.name)

        print()

        data4 = dafa.read_csv(r'dataset/data.csv')
        
        width = make_range(data4['leaf width'].tolist(), species_list)
        length = make_range(data4['leaf length'].tolist(), species_list)
        print(f"Pembagian range lebar daun : {width}\n")
        print(f"Pembagian range panjang daun : {length}\n")
        # print(type(data4['leaf width'].tolist()[0]))

        for i in range(len(species_list)):
            species_list[i].max_length = length[i][1]
            species_list[i].min_length = length[i][0]
            species_list[i].max_width = width[i][1]
            species_list[i].min_width = width[i][0]
            species_list[i].max_area = species_list[i].max_length * species_list[i].max_width
            species_list[i].min_area = species_list[i].min_length *  species_list[i].min_width
            # print(species_list[i].max_length)
        
        #make species list into dataframe
        species_df = dafa.DataFrame(columns=['name', 'min_length', 'max_length', 'min_width', 'max_width', 'min_area', 'max_area'])
        for species in species_list:
            species_df.loc[len(species_df)] = [species.name, species.min_length, species.max_length, species.min_width, species.max_width, species.min_area, species.max_area]
        print(species_df)
        print()

        data4 = dafa.read_csv(r'dataset/soal4.csv')
        header4 = data4.columns.tolist()
        temp4 = process_data(data4, header4)
        daun4 = labelling(temp4.values.tolist())
        res4 = dafa.DataFrame(columns=header)
        for daun in daun4:
            # print(daun.species)
            daun.define_species(species_list)
            daun = daun.tolist()
            res4.loc[len(res4)] = daun
        
        print(res4)
        # for x in species_list:
        #     print(x.name, x.max_length, x.min_length, x.max_width, x.min_width)



        # species_list.insert(2, 'test')
        # dict_priority = {}

        # counter = 1
        # for species in species_list:
        #     dict_priority[counter] = species
        #     counter += 1

        # for x in dict_priority:
        #     print(x, dict_priority[x].name)

        # print(*dict_priority.keys(), sep=', ')
        # for x in species_list:
        #     print(x.name)

        # data4 = dafa.read_csv(r'dataset/soal4.csv')
        # header4 = data4.columns.tolist()

        # temp4 = process_data(data4, header4)
        # daun4 = labelling(temp4.values.tolist())
        # res4 = dafa.DataFrame(columns=header4)
        # for daun in daun4:
        #     daun.define_species()
        #     daun = daun.tolist()
        #     res4.loc[len(res4)] = daun
        # print(res4)
main()