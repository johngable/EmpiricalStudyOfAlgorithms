import random
import os


#This function can be used with an input multiplier to create a file
#of randomly generated numbers from 10k-1million
def generateFileSmallUnsorted(multiplier):
    num = []
    for i in range(multiplier*10000):
        num.append(random.randint(0, 9999))
        i = i+1
    return num

#This function takes in an output path, a file name, and a list of randomly generated ints.
#It then writes each int from the random list to the output file/path.
def writeFile(path, file, randInt):
    f = open("/home/johngable/Desktop/AlgorithmsProject/"+path+"/"+file+".txt", 'w')
    for num in randInt:
        f.write(str(num)+"\n")

#This function takes a path and a multiplier and creates
#30 files in the given path of 10k-1million randomly generated ints.
#UNSORTED
def createThirtyFiles(path, multiplier):
    for i in range(30):
        writeFile(path, path+str(i), generateFileSmallUnsorted(multiplier))
        i = i+1

#This function also outputs 30 files to a given path but
#writes the randomly generated ints sorted.
def createThirtyFilesSorted(pathTo, pathFrom):
    i=0
    for filenames in os.listdir(pathFrom):
        print(i)
        lst = []
        with open (pathFrom+"/"+filenames, "r") as f:
            for line in f:
                #print(line)
                lst.append(int(line))
        writeFile(pathTo, pathTo+str(i), sorted(lst))
        i=i+1


#This function outputs 30 files to a given path but writes
#them in REVERSE sorted order.
def createThirtyFilesReverseSorted(pathTo, pathFrom):
    i=0
    for filenames in os.listdir(pathFrom):
        print(i)
        lst = []
        with open (pathFrom+"/"+filenames, "r") as f:
            for line in f:
                #print(line)
                lst.append(int(line))
        writeFile(pathTo, pathTo+str(i), sorted(lst, reverse = True))
        i=i+1


#The main calls the createThirtyFiles/Sorted/Reverse functions with an associated path
#and multipler. The multiplier tells the associated funcions to generate
#10k-1million random ints to output to a file.
def main():

    createThirtyFiles("SmallUnsorted", 1)
    createThirtyFiles("MediumUnsorted", 10)
    createThirtyFiles("LargeUnsorted", 100)


    createThirtyFilesSorted("/SmallSorted", "/home/johngable/Desktop/AlgorithmsProject/SmallUnsorted")
    createThirtyFilesSorted("/MediumSorted", "/home/johngable/Desktop/AlgorithmsProject/MediumUnsorted")
    createThirtyFilesSorted("/LargeSorted", "/home/johngable/Desktop/AlgorithmsProject/LargeUnsorted")

    createThirtyFilesReverseSorted("/SmallReverse", "/home/johngable/Desktop/AlgorithmsProject/SmallUnsorted")
    createThirtyFilesReverseSorted("/MediumReverse", "/home/johngable/Desktop/AlgorithmsProject/MediumUnsorted")
    createThirtyFilesReverseSorted("/LargeReverse", "/home/johngable/Desktop/AlgorithmsProject/LargeUnsorted")

main()
