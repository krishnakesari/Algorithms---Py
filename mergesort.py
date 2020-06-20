
# Merge sort
## 1. Recursively sort the left half of the input array
## 2. Recursively sort the right half of the input array
## 3. merge two sorted sub arrays into one

def mergeSort(A): 
        #base case if the input array is one or zero just return. 
        if len(A) > 1: 
            # splitting input array 
            print('splitting ', A ) 
            mid = len(A)//2 
            left = A[:mid] 
            right = A[mid:] 
            #recursive calls to mergeSort for left and right sub arrays                 
            mergeSort(left) 
            mergeSort(right) 
            #initalizes pointers for left (i) right (j) and output array (k)  
    # 3 initalization operations 
            i = j = k = 0         
            #Traverse and merges the sorted arrays 
            while i <len(left) and j<len(right): 
    # if left < right comparison operation  
                if left[i] < right[j]: 
    # if left < right Assignment operation 
                    A[k]=left[i] 
                    i=i+1 
                else: 
    #if right <= left assignment 
                    A[k]= right[j] 
                    j=j+1 
                k=k+1 

            while i<len(left): 
    #Assignment operation 
                A[k]=left[i] 
                i=i+1 
                k=k+1 

            while j<len(right): 
    #Assignment operation 
                A[k]=right[j] 
                j=j+1 
                k=k+1 
        print('merging ', A) 
        return(A)   

mergeSort([356,97,846,215])

import matplotlib.pyplot as plt 
import math 

x=list(range(1,100)) 
l =[]; l2=[]; a = 1 
plt.plot(x , [y * y for y in x] ) 
plt.plot(x, [(7 *y )* math.log(y, 2) for y in x]) 
plt.show() 

plt.plot(x, [(6 *y )* math.log(y, 2) for y in x]) 