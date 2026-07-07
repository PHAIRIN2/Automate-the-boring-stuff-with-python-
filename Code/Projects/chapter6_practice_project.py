


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
            print(tableData[colIndex][rowIndex].rjust(colWidths[colIndex]), end= " ")
        print()


printTable(tableData)
