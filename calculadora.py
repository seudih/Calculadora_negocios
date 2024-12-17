#Idenificação do usuario e saudação
nome = input ('Qual o seu nome?' )
print ('Olá,', nome, 'seja bem vindo a calculadora de negócios!')


#Solicitação de entrada de valores
print (nome, 'Para iniciar, informe o valor de custo do seu produto')
valorprod = input ('Digite o valor: ')
print (nome, 'Agora informe o calculo que deseja efetuar: Digite 1- soma de estoque, 2- divisão de custo, 3- margem de lucro ou 4- subtração de vendas: ')
calc = input ('Digite o calculo: ')
if calc == '1':
    print (nome, 'Agora informe a quantidade de estoque: ')
    valorest = input ('Digite o valor: ')
elif calc == '2':
    print (nome, 'Agora informe a quantidade de processos existentes no seu produto/serviço')
    valorcust = input ('Digite o valor: ')
elif calc == '3':
  print ('A margem de lucro é de' , int(valorprod) * int(30)/100)
elif calc == '4':
    print (nome, 'Agora informe a quantidade de vendas: ')
    valorvend = input ('Digite o valor: ')
else:
    print ('Operação incompativel')

#calculo das operações
if calc == '1':
  print ('O valor em estoque é de' , int(valorprod) * int(valorest))
elif calc == '2':
  print ('O valor do custo é de' , int(valorprod) / int(valorcust))
elif calc == '4':
  print ('A quantidade de vendas é de' , int(valorprod) * int(valorvend))
elif calc == '3':
  print ('Este lucro está baseado em uma taxa de 30%')
else:
  print ('Operação incompativel')
