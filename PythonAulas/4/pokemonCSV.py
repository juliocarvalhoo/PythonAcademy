filePath = "PythonAulas\\4\\pokemon.csv"

listColumn = []


openFile = open(filePath,"r")
listTransform = openFile.read().split("\n")
openFile.close()
for item in listTransform:
    listColumn.append(item.split(","))
    
print(listColumn[0])

listName = []
countPokemons = 0


for element in range(len(listColumn)-1):
    print(listColumn[element][1])
    


    
