import math

#implementation of main function

def mainFunction(A,B):
    C = []
    quickSort(B,0,len(B)-1)
    for x in A:
        a = count(B, x, len(B))
        if isPrimeNumber(a) == False: 
            C.append(x)
    return C   


#This function checks if number is a prime number
#Time complexity: O(sqrt(n))

def isPrimeNumber(n):
  if n == 1:
      return False
  if n == 0:
      return False
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

#This function implements QuickSort algorithm
#Time complexity: O(n log n)
 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

#This function counts occurances of number in a sorted array
#Tt uses Improved Binary Search
#Time complexity: O(log n) 
         
def count(arr, x, n):
    i = first(arr, 0, n-1, x, n)
    if i == -1:
        return 0
    j = last(arr, i, n-1, x, n);    
    return j-i+1;
 
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def first(arr, low, high, x, n):
    if high >= low:
        mid = (low + high)//2     
         
        if (mid == 0 or x > arr[mid-1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return first(arr, (mid + 1), high, x, n)
        else:
            return first(arr, low, (mid -1), x, n)
    return -1;
  
def last(arr, low, high, x, n):
    if high >= low:
        mid = (low + high)//2;
  
        if(mid == n-1 or x < arr[mid+1]) and arr[mid] == x :
            return mid
        elif x < arr[mid]:
            return last(arr, low, (mid -1), x, n)
        else:
            return last(arr, (mid + 1), high, x, n)    
    return 0       

#testing 
A = [2,3,9,2,5,1,3,7,10]
B = [2,1,3,4,3,10,6,6,1,7,10,10,10]

C = mainFunction(A,B)

if C == [2,9,2,5,7,10]:
    print('success')
