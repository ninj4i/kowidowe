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
sns.scatterplot(data = arch_data, x = 'Data', y = 'Nowe przypadki', size= 2)

print(arch_data.dtypes)

plt.show()
