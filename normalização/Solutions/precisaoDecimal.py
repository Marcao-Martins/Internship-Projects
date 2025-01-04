import re
import logging
import conllu
from Parser import ConlluParser


# Configura o logging para registrar as correções realizadas
logging.basicConfig(filename='decimal_precision_corrections.log',
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger()

class DecimalPrecisionModifier(ConlluParser):
    def __init__(self, file_path):
        super().__init__(file_path)
        # Inicializa o modificador com o caminho para o arquivo .conllu

    def correct_decimal_precision(self):
        decimal_pattern = re.compile(r'\d+[.,]\d+')
        integer_pattern = re.compile(r'\b\d+\b')
        changes_made = False

        for sentence in self.sentences:
            original_text = sentence.metadata.get('text', '')
            original_decimals = decimal_pattern.findall(original_text)
            original_integers = integer_pattern.findall(original_text)

            for token in sentence:
                # Itera tanto sobre a forma do token quanto sobre o lema
                for key in ['form', 'lemma']:  
                    token_value = token[key]
                    if decimal_pattern.match(token_value):
                        corrected_value = self._match_and_correct_form(token_value, original_decimals)
                    elif integer_pattern.match(token_value):
                        corrected_value = self._match_and_correct_integer(token_value, original_integers, original_decimals)
                    else:
                        corrected_value = None

                    if corrected_value and corrected_value != token_value:
                        token[key] = corrected_value
                        logger.info(f"Corrigido: {token_value} para {corrected_value} na sentença: '{original_text}'")
                        changes_made = True

        if changes_made:
            self._save_changes()

    def _match_and_correct_form(self, token_form, original_decimals):
        try:
            token_value = float(token_form.replace(',', '.'))
        except ValueError:
            return None  # Retorna None se a conversão falhar

        for original_form in original_decimals:
            try:
                original_value = float(original_form.replace(',', '.'))
                if token_value == original_value and token_form != original_form:
                    return original_form
            except ValueError:
                continue  # Ignora o valor se não puder ser convertido para float
        return None

    def _match_and_correct_integer(self, token_form, original_integers, original_decimals):
        try:
            token_value = int(token_form)
        except ValueError:
            return None  # Retorna None se a conversão falhar

        # Verifica se existe uma forma correspondente com duas casas decimais no texto original
        formatted_value = f"{token_value},00"
        if formatted_value in original_decimals:
            return formatted_value

        return None

    def _save_changes(self):
        conllu_string = ""
        for sentence in self.sentences:
            conllu_string += sentence.serialize()
        
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(conllu_string)