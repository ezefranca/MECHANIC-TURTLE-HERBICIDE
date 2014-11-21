import simplejson
import urllib

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

for x in range(0, 12):
    print cesta_basica[x]['valor']