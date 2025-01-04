import os

def concatenate_conllu_from_folder(input_folder, output_file):
    # Lista todos os arquivos .conllu na pasta
    input_files = [
        os.path.join(input_folder, f) 
        for f in os.listdir(input_folder) 
        if f.endswith('.conllu')
    ]
    
    print(f"Encontrados {len(input_files)} arquivos CONLLU:")
    for f in input_files:
        print(f"- {f}")

    # Concatena todos os arquivos
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, file in enumerate(input_files):
            print(f"Processando: {file}")
            with open(file, 'r', encoding='utf-8') as infile:
                for line in infile:
                    outfile.write(line)
                # Adiciona duas linhas em branco entre os arquivos (exceto após o último)
                if i < len(input_files) - 1:
                    outfile.write('\n\n')
    
    print(f"\nArquivo concatenado salvo em: {output_file}")

# Pasta que contém os arquivos CONLLU
input_folder = 'concatenador\\individuals'

# Arquivo de saída
output_file = 'concatenador\\DANTEStocksV2.1.conllu'

# Executa a concatenação
concatenate_conllu_from_folder(input_folder, output_file)