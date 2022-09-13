from typing import List

def insertionSort(arr) -> List[int]:
  for i in range(i,len(arr))
   temp = arr[i]
      j = i -1
    while j >=0 and temp < arr[j]
        arr[j+1] = arr[j]
           j = j - 1
        arr[j+1] = temp
        
# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
