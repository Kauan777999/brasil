#Cores no terminal
#Aula extra: Essa parte não é muito essencial nos programas!

#ANSI: Escape sequence = Sempre começa com '\' e depois vem código, sempre que quiser uma cor em python se começa: \033[m onde entre o '[' e o 'm' vai se botar o código da cor!
#Sendo em ordem style(estilo); text(Fonte do texto); Back(Cor de fundo) entre '['  e 'm'
#Style: 0, 1, 4_ , 7  text: 30(branco), 31(Vermelho), 32(Verde), 33(Amarelo), 34(Azul), 35(Roxo), 36(Azul água), 37(cinza)  back: 40(branco), 41(Vermelho), 42(verde), 43(amarelo), 44(Azul), 45(Roxo), 46(Azul água), 47(cinza)

#Teste

n = float(input('Você tirou quanto na prova?'))  #Código para o programa fazer uma pergunta
if n > 6:  #Condição se a nota for >6
    print('\033[1;32;40mParabéns você foi muito bem na prova, estou orgulhoso!\033[m')  #O programa responde dessa forma!
else: #Condição se a nota for <6 
    print('\033[1;31;40mVocê foi muito mal, estou decepcionado!\033[m') #O programa responde dessa forma!

#Basicamente fazer com que um programa fique colorido, é base de estética mas possivelmente isso não vai ser usado muito nos programas mais é bom ficar sabendo!