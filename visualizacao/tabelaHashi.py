#!/usr/bin/env python
# coding=utf8

#import psycopg2
import math

from random import randint
from threading import Thread

from turtle import *

def modTupByIndex(tup, index, ins):
    return tuple(tup[0:index]) + (ins,) + tuple(tup[index+1:])


cor0  = (251/255.0,  16/255.0,  34/255.0)
cor1  = (252/255.0,  24/255.0, 128/255.0)
cor2  = (237/255.0,  40/255.0, 251/255.0)
cor3  = (108/255.0,  47/255.0,  15/255.0)
cor4  = (192/255.0, 113/255.0,  36/255.0)
cor5  = (253/255.0, 212/255.0,  48/255.0)
cor6  = (185/255.0, 160/255.0,  34/255.0)
cor7  = (174/255.0, 182/255.0,  37/255.0)
cor8  = ( 48/255.0, 190/255.0,  33/255.0)
cor9  = ( 30/255.0, 186/255.0, 185/255.0)
cor10 = ( 29/255.0, 173/255.0, 250/255.0)
cor11 = ( 14/255.0,  38/255.0, 251/255.0)
cor12 = ( 12/255.0,  91/255.0, 183/255.0)
cores = (cor0, cor1, cor2, cor3, cor4, cor5, cor6, cor7, cor8, cor9, cor10, cor11, cor12)

#produtosCesta = ("Carne", "Leite", "Feijão", "Arroz", "Farinha", "Batata", "Tomate", "Pão Francês", "Café em Pó", "Banana", "Açúcar", "Óleo", "Manteiga")
produtosCesta = ("Açúcar", "Arroz", "Banana Prata", "Café em Pó", "Carne Bovina", "Farinha de Trigo", "Feijão",   "Leite tipo B", "Manteiga", "Óleo de Soja", "Batata", "Pão Francês", "Tomatede mesa")

'''               julho/1994     julho/2004   julho/2014
"Açúcar"            0,80           0,95         1,85   kg
"Arroz"             0,67           2,01         2,48   duzia.
"Banana Prata"      0,93           2,18         4,89   kg
"Batata"            0,69           1,44         2,99   500g
"Café em Pó"        3,51           4,19         6,93   kg
"Carne Bovina"      2,86           6,97        18,05   kg
"Farinha de trigo"  0,53           1,64         2,80   kg
"Feijão"            1,12           2,43         3,71   litro
"Leite tipo B"      0,63           1,66         2,85   litro
"Manteiga"          1,08           2,80         3,47   200g
"Óleo de Soja"      0,96           2,39         4,75   900ml
"Pão Francês"       0,06           0,20         9,05  u.50g / kg
"Tomate de mesa"    0,54           2,32         4,24   kg
'''


#configuragoes da tabela
alturaTabela = 700      #valor da altura em pixels               #<-valor temporario
comprimentoTabela = 800 #valor do comprimento em pixels          #<-valor temporario
qteColunas = 3          # qte de colunas, ou datas para mostrar  #<-valor temporario

divs = qteColunas - 1   # qte de "hastes" divisorias
space =  30             # qte de pixels para transicao de nivel
cBase = (comprimentoTabela - (divs * space))/qteColunas  #comprimento da "base"


#configura e posicia a turtle original para ser copiada
color('black')
pensize(1)
#ht()
showturtle()
st()
speed(0)
tracer(1, 1)

penup()
goto(-comprimentoTabela/2, alturaTabela/2)
#left(90)
pendown()

# cria a copia das turtles que iram desenhar a tabela
turtles = [];
qte = 13

for x in range(0, qte):
    alberto = clone()
    alberto.color( "white")
    alberto.fillcolor( cores[x] )
    turtles.append( alberto )



''' valores do banco
                     julho/1994     julho/2004   julho/2014
    "Açúcar"            0,80           0,95         1,85   kg
    "Arroz"             0,67           2,01         2,48   kg
    "Banana Prata"      0,93           2,18         4,89   dz
    "Batata"            0,69           1,44         2,99   kg
    "Café em Pó"        3,51           4,19         6,93   500g
    "Carne Bovina"      2,86           6,97        18,05   kg
    "Farinha de trigo"  0,53           1,64         2,80   kg
    "Feijão"            1,12           2,43         3,71   litro
    "Leite tipo B"      0,63           1,66         2,85   litro
    "Manteiga"          1,08           2,80         3,47   200g
    "Óleo de Soja"      0,96           2,39         4,75   900ml
    "Pão Francês"       1,20           4,00         9,05   kg
    "Tomate de mesa"    0,54           2,32         4,24   kg
    '''

''' qte para cesta
    Açúcar       kg  3,0
    Arroz        kg  3,0
    Banana     unid. 90
    Batata       kg  6,0
    Café em Pó   kg  0,600
    Carne        kg  6,0
    Farinha      kg  1,5
    Feijão       kg  4,5
    Leite         l  7,5
    Manteiga    kg  0,750
    Óleo         ml  750
    Pão Francês   kg 6,0
    Tomate        kg 9,0
    '''



