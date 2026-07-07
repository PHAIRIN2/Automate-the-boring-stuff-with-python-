# Table Printer


tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def printTable(tableData):
    colWidths = [0] * len(tableData)
    for colIndex in range(len(tableData)):
        for rowIndex in range(len(tableData[colIndex])):
            if len(tableData[colIndex][rowIndex]) > colWidths[colIndex]:
                colWidths[colIndex] = len(tableData[colIndex][rowIndex])

    for rowIndex in range(len(tableData[0])):
        for colIndex in range(len(tableData)):
            print(tableData[colIndex][rowIndex].rjust(colWidths[colIndex]), end=" ")
        print()


tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def printTable(data):
    colWidths = [0] * len(data)
    for i in range(len(data)):
        for items in data[i]:
            if len(items) > colWidths[i]:
                colWidths[i] = len(items)

    for col in range(len(data[0])):
        for row in range(len(data)):
            print(data[row][col].rjust(colWidths[row]), end=" ")
        print()


printTable(tableData)
