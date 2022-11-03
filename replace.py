# importing pandas as pd
import pandas as pd
 
# importing numpy as np
import numpy as np


data= pd.read_csv("C:/Users/SPTINT-29/Desktop/dataset/employees (1).csv")
print(data)
print(data.head(10))
# creating a dataframe from list
df = pd.DataFrame(data)
 
# using isnull() function 
print(data.replace(to_replace = np.nan, value = -99))