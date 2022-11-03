import requests
import zipfile
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



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

arch_data = pd.read_csv(pathlib.Path('dane/mat_arch.csv'), sep = ';',decimal=' ', encoding= 'windows-1250')

arch_data['Data'] = pd.to_datetime(arch_data['Data'], format='%d.%m.%Y')
arch_data['Nowe przypadki'] = arch_data['Nowe przypadki'].astype('int')


plt.rcParams['figure.dpi']     = 100
plt.rcParams['figure.figsize'] = 15,5
print(arch_data)
print(arch_data.dtypes)

kokokoko1= pd.read_csv(lista_plikow[100], sep = ';',decimal=' ', encoding= 'windows-1250')

kokokoko = pd.DataFrame().assign(data = arch_data.loc[:,'Data'], liczba_przypadkow = arch_data.loc[:,'Nowe przypadki'])
kokokoko2= pd.DataFrame().assign(data = kokokoko1.loc[:0,'stan_rekordu_na'], liczba_przypadkow = kokokoko1.loc[0:,'Nowe przypadki'])
koko =pd.concat(kokokoko, kokokoko2)

sns.scatterplot(data = koko, x = 'data', y = 'liczba_przypadkow', size= 1, legend = False)
plt.show()
print(kokokoko)