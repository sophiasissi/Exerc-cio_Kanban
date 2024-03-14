from os import truncate
def soma (a,b):
  s = a + b
  return s

def subtracao (a,b):
  sub = a - b
  return sub

def  multiplica (a,b):
  multi = a*b
  return multi

def divisao (a,b):
  div = a/b
  return div


x = False
while not x:
  decisao = int(input('''Vamos calcular. Qual operação vc deseja fazer?
  1 - Adição
  2 - Subtração
  3 - Multiplicação
  4 - Divisão\n'''))
  if decisao >4 or decisao < 1:
    x=False
  else:
    valor1 = int(input('quais valores você deseja calcular? '))
    valor2 = int(input())


    if decisao == 1:
      print(f'A soma de {valor1} por {valor2} é:', soma(valor1, valor2))
      x=True

    if decisao == 2:
      print(f'A subtração de {valor1} por {valor2} é:', subtracao(valor1, valor2))
      x=True
    if decisao == 3:
      print(f'A multiplicação de {valor1} por {valor2} é:', multiplica(valor1, valor2))
      x=True
    if decisao == 4:
      print(f'A divisão de {valor1} por {valor2} é:', divisao(valor1, valor2))
      x=True
