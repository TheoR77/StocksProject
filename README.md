## Stocks Project 💰
### What does this program do?
The “Stocks_main” python file creates a dataframe with a given number of stocks and
optionally saves this dataframe as an excel and a csv file. All of the stocks names and
attributes are randomly generated. The “Stocks_filter” python file gets the random stocks
csv file to filter only good companies - if there are any - that are worth an investment,
creating an excel file with those.
### What filter is applied?
The “Stocks_filter” python file gets the mean of all PE ratios, then gets only companies with
a acceptable PEG ratio (less than <50), removes those with “sell” and “underperform”
analysts review and then exclude all those with a PE ratio greater than the inicial PE ratio
mean.

///

### O que este programa faz?
O arquivo python “Stocks_main” cria um dataframe com um determinado número de ações e,
opcionalmente, salva esse dataframe em arquivos excel e csv. Todos os nomes e os atributos
dessas ações são gerados aleatoriamente. O arquivo python “Stocks_filter” obtém o arquivo
csv de ações aleatórias para filtrar apenas boas empresas - se houverem - que valem um
investimento, criando um arquivo excel com elas.

### Qual filtro é aplicado?
O arquivo python “Stocks_filter” obtém a média de todos os PE ratios, seleciona apenas
empresas com um índice de PEG aceitável (menor que <50), remove aqueles com revisão de
analistas de “venda” e “baixo desempenho” e exclui todos aqueles com um PE ratio maior que
a média do PE ratio inicial.
