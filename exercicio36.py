 
 #Crie um script que tenha uma lista, faça 3 msgs, as 2 primeiras vão ter interação 
 #com a lista no loop for, a 2 msg , vai ter uma quebra de linha no 
 #final \n , a 3 msg  vai ser uma qualquer dentro do loop, vai acontecer uma desordem 
 #nas msgs, tente arrumar e explique, oque aconteceu.

namoradas = ['maria', 'raquel', 'janaina'] 
for namorada in namoradas: 
	print(namorada.title() + ", era uma otima namorada!") 
print("Mas eu gostava mais da, " + namorada.title() + ".\n")

print ('============================================')

# esse erro ocorre por que o python nao intedifica a ultima linha de codigo 
#como pertecente a linha de cima e consegue ler o codigo porem a resposta nao e a 
#desejada entao devemos anexar a ultima linha do codido dando indequisacao (espaco) assim o python 
#vai comcluir q a ultima linha tambem pertence ao codigo acima e assim secura o codigo 
#da forma q esperamos como no exemplo abaixo.

namoradas = ['maria', 'raquel', 'janaina'] 
for namorada in namoradas: 
 print(namorada.title() + ", era uma otima namorada!") 
 print("Mas eu gostava mais da, " + namorada.title() + ".\n")
