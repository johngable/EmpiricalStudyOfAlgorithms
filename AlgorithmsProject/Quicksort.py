import os, time

#This is the main recursive runner function for quicksort. 
def quicksort(A, l, r):
	if l<r:
		pIndex = threeWayPartition(A, l, r)
		quicksort(A, l, pIndex)
		quicksort(A, pIndex+1, r)
	
	
#This method takes in a list, left bounds, and right bounds. 
#It then calculates the middle of the list (b/w the left and right bounds),
#and finds the correct "middle value" of the three numbers. The middle value and
#its index are returned then. 
def medianOfThree(A, l, r):
	tempR = r-1
	left = A[l]
	right = A[tempR]
	middleIndex = l+(r-l)//2-1
	middle = A[middleIndex]
	
	#Find the largest of the three values
	largest = max(left, middle, right)

	#Once the largest is found, find the "middle"
	#and return that value+index as the pivot
	if largest == left:
		if right > middle:
			return right, tempR
		else:
			return middle, middleIndex
	elif largest == middle:
		if left > right:
			return left, l
		else:
			return right, tempR
	else:
		return middle, middleIndex
			

#This method will take in a list, left bound and right bound.
#It will then find a pivot value and continue to move values from the left and right bounds 
#around the pivot value, which will then be incremented for each value moved
def threeWayPartition(A, l, r):
	pivot, pIndex = medianOfThree(A, l, r)

	A[pIndex] = A[l]
	A[l]=pivot

	#Keep a temporary pivot index value that 
	#is incremented as numbers are swapped
	tempPivotIndex = l+1

	#Run through the array from bound-bound
	#and swap items with the tempPivot as needed
	for i in range(l+1, r):
		if A[i]<pivot:
			temp = A[i]
			A[i] = A[tempPivotIndex]
			A[tempPivotIndex] = temp
			tempPivotIndex+=1

	#Handle the remaining unswapped element
	temp = A[l]
	A[l] = A[tempPivotIndex-1]
	A[tempPivotIndex-1] = temp
	
	return tempPivotIndex-1



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
		quicksort(A, 0, len(A))
		end = time.time()
		i+=1
		print(i)
		execTime.append(round((end-start)*1000, 4))
		A.clear()
		
	results = open("/home/johngable/Desktop/AlgorithmsProject/QuickResults/QuickResults"+path+".txt", "w")
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






														
