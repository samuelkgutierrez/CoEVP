import sys
import os
import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt

def genTimings(filePtr):
    scale = 0
    totalTime = 0.0
    retList = [[0, 0.0]]
    for line in filePtr:
        strArr = line.split()
        if strArr[0][0].isdigit():
            #This is a data line
            if len(strArr) == 5:
                #This is not the final line of a successful run
                index = int(strArr[0])
                if index == 0:
                    #This is a scale change line
                    index = int(strArr[2].replace(":",""))
                    totalTime = float(strArr[3])
                    retList.append([index, totalTime])
                else:
                    #This is a normal data line
                    index = int(strArr[2].replace(":",""))
                    totalTime += float(strArr[3])
                    retList.append([index, totalTime])
    retArr = np.array(retList)
    return retArr

def main():
    if len(sys.argv) != 2:
        print("Error: Pass in a directory")
        return
    inPath = sys.argv[1]
    resultList = []
    for root, dirs, files in os.walk(inPath):
        for fName in files:
            if fName.endswith('.timer'):
                fPath =  os.path.join(root, fName)
                inFile = open(fPath, 'r')
                fileArr = genTimings(inFile)
                inFile.close()
                if fileArr.shape[0] > 1:
                    resultList.append((fName, fileArr))
    #print resultList
    return

if __name__ == "__main__":
    main()
