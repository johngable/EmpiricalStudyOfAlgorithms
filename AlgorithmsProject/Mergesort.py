import time
import os

#This method will sort the three sub-arrays/list
#that are given via input parameters, and then merge 
#back into list A. 
def merge(B, C, A):
    i = 0
    j = 0
    k = 0

    p = len(B)
    q = len(C)

    while i<p and j<q: 
        if B[i] <= C[j]:
            A[k] = B[i]
            i+=1
        else:
            A[k] = C[j]
            j+=1
        
        k+=1
    if i==p:
        A[k:p+q] = C[j:q]
    else: 
        A[k:p+q] = B[i:p]


#This method is the main runner for my algorithm. 
#It will take in a list A, and diverge it into two list
#B, C. The three list are then passed into merge where they are
#sorted and then they also recursively mergesort themselves individually.
def mergeSort(A):
    A = A
    B = []
    C = []
    n = len(A)

    j= n/2
    

    if n>1: 
        B = A[:int(j)]
        C = A[int(j):int(n)]
    
        mergeSort(B)
        mergeSort(C)
        merge(B, C, A)
    

def sortFolder(path):
    execTime = []
    A = []

    for filenames in os.listdir("/home/johngable/Desktop/AlgorithmsProject/"+path):
        with open ("/home/johngable/Desktop/AlgorithmsProject/"+path+"/"+filenames, "r") as f:
            for line in f:
                A.append(int(line))
        
        
        
        start = time.time()
        mergeSort(A)
        end = time.time()
        execTime.append(round((end-start)*1000, 4))
        A.clear()
        
    results = open("/home/johngable/Desktop/AlgorithmsProject/MergeResults/MergeResults"+path+".txt", "w")
    for num in execTime:
        results.write(str(num)+"\n")


def main():
    sortFolder("SmallUnsorted")
    sortFolder("MediumUnsorted")
    sortFolder("LargeUnsorted")

    print("33%")

    sortFolder("SmallSorted")
    sortFolder("MediumSorted")
    sortFolder("LargeSorted")

    print("66%")

    sortFolder("SmallReverse")
    sortFolder("MediumReverse")
    sortFolder("LargeReverse")

    print("Done")


    

main()