
# O que este programa faz?
O arquivo python “Stocks_main” cria um dataframe com um determinado número de ações e,
opcionalmente, salva esse dataframe em arquivos excel e csv. Todos os nomes e os atributos
dessas ações são gerados aleatoriamente. O arquivo python “Stocks_filter” obtém o arquivo
csv de ações aleatórias para filtrar apenas boas empresas - se houverem - que valem um
investimento, criando um arquivo excel com elas.

# Qual filtro é aplicado?
O arquivo python “Stocks_filter” obtém a média de todos os PE ratios, seleciona apenas
empresas com um índice de PEG aceitável (menor que <50), remove aqueles com revisão de
analistas de “venda” e “baixo desempenho” e exclui todos aqueles com um PE ratio maior que
a média do PE ratio inicial.
