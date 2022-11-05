import requests
import zipfile
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


"""
wstępnie niepotrzebne linie bo mamy na dysku plik
"""
#r = requests.get('https://arcgis.com/sharing/rest/content/items/a8c562ead9c54e13a135b02e0d875ffb/data')
#zawartosc = r.content

#with open('dane//dane.zip', 'wb') as plik:
#    plik.write(zawartosc)


#with zipfile.ZipFile('dane//dane.zip') as spaklowany_plik:
#    spaklowany_plik.extractall(pathlib.Path('dane/pliki'))


lista_plikow = list(pathlib.Path.glob(pathlib.Path('dane/pliki'), '*.csv'))

for i in lista_plikow[:5]:
    print(i)

arch_data0 = pd.read_csv(pathlib.Path('dane/mat_arch.csv'), sep = ';',decimal=' ', encoding= 'windows-1250')
arch_data = pd.DataFrame()
arch_data['Data'] = pd.to_datetime(arch_data0['Data'], format='%d.%m.%Y')
arch_data['Liczba Przypadkow'] = arch_data0['Nowe przypadki'].astype('int')
arch_data.index = arch_data['Data']


plt.rcParams['figure.dpi']     = 100
plt.rcParams['figure.figsize'] = 15,5

#kokokoko = []
#kokokoko.append(pd.DataFrame().assign(data = arch_data.loc[:,'Data'], liczba_przypadkow = arch_data.loc[:,'Nowe przypadki']))
#for plik in lista_plikow[:2]:
#    ko = pd.read_csv(plik)
#    print(ko.columns = ['Data', 'columns']
#    kokokoko.append(ko.iloc[0,1])

print(arch_data)
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

#koko =pd.concat(kokokoko)

#sns.scatterplot(data = koko, x = 'data', y = 'liczba_przypadkow', size= 1, legend = False)
#plt.show()
#print(kokokoko)


x = []
#x.append(arch_data)

for i, _ in enumerate(lista_plikow):
    nazwa_kolumny = 'liczba_przypadkow' if 'liczba_przypadkow' in list(pd.read_csv(lista_plikow[i], sep = ';',decimal=' ', encoding= 'windows-1250').columns.values) else 'liczba_wszystkich_zakazen'
    #print(pd.to_datetime(str(lista_plikow[i])[11:19],format='%Y%m%d')-datetime.timedelta(days = 1))
    #print(f"\t {pd.read_csv(lista_plikow[i], sep = ';',decimal=' ', encoding= 'windows-1250').loc[0,nazwa_kolumny]}")
    x.append([pd.to_datetime(str(lista_plikow[i])[11:19],format='%Y%m%d'),\
        pd.read_csv(lista_plikow[i], sep = ';',decimal=' ', encoding= 'windows-1250').loc[0,nazwa_kolumny]])


#print(pd.DataFrame(x))
y = pd.DataFrame(x, columns=['Data', 'Liczba Przypadkow'])
y.index = y['Data']
X = pd.concat([arch_data, y])
print(X)
X.columns = ['Data', 'Liczba Przypadkow']
X.index = X['Data']


print(X[X['Data'] < pd.to_datetime('2020-11-25', format='%Y-%m-%d')])
sns.lineplot(data = X.rolling(window = 7).mean(), x = 'Data', y = 'Liczba Przypadkow', size= 1, legend=False)
#sns.lineplot(data = X, x = 'Data', y = X['Liczba Przypadkow'].cumsum(), size= 1, legend=False)

plt.xticks(pd.to_datetime([f'{yr}-{mo}-01' for mo in range(1,13) for yr in range(2020, 2023)]),rotation = 45, size = 7,\
    labels = [f'{yr}-{mo}' for mo in range(1,13) for yr in range(2020, 2023)])
plt.tight_layout()
plt.show()
