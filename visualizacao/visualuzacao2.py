#!/usr/bin/env python
# coding=utf8

import simplejson
import urllib

import math
import random

from turtle import *

def modTupByIndex(tup, index, ins):
    return tuple(tup[0:index]) + (ins,) + tuple(tup[index+1:])

#metodo/funcao pra segunda visualizacao
def valorTotalDaCesta(valoresNumaData):
    total = 0
    for x in range(0, qte):
        total += valoresNumaData[x]
    return total

def desenhaEPreencheQuadrado(tamanho):
    begin_fill()
    for x in range(0,4):
        left(90)
        forward(tamanho)
    end_fill()


def stringDoMes(numero): #nao sei fazer switch no python, cabo a luz e nao tem internet pra pesquisar
    if (numero == 1 ):
        return "Janeiro"
    if (numero == 2 ):
        return "Fevereiro"
    if (numero == 3 ):
        return "Marco"
    if (numero == 4 ):
        return "Abril"
    if (numero == 5 ):
        return "Maio"
    if (numero == 6 ):
        return "Junho"
    if (numero == 7 ):
        return "Julho"
    if (numero == 8 ):
        return "Agosto"
    if (numero == 9 ):
        return "Setembro"
    if (numero == 10 ):
        return "Outubro"
    if (numero == 11 ):
        return "Novembro"
    if (numero == 12 ):
        return "Dezembro"
    else:
        return "mes invalido"

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

corProduto = cores[ random.randrange(0, 6, 1) ]
corCesta = cores[ random.randrange(7, 13, 1)]


mesAno1 = (random.randrange(7, 13, 1), 1900 +random.randrange(  94, 101, 1) )
mesAno2 = (random.randrange(1, 13, 1), 1900 +random.randrange( 101, 108, 1) )
mesAno3 = (random.randrange(1, 10, 1), 1900 +random.randrange( 108, 114, 1) )

datasPesquisa = (mesAno1, mesAno2, mesAno3)


##para datas custom
#datasPesquisa = (( 7, 1994 ) ,  ( 7, 2004 ) , ( 7, 2014 ))


#configuragoes da tabela
alturaGrafico= 600       #valor da altura em pixels       #<-valor mutavel
comprimentoGrafico = 700 #valor do comprimento em pixels  #<-valor mutavel
qte = 13 #qte de itens na cesta
qteColunas = len(datasPesquisa)

fatorAmpliacao = 1.5

#configura e posicia a turtle original
screensize(1300,1000)
color('black')
pensize(1)
#ht()
showturtle()
st()
speed(0)
tracer(1, 1)
penup()
goto(0, 0)

#linha horizontal
tutsGraficoTempo = clone()
tutsGraficoTempo.penup()
tutsGraficoTempo.goto( -comprimentoGrafico/2 -100, -alturaGrafico/2)
tutsGraficoTempo.pendown()
tutsGraficoTempo.goto(comprimentoGrafico/2, -alturaGrafico/2)
tutsGraficoTempo.penup()
tutsGraficoTempo.goto(comprimentoGrafico/2, -alturaGrafico/2 - 20)
tutsGraficoTempo.write("Tempo" , move=False, align="right", font=('Arial', 14, 'normal'))
tutsGraficoTempo.goto(comprimentoGrafico/2, -alturaGrafico/2)

#linha vertical
left(90)
tutsGraficoValor = clone()
tutsGraficoValor.penup()
tutsGraficoValor.goto(-comprimentoGrafico/2, -alturaGrafico/2 -100)
tutsGraficoValor.pendown()
tutsGraficoValor.goto( -comprimentoGrafico/2 , alturaGrafico/2)
tutsGraficoValor.penup()
tutsGraficoValor.goto( -comprimentoGrafico/2 +80, alturaGrafico/2)
tutsGraficoValor.write("Valor da Cesta Basica (R$)" , move=False, align="right", font=('Arial', 14, 'normal'))
tutsGraficoValor.goto( -comprimentoGrafico/2 , alturaGrafico/2)


#escreve os valores a cada 50 reais pra termos nocao da proporcao
penup()
goto(-comprimentoGrafico/2, -alturaGrafico/2)

guiaReais = 0
while guiaReais*fatorAmpliacao < alturaGrafico:
    novaGuia = guiaReais * fatorAmpliacao
    penup()
    goto(-comprimentoGrafico/2 -10, -alturaGrafico/2 + novaGuia)
    write( guiaReais , move=False, align="right", font=('Arial', 14, 'normal'))
    pendown()
    goto(comprimentoGrafico/2, -alturaGrafico/2 + novaGuia)
    guiaReais += 50

produtosCesta = ("Açúcar", "Arroz", "Banana Prata", "Batata", "Café em Pó", "Carne Bovina", "Farinha de Trigo", "Feijão",   "Leite tipo B", "Manteiga", "Óleo de Soja", "Pão Francês", "Tomate de mesa")

