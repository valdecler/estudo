
 #Crie um script com uma lista , exiba 2 msgs na tela, ambas vão ter interação 
 #com o loop for,  a segunda msg  estará fora do bloco, e so vai ser executada 
 #ao final do loop, apenas o ultimo elemento da lista aparecerá na 2msg, 
 #explique por que isso acontece.

nomes = [ 'rafael', 'danela', 'Carolina'] 

for nome in nomes: 
	
 print (nome.title () + "vamos comer uma pizza!")
	
	
print ( "eu mal posso esperar para comer a proxima fatia, " + nome.title () +  "\n")

#Este é um erro lógico . A sintaxe é código Python válida o codigo, mas
#faz não produzir o resultado desejado porque ocorre um problema na sua lógica
