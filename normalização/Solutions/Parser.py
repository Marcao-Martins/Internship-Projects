from conllu import parse

class ConlluParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.sentences = self._load_and_parse()

    def _load_and_parse(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        sentences = parse(data)
        return sentences
    









