from precisaoDecimal import DecimalPrecisionModifier
from zeroEsquerda import ZeroEsquerdaModifier
from conllu import parse

def parse_conllu_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return parse(data)

def compare_conllu_files_and_report(file_path1, file_path2, output_file):
    sentences1 = parse_conllu_file(file_path1)
    sentences2 = parse_conllu_file(file_path2)

    if len(sentences1) != len(sentences2):
        print("Número diferente de sentenças!")

    differences = []
    for sent1, sent2 in zip(sentences1, sentences2):
        sent_id1 = sent1.metadata['sent_id']
        sent_id2 = sent2.metadata['sent_id']
        if sent_id1 != sent_id2:
            print(f"IDs de sentença não correspondem: {sent_id1} vs {sent_id2}")
            continue
        
        for token1, token2 in zip(sent1, sent2):
            if token1['form'] != token2['form']:
                differences.append((sent_id1, token1['id'], token1['form'], token2['form']))

    with open(output_file, 'w', encoding='utf-8') as f_out:
        for diff in differences:
            sent_id, token_id, form1, form2 = diff
            f_out.write(f"Diferença na sentença {sent_id}, token {token_id}:\n")
            f_out.write(f"DANTES Corrigido-> {form1}\n")
            f_out.write(f"DANTES Original-> {form2}\n")
            f_out.write("\n")

def main():
    # Definição dos caminhos dos arquivos
    original_file = r'C:\Users\Marcos\Desktop\tic\bases\DANTEStocksV2.1.conllu'
    backup_file = r'C:\Users\Marcos\Desktop\tic\bases\DANTEStocksV2.1 backup.conllu'
    differences_file = 'output_differences.txt'

    try:
        # 1. Aplicar correções de precisão decimal
        print("Aplicando correções de precisão decimal...")
        decimal_modifier = DecimalPrecisionModifier(original_file)
        decimal_modifier.correct_decimal_precision()
        print("Correções de precisão decimal concluídas")

        # 2. Aplicar correções de zeros à esquerda
        print("\nAplicando correções de zeros à esquerda...")
        zero_esquerda_modifier = ZeroEsquerdaModifier(original_file)
        zero_esquerda_modifier.correct_left_zeros()
        print("Correções de zeros à esquerda concluídas")

        # 3. Comparar arquivos e gerar relatório
        print("\nComparando arquivos e gerando relatório de diferenças...")
        compare_conllu_files_and_report(original_file, backup_file, differences_file)
        print(f"Relatório de diferenças gerado em: {differences_file}")

    except Exception as e:
        print(f"\nErro durante a execução: {str(e)}")
    else:
        print("\nTodas as operações foram concluídas com sucesso!")

if __name__ == "__main__":
    main()