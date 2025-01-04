from Parser import ConlluParser
import re
import logging

class ZeroEsquerdaModifier(ConlluParser):
    def __init__(self, file_path, log_file='ZeroEsquerda.log'):
        super().__init__(file_path)
        # Configura o logger dedicado para esta classe
        self.logger = logging.getLogger('ZeroEsquerdaModifier')
        self.logger.setLevel(logging.INFO)
        # Evita que as mensagens do logger se propaguem para o logger pai
        self.logger.propagate = False

        # Configura o manipulador do arquivo de log com o formato e arquivo especificados
        file_handler = logging.FileHandler(log_file, mode='w')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def correct_left_zeros(self):
        # Padrão para identificar números na sentença
        number_pattern = re.compile(r'\b\d+')

        # Itera sobre as sentenças do arquivo .conllu
        for sentence in self.sentences:
            original_text = sentence.metadata.get('text', '')
            # Identifica números com zeros à esquerda no texto original
            original_numbers_with_zeros = [match for match in re.findall(r'\b0+\d+', original_text)]

            # Itera sobre os tokens da sentença
            for token in sentence:
                for key in ['form', 'lemma']:  
                    token_value = token[key]
                    # Verifica se o valor do token é um número sem zero à esquerda
                    if number_pattern.match(token_value) and not token_value.startswith('0'):
                        # Corrige o valor do token se necessário
                        corrected_value = self._find_matching_number_with_zeros(token_value, original_numbers_with_zeros)
                        if corrected_value and corrected_value != token_value:
                            # Atualiza o token com o valor corrigido
                            token[key] = corrected_value
                            # Registra a correção no arquivo de log
                            self.logger.info(f"Corrigido: {token_value} para {corrected_value} na sentença: '{original_text}'")

    def _find_matching_number_with_zeros(self, token_form, original_numbers_with_zeros):
        # Compara o token com os números originais para encontrar uma correspondência exata
        for original_form in original_numbers_with_zeros:
            try:
                # Compara convertendo para float para lidar com números decimais
                if float(token_form.replace(',', '.')) == float(original_form.replace(',', '.')):
                    return original_form
            except ValueError:
                continue
        return None

    def _save_changes(self):
        # Serializa a lista de sentenças para o formato .conllu e salva no arquivo
        conllu_string = ""
        for sentence in self.sentences:
            conllu_string += sentence.serialize()
        
        # Escreve a string serializada no arquivo .conllu
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(conllu_string)
