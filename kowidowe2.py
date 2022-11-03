import requests
import zipfile
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

kowidowe = []


lista_plikow = list(pathlib.Path.glob(pathlib.Path('dane/pliki'), '*.csv'))

for plik in lista_plikow:
    kowidowe.append(pd.read_csv(plik,encoding= 'windows-1250', sep = ';'))


print(len(kowidowe))


for i in range(1, len(kowidowe)):
    if list(kowidowe[i].columns) == list(kowidowe[i-1].columns):
        continue
    else:
        print(f'{i: ^5} : ')
        for q in kowidowe[i-1].columns:
            print(q)

i = 707
print(f'{i: ^5} : ')
for w in kowidowe[707].columns:
    print(w)

print(kowidowe[,2707])
