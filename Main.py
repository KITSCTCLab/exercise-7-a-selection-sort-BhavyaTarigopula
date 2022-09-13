from typing import List

def selectionSort(array, size) -> List[int]:
  for i in range (len(arr)):
    arr = i
    for j in range (i+1,len(arr)):
      if arr[min] > arr[j]:
        min = j
  arr[i],arr[min] = arr[min],arr[i]   

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
