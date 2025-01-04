def analyze_conllu_file(file_path, output_file_path):
    with open(file_path, 'r', encoding='utf-8') as conllu_file:
        lines = conllu_file.readlines()
    
    current_sent_id = None  # Para armazenar o ID do bloco atual
    discrepancies = []  # Para armazenar as linhas com discrepâncias

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        if line.startswith('# sent_id'):
            current_sent_id = line.split('=')[1].strip()  # Atualiza o sent_id atual
        elif line.startswith('#') or not line:  # Ignora comentários e linhas vazias
            continue
        else:
            groups = line.split()
            num_groups = len(groups)
            if num_groups != 10:
                discrepancies.append((current_sent_id, line_number, num_groups, line))
    
    # Escrever as discrepâncias no arquivo de saída
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        if discrepancies:
            for sent_id, line_number, num_groups, line in discrepancies:
                output_file.write(f"Bloco {sent_id}, Linha {line_number} tem {num_groups} grupos: {line}\n")
        else:
            output_file.write("Nenhuma discrepância encontrada.\n")

# Exemplo de uso
file_path = r'normalização\DANTEStocksV2.1.conllu'
output_file_path = r'normalização\contador.txt'
analyze_conllu_file(file_path, output_file_path)
