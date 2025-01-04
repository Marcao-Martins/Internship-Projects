ESTATÍSTICO
===========

Conjunto de ferramentas para processamento e análise estatística de arquivos CONLLU.

ÍNDICE
------
1. Visão Geral
2. Pré-processamento (preprocessing.ipynb)
3. Análise Estatística (statistical_analyzer.ipynb)
4. Requisitos
5. Como Usar

VISÃO GERAL
-----------
Ferramentas para análise linguística de corpus CONLLU, divididas em dois componentes:
- Pré-processamento: Limpeza e preparação dos dados
- Análise Estatística: Geração de métricas e visualizações

PRÉ-PROCESSAMENTO (preprocessing.ipynb)
-------------------------------------
Funções principais:
1. preprocess_conllu():
   - Remove linhas vazias
   - Limpa formatação
   - Padroniza separadores

2. preprocess_conllu_text():
   - Consolida linhas de texto
   - Trata quebras de linha
   - Mantém consistência do formato

3. preprocess_conllu_and_remove_invalid_ids():
   - Remove IDs inválidos
   - Limpa pontuações problemáticas
   - Garante integridade dos dados

ANÁLISE ESTATÍSTICA (statistical_analyzer.ipynb)
---------------------------------------------
Funcionalidades:
1. def parsear_conllu(caminho_arquivo):
   - Processa os arquivos conllu e faz o parsing para posterior análise

2. def gerar_relatorio_latex(corpora_data, nomes_corpora, arquivo_saida_latex):
    -Utiliza de diversas funcões auxiliares para gerar um relatório estatistico em latex formatado, além das imagens dos gráficos

REQUISITOS
----------
- Python 3.12+
- pandas
- matplotlib
- seaborn
- scipy
- conllu
- numpy

COMO USAR
---------
1. Pré-processamento (preprocessing.ipynb):
   a. Configure os caminhos dos arquivos:
      ```python
      nome_arquivo_original = 'caminho/do/seu/arquivo.conllu'
      nome_arquivo_tratado = 'arquivo_tratado.conllu'
      ```
   
   b. Execute as células na seguinte ordem:
      1. Configuração de caminhos
      2. preprocess_conllu() - Remove linhas vazias e padroniza formatação
      3. preprocess_conllu_text() - Consolida linhas de texto
      4. preprocess_conllu_and_remove_invalid_ids() - Remove IDs inválidos
   
   c. Verifique o arquivo de saída:
      - Confirme se o arquivo tratado foi gerado
      - Examine as primeiras linhas para garantir formatação correta
      - Verifique logs de linhas removidas/alteradas

2. Análise Estatística (statistical_analyzer.ipynb):
   a. Carregue os arquivos CONLLU:
      ```python
      caminho_arquivo1 = 'corpus1.conllu'
      caminho_arquivo2 = 'corpus2.conllu'
      caminho_arquivo3 = 'corpus3.conllu'
      
      dados_conllu1 = parsear_conllu(caminho_arquivo1)
      dados_conllu2 = parsear_conllu(caminho_arquivo2)
      dados_conllu3 = parsear_conllu(caminho_arquivo3)
      ```

   b. Execute as análises:
      1. Defina nomes dos corpora
      2. Configure caminhos para gráficos
      3. Execute gerar_relatorio_latex()
   
   c. Examine os resultados:
      - Relatório LaTeX gerado (relatorio_comparativo.tex)
      - Gráficos salvos na pasta de saída
      - Logs de análise no notebook

Observações:
- Mantenha backups dos arquivos originais
- Verifique o encoding (UTF-8) dos arquivos
- Para corpus grandes, monitore o uso de memória

NOTAS
-----
- Verifique encoding (UTF-8)

