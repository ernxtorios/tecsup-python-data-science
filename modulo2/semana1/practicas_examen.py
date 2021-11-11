
import numpy as np
nro_list = [ [1.1, 2.3 , 3.1 ], [4.2, 5.8 , 8.3] ]
nro_array = np.array(nro_list)
print(nro_array.shape)


import numpy as np

a_array = np.arange(1,8)
print(a_array.max()-a_array.min())


import numpy as np

a_array = np.arange(0,10)
print(a_array[0:5])


import numpy as np

d1 = np.ones((1,3))
d2 = np.zeros((1,3))
print(np.hstack((d2,d1)))


import numpy as np

a_matrix = np.arange(0,16).reshape(4,4)
a_matrix.var(ddof=1)


import pandas as pd

poblaciones = [31,11,17,18,44]
paises= ["Peru", "Bolivia", "Chile", "Ecuador", "Argentina"]
df=pd.Series(poblaciones, index=paises)
print(df["Chile"])


import pandas as pd

data_dic ={ "Pais": ["Perú","Chile","Ecuador"],
                          "Oro": [ 11, 9, 7],
                           "Plata": [ 22,20,10]}
df = pd.DataFrame(data_dic)

print(df['Oro'].sum())



import pandas as pd

data_dic ={ "Pais": ["Perú","Chile","Ecuador","Bolivia"],
                          "Oro": [11, 9, 8, 4],
                          "Plata": [22, 20, 10, 5]}
df = pd.DataFrame(data_dic)

print(df['Oro'].mean())


import pandas as pd

data_dic ={ "Pais": ["Perú","Chile","Ecuador","Bolivia"],
                          "Oro": [11, 9, 8, 4],
                          "Plata": [22, 20, 10, 5]}
df = pd.DataFrame(data_dic)

print(df['Oro'].median())
