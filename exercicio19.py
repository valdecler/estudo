
# Explique Quando usar o del  e quando usar o pop() ?

carro = [ ' monza ' , ' celta ' , ' palio ' , ' parati ' , ' vectra ' , ' corsa ' ]

del carro [2]
print (carro)
 # no exemplo acima ao usar a opcao (del[]) eu estou removendo de forma permanente 
 # o item da lista sera usado quado eu nao quiser mais usar este item
 
carro = [ ' monza ' , ' celta ' , ' palio ' , ' parati ' , ' vectra ' , ' corsa ' ]
first_owned = carro.pop(4)
print ( " Eu tenho um "  + first_owned.title () +  " mas bati ele no poste kkk " )
 # ja a opcao pop() eu vou usar sempre que quiser excluir um item mas que
 #futuramente eu venha a usa novamente 
