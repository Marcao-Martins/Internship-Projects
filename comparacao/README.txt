Comparador de Tokenizações CONLLU
================================

Esta ferramenta permite comparar diferentes versões de arquivos CONLLU, focando especialmente na análise de diferenças de tokenização entre arquivos.

ÍNDICE
------
1. Visão Geral
2. Funcionalidades
3. Como Usar
4. Saídas Geradas
5. Exemplos

VISÃO GERAL
-----------
O comparador consiste em dois componentes principais:
1. Comparação bruta de tokens (comparacao_bruta)
2. Geração de relatório HTML interativo (report_comparacao)

FUNCIONALIDADES
--------------
1. Comparação Bruta (primeira célula):
   - Lê arquivos CONLLU
   - Extrai e compara tokens
   - Identifica diferenças na tokenização
   - Gera relatório CSV com diferenças encontradas

2. Relatório HTML (segunda célula):
   - Converte o CSV em relatório HTML interativo
   - Destaca diferenças visualmente
   - Permite fácil navegação e análise
   - Formata o output de maneira amigável

COMO USAR
---------
1. Configuração dos Arquivos:
   Defina os caminhos dos arquivos no código:
   
   conllu_file1 = 'caminho/para/primeiro/arquivo.conllu'
   conllu_file2 = 'caminho/para/segundo/arquivo.conllu'
   report_file = 'caminho/para/relatorio.csv'
   html_report_file = 'caminho/para/relatorio.html'

2. Execução:
   Execute as células do notebook na ordem:
   - Primeira célula: gera comparação bruta
   - Segunda célula: gera relatório HTML

SAÍDAS GERADAS
-------------
1. Arquivo CSV (comparacao.csv):
   - ID da sentença
   - Tokens do primeiro arquivo
   - Tokens do segundo arquivo

2. Relatório HTML (comparacao.html):
   - Tabela interativa
   - Diferenças destacadas em vermelho
   - Formatação responsiva
   - Fácil visualização das discrepâncias

CONLLU TO CSV (conllu_to_csv.py)
--------------------------------
Ferramenta auxiliar que extrai o ID e texto original de arquivos CONLLU para um formato CSV simplificado.

Funcionalidade:
- Extrai "sent_id" e "text" de cada bloco CONLLU
- Gera CSV com duas colunas: ID e Text
- Preserva o texto original da linha "# text = "

Utilizada para gerar o arquivo CSV que será usado para gerar o segundo Conllu para a comparação.


ESTRUTURA DO CÓDIGO
------------------
1. Funções Principais:
   
   read_conllu_file(conllu_file):
   - Lê e processa arquivo CONLLU
   - Extrai tokens e IDs
   - Trata duplicações de IDs

   compare_tokenizations(file1, file2, report_file):
   - Compara tokens entre arquivos
   - Identifica diferenças
   - Gera relatório CSV

   create_comparison_report(csv_file, html_report_file):
   - Gera relat��rio HTML
   - Aplica formatação e estilos
   - Destaca diferenças

DICAS DE USO
------------
1. Sempre verifique os caminhos dos arquivos antes da execução
2. Verifique o encoding dos arquivos CONLLU (UTF-8)
3. Analise o relatório HTML para uma visão mais clara das diferenças

REQUISITOS
----------
- Python 3.12
- Pandas
- Jinja2
- Navegador web moderno para visualizar relatório HTML

NOTAS IMPORTANTES
----------------
1. O script assume que os arquivos CONLLU estão bem formatados
2. IDs duplicados são tratados automaticamente
3. O relatório HTML funciona melhor em navegadores modernos
4. Grandes arquivos podem requerer mais tempo de processamento

TRATAMENTO DE ERROS
------------------
O código inclui tratamento para:
- Arquivos não encontrados
- Problemas de encoding
- IDs duplicados
- Diferenças estruturais entre arquivos
