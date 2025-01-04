import csv
import re

def conllu_to_csv(conllu_file, csv_file):
    # Abre o arquivo conllu para leitura
    with open(conllu_file, 'r', encoding='utf-8') as infile:
        # Abre o arquivo CSV para escrita
        with open(csv_file, 'w', newline='', encoding='utf-8') as outfile:
            csv_writer = csv.writer(outfile)
            # Escreve o cabeçalho do CSV
            csv_writer.writerow(['ID', 'Text'])

            current_id = None
            current_text = None

            for line in infile:
                line = line.strip()
                if line.startswith("# sent_id = "):
                    # Se temos um ID e texto anteriores, salvamos antes de começar novo
                    if current_id is not None and current_text is not None:
                        csv_writer.writerow([current_id, current_text])
                    current_id = line.replace("# sent_id = ", "")
                    current_text = None
                elif line.startswith("# text = "):
                    current_text = line.replace("# text = ", "")
                elif line == "" and current_id is not None and current_text is not None:
                    # Ao encontrar uma linha vazia, escreve o par atual
                    csv_writer.writerow([current_id, current_text])
                    current_id = None
                    current_text = None

            # Escreve o último par se houver
            if current_id is not None and current_text is not None:
                csv_writer.writerow([current_id, current_text])

# Usando a função para converter o arquivo conllu para csv
conllu_to_csv(r'C:\Users\Marcos\Desktop\tic\bases\DANTEStocksV2.1 backup.conllu', 
              r'C:\Users\Marcos\Desktop\tic\comparação\comparacao\danteV2.1.csv')