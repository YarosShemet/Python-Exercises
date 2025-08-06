import pandas as pd
fb = pd.read_csv("data/facebook.csv")
ms = pd.read_csv("data/microsoft.csv")
fb.head()
fb.tail(5)
fb.describe()
fb.loc("index_name", "column_name")
fb.iloc(1, 3)  #numbers show the position (index, column)
#we can use slicing
