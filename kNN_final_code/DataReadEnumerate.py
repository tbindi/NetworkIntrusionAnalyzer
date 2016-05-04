import csv

def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def enumerateStringColumns(secondColumn, thirdColumn, fourthColumn, classColumn, trainData):
    enum1Count = 1.0
    enum2Count = 1.0
    enum3Count = 1.0
    enumClassCount = 1.0
    for train in trainData:
        # print "....."
        if train[1] not in secondColumn.keys():
            secondColumn[train[1]] = enum1Count
            enum1Count += 1
        if train[2] not in thirdColumn.keys():
            thirdColumn[train[2]] = enum2Count
            enum2Count += 1
        if train[3] not in fourthColumn.keys():
            fourthColumn[train[3]] = enum3Count
            enum3Count += 1
        if train[41] not in classColumn.keys():
            classColumn[train[41]] = enumClassCount
            enumClassCount += 1

    return secondColumn, thirdColumn, fourthColumn, classColumn

def replaceWithEnumeratedValues(column2, column3, column4, classColumn, trainData):
    for train in trainData:
        train[1] = column2[train[1]]
        train[2] = column3[train[2]]
        train[3] = column4[train[3]]
        #print "Class is",train[41]
        train[41] = classColumn[train[41]]
    return trainData


def open_file(data_set):

    secondColumn={}
    thirdColumn={}
    fourthColumn={}
    classColumn={}

    print("in Data Read Enumerate",len(data_set))

    for i in range(len(data_set)):
        for j in range(len(data_set[i])):
            if data_set[i][j].isdigit():
                data_set[i][j] = float(data_set[i][j])+1
            elif isFloat(data_set[i][j]):
                data_set[i][j] = float(data_set[i][j])+1
            else:
                data_set[i][j] = data_set[i][j]

    #done reading data call enumerate
    secondColumn,thirdColumn,fourthColumn,classColumn=enumerateStringColumns(secondColumn,thirdColumn,fourthColumn,classColumn,data_set)

    train_set = replaceWithEnumeratedValues(secondColumn, thirdColumn, fourthColumn,classColumn,data_set)

    return train_set


