#Aprendendo a lidar com arquivos
#PYPI

caminhoTeste ="PythonAulas\\4\\Teste.txt"


def Leitura(path):
    PathTeste = open(path,"r")
    leituraTeste = PathTeste.readlines()
    print(leituraTeste)
    PathTeste.close()

def Gravacao(path,texto):
    PathTeste = open(path,"a")
    PathTeste.write(texto)
    PathTeste.close()
    
def CriarArquivos(FileName):
    FileName = FileName + ".txt"
    createFile = open("PythonAulas\\4\\" + FileName,"w")
    createFile.write("O Brasil Nao e HEXAAAAAAAA")
    createFile.close()

    

#openai pesquisar
Gravacao(caminhoTeste,"\nO bagulho e louco")
Leitura(caminhoTeste)
CriarArquivos("XandaoFile")
Leitura("PythonAulas\\4\\XandaoFile.txt")

# PathTeste = open("PythonAulas\4\Teste.txt","a") 
# textoAleatorio = "Aqui está um texto aleatório"
# PathTeste.close()
