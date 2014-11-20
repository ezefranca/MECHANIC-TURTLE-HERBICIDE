#!/usr/bin/env python
# coding=utf8

#import psycopg2
import math

from random import randint
from threading import Thread

from turtle import *

def modTupByIndex(tup, index, ins):
    return tuple(tup[0:index]) + (ins,) + tuple(tup[index+1:])


#metodo/funcao pra segunda visualizacao
def valorTotalDaCesta(valoresNumaData):
    qteNaCestaBasica = (3.0, 3.0, 7.5, 6.0, 1.2, 6.0, 1.5, 4.5, 7.5, 3.75, 1.2, 6.0, 9.0)
    for x in range(0, qte):
        valoresNumaData = modTupByIndex( valoresNumaData, x, valoresNumaData[x]*qteNaCestaBasica[x] )

    dataTotal = 0
    for x in range(0, qte):
        dataTotal += valoresNumaData[x]
    return dataTotal


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


produtosCesta = ("Açúcar", "Arroz", "Banana Prata", "Café em Pó", "Carne Bovina", "Farinha de Trigo", "Feijão",   "Leite tipo B", "Manteiga", "Óleo de Soja", "Batata", "Pão Francês", "Tomatede mesa")

#configuragoes da tabela
alturaGrafico= 600      #valor da altura em pixels               #<-valor temporario
comprimentoGrafico = 700 #valor do comprimento em pixels          #<-valor temporario
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
goto(0, 0)
#left(90)
pendown()

tutsGraficoTempo = clone()

tutsGraficoTempo.penup()
tutsGraficoTempo.goto(-100, 0)
tutsGraficoTempo.pendown()
tutsGraficoTempo.goto(comprimentoGrafico, 0)

left(90)
tutsGraficoValor = clone()
tutsGraficoValor.penup()
tutsGraficoValor.goto(0, -100)
tutsGraficoValor.pendown()
tutsGraficoValor.goto(0, alturaGrafico)

#valor de por "unidade" de cada item no banco, nas mesma ordem do produtosCesta
julho94valores = (0.80, 0.67, 0.93, 0.69, 3.51, 2.86, 0.53, 1.12, 0.63, 1.08, 0.96, 1.20, 0.54)
julho04valores = (0.95, 2.01, 2.18, 1.44, 4.19, 6.97, 1.64, 2.43, 1.66, 2.80, 2.39, 4.00, 2.32)
julho14valores = (1.85, 2.48, 4.89, 2.99, 6.63,18.05, 2.80, 3.71, 2.85, 3.47, 4.75, 9.05, 4.24)

julho94PrecoFinal = valorTotalDaCesta(julho94valores)
julho04PrecoFinal = valorTotalDaCesta(julho04valores)
julho14PrecoFinal = valorTotalDaCesta(julho14valores)


#for viera in turtles:
#    viera.begin_fill()
#
#
#    viera.end_fill()
#
#    #escreve o nome do produto
#    penup()
#    color( cores[nivel] )
#    write( produtosCesta[nivel], move=False, align="right", font=('Arial', 18, 'normal'))
#
#    nivel += 1

done()


