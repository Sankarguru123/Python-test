'''numpy array'''
import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(a)
print(b)


'''np.arange()

function takes start,end 
numpy.arange([start,] stop, [step], dtype=None)
'''

v = np.arange(5,50,5)
print(v)




v1 = np.ones((4,5),dtype=np.int16)

print(v1)
v2 = np.zeros((4,5),dtype=np.int16)
print(v2)



print(np.random.rand(3,2))




'''pandas '''

'''write a program that creates a data fracme a list of dictionary'''


import  pandas  as pd
import numpy as np


data = [
    {
    "name":"Sankar",
    "marks":90
},

{
    "name":"Anitha",
    "marks":95
},

{
    "name":"Yaswanth Krishna",
    "marks":97
},
{
    "name":"Nishanth krishna",
},

]

df = pd.DataFrame(data, index = ["Student1", "Student2", "Student3","Student4"])
print(df)



'''write a program  to create  a data frame from dictionary of series'''


data1 = {
    "ram": pd.Series([88,99,100,89], index=["M1", "M2", "M3","M4"]),
    "raj": pd.Series([90,93,95,96], index=["M1", "M2", "M3","M4"]),
    "dina": pd.Series([98,94,95,76], index=["M1", "M2", "M3","M4"]),
    "nishanth": pd.Series([95,94,95,89], index=["M1", "M2", "M3","M4"])
}
print(data1)

df1 = pd.DataFrame(data1)
print(df1.loc['M2'])
print(df1.iloc[1])



'''sort by brand in descending order'''

cars = {
    "Brand":["Ecosport","Brezza","Nexon", "Audi A5"],
   "Price":[993678,873456,908765,654789],
    "Year":[2011,2014,2016,2019]
}

df_2 = pd.DataFrame(cars, columns=['Brand','Price','Year'])
print(df_2)
df_2.sort_values(by=["Brand"], inplace=True, ascending=False)
print(df_2)