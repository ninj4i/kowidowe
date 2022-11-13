import pandas as pd
import numpy as np
a = pd.DataFrame({'x': [1,2,3,4,5,6,7,8,9,10], 'y': [2,2,2,3,4,5,6,6,6,0]})
print(a)
print(a.rolling(window = 3, min_periods = 1).mean())

kolory= ['goldenrod', 'firebrick' , 'darkcyan', 'darkmagenta]