Solutions - Normalizador de Arquivos CONLLU
===========================================

Este módulo fornece um conjunto de ferramentas para normalização e verificação de arquivos CONLLU, especialmente focado em normalização de números decimais e zeros à esquerda.

ÍNDICE
------
1. Estrutura do Projeto
2. Requisitos
3. Instalação
4. Como Usar
5. Funcionalidades Detalhadas
6. Arquivos de Log
7. Tratamento de Erros
8. Exemplos

ESTRUTURA DO PROJETO
-------------------
Solutions/
    __init__.py
    Parser.py
    contador_colunas.py
    precisaoDecimal.py
    zeroEsquerda.py
    main.py

REQUISITOS
----------
- Python 3.6 ou superior
- Biblioteca conllu
- Biblioteca re (built-in)
- Biblioteca logging (built-in)

INSTALAÇÃO
----------
1. Instale as dependências necessárias:
   pip install conllu


COMO USAR
---------
Passo 1: Preparação
    1. Faça uma cópia de backup do seu arquivo CONLLU original
    2. Coloque o arquivo CONLLU que deseja normalizar em um diretório conhecido

Passo 2: Configuração
    Abra o arquivo main.py e ajuste os caminhos dos arquivos:
    original_file = r'caminho/para/seu/arquivo.conllu'
    backup_file = r'caminho/para/seu/arquivo_backup.conllu'
    differences_file = 'output_differences.txt'

Passo 3: Execução
    Execute o script principal:
    python main.py

FUNCIONALIDADES DETALHADAS
-------------------------
1. Verificação de Colunas (contador_colunas.py)
   - Verifica se cada linha do arquivo CONLLU possui exatamente 10 colunas
   - Gera um relatório de discrepâncias encontradas
   - Identifica o bloco e linha exata onde há problemas

2. Normalização de Precisão Decimal (precisaoDecimal.py)
   - Corrige a formatação de números decimais
   - Mantém consistência entre o texto original e as anotações
   - Padroniza o uso de vírgula como separador decimal
   - Adiciona zeros à direita quando necessário (ex: 5 -> 5,00)

3. Normalização de Zeros à Esquerda (zeroEsquerda.py)
   - Preserva zeros à esquerda conforme o texto original
   - Corrige inconsistências entre tokens e texto
   - Mantém a formatação original de números com zeros à esquerda

ARQUIVOS DE LOG
--------------
O sistema gera três arquivos de log principais:
1. decimal_precision_corrections.log: Registra todas as correções de precisão decimal
2. ZeroEsquerda.log: Registra correções de zeros à esquerda
3. output_differences.txt: Mostra as diferenças entre o arquivo original e o corrigido

TRATAMENTO DE ERROS
------------------
O sistema inclui tratamento robusto de erros para:
- Arquivos não encontrados
- Problemas de codificação
- Erros de formato
- Problemas de conversão numérica

