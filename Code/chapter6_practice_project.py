# Table Printer

tableData = [["apples", "oranges", "cherries","banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["dogs", "cats", "moose","goose"]]

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