import os

def sortImages(imagesFolderPath):
    imagesArray = []
    files = os.listdir(imagesFolderPath)

    for file in files:
        imagesArray.append(file)

    imagesArray = sorted(imagesArray, key=lambda x: x[0])
    column = []
    imagesSort = []
    print(imagesArray)
    for i in range(len(imagesArray)-1):
        if imagesArray[i+1][0] == imagesArray[i][0]:
            if i == len(imagesArray) - 2:
                column += [imagesArray[i+1]]
                column += [imagesArray[i]]
                imagesSort += sortCols(column)
            else:
                column += [imagesArray[i]]
        else:
            column += [imagesArray[i]]
            imagesSort += sortCols(column)
            column = []
            
    if imagesArray[i+1][0] != imagesArray[i][0]:
        column += [imagesArray[i+1]]
        imagesSort += sortCols(column)

    return (imagesSort, len(column))


def sortCols(column):
    column = sorted(column, key=lambda x: int(x[1]))
    
    return column
    
    
# path = "/Users/vladprotsenko/Documents/POC/Drone/photos"
# print(sortImages(path))