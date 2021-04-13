# Aplicação que determina o caminho que uma mensagem deve fazer para ter menos chances de ser entendida, usando apenas mudança de tradução em cada país.

## Dado um país de origem e um de destino, a aplicação retorna o caminho que deve fazer no mundo e para quais idiomas ela deve ser traduzida em cada país.

## As restrições são: 
###     Um país só pode traduzir para um idioma que os habitantes saibam escrever e ler, 
###     Do mesmo modo, só pode receber a mensagem em idioma que alguns entendam.

## Explicando os termos:

## Mensagem: um arquivo de texto, com algum texto, e em algum idioma.

## Caminho: sequencias de países que a mensagem percorre sendo enviada e em qual idioma ela foi enviada para cada país. 
###     Exemplo: Brasil -> italiano ->  EUA -> grego -> França.  Nesse caso a origem é o Brasil, o destino é a França, 
###     a mensagem foi passada do Brasil para os EUA em italiano; depois foi passada dos EUA para França em grego.
###     Temos então que a mensagem foi traduzida nos EUA do italiano para o grego.

##Menos chances de ser entendida: caminho pelo qual a soma das frações da população de cada país que leem no idioma em que mensagem foi recebida e no qual será enviada é mínima.

### Uma das bases de dados usadas informa a fração de pessoas em um país que fala determinado idioma. 
### Exemplo: Brasil português 0.91 , significa que 91% dos brasileiros leem em português.
### (na verdade, a descrição completa não é somente ler, mas: "the population that is able to read and write each language, and is comfortable enough to use it with computers.".
### Falo ler, para ser mais breve).

### Exemplode caminho ineficiente: Brazil -> português ->portugal -> inglês -> EUA.  
### A ineficiência se dá porque muitos no Brasil e em Portugal podem ler em português, e muitos em Portugal e nos EUA podem ler em inglês.
### Um caminho eficiente:  Brazil -> italiano -> EUA, pois existem pessoas no Brasil e no EUA que falam italiano, mas não são muitas (comparativamente).
### Um caminho impossível: Brazil -> Húngaro -> EUA, pois apesar de poder haver na realidade pessoas tanto nos EUA como no Brasil que falam Húngaro, 
### a base de dados considera desprezível, por isso não haveria também quem pudesse ler e traduzir a mensagem.


##Mudança de tradução: mudança de idioma de um país para outro.
###Exemplo: Brasil ->italiano ->EUA -> francês -> Inglaterra,  a mensagem foi traduzida nos EUA do italiano para o francês.

##Algumas informações gerais sobre os arquivos:

data_treatment: tratamento dos dados nos dois links no final deste README e
armazenamento dos dados que relacionam siglas a nomes.


Database: armazenamento dos dados do Unicodelang, os dados principais de
relação entre países e línguas.

Dijkstra_pygame_animation: o main.py deste diretório contém um programa que
ilustra, em escala reduzida, o funcionamento do Dijkstra aplicado sobre a
base de dados coletada  (ou um exemplo qualquer, dependendo do graph que estamos usando), através de uma animação.


main.py: programa principal, que apresenta o menor caminho entre dois países
passados como input.

NOTA: 
ALTERAMOS O NOME DOS ARQUIVOS ORIGINAIS DO DATABASE, PORÉM OS MESMOS ESTÃO FACILMENTE RECONHECÍVEIS

Pegamos as informacoes dos sites:
    https://www.unicode.org/cldr/cldr-aux/charts/25/supplemental/language_territory_information.html
    http://konect.cc/networks/unicodelang/
    https://developers.google.com/public-data/docs/canonical/countries_csv
