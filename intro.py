def permute(text):
    returnList=[]
    if len(text) == 1:
        returnList.append(text)
    else:
        for pos in range(len(text)):
            permuteList=permute(text[0:pos] + text[pos + 1:len(text)])
            for item in permuteList:
                returnList.append(text[pos] + item)
    return returnList

def unitChar(text):
    for pos in range(len(text)):
        listaFinal.append(text[pos])
    return listaFinal

def pairChars(text):
    for pos in range(len(text)):
        for j in range(len(text)):
            if pos != j:
                newWord = text[pos] + text[j]
                listaFinal.append(newWord)
    return listaFinal

def montaListaFinal(text):
    lista = permute(text)
    for item in range(len(lista)):
        listaFinal.append(lista[item])
    return listaFinal

listaFinal=[]
text =input("Digite um conjunto de caracteres: ")

if len(text) == 1:
    print(permute(text))
elif len(text) == 2:
    unitChar(text)
    montaListaFinal(text)
    print(listaFinal)
else:
    unitChar(text)
    pairChars(text)
    montaListaFinal(text)
    print(listaFinal)