#------------------------ corassaum dos dados de desenho ------------------------------#
#--------------------------------------------------------------------------------------#
#coisa com o BD aki e pega os valores no banco #
produtoX = random.randrange(0, 13, 1)
produtoXValores = ()
produtoXNome = produtosCesta[ produtoX ]

datas = ()
for x in range(0, qteColunas):
    url = ''
    
    if datasPesquisa[x][0] < 10:
        url = 'http://172.246.16.27/pi/sexta_basica.php?mes=' + '0'+ str(datasPesquisa[x][0]) + '&ano=' + str(datasPesquisa[x][1])
    else:
        url = 'http://172.246.16.27/pi/sexta_basica.php?mes=' +      str(datasPesquisa[x][0]) + '&ano=' + str(datasPesquisa[x][1])

    json = simplejson.load(urllib.urlopen(url))

    acucar   = json['Acucar']
    arroz    = json['Arroz']
    banana   = json['Banana_Prata']
    batata   = json['Batata']
    cafe     = json['Cafe']
    carne    = json['Carne']
    farinha  = json['Farinha_de_Trigo']
    feijao   = json['Feijao']
    leite    = json['leite']
    manteiga = json['Manteiga']
    oleo     = json['Oleo_de_Soja']
    pao      = json['Pao']
    tomate   = json['Tomate']
    
    cesta_basica = [acucar, arroz, banana, batata ,cafe, carne, farinha, feijao, leite,  manteiga, oleo, pao, tomate ]

    produtoXValores = produtoXValores + (cesta_basica[x]['valor'], )

    #conversao do json pra tuplas e encaixar no codigo
    dataValores = ()
    for x in range(0, qte):
        tuplaTemporaria = ( cesta_basica[x]['valor'], )
        dataValores = dataValores + tuplaTemporaria

    dataValores = (valorTotalDaCesta(dataValores) ,)

    #monstrinho pra percorrer e desenha o grafico
    datas = datas + dataValores
#--------------------------------------------------------------------------------------#

#prepara os valores para desenhar o grafico
penup()
goto( -comprimentoGrafico/2, -alturaGrafico/2)
larguraDoRetCesta = 75
larguraDoRetProduto = 75 #soh pro codigo ficar legivel
espaco = 50
coordX = -comprimentoGrafico/2 + espaco

alturaEscrita = -alturaGrafico/2 - 20
posEscrita = -comprimentoGrafico/2 + espaco + (larguraDoRetProduto + larguraDoRetCesta)/2

color("black")

for x in range(0, len(datasPesquisa)):
    penup()
    goto( coordX                     , -alturaGrafico/2)
    fillcolor( corProduto )
    begin_fill()
    #comeca a desenha o retangulo do preco da cesta
    pendown()
    goto( coordX                      , -alturaGrafico/2 + produtoXValores[x]*fatorAmpliacao)
    goto( coordX + larguraDoRetProduto, -alturaGrafico/2 + produtoXValores[x]*fatorAmpliacao)
    goto( coordX + larguraDoRetProduto, -alturaGrafico/2)
    goto( coordX                      , -alturaGrafico/2)
    end_fill()
    coordX += larguraDoRetProduto
    
    penup()
    goto( coordX                    , -alturaGrafico/2)
    fillcolor( corCesta )
    begin_fill()
    #comeca a desenha o retangulo do preco do produto
    pendown()
    goto( coordX                    , -alturaGrafico/2 + datas[x]*fatorAmpliacao)
    goto( coordX + larguraDoRetCesta, -alturaGrafico/2 + datas[x]*fatorAmpliacao)
    goto( coordX + larguraDoRetCesta, -alturaGrafico/2)
    goto( coordX                    , -alturaGrafico/2)
    end_fill()
    coordX += larguraDoRetCesta + espaco
    
    #escreve embaixo da tabela o nome das datas centralizado com as colunas
    penup()
    goto( posEscrita , alturaEscrita)
    texto = stringDoMes(datasPesquisa[x][0]) + " de " + str(datasPesquisa[x][1])
    write( texto , move=False, align="center", font=('Arial', 14, 'normal'))
    posEscrita += espaco + larguraDoRetProduto + larguraDoRetCesta


penup()
goto(-100, -alturaGrafico/2 - 50)
fillcolor(corProduto)
desenhaEPreencheQuadrado(50)
goto(-125, -alturaGrafico/2 - 120)
write( produtoXNome , move=False, align="center", font=('Arial', 14, 'normal'))

goto(100, -alturaGrafico/2 - 50)
fillcolor(corCesta)
desenhaEPreencheQuadrado(50)
goto(75, -alturaGrafico/2 - 120)
write( "Cesta" , move=False, align="center", font=('Arial', 14, 'normal'))


done()


