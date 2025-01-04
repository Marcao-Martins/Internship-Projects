CONCATENADOR
===========

Ferramenta para concatenar múltiplos arquivos CONLLU em um único arquivo.

VISÃO GERAL
-----------
O script concat.py combina vários arquivos CONLLU de uma pasta em um único arquivo, mantendo o formato CONLLU e adicionando separadores apropriados entre os arquivos.

ESTRUTURA
---------
/concatenador
    /individuals     # Pasta com arquivos CONLLU individuais
    concat.py        # Script principal
    README.txt       # Este arquivo

FUNCIONALIDADE
-------------
concatenate_conllu_from_folder():
- Localiza todos os arquivos .conllu na pasta de entrada
- Concatena os arquivos sequencialmente
- Adiciona separadores entre arquivos
- Mantém encoding UTF-8
- Gera logs do processo

COMO USAR
---------
1. Organize seus arquivos:
   - Coloque todos os arquivos .conllu na pasta 'individuals'

2. Configure os caminhos no script:
   ```python
   input_folder = 'concatenador/individuals'
   output_file = 'concatenador/arquivo_final.conllu'
   ```

3. Execute o script:
   ```
   python concat.py
   ```

4. Verifique:
   - O arquivo concatenado na localização especificada
   - Os logs de processamento no console

REQUISITOS
----------
- Python 3.x
- Sistema de arquivos com permissões de leitura/escrita
- Arquivos CONLLU em UTF-8

NOTAS
-----
- Mantenha backups dos arquivos originais
- Verifique o encoding dos arquivos de entrada
- Monitore espaço em disco para arquivos grandes