#prepara os valores para desenhar a tabela
alturaItensRegular = alturaTabela/qte

#---- corassaum dos dados de desenho ----#
#----------------------------------------#
julho94valores = (0.80*3.0,
                0.67*3.0,
                0.93*7.5,
                0.69*6.0,
                3.51*1.2,
                2.86*6.0,
                0.53*1.5,
                1.12*4.5,
                0.63*7.5,
                1.08*3.75,
                0.96*1.2,
                1.20*6.0,
                0.54*9.0)

julho94total = 0
for x in range(0, qte):
    julho94total += julho94valores[x]

julho94porcentagestemp = (0,)
for x in range(0, qte):
    tuplaTemporaria = (julho94valores[x]*100/julho94total,)
    julho94porcentagestemp = julho94porcentagestemp + tuplaTemporaria

julho94porcentages = (0, )
#for i in range(0, qte):

# continua aki---
print modTupByIndex((1,2,3),2,"a")



tuplaitens = (0,1,2,3,4,5,6,7,8,9,10,12,13) # porcentage dos precos de cada produto em uma data vindos do BD

#itens1
#itens2
#itens3
itens = ()#porcentagens aditivas dos precos em cada lugar da tupla (tipo fibonacci sqn)
          #o primeiro valor precisa ser 0%
          #exemplo: (0%, 10%, 15%, 35%, 65%, 90%, 100%)

#aki converte as %s em em valor de pixel para desenhar
alturas = 0
for x in range(0, qte + 1):
    tuplaAlturas = (alturas,)
    itens = itens + tuplaAlturas  #<-valor temporario
    alturas = alturas + alturaItensRegular


#datas = (itens1, itens2, itens3)
datas = ()
for x in range(0, qteColunas):
    tupladatas = (itens,)
    datas = datas + tupladatas
#----------------------------------------#


#comeca a desenhar e pintar a tabela em cascata
# ate este commit nao há mais bugs aki

nivel = 0
for viera in turtles:
    viera.begin_fill()

    #o primeiro valor de itens no vetor para a tabela precisa ser 0, pra fazer a borda superior bunitinho
    penup()
    viera.goto(-comprimentoTabela/2        , alturaTabela/2 -  datas[0][nivel] ) #valores 1
    pendown()
    viera.goto(-comprimentoTabela/2 + cBase, alturaTabela/2 -  datas[0][nivel] ) #valores 1
    #o espaco entre esses 2 pontos forma o retangulozinho
    
    #print -comprimentoTabela/2
    
    # a primeira coluna(data) precisa ser feita assim, porem se as %'s nos itens vierem
    # numa tupla de tuplas(ideia de matriz, nao confundir com array de arrays de python)
    # da pra melhorar isso 'for' assim se nao tem que fazer na mao todas as 'iteracoes'
    # desse 'for' na mao, atraves das colunas relevantes
    
    distAtual = cBase
    #valorDeTeste = -10
    for coluna in range(1, qteColunas):
        distAtual += space
        viera.goto( -comprimentoTabela/2 + distAtual, alturaTabela/2 -  datas[coluna][nivel] ) #valores n
        distAtual += cBase
        viera.goto( -comprimentoTabela/2 + distAtual, alturaTabela/2 -  datas[coluna][nivel] ) #valores n
    
#        valorDeTeste = valorDeTeste*-1
#        distAtual += space
#        viera.goto( -comprimentoTabela/2 + distAtual, alturaTabela/2 -  datas[coluna][nivel] +valorDeTeste) #valores n
#        print -comprimentoTabela/2 + distAtual
#        distAtual += cBase
#        viera.goto( -comprimentoTabela/2 + distAtual, alturaTabela/2 -  datas[coluna][nivel] +valorDeTeste) #valores n
#        print -comprimentoTabela/2 + distAtual


    viera.goto(  -comprimentoTabela/2 + distAtual ,  alturaTabela/2 -  datas[coluna][nivel] )#borda direita
    viera.goto(  -comprimentoTabela/2 + distAtual , -alturaTabela/2 )                        #canto inferior direito
    viera.goto( -comprimentoTabela/2 , -alturaTabela/2 )                                     #canto inferior esquerdo
    viera.goto( -comprimentoTabela/2 ,  alturaTabela/2 -  datas[0][nivel] )                  #fecha o poligono para a turtle pintar

    viera.end_fill()

    #escreve o nome do produto
    penup()
    goto(-comprimentoTabela/2 -5, alturaTabela/2 -(datas[0][nivel]+ datas[0][nivel +1])/2 -18 )
    write( produtosCesta[nivel], move=False, align="right", font=('Arial', 18, 'normal'))
   #write("manoloooo", move=False, align="right", font=('Arial', 18, 'normal'))

    nivel += 1

done()


