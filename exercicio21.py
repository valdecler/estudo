
jantar = ['amanda','daniela','renata','maria']
print (jantar)

first_owned = jantar.pop()
print ( " \n\tBoa noite! voce nao pago a conta "  + first_owned.title () +  " se nao paga terei q expusa-la" )

jantar.append ('carla')
print (jantar)

first_owned = jantar.pop()
print ( " \n\tBoa noite! "  + first_owned.title () +  " gostaria de jantar conosco?" )

print ("\n\t" + first_owned.title () + " gostaria de convidar mais alguem para jantar")

jantar.append ('camila')
print (jantar)
print ('\n\tsim eu gostaria de chamar ' + first_owned.title () + 'para jantar conosco')



