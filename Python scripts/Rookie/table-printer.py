tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    
    #store maximum width of each column in new list
    colWidths=[0]*len(table)

    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(table[i][j])>colWidths[i]:
                colWidths[i]=len(table[i][j])

    #Justify to right 
    for k in range(len(table)):
        for v in range(len(table[k])):
            table[k][v]=table[k][v].rjust(colWidths[k])
    
    #Print the list
    for i in range(len(table[-1])):
        for j in range(len(table)):
            if j< len(table)-1:
                print(table[j][i],end=' ')
            else:
                print(table[j][i])

    
    
printTable(tableData)
