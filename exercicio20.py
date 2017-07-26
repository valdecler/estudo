
# Crie um script com uma lista depois armazene um elemento da lista, em uma 
#variável ,remova o elemento da lista, com o método  .remove() faça a concatenação 
#usando o segundo valor da variável, com uma frase ‘string’  observe que o remove a
#penas elimina a primeira ocorrência explique pq isso acontece.

carro = ['monza','celta','palio','parati','vectra','corsa']
print (carro)

removido = 'parati'
carro.remove (removido)
print (carro)
first_owned = carro.pop(1)
print ("\nComprei uma " + first_owned.title () + " mas o carro e muito duro.")

# O remove () método exclui apenas a primeira ocorrência do valor especificado
