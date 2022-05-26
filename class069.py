# O custo total de um produto é a soma dos Valor do Produto e de seu Imposto  de Importação
# Os valores de imposto de importação para os estados de MG, SP, TO, GO e RJ: 
# 5%, 7%, 6%, 10% e 1%, respectivamente.

listaEstados = ["MG", "SP", "TO", "GO", "RJ"]
listaImpostos = [0.05, 0.07, 0.03, 0.10, 0.01]

valProd = float(input("Entre com o valor: "))
estado = input("Entre com o estado: ")

contador = 0
while(contador < 5):
    if(estado == listaEstados[contador]):
        imposto = listaImpostos[contador]
    
    contador += 1

custoTotal = valProd + valProd*imposto
print(custoTotal)