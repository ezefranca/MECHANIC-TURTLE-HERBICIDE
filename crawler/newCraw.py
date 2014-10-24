#!/usr/bin/env python
import psycopg2
from contextlib import closing
from selenium.webdriver import Firefox # pip install selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#EXEMPLO MANEIRO DE FUNCAO
def crawlar(browser , numPagina):
	return
#INICIAR A CONECCAO COM O BANCO
conn = psycopg2.connect("host=23.89.198.31 dbname=magikarp user=gabriel password=8963")
cur = conn.cursor()

#INICIAR
browser = webdriver.Firefox()
browser.get('http://ciagri.iea.sp.gov.br/nia1/precos_medios.aspx?cod_sis=4')

#CHECAR TODOS OS PRODITOS
element = browser.find_element_by_id('chkTodos')
element.click()


#SETAR DATAS
browser.find_element_by_xpath("//select[@id='cmbPeriodo_Inicial']/option[@value='1970/MAI']").click()
browser.find_element_by_xpath("//select[@id='cmbPeriodo_Final']/option[@value='2014/SET']").click()

#CLICAR NO BOTAO DE PESQUISAR
element = browser.find_element_by_id('imgPesquisar')
element.click()

#ESPERAR CARREGAR
browser.implicitly_wait(10) 

#CONTAR AS PEGINAS GERADAS
count = 0

#PROCURA NA TABELA A ULTIMA LINHA QUE CONTEM A QUANTIDADE DE PAGINAS
"""
linhas = browser.find_element_by_id('Grid').find_elements_by_tag_name('tr')

for linha in linhas:
	ultimo = linha;

#CONTA QUANTAS PAGINAS FORAM GERADAS
paginas = ultimo.find_element_by_tag_name('td').find_elements_by_tag_name('a')

for pagina in paginas:
	if count == 0:
		count = int(pagina.text)
	else:
		if count < int(pagina.text):
			count = int(pagina.text)
			
"""
#PARA A QUANTIDADE DE PAGINAS QUE FORAM GERADAS

#MARCAR O NUMERO DA PAGINA
numPagina = 1
first = 1
focaGay = 20
#PARA CADA GRUPO DE PAGINAS
for x in xrange(1,30):
	#PARA CADA PAGINA
	for x in range(1, 21):
		#PEGA AS INFORMACOES DAS LINHAS
		linhas = browser.find_element_by_id('Grid').find_elements_by_tag_name('tr')
		#PARA CADA LINHA
		for linha in linhas:
			#NAO PEGAR A PRIMEIRA LINHA PQ E A DESCRICAO DAS PARADAS
			if not (first):
				ultimo = linha;
				#CRIAR O OBEJTO MANEIRO DA COLUNA
				coluna = linha.find_elements_by_tag_name('td')
				#VER SE E UMA COLUNA VALIDA
				if (len(coluna) == 6):
					num = coluna[4].text
					num = num.replace("." , "")
					num = num.replace("," , ".")
					#GERAR A QUERY PARA INSERIR
					query = "INSERT INTO preco_mensal_varejo( produto, mes, ano, moeda, preco, unidade) \
					VALUES ( '%s', '%s', '%s', '%s' ,  '%f' , '%s')" % (coluna[0].text , coluna[1].text , coluna[2].text , coluna[3].text ,float(num) , coluna[5].text)
					#INSERIR
					#cur.execute(query)
					#conn.commit()
					print(query)
			else:
				first = 0	

		#IR PARA A PROXIMA PAGINA
		paginas = ultimo.find_element_by_tag_name('td').find_elements_by_tag_name('a')
		for pagina in paginas:
			if pagina.text != "...":
				if int(pagina.text) == numPagina+1:
					numPagina = numPagina + 1
					pagina.click()
					first = 1
					browser.implicitly_wait(10)
					break 
		print(numPagina)

	#PROCURAR OS PONTINHOS
	linhas = browser.find_element_by_id('Grid').find_elements_by_tag_name('tr')

	for linha in linhas:
		ultimo = linha;
	#PASSAR PARA O PROXIMO GRUPO DE PAGINAS GG
	paginas = ultimo.find_element_by_tag_name('td').find_elements_by_tag_name('a')

	buceta = 0
	for pagina in paginas:
		buceta = buceta + 1
		if (pagina.text == "...") & (buceta > 4):
			numPagina = numPagina + 1
			pagina.click()
			first = 1
			focaGay = 22



cur.close()
conn.close()
browser.close()