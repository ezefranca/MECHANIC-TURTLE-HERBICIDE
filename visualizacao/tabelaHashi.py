#!/usr/bin/env python
# coding=utf8

#import psycopg2
import math

from random import randint
from threading import Thread

from turtle import *

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

produtosCesta = ("Carne", "Leite", "Feijão", "Arroz", "Farinha", "Batata", "Tomate", "Pão Francês", "Café em Pó", "Banana", "Açúcar", "Óleo", "Manteiga")

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


#prepara os valores para desenhar a tabela
alturaItensRegular = alturaTabela/qte

#---- corassaum dos dados de desenho ----#
#----------------------------------------#
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


