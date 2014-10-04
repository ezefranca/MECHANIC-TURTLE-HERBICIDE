#!/usr/bin/env python
from contextlib import closing
from selenium.webdriver import Firefox # pip install selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def crawlar(browser , numPagina):
	return

# use firefox to get page with javascript generated content

#INICIAR
browser = webdriver.Firefox()
browser.get('http://ciagri.iea.sp.gov.br/nia1/precos_medios.aspx?cod_sis=4')

#CHECAR TODOS OS PRODITOS
element = browser.find_element_by_id('chkTodos')
element.click()

#CLICAR NO BOTAO DE PESQUISAR
element = browser.find_element_by_id('imgPesquisar')
element.click()

#ESPERAR CARREGAR
browser.implicitly_wait(10) 


#CONTAR AS PEGINAS GERADAS
count = 0

#PROCURA NA TABELA A ULTIMA LINHA QUE CONTEM A QUANTIDADE DE PAGINAS
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
			

#PARA A QUANTIDADE DE PAGINAS QUE FORAM GERADAS
for x in range(1, count + 1):
	
	#PEGA AS INFORMACOES DAS LINHAS
	linhas = browser.find_element_by_id('Grid').find_elements_by_tag_name('tr')

	for linha in linhas:
		ultimo = linha;
		print(linha.text)

	#IR PARA A PROXIMA PAGINA
	paginas = ultimo.find_element_by_tag_name('td').find_elements_by_tag_name('a')
	for pagina in paginas:
		if int(pagina.text) == x+1:
			pagina.click()
			browser.implicitly_wait(10)
			break 
	print(x)


browser.close()