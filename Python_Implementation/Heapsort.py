import os
import time
import sys

#This code is meant to replicate the functionality of the
#books version of heapBottomUp. I had to make slight changes
#because of optimizations.
def heapBottomUp(H):
    n=len(H)
    i=n/2

    while i>=1:
        k=int(i)
        v=H[int(k)-1]
        heap = False

        while( not heap and (2*k)<=n):
            j=2*k
            if j<n:
                if H[int(j-1)] < H[int(j)]: j=j+1
            if v>=H[int(j-1)]:
                heap = True
            else:
                H[int(k-1)] = H[int(j-1)]
                k=j
            
        H[k-1]=v
        i-=1
       
    
    return(H)
    

#This function is used specifically for the heap deletion.
#It will recurse with a current array and root until the root
#meets the parental conditions described in the textbook.
#H -> Current list, n -> size so heap until, root -> current parent node we are verifying
def heapify(H, n, root):
    #assume the largest is currently the root
    largest = root

    #Due to array implementations of heaps, 
    #the left and right nodes are located 2* the parent nodes
    #location and then +1,+2
    left = 2*largest+1
    right = 2*largest+2

    #Checks to ensure we are within bounds
    if(left and right <n):
        #Finds the larger of the children and swaps with root if 
        #they are larger than the root. 
        if H[left] > H[right]:
            if H[largest]<H[left]:
                largest=left
        if H[left] < H[right]:
            if H[largest]<H[right]:
                largest=right

        #If a swap was made, continue to heapify until we are heaped again
        if largest != root:
            temp = H[root]
            H[root] = H[largest]
            H[largest] = temp
            heapify(H, n, largest)
    
    

#The main heapsort runner.
#Takes in an unsorted/unheaped list, will then
#heap the list using bottomUp implementation
#and then runs n-1 times sorting and heapifying the list
def heapSort(H):
    H = heapBottomUp(H)

    n=len(H)
    for i in range(n-1, 0, -1):
        H[0], H[i] = H[i], H[0]
        heapify(H, i, 0)
        
    
#Runs through a given directory folder and then pulls the data from 
#each .txt file and heapsorts the list.
def sortFolder(path):
    execTime = []
    A = []
    i=0
    for filenames in os.listdir("/home/johngable/Desktop/AlgorithmsProject/"+path):
        with open ("/home/johngable/Desktop/AlgorithmsProject/"+path+"/"+filenames, "r") as f:
            for line in f:
                A.append(int(line))
        
        
        
        start = time.time()
        heapSort(A)
        end = time.time()
        i+=1
        print(i)
        execTime.append(round((end-start)*1000, 4))
        A.clear()
        
    results = open("/home/johngable/Desktop/AlgorithmsProject/HeapResults/HeapResults"+path+".txt", "w")
    for num in execTime:
        results.write(str(num)+"\n")


def main():
    sortFolder("SmallUnsorted")
    print("11%")
    sortFolder("MediumUnsorted")
    print("22%")
    sortFolder("LargeUnsorted")
    print("33%")

    sortFolder("SmallSorted")
    print("44%")
    sortFolder("MediumSorted")
    print("55%")
    sortFolder("LargeSorted")
    print("66%")

    sortFolder("SmallReverse")
    print("77%")
    sortFolder("MediumReverse")
    print("88%")
    sortFolder("LargeReverse")
    print("Done")


main()