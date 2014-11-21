#!/usr/bin/env python
# coding=utf8

#import psycopg2
import math

import random
from threading import Thread

import simplejson
import urllib

from turtle import *

def modTupByIndex(tup, index, ins):
    return tuple(tup[0:index]) + (ins,) + tuple(tup[index+1:])


#metodo/funcao pra segunda visualizacao
def valorTotalDaCesta(valoresNumaData):
#    qteNaCestaBasica = (3.0, 3.0, 7.5, 6.0, 1.2, 6.0, 1.5, 4.5, 7.5, 3.75, 1.2, 6.0, 9.0)
#    for x in range(0, qte):
#        valoresNumaData = modTupByIndex( valoresNumaData, x, valoresNumaData[x]*qteNaCestaBasica[x] )

    dataTotal = 0
    for x in range(0, qte):
        dataTotal += valoresNumaData[x]
    return dataTotal

def converteValoresDoBancoEmPixelsPraDesenhar (valoresNumaData): #nome auto-explicativo
#    qteNaCestaBasica = (3.0,  #kg
#                        3.0,  #kg
#                        7.5,  #duzia      (duzias(12) tabelado do banco mas precisa de 90 unidades pra cesta)
#                        6.0,  #kg
#                        1.2,  #500 gramas (500g tabelado do banco, mas precisa de 600g pra cesta)
#                        6.0,  #kg
#                        1.5,  #kg
#                        4.5,  #kg
#                        7.5,  #litro
#                        3.75, #200 gramas (200g tabelado do banco, mas precisa de 750g pra cesta)
#                 750.0/900.0, #750ml      (900ml tabelado do banco, mas precisa de 750ml pra cesta (sobra oleo))
#                        6.0,  #kg
#                        9.0)  #kg
#
#    for x in range(0, qte):
#        valoresNumaData = modTupByIndex( valoresNumaData, x, valoresNumaData[x]*qteNaCestaBasica[x] )

   #esta parte ja vem pronta do json direto no valoresNumaData
   

    #valor total da cesta para determinar a % de cada item
    dataTotal = 0
    for x in range(0, qte):
        dataTotal += valoresNumaData[x]


    # porcentagens dos precos de cada produto em uma data vindos do BD
    dataPorcentagens= (0,)
    for x in range(0, qte):
        tuplaTemporaria = (valoresNumaData[x]*100/dataTotal,)
        dataPorcentagens = dataPorcentagens+ tuplaTemporaria


    #porcentagens aditivas dos precos em cada lugar da tupla (tipo fibonacci sqn)
    #o primeiro valor precisa ser 0%
    #exemplo: (0%, 10%, 15%, 35%, 65%, 90%, 100%)
    porcents = 0
    for x in range(1, qte + 1):
        porcents += dataPorcentagens[x]
        dataPorcentagens = modTupByIndex(dataPorcentagens, x, porcents)


    #aki converte as %s em em valor de pixel para desenhar
    dataAlturas = (0,)
    for x in range(1, qte + 1):
        alturaTemp = ( (alturaTabela*dataPorcentagens[x])/100.0 , )
        dataAlturas = dataAlturas+ alturaTemp

    # dataAlturas eh o que precisamos agora para desenhar com a turtle
    return dataAlturas


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


#mesAno1 = (random.randrange(7, 13, 1), 1900 +random.randrange(  94, 101, 1) )
#mesAno2 = (random.randrange(1, 13, 1), 1900 +random.randrange( 101, 108, 1) )
#mesAno3 = (random.randrange(1, 10, 1), 1900 +random.randrange( 108, 114, 1) )
#
#datasPesquisa = (mesAno1, mesAno2, mesAno3)

#para datas custom
datasPesquisa = (( 7, 1994 ) ,  ( 7, 2004 ) , ( 7, 2014 ))


#configuragoes da tabela
alturaTabela = 700              #valor da altura em pixels               #<-valor mutavel
comprimentoTabela = 800         #valor do comprimento em pixels          #<-valor mutavel
qteColunas = len(datasPesquisa) # qte de colunas, ou datas para mostrar

divs = qteColunas - 1           # qte de "hastes" divisorias
space =  30                     # qte de pixels para transicao de nivel  #<-valor mutavel
cBase = (comprimentoTabela - (divs * space))/qteColunas  #comprimento da "base"

qte = 13 #qte de itens na cesta

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


for x in range(0, qte):
    alberto = clone()
    alberto.color( "white")
    alberto.fillcolor( cores[x] )
    turtles.append( alberto )



produtosCesta = ("Açúcar", "Arroz", "Banana Prata", "Café em Pó", "Carne Bovina", "Farinha de Trigo", "Feijão",   "Leite tipo B", "Manteiga", "Óleo de Soja", "Batata", "Pão Francês", "Tomatede mesa")

#prepara os valores para desenhar a tabela
#------------------------ corassaum dos dados de desenho ------------------------------#
#--------------------------------------------------------------------------------------#

#----------------------------------------------#
#coisa com o BD aki e pega os valores no banco #
mes = 7
ano = 1994

if mes < 10:
    url = 'http://172.246.16.27/pi/sexta_basica.php?mes=' + '0'+ str(mes) + '&ano=' + str(ano)
else:
    url = 'http://172.246.16.27/pi/sexta_basica.php?mes=' +      str(mes) + '&ano=' + str(ano)


json = simplejson.load(urllib.urlopen(url))

acucar = json['Acucar']
arroz = json['Arroz']
banana = json['Banana_Prata']
batata = json['Batata']
cafe = json['Cafe']
carne = json['Carne']
farinha = json['Farinha_de_Trigo']
feijao = json['Feijao']
leite = json['leite']
manteiga = json['Manteiga']
oleo =     json['Oleo_de_Soja']
pao = json['Pao']
tomate = json['Tomate']


cesta_basica = [acucar, arroz, banana, batata ,cafe, carne, farinha, feijao, leite,  manteiga, oleo, pao, tomate ]

#conversao do json pra tuplas e encaixar no codigo
julho94valores = ()
for x in range(0, qte):
    tuplaTemporaria = ( cesta_basica[x]['valor'], )
    julho94valores = julho94valores + tuplaTemporaria

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
#----------------------------------------------#

#valor de por "unidade" de cada item no banco, nas mesma ordem do produtosCesta
#julho94valores = (0.80, 0.67, 0.93, 0.69, 3.51, 2.86, 0.53, 1.12, 0.63, 1.08, 0.96, 1.20, 0.54)
julho04valores = (0.95, 2.01, 2.18, 1.44, 4.19, 6.97, 1.64, 2.43, 1.66, 2.80, 2.39, 4.00, 2.32)
julho14valores = (1.85, 2.48, 4.89, 2.99, 6.63,18.05, 2.80, 3.71, 2.85, 3.47, 4.75, 9.05, 4.24)

julho94alturas = converteValoresDoBancoEmPixelsPraDesenhar(julho94valores)
julho04alturas = converteValoresDoBancoEmPixelsPraDesenhar(julho04valores)
julho14alturas = converteValoresDoBancoEmPixelsPraDesenhar(julho14valores)


datas = (julho94alturas, julho04alturas, julho14alturas)
#--------------------------------------------------------------------------------------#


penup()
color("black")
alturaEscrita = alturaTabela/2 + 10
goto( -comprimentoTabela/4 , alturaEscrita)
write( "Julho de 1994", move=False, align="right", font=('Arial', 18, 'normal'))
goto( -comprimentoTabela/4 +(space +cBase), alturaEscrita)
write( "Julho de 2004", move=False, align="right", font=('Arial', 18, 'normal'))
goto( -comprimentoTabela/4 +2*(space +cBase), alturaEscrita )
write( "Julho de 2014", move=False, align="right", font=('Arial', 18, 'normal'))


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
    
    
    distAtual = cBase
    #valorDeTeste = -10
    for coluna in range(1, qteColunas):
        distAtual += space
        viera.goto( -comprimentoTabela/2 + distAtual, alturaTabela/2 -  datas[coluna][nivel] ) #valores n
        distAtual += cBase
        viera.goto( -comprimentoTabela/2 + distAtual, alturaTabela/2 -  datas[coluna][nivel] ) #valores n


    viera.goto(  -comprimentoTabela/2 + distAtual ,  alturaTabela/2 -  datas[coluna][nivel] )#borda direita
    viera.goto(  -comprimentoTabela/2 + distAtual , -alturaTabela/2 )                        #canto inferior direito
    viera.goto( -comprimentoTabela/2 , -alturaTabela/2 )                                     #canto inferior esquerdo
    viera.goto( -comprimentoTabela/2 ,  alturaTabela/2 -  datas[0][nivel] )                  #fecha o poligono para a turtle pintar

    viera.end_fill()

    #escreve o nome do produto
    penup()
    color( cores[nivel] )
    goto(-comprimentoTabela/2 -5, alturaTabela/2 -(datas[0][nivel]+ datas[0][nivel +1])/2 -18 )
    write( produtosCesta[nivel], move=False, align="right", font=('Arial', 18, 'normal'))
   #write("manoloooo", move=False, align="right", font=('Arial', 18, 'normal'))

    nivel += 1


done()





