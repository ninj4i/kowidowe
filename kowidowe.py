import requests
import zipfile
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from cycler import cycler

"""
wstępnie niepotrzebne linie bo mamy na dysku pliki
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
print(arch_data0.columns)
arch_data = pd.DataFrame()
arch_data['Data'] = pd.to_datetime(arch_data0['Data'], format='%d.%m.%Y')
arch_data['Liczba Przypadkow'] = arch_data0['Nowe przypadki'].astype('int')
arch_data.index = arch_data['Data']

"""
DF ze zgonami
kolumny:
    Data
    zgony_wszystkie
    zgony_w_wyniku_covid_bez_chorob_wspolistniejacych
    zgony_w_wyniku_covid_i_chorob_wspolistniejacych
index:
    Data
"""
zgony0 = pd.DataFrame()
zgony0['Data']  = pd.to_datetime(arch_data0['Data'], format='%d.%m.%Y')
zgony0['zgony'] = arch_data0['Zgony'].astype('int')

nazwy_kolumn =['zgony', 'zgony_w_wyniku_covid_bez_chorob_wspolistniejacych','zgony_w_wyniku_covid_i_chorob_wspolistniejacych']
zgony1 = {'Data':[], 'zgony':[], 'zgony_w_wyniku_covid_bez_chorob_wspolistniejacych':[],'zgony_w_wyniku_covid_i_chorob_wspolistniejacych':[]}
for i, _ in enumerate(lista_plikow):
    odczytane_dane= pd.read_csv(lista_plikow[i], sep = ';',decimal=' ', encoding= 'windows-1250')

    zgony1['Data'].append(pd.to_datetime(str(lista_plikow[i])[11:19],format='%Y%m%d'))
    zgony1[nazwy_kolumn[0]].append(odczytane_dane.loc[0,'zgony'])
    zgony1[nazwy_kolumn[1]].append(odczytane_dane.loc[0,nazwy_kolumn[1]])
    zgony1[nazwy_kolumn[2]].append(odczytane_dane.loc[0,nazwy_kolumn[2]])




print(zgony1)
zgony1 = pd.DataFrame(zgony1, index = zgony1['Data'])
zgony1.columns = ['Data', 'zgony', 'zgony_w_wyniku_covid_bez_chorob_wspolistniejacych','zgony_w_wyniku_covid_i_chorob_wspolistniejacych']
zgony1 = pd.concat([zgony0,zgony1])
zgony1.index = zgony1['Data']

print(zgony1)
#plt.rcParams['size']
plt.rcParams['figure.dpi']     = 100
plt.rcParams['figure.figsize'] = 15,10
plt.rcParams['axes.prop_cycle'] = cycler('color', ['cadetblue','orangered','darkolivegreen'])
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
    nazwa_kolumny = 'liczba_przypadkow' if 'liczba_przypadkow' in list(pd.read_csv(lista_plikow[i], sep = ';',decimal=' ', encoding= 'windows-1250').columns.values) else 'liczba_nowych_zakazen'
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

fig, axs = plt.subplot_mosaic(mosaic="""
A
B
""")


print(X[X['Data'] < pd.to_datetime('2020-11-25', format='%Y-%m-%d')])
sns.lineplot(data = X, x = 'Data', y = 'Liczba Przypadkow', legend=False, ax = axs['A'], label = 'Przypadki dzienne')
sns.lineplot(data = X.rolling(window = 7).mean(), x = 'Data', y = 'Liczba Przypadkow', legend=False, ax = axs['A'], label = 'Wygładzony przebieg')
#sns.lineplot(data = X, x = 'Data', y = X['Liczba Przypadkow'].cumsum(), size= 1, legend=False)

axs['A'].set_xticks(pd.to_datetime([f'{yr}-{mo}-01' for mo in range(1,13) for yr in range(2020, 2023)]))
axs['A'].set_xticklabels(rotation = 45, size = 7, labels = [f'{yr}-{mo}' for mo in range(1,13) for yr in range(2020, 2023)])
axs['A'].legend()
axs['A'].grid(axis = 'both', c = '0.90')



sns.lineplot(data = zgony1.rolling(window = 7).mean(), x = 'Data', y = 'zgony', legend = True, ax = axs['B'], label = 'Wszystkie zgony')
sns.lineplot(data = zgony1.rolling(window = 7).mean(), x = 'Data', y = 'zgony_w_wyniku_covid_bez_chorob_wspolistniejacych', legend = True, ax = axs['B'], label = 'Zgony bez chorób wsp.')
sns.lineplot(data = zgony1.rolling(window = 7).mean(), x = 'Data', y = 'zgony_w_wyniku_covid_i_chorob_wspolistniejacych', legend = True, ax = axs['B'], label = 'Zgony z chorobami wsp.')

axs['B'].set_xticks(pd.to_datetime([f'{yr}-{mo}-01' for mo in range(1,13) for yr in range(2020, 2023)]))
axs['B'].set_xticklabels(rotation = 45, size = 7, labels = [f'{yr}-{mo}' for mo in range(1,13) for yr in range(2020, 2023)])
axs['B'].legend()
axs['B'].grid(axis = 'both', c = '0.90')
plt.tight_layout()


plt.show()