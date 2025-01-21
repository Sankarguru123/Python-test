
#frequencycount
data = "hello"
value_data = {i:data.count(i) for i in  data }
print(value_data)
b = ''.join(f"{key}{value}" for key,value in value_data.items())
print(b)


arr = [1, 2, 0, 4, 3, 0, 5, 0]
da = []

for item in arr:
    if item !=0:
        da.append(item)


zero = arr.count(0)
print(zero)
da.extend([0] * zero)
arr =da
print(da)
print(arr